import psutil
import time
import logging
from logging.handlers import RotatingFileHandler

log_handler = RotatingFileHandler('alert_system.log', maxBytes=2000, backupCount=3)
log_formatter = logging.Formatter('%(asctime)s - [%(Levelname)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
log_handler.setFormatter(log_formatter)


logger = logging.getLogger("DevOpsLogger")
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

CPU_THRESHOLD = 10.5
RAM_THRESHOLD = 50.0

def check_cpu():
    try:
        return psutil.cpu_percent(interval=0.5)
    except Exception as e:
        logger.error(f"Error checking CPU usage: {e}")
        return 0.0
    
def check_ram():
    try:
        virtual_memory = psutil.virtual_memory()
        return virtual_memory.percent
    except Exception as e:
        logger.error(f"Error checking RAM usage: {e}")
        return 0.0

def monitor_system():
    print("================================")
    print("[INFO] TASK-005: Alert Sentinel Active...")
    print("[INFO] Monitoring System with Live Alerts. Press Ctrl+C to Stop")
    print("================================")
    
    try:
        while True:
            cpu = check_cpu()
            ram = check_ram()

            log_message = f"CPU Usage: {cpu}% | RAM Usage: {ram}%"
            logger.info(log_message)
            
            if cpu > CPU_THRESHOLD:
                alert_msg = f"[CRITICAL ALERT] CPU Usage is dangerously HIGH: {cpu}%"
                logger.warning(alert_msg)
                
            time.sleep(2)
                
    except KeyboardInterrupt:
            print("\n[INFO] Alert Sentinel stopped cleanly by administrator")
if __name__ == "__main__":
                monitor_system()
    
             
        