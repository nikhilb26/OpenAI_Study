import psutil
import os

print("------------------------------")
print(" Devops System Monitor Active ")
print("------------------")

dream_company = os.getenv("COMPANY_NAME", "Tech Wrold")
print(f" Target: {dream_company}")
print("--------------------------------")

print(f" CPU Uusage: {psutil.cpu_percent(interval=1)}%")
print(f" RAM Usage: {psutil.virtual_memory().percent}%")
print("---------------------------------")
print(" Custom Docker Container is running perfectly!")