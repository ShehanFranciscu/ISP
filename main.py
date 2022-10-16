import os
import socket
import pyfiglet
from tabulate import tabulate
import nmap3


ascii_banner = pyfiglet.figlet_format("YAKA!!!")
print(ascii_banner)

#Table
data = [["Yaka Port Scanner", 1], 
        ["Yaka OS Scanner", 2], 
        ["Yaka Clickjacking Tester", 3], 
        ["Yaka Xss Tester", 4]]

#define header names
col_names = ["Type of Scanner", "Selection Number"]
  
#display table
print(tabulate(data, headers=col_names, tablefmt="fancy_grid", showindex="always"))

def OS(host):
    
    nmap = nmap3.Nmap()
    os_results = nmap.nmap_os_detection("host")
    print(os_results)

def portScanner(portx,porty):
    for x in range(portx,porty):
        y=x
        if s.connect_ex((host, y)):
         print("The" "port",y, "is closed")
        else:
         print("The" "port",y, "is open")
         s.close()

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

O=int(input("Enter Selection Number: "))
if O==1:
    host= input("Enter Target IP Address : ")
    portx=int(input("Enter First port :"))
    porty=int(input("Enter Last Port :"))
    portScanner(portx,porty)

elif O==2:
    host= input("Enter Target IP Address : ")
    OS(host)











    



 
    

