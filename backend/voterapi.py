from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATASET_PATH = "dataset/"
VOTED_USERS_PATH = os.path.join(DATASET_PATH, "voted_users.json")

@app.route("/vote", methods=["POST"])
def vote():
    data = request.json
    voter_id = data.get("voter_id")
    choice = data.get("choice")

    if not voter_id or not choice:
        return jsonify({"status": "error", "message": "Voter ID and choice required"}), 400

    # Load voted users
    try:
        with open(VOTED_USERS_PATH, "r") as f:
            voted_users = json.load(f)
    except FileNotFoundError:
        voted_users = {}

    # Prevent duplicate voting
    if voter_id in voted_users:
        return jsonify({"status": "error", "message": "You have already voted!"}), 403

    voted_users[voter_id] = choice

    # Save vote
    with open(VOTED_USERS_PATH, "w") as f:
        json.dump(voted_users, f, indent=4)

    return jsonify({"status": "success", "message": f"Vote recorded for {choice}"})

if __name__ == "__main__":
    app.run(debug=True)
