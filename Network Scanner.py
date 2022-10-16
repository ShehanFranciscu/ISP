#!/usr/bin/python3

import nmap
import pyfiglet

ascii_banner = pyfiglet.figlet_format("YAKA!!!")
print(ascii_banner)

scanner = nmap.PortScanner()

print("Welcome to YAKA Vulnerability Scanning Tool")
print("<----------------------------------------------------->")

ip_addr = input("Please enter the target IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you
                1)Comprehensive Scanning
                2)UDP Scanning
                3)SYN and ACK scanning \n""")
print("You have selected option: ", resp)
if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -SV -SC-A-0')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print (scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2': 
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -SU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print (scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udg'].keys()) 
elif resp =='3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -s5')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print (scanner[ip_addr].all_protocols()) 
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())