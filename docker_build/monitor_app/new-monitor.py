import psutil

print("-----------------------------------------")
print("🚀 DevOps System Monitor Active 🚀")
print("-----------------------------------------")
print(f"🖥️  CPU Usage: {psutil.cpu_percent(interval=1)}%")
print(f"💾  RAM Usage: {psutil.virtual_memory().percent}%")
print("-----------------------------------------")
print("✅ Custom Docker Container is running perfectly!")