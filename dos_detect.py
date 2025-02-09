#!/usr/bin/env python3

import psutil
import logging
import time

logging.basicConfig(filename="dos_detection.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Set thresholds for DOS detection (customize these values based on your environment)
NETWORK_THRESHOLD = 50000  # Network bytes sent per second (bytes/second)
CPU_THRESHOLD = 90  # CPU usage threshold for DOS detection (%)
MEMORY_THRESHOLD = 85  # Memory usage threshold for DOS detection (%)


def check_network_activity():
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent
    bytes_received = net_io.bytes_recv
    return bytes_sent, bytes_received

def check_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)  # CPU usage over 1 second
    memory_usage = psutil.virtual_memory().percent  # Memory usage
    return cpu_usage, memory_usage
    
def detect_dos():
    while True:
        # Check system metrics
        cpu_usage, memory_usage = check_system_metrics()

        # Check network activity
        bytes_sent, bytes_received = check_network_activity()

        # Log and report if metrics exceed thresholds
        if bytes_sent > NETWORK_THRESHOLD or bytes_received > NETWORK_THRESHOLD:
            print(f"[!] High network activity detected: Sent: {bytes_sent} bytes, Received: {bytes_received} bytes -- possibly a false positive")
            logging.warning("[!] High network activity detected: Sent: %d bytes, Received: %d bytes -- possibly a false positive", bytes_sent, bytes_received)

        if cpu_usage > CPU_THRESHOLD:
            print(f"[!] High CPU usage detected: {cpu_usage}%")
            logging.warning("[!] High CPU usage detected: %f%%", cpu_usage)

        if memory_usage > MEMORY_THRESHOLD:
            print(f"[!] High memory usage detected: {memory_usage}%")
            logging.warning("[!] High memory usage detected: %f%%", memory_usage)

        # Log every check for review
        print(f"[+] Current CPU: {cpu_usage}%, Memory: {memory_usage}%, Bytes Sent: {bytes_sent}, Bytes Received: {bytes_received}")
        logging.info("[+] Current CPU: %f%%, Memory: %f%%, Bytes Sent: %d, Bytes Received: %d", cpu_usage, memory_usage, bytes_sent, bytes_received)

        # Wait before checking again
        time.sleep(5)  # Adjust the interval as needed
        
if __name__ == "__main__":
    try:
        print("[+] Starting DoS detection...")
        detect_dos()
    except KeyboardInterrupt:
        print("[x] Detected ctrl+c.. Exiting")
        exit(1)
