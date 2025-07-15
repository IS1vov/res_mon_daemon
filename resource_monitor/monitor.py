# resource_monitor/monitor.py
import time
import logging
import psutil
from config import LOG_FILE, CPU_THRESHOLD, RAM_THRESHOLD
from send_alert import send_alert

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s CPU: %(message)s"
)

def get_resource_usage():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    logging.info(f"{cpu}% | RAM: {mem}%")

    if cpu > CPU_THRESHOLD:
        send_alert(f"⚠️ High CPU usage: {cpu}%")
    if mem > RAM_THRESHOLD:
        send_alert(f"⚠️ High RAM usage: {mem}%")

def main():
    while True:
        get_resource_usage()
        time.sleep(30)

if __name__ == "__main__":
    main()
