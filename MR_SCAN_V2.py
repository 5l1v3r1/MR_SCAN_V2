import socket, os, sys, subprocess, time, signal, uuid
import netifaces as ni
import urllib.request
from scapy.all import *
global ip_str, discovered_ip, max_range, no_reach
no_reach = False
max_range = 255
discovered_ip = []
ver = str(2.0)
ip_str = str(ni.ifaddresses('eth0')[ni.AF_INET][0]['addr'])
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def getip():
	return socket.gethostbyname(socket.gethostname())

def quit():
    os.system('clear')
    exit()

def line():
    sys.stdout.write(MAGENTA + """--------------------------------------------------------------------""" + '\n')

def banner():
    spaces = " " * 76
    sys.stdout.write(GREEN + spaces + """
    ███▄ ▄███▓ ██▀███    ██████  ▄████▄   ▄▄▄       ███▄    █
    ▓██▒▀█▀ ██▒▓██ ▒ ██▒▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █
    ▓██    ▓██░▓██ ░▄█ ▒░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
    ▒██    ▒██ ▒██▀▀█▄    ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
    ▒██▒   ░██▒░██▓ ▒██▒▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
    ░ ▒░   ░  ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒
    ░  ░      ░  ░▒ ░ ▒░░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
    ░      ░     ░░   ░ ░  ░  ░  ░          ░   ▒      ░   ░ ░
          ░      ░           ░  ░ ░            ░  ░         ░
                                ░
    """ + YELLOW + """Version """ + str(ver) + RED + """                                         (By b3rt1ng)""" + '\n')
    line()

def get_mac(ip):
    command = "arp | grep " + str(ip)
    r = subprocess.check_output([command], shell=True)
    r=str(r) 
    r=r[35:]
    r=r[:17]
    return r

def resolveMac(mac):
    url = "https://api.macvendors.com/" + str(mac)
    b_str = urllib.request.urlopen(url).read()
    b_str = str(b_str, 'utf-8')
    return b_str

def ip_info(ip):
    os.system('clear')
    sys.stdout.write(BLUE + """IP: """ + GREEN + str(ip) + '\n')
    mac = get_mac(ip)
    sys.stdout.write(BLUE + """Mac: """ + GREEN + str(mac) + '\n')
    vendor = resolveMac(mac)
    sys.stdout.write(BLUE + """Vendor: """ + GREEN + vendor + '\n')
    stopper()


def ping(ip):
    try:
        subprocess.check_output(["ping", "-c", "1", ip])
        return True                      
    except subprocess.CalledProcessError:
        return False

def version():
    git=str(urllib.request.urlopen("https://raw.githubusercontent.com/b3rt1ng/MR_SCAN_V2/master/version").read())
    git=git[:-3]
    git=git.replace('b', '')
    git=git.replace("'", '')
    return git
cur=version()

def ipbase():
    stop = 3
    size = len(ip_str)
    ip_resized = ip_str[:-2]
    return str(ip_resized)


def scan():
    fisrt = 0
    ip = ipbase()
    sub = 0
    full_ip = ip + str(sub)
    while sub <= max_range:
        try:
            full_ip = ip + str(sub)
            if ping(full_ip) is True:
                if fisrt == 0:
                    os.system('clear')
                    fisrt = fisrt + 1
                discovered_ip.append(full_ip)
                sys.stdout.write(MAGENTA + """[""" + GREEN + """+""" + MAGENTA + """] """); sys.stdout.write(YELLOW + full_ip); sys.stdout.write(WHITE + ' is reachable' + '\n')
            else:
                if fisrt == 0:
                    os.system('clear')
                    fisrt = fisrt + 1
                if no_reach==True:
                    sys.stdout.write(MAGENTA + """[""" + RED + """-""" + MAGENTA + """] """); sys.stdout.write(YELLOW + full_ip); sys.stdout.write(WHITE + ' is not reachable' + '\n')
            sub = sub + 1
        except:
            os.system('clear')
            sys.stdout.write(MAGENTA + """[""" + RED + """!""" + MAGENTA + """]""" + WHITE + ' interrupted.' + '\n')
            time.sleep(1)
            sys.stdout.write(MAGENTA + """[""" + RED + """?""" + MAGENTA + """]""" + WHITE + ' returning to main menu.' + '\n')
            time.sleep(1)
            menu()
        
def stopper():
    try:
        sys.stdout.write('\n' + MAGENTA + """[""" + RED + """?""" + MAGENTA + """]""" + YELLOW + ' Hit CTRL + C to get back on the menu.' + '\n')
        time.sleep(6200)
    except:
        menu()

def show_disip():
    i=0
    while i < len(discovered_ip):
        sys.stdout.write(MAGENTA + """[""" + RED + str(i) + MAGENTA + """] """ + YELLOW + str(discovered_ip[i]) + '\n')
        i = i + 1
    stopper()

def empty():
    sys.stdout.write(MAGENTA + """[""" + RED + """?""" + MAGENTA + """]""" + YELLOW + ' The list is currently empty.' + '\n')
    stopper()

def result():
    os.system('clear')
    if len(discovered_ip)==0:
        empty()
    else:
        show_disip()

def param():
    os.system('clear')
    sys.stdout.write( RED + """[""" + BLUE + """*""" + RED + """]""" + YELLOW + """ Maximum range: """ + GREEN)
    print(max_range)
    sys.stdout.write( RED + """[""" + BLUE + """*""" + RED + """]""" + YELLOW + """ Your IP: """ + GREEN)
    print(ip_str)
    sys.stdout.write( RED + """[""" + BLUE + """*""" + RED + """]""" + YELLOW + """ Show unreachable IP: """ + GREEN)
    print(no_reach)
    stopper()


def adv_ip():
    os.system('clear')
    print(YELLOW, discovered_ip)
    sys.stdout.write( RED + """[""" + BLUE + """*""" + RED + """]""" + YELLOW + """ Type in an IP: """ + GREEN)
    IP = input()
    ip_info(IP)

def menu():
    os.system('clear')
    banner()
    sys.stdout.write('\n')
    if cur != ver:
        sys.stdout.write( RED + """[""" + BLUE + """!""" + RED + """]""" + YELLOW + """ Another version is avariable on github""" + '\n')
    sys.stdout.write( RED + """[""" + BLUE + """1""" + RED + """]""" + YELLOW + """ Start Scan""" + '\n')
    sys.stdout.write( RED + """[""" + BLUE + """2""" + RED + """]""" + YELLOW + """ Display discovered IP""" + '\n')
    sys.stdout.write( RED + """[""" + BLUE + """3""" + RED + """]""" + YELLOW + """ Advanced IP informations""" + '\n')
    sys.stdout.write( RED + """[""" + BLUE + """4""" + RED + """]""" + YELLOW + """ Settings""" + '\n')
    sys.stdout.write( RED + """[""" + BLUE + """5""" + RED + """]""" + YELLOW + """ Exit""" + '\n')
    sys.stdout.write('\n')
    sys.stdout.write( RED + """Mr""" + YELLOW + """_""" + BLUE + """Scan""" + MAGENTA + """:""" + GREEN + """ """)
    choice = input()
    if choice=="1":
        scan()
    elif choice=="2":
        result()
    elif choice=="3":
        adv_ip()
    elif choice=="4":
        param()
    elif choice=="5":
        os.system('clear')
        exit()



menu()