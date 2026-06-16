import psutil

print("-----------------------------------------")
print("🌡️ System Temperature Monitor 🌡️")
print("-----------------------------------------")

# हा मुख्य if आहे
if hasattr(psutil, "sensors_temperatures"):
    # इथे बघ, if च्या आतल्या ओळींना मी Tab मारून पुढे घेतलं आहे 
    temps = psutil.sensors_temperatures()
    
    if not temps:
        print("⚠️  Warning: OS temperature डेटा देत नाहीये.")
    else:
        for name, entries in temps.items():
            for entry in entries:
                print(f"🔥 {name} - {entry.label or 'Core'}: {entry.current}°C")
else:
    # हे else मुख्य if च्या सरळ रेषेत आहे, पण आतली प्रिंट लाईन पुढे (Tab) आहे 
    print("🚫 Error: तुझ्या Windows OS मध्ये 'psutil' ला तापमान मोजण्याची परवानगी नाही.")
    print("💡 DevOps Note: हाच कोड जेव्हा आपण Linux Server वर चालवू, तेव्हा हे काम करेल!")

print("-----------------------------------------")