## importing socket module
import socket
from subprocess import check_output
#-------------------------------------------------------
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print('Your IP adress is ' + s.getsockname()[0])
    #return s.getsockname()[0]
get_ip_address()

#-------------------------------------------------------
proc =  check_output('ipconfig', encoding='oem') 
print (proc)
#-------------------------------------------------------
get_ip_address()

#import netifaces as ni
#print(ni.interfaces())
# Поставь wheel (просить у Лены)