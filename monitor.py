# import psutil
# import time
# def check_cpu_health():
#     print("--- System Monitoring Started ---")

#     try:
#         usage = psutil.cpu_percent(interval=1)
#         print(f"Current CPU Usage: {usage}%")

#         if usage > 80:
#             print(" ALERT: High CPU Usage Detected!")

#             with open("system_alerts.txt", "a") as file:
#                 file.writer(f"Alert! High Usage: {usage}% at {time.ctime()}\n")

#         else:
#              print("System Health: Normal") 

#     except Exception as e:
#         print(f"Error: {e}")



# while True:
#     check_cpu_health()
#     print("Waiting for next check (5 seconds)...")
#     time.sleep(5)                                                    
    
import psutil
import time

def check_system_health():

    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    ram_usage = memory.percent
    
    battery = psutil.sensors_battery()
    battery_usage = battery.percent if battery else "N/A"
    print(f"CPU: {cpu_usage}% | RAM: {ram_usage}% | BATTERY: {battery_usage}%")

    if cpu_usage > 80 or ram_usage > 80:
        print(" CRITICAL: System Overloaded!")
        with open("system_alerts.txt", "w") as file:
            file.write(f"Alert! CPU: {cpu_usage}%, RAM: {ram_usage}%, BATTERY: {battery_usage}% at {time.ctime()}\n")
while True:
    check_system_health()
    print(" waiting in 5 minitues")
    time.sleep(5)
