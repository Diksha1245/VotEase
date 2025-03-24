import cv2
import json
import os
from deepface import DeepFace

DATASET_PATH = "dataset/"
DB_PATH = os.path.join(DATASET_PATH, "voter_database.json")
TEMP_IMG_PATH = "current_user.jpg"

def recognize_voter():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    
    if not ret:
        print("Error capturing image")
        return None

    cv2.imwrite(TEMP_IMG_PATH, frame)
    cap.release()

    try:
        with open(DB_PATH, "r") as f:
            voter_db = json.load(f)
    except FileNotFoundError:
        print("Voter database not found.")
        return None

    for name, data in voter_db.items():
        stored_img = os.path.join(DATASET_PATH, f"{name}.jpg")

        result = DeepFace.verify(img1_path=stored_img, img2_path=TEMP_IMG_PATH, model_name="Facenet")
        
        if result["verified"]:
            print(f"User recognized: {name} (ID: {data['voter_id']})")
            return data['voter_id']

    print("User not found. Redirecting to registration...")
    return None

# Test voter recognition
voter_id = recognize_voter()
if voter_id:
    print(f"Voter ID: {voter_id}")
else:
    print("Please register first.")
