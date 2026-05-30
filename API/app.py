import os
import json
import pika

from flask import Flask, request, jsonify

app = Flask(__name__)

RABBITMQ_URL = os.getenv("RABBITMQ_URL")

params = pika.URLParameters(RABBITMQ_URL)

connection = pika.BlockingConnection(params)
channel = connection.channel()

QUEUE_NAME = "votes"

channel.queue_declare(
    queue=QUEUE_NAME,
    durable=True
)
@app.route("/")
def home():
    return jsonify({
        "status": "API Running"
    })


@app.route("/vote", methods=["POST"])
def vote():

    data = request.json

    required_fields = [
        "doc_id",
        "user_id",
        "poll_id",
        "choice",
        "timestamp",
        "edge_id"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"Missing field: {field}"
            }), 400
    channel.basic_publish(
        exchange="",
        routing_key=QUEUE_NAME,
        body=json.dumps(data),
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )

    return jsonify({
        "status": "queued",
        "vote": data
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
