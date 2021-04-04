import subprocess

print("Shutting down...Please Wait")
subprocess.call(["ifconfig", "wlan0mon", "down"])
subprocess.call(["iwconfig", "wlan0mon", "mode", "monitor"])
subprocess.call(["airmon-ng", "stop", "wlan0mon"])
subprocess.call(["systemctl", "restart", "NetworkManager"])
