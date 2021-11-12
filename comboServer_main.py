from flask import Flask, render_template
import subprocess,os
from termcolor import cprint

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return render_template("homepage.html")

@app.route('/jquery.js', methods=['GET'])
def jquery():
    return render_template("jquery.js")
    
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



if not 'SUDO_UID' in os.environ.keys():
    print("Try running this program with sudo.")
    exit()
else:
    cprint('''  _   _      _   _                   
 | \ | | ___| |_| |_ _ __ __ _ _ __  
 |  \| |/ _ \ __| __| '__/ _` | '_ \ 
 | |\  |  __/ |_| |_| | | (_| | |_) |
 |_| \_|\___|\__|\__|_|  \__,_| .__/ 
                              |_|    
''',"red")
    cprint("                         By Kalihackz","green")
    cprint("                         Version : Final\n","yellow")
app.run(debug=False)
