import psutil
import time
import logging
from logging.handlers import RotatingFileHandler

log_handler = RotatingFileHandler('bulletproof_system.log', maxBytes=150, backupCount=3)
log_formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
log_handler.setFormatter(log_formatter)

logger = logging.getLogger("DevopsLogger")
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

def check_cpu():
    """CPU Check (Errpr Handling saha)"""
    try:
        return psutil.cpu_percent(interval=0.5)
    except Exception as e:
        logger.error(f"Error checking CPU usage: {e}")
        return 0.0
def check_ram():
        """RAM Check (Error Handling Saha)"""
        try:
            virtual_memory = psutil.virtual_memory()
            return virtual_memory.percent
        except Exception as e:
            logger.error(f"Error checking RAM usage: {e}")
            return 0.0
def monitor_system():
     
     print("===================================")
     print("[INFO] TASK-004: Bulletproof Engine Active...")
     print("[INFO] Background logging started. Press Ctrl+C to Stop")
     print("===================================")

     try:
          while True:
               cpu = check_cpu()
               ram = check_ram()

               log_message = f"CPU Usage: {cpu}% | RAM Usage: {ram}%"
               logger.info(log_message)

               time.sleep(2)

     except keyboardIntrrupt:
        print("\n[INFO] Monitoring stopped cleanly by administrator.")

if __name__ == "__main__":
    monitor_system()
        
