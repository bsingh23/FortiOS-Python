#!/usr/bin/python3

import datetime

time_now = datetime.datetime.now().isoformat(timespec="seconds")

#Give the name  of file that contain IP-Address information
filename = input("Enter the name of file to open: ")

#Open File, Read content and create a List
with open(filename) as f:  
   ip_addrs = f.read() 

ip_addr_list = ip_addrs.split()

#For loop that will create the configuration file
with open (filename + "_"  + time_now + ".txt", "w") as f:
    f.write("config firewall address\n")
    for ip in ip_addr_list:
        f.write(f"edit {filename}_{ip}") 
        f.write("\n")
        f.write(f"set subnet {ip}")
        f.write("\n")
        f.write("next")
        f.write("\n")
    f.write("end")
