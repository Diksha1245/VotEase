from backend.voterverify import recognize_voter

user = recognize_voter()
if user:
    print(f"Welcome, {user}! Proceed to voting.")
else:
    print("New user detected! Redirecting to registration...")
