import psutil
import time
import logging

from logging.handlers import RotatingFileHandler

log_handler = RotatingFileHandler('system_monitor.log', maxBytes=150, backupCount=3)
log_formatter = logging.Formatter('%(asctime)s - [%(levelname)s] -%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
log_handler.setFormatter(log_formatter)

logger = logging.getLogger("DevOpsLogger")
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)



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
           # print(f"[LIVE] {log_message}")
            logger.info(log_message)

            print("-" * 46)
            time.sleep(2)

    except KeyboardInterrupt:
                print("\n[INFO] Monitoring stopped by administrator.")
                logging.info("DevOps System Monnitor Engine STOPPED cleanly by adimistrator.")
            
if __name__ =="__main__":
            monitor_system()