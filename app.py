# import psutil
# virtual_memory = psutil.virtual_memory()
# ram_usage = virtual_memory.percent
# print(f"Maza RAM usage: {ram_usage}%")

# cpu_usage = psutil.cpu_percent(interval=1)
# print(f"MAZA CPU usage: {cpu_usage}%")

# print("Maza NPU usage: (NPU see the task manager)")

# battery = psutil.sensors_battery()
# if battery:
#     battery_percent = battery.percent
# else:
#     print("Battery chi information available")

import psutil
import time
import os

def check_ram():
    virtual_memory = psutil.virtual_memory()
    return virtual_memory.percent

def check_cpu():
    return psutil.cpu_percent(interval=0.5)

def check_battery():
    battery = psutil.sensors_battery()
    if battery:
        return battery.percent
    return "N/A"

if  __name__ == "__main__":
    print("---DEVOPS SYSTEM MONITORUNG STARTED ---")

    try:
        while True:
            ram = check_ram()
            cpu = check_cpu()
            bat = check_battery()

            print(f"[MONITOR] CPU: {cpu}% | RAM: {ram}%) | Battery: {bat}%")

            time.sleep(2)

    except KeyboardInterrupt:
        print("\n[INFO] Monitoring stopped by User.")
        
    


print('Git Diff Demo')
