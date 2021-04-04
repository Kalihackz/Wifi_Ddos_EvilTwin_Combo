from time import localtime, strftime
import sys

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

def banner(AP,Channel,Interface):
    """
        Displays ASCII art of the highest caliber.
    """
    print ('')
    print (G + "  .;'                     `;,   |   *******************************")
    print (G + " .;'  ,;'             `;,  `;,  |   *"+O+"     EvilTwin Information    "+G+"*")
    print (G + ".;'  ,;'  ,;'     `;,  `;,  `;, |   *     --------------------    *")
    print (G + "::   ::   :   " + GR + "( )" + G + "   :   ::   :: |   *******************************")
    print (G + "':.  ':.  ':. " + GR + "/_\\" + G + " ,:'  ,:'  ,:' |   *   Access Point Type :"+C+" OPEN  "+G+"*")
    print (G + " ':.  ':.    " + GR + "/___\\" + G + "    ,:'  ,:'  |   *                             *")
    print (G + "  ':.       " + GR + "/_____\\" + G + "      ,:'    |   *      TIME  :  "+strftime("%H:%M:%S", localtime())+"      *")
    print (G + "           " + GR + "/       \\" + G + "            |   *******************************")
    print ('\n\n')
    print (O+' More Information')
    print ('------------------\n')
    print (P+' * SSID : '+B+AP)
    print (C+' * ENC. : '+G+'OPEN')
    print (C+' * Channel and Interface : '+R+Channel+" , "+Interface)
    print (O+' * MODE : '+R+'Evil Twin and Captive Portal')
    print ('\n\n'+G+'                                               - Made By Kalihackz\n')

banner(sys.argv[1],sys.argv[2],sys.argv[3])
