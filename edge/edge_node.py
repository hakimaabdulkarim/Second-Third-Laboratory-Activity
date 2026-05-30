import os
import uuid
import time
import random
import requests

API_URL = os.getenv(
    "API_URL"
)

NODE_ID = os.getenv(
    "NODE_ID",
    "node-default"
)


def generate_vote():

    return {
        "doc_id": str(uuid.uuid4()),
        "user_id": f"user-{random.randint(1,100)}",
        "poll_id": "poll-1",
        "choice": random.choice(
            ["A", "B", "C"]
        ),
        "timestamp": time.time(),
        "edge_id": NODE_ID
    }

def send_vote(vote):

    try:

        response = requests.post(
            API_URL,
            json=vote,
            timeout=10
        )

        print(
            vote["doc_id"],
            response.status_code
        )

    except Exception as e:

        print(e)


def run_edge_node(
        duplicate=False
):

    while True:

        vote = generate_vote()

        send_vote(vote)

        if duplicate:
            send_vote(vote)

        time.sleep(
            random.randint(1, 3)
        )


if __name__ == "__main__":
    run_edge_node()
