import psutil

print("="*40)
print("🚀 Satara Server: System Health Monitor")
print("="*40)

# 1. CPU Check
cpu_usage = psutil.cpu_percent(interval=1)
print(f"🖥️  CPU Usage: {cpu_usage}%")

# 2. RAM Check
ram = psutil.virtual_memory()
print(f"🧠 RAM Usage: {ram.percent}%")

print("="*40)