#!/usr/bin/python3

from datetime import datetime
import ipaddress

time_now = datetime.now().strftime('%Y%m%d-%H%M%S')

#Give the name of file that contain IP-Address information
filename = input("Enter the name of file to open: ")

#Open File, Read content and create a List
#Error Handling - To check for provided FileName and valid IP address
try:
    with open(filename) as f:
        ip_addr_list = f.read().splitlines()

        with open (filename + "_"  + time_now + ".txt", "w") as f:
            f.write("config firewall address \n")
            for ip in ip_addr_list:
                ip = ip.strip()
                try:
                    #ipaddress module to check if the provided IP address or IP-NETWORK's are valid
                    if bool(ipaddress.ip_network(ip)):
                        f.write(f"edit {filename}_{ip} \n")
                        f.write(f"set subnet {ip} \n")
                        f.write("next \n")
                except ValueError:
                    print(f"{ip} does not appear to be an IPv4 or IPv6 network. Please check in File.")
            f.write("end")
except FileNotFoundError:
    print("File not found or incorrect file name.")
