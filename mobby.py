# MobbyOS v1.0 - Identity Management
import time

def start_system():
    print("--- MOBBY OS INITIALIZED ---")
    print("Creator: Roy | SIC Corp")
    print("----------------------------")
    time.sleep(1)

    # This is a 'List' - it's like a database of forbidden names
    blacklist = ["nexaflow", "admin", "guest"]

    username = input("ENTER YOUR ALIAS: ").lower()

    if username in blacklist:
        print(f"!! ALERT !! '{username}' is a restricted alias. Access Denied.")
    elif len(username) < 3:
        print("!! ERROR !! Alias too short for SIC encryption.")
    else:
        print(f"Handshake successful. Welcome, {username}.")
        print(f"Your SIC Relay is: {username}@duck.com")
        # In the next phase, we will save this to a file!

start_system()
