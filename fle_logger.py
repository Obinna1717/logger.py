from datetime import datetime

# Open file in append mode
with open("user_log.txt", "a") as file:
    while True:
        user_input = input("Enter something (type SAVE to stop): ")

        if user_input.upper() == "SAVE":
            print("Saving and exiting...")
            break

        # Get current time
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Write to file
        file.write(f"[{timestamp}] {user_input}\n")