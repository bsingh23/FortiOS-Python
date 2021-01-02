#!/usr/bin/python3

import sys
from argparse import ArgumentParser
from datetime import datetime
import ipaddress


def open_ip_file(filename):
    try:
        with open(filename) as f:
            return f.read().splitlines()
    except FileNotFoundError as e:
        print(e)
        sys.exit()


def is_valid_ip(ip):
    try:
        return bool(ipaddress.ip_network(ip))
    except ValueError:
        print(f"{ip} does not appear to be an IPv4 or IPv6 network. Please check in File.")


def write_config(filename, lines):
    time_now = datetime.today().strftime('%Y-%m-%d')
    try:
        with open(filename + "_" + time_now + ".txt", "w+") as f:
            f.writelines(lines)
    except IOError as e:
        print(e)
        sys.exit()


def main(args):
    write_config(
        args.filename,
        [
            f"edit {args.filename}_{ip.strip()} \n" f" set subnet {ip} \n" "next \n"
            for ip in open_ip_file(args.filename)
            if is_valid_ip(ip.strip())
        ]
        + ["end\n"],
    )


if __name__ == "__main__":
    parser = ArgumentParser(description="Render Fortigate Objects")
    parser.add_argument("filename", type=str, help="File containing primitive data")
    main(parser.parse_args())
