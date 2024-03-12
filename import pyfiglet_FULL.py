import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("Port Scanner PETI GOLD")
print(ascii_banner)

if len(sys.argv) == 2:  
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Argumentos invalidos")
    
print("-"*50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-"*50)

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = s.connect_ex((target,port))
        if result ==0:
            print ("Port {} is open.format(port)")
        s.close()
        
except KeyboardInterrupt:
    print("\n Host abierto")
    sys.exit()
except socket.gaierror:
    print("\n Host No se peude resolver")
    sys.exit()
except socket.error:
    print("\ No responde el servidor")
    sys.exit()
            