import os
import json
import time
import threading

import pika

from flask import Flask, jsonify
from supabase import create_client

app = Flask(__name__)

RABBITMQ_URL = os.getenv("RABBITMQ_URL")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

processed_count = 0


def process_message(ch, method, properties, body):
    global processed_count

    try:
        vote = json.loads(body)

        existing = (
            supabase
            .table("votes")
            .select("doc_id")
            .eq("doc_id", vote["doc_id"])
            .execute()
        )

        if existing.data:
            print("Duplicate skipped")
            ch.basic_ack(delivery_tag=method.delivery_tag)
            return

        supabase.table("votes").insert({
            "doc_id": vote["doc_id"],
            "user_id": vote["user_id"],
            "poll_id": vote["poll_id"],
            "choice": vote["choice"],
            "timestamp": vote["timestamp"],
            "edge_id": vote["edge_id"],
            "processed_at": time.time()
        }).execute()

        processed_count += 1

        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        print(e)

def consumer_loop():

    while True:

        try:

            params = pika.URLParameters(
                RABBITMQ_URL
            )

            connection = pika.BlockingConnection(
                params
            )

            channel = connection.channel()

            channel.queue_declare(
                queue="votes",
                durable=True
            )

            channel.basic_qos(
                prefetch_count=1
            )

            channel.basic_consume(
                queue="votes",
                on_message_callback=process_message
            )

            print("Worker started")

            channel.start_consuming()

        except Exception as e:

            print("Reconnect:", e)

            time.sleep(5)


@app.route("/")
def home():

    return jsonify({
        "status": "worker running",
        "processed": processed_count
    })


threading.Thread(
    target=consumer_loop,
    daemon=True
).start()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
)
