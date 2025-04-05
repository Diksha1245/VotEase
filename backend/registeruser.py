import cv2
import json
import os
from deepface import DeepFace

def register_user(name):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    
    if not ret:
        print("Error capturing image")
        return


    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        print("No face detected. Try again.")
        cap.release()
        return
    
    file_path = f"dataset\{name}.jpg"
    cv2.imwrite(file_path, frame)
    cap.release()
    if os.path.exists(file_path):
        print(f"Image saved successfully: {file_path}")
    else:
        print(f"Failed to save image: {file_path}")

    try:
        encoding = DeepFace.represent(img_path=file_path, model_name="Facenet", enforce_detection=False)[0]["embedding"]
    except Exception as e:
        print("DeepFace encoding failed:", e)
        return

    voter_db_path = "dataset/voter_database.json"

    # Ensure the database file is initialized properly
    if not os.path.exists(voter_db_path) or os.stat(voter_db_path).st_size == 0:
        with open(voter_db_path, "w") as f:
            json.dump({}, f)

    try:
        with open(voter_db_path, "r") as f:
            voter_db = json.load(f)
        if not isinstance(voter_db, dict):
            voter_db = {}
    except (FileNotFoundError, json.JSONDecodeError):
        voter_db = {}

    # Check if the user already exists
    if name in voter_db:
        print("Error: User already exists in the database.")
        return

    voter_id = f"VOTER_{len(voter_db) + 1000}"
    voter_db[name] = {"voter_id": voter_id, "encoding": encoding}

    with open(voter_db_path, "w") as f:
        json.dump(voter_db, f, indent=4)

    print(f"User {name} registered successfully with ID {voter_id}")

name = input("Enter your name to register: ")
register_user(name)
