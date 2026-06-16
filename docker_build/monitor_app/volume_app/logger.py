import datetime
import os

print("--------------------------")
print(" Docker Volume Task Active ")
print("-----------------------------")

folder_path = "/app/data"
file_path = f"{folder_path}/my_logs.txt"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

with open(file_path, "a") as file:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f" Log Entry: {current_time} - Volume is working perfectly!\n")

print(f" Log successfully written inside container at: {file_path}")
print("-----------------------------------")
