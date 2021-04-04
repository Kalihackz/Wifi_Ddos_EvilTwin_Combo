from flask import Flask, render_template
import subprocess

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return render_template("homepage.html")
    
@app.route('/evil_on', methods=['GET'])
def on_evil():
    subprocess.call(['gnome-terminal', '--',"sudo", "python3", "FakeAuth_EvilTwin/start_Evil_Twin.py"])
    return ("Activated")
    
@app.route('/evil_off', methods=['GET'])
def off_evil():
    subprocess.call(['gnome-terminal', '--',"sudo", "python3", "FakeAuth_EvilTwin/stop_Evil_Twin.py"])
    return ("De-Activated")

@app.route('/ddos_on', methods=['GET'])
def on_ddos():
    subprocess.call(['gnome-terminal', '--',"sudo", "python3", "Ddos_Wifi/Ddos_Wifi.py"])
    return ("Activated")
    
@app.route('/ddos_off', methods=['GET'])
def off_ddos():
    subprocess.call(['gnome-terminal', '--',"sudo", "sh", "Ddos_Wifi/off_wifiDos.sh"])
    return ("De-Activated")

app.run()
