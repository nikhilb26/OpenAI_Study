import psutil
import time
import logging

logging.basicConfig(
    filename= 'system_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def check_cpu():
    return psutil.cpu_percent(interval=0.5)

def check_ram():
    virtual_memory = psutil.virtual_memory()
    return virtual_memory.percent

def monitor_system():
    print("=============================")
    print("[INFO] Logging Engine Started... Press Ctrl+c to Stop")
    print("==================================")

    logging.info("DevOps System Monitor Engine STARTED successfully.")

    try:
        while True:
            cpu = check_cpu()
            ram = check_ram()

            log_message = f"CPU Usage: {cpu}% | RAM Usage: {ram}%"
            print(f"[LIVE] {log_message}")
            logging.info(log_message)

            print("-" * 46)
            time.sleep(2)

    except KeyboardInterrupt:
                print("\n[INFO] Monitoring stopped by administrator.")
                logging.info("DevOps System Monnitor Engine STOPPED cleanly by adimistrator.")
            
if __name__ =="__main__":
            monitor_system()