import cv2
import json
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

    file_path = f"../dataset/{name}.jpg"
    cv2.imwrite(file_path, frame)
    cap.release()

    encoding = DeepFace.represent(img_path=file_path, model_name="Facenet", enforce_detection=False)[0]["embedding"]

    try:
        with open("../dataset/voter_database.json", "r") as f:
            voter_db = json.load(f)
    except FileNotFoundError:
        voter_db = {}

    voter_id = f"VOTER_{len(voter_db) + 1000}"
    voter_db[name] = {"voter_id": voter_id, "encoding": encoding}

    with open("../dataset/voter_database.json", "w") as f:
        json.dump(voter_db, f)

    print(f"User {name} registered successfully with ID {voter_id}")

name = input("Enter your name to register: ")
register_user(name)
