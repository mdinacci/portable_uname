#!/usr/bin/env python

import platform
import os
import sys
import argparse

def uname(options):
    system = platform.system()
    node = platform.node()
    release = platform.release()
    version = platform.version()
    machine = "arm64"  # Always return "arm64" for machine

    if options.all:
        print(f"System: {system}")
        print(f"Node: {node}")
        print(f"Release: {release}")
        print(f"Version: {version}")
        print(f"Machine: {machine}")
    elif options.kernel:
        print(system)
    elif options.node:
        print(node)
    elif options.release:
        print(release)
    elif options.version:
        print(version)
    elif options.machine:
        print(machine)
    else:
        print(f"Unknown option: {options}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Emulate uname command")
    parser.add_argument("-a", "--all", help="Print all information", action="store_true")
    parser.add_argument("-s", "--kernel", help="Print the kernel name", action="store_true")
    parser.add_argument("-n", "--node", help="Print the node name", action="store_true")
    parser.add_argument("-r", "--release", help="Print the kernel release", action="store_true")
    parser.add_argument("-v", "--version", help="Print the kernel version", action="store_true")
    parser.add_argument("-m", "--machine", help="Print the machine hardware name", action="store_true")

    args = parser.parse_args()
    uname(args)
    sys.exit(0)

