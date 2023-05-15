import time
import sys
import os
import WGMO as a
from sys import platform
import subprocess
import urllib.request

upDown = False
wireguard_status = input("Did you configure Wireguard already? (Y/N): ")

if wireguard_status.lower() == 'y':
        
    def stopConnection():
        global upDown
        try:
            subprocess.run(["sudo", "wg-quick", "down", "wg0"])
            print("Wireguard connection closed")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.output.decode('utf-8').strip()}")
        upDown = True


    def startConnection():
        global upDown
        try:
            subprocess.run(["sudo", "wg-quick", "up", "wg0"])
            print("Wireguard connection successful")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.output.decode('utf-8').strip()}")
        upDown = True


    def status():
        global upDown
        try:
            result = subprocess.run(["sudo", "wg", "show", "wg0"], capture_output=True, text=True)
            if "interface: wg0" in result.stdout:
                print(result.stdout)
                print("Wireguard connection status: connected")
            else:
                print("Wireguard connection status: disconnected")
        except subprocess.CalledProcessError as e:
            if "No such device" in e.output.decode('utf-8').strip():
                print("Wireguard is not configured or has been stopped")
                print("Wireguard is not configured or has been stopped")
            else:
                print(f"Error: {e.output.decode('utf-8').strip()}")
                print("Wireguard connection status: disconnected")
        upDown = True


    try:
        if sys.argv[1] == "up":
            startConnection()
        elif sys.argv[1] == "down":
            stopConnection()
        elif sys.argv[1] == "status":
            status()
    except:
        pass

    if upDown:
        sys.exit()
        
    # move the rest of the code into the if block
    # for wireguard_status.lower() == 'y'
    
elif wireguard_status.lower() == 'n':
    # Define some HTML text
    with open("logo.txt") as f:
        print(f.read())

    print("Your OS information:")
    print("-" * 20)
    print("Operating system: {}".format(sys.platform))
    print("Operating system version: {}".format(sys.version))

    print("-" * 20)
    while True:
        wireguard_install_or_not = input(
            "Did you install Wireguard already? (Y/N): ").lower()
        if wireguard_install_or_not in ('y', 'n'):
            break
        else:
            print("Invalid input. Please enter either 'y' or 'n'.")
    if wireguard_install_or_not == 'n':
        try:
            a.loading_animation("Checking net connection")
            urllib.request.urlopen("https://www.google.com")
        except:
            print("Please check your internet connection.")
        try:
            a.loading_animation("Installing Wireguard")
            wgst = subprocess.check_output(
                ['sudo', 'apt-get', 'install', 'wireguard', '-y'], input=b'yes\n', stderr=subprocess.STDOUT)
            wgst_str = wgst.decode("utf-8")
            if "is already the newest version" in wgst_str:
                print("Wireguard is already installed.")
            else:
                print("Wireguard installed.")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.output.decode('utf-8').strip()}")
    else:
        a.private_key_gen()
    a.public_key_gen()
    a.sna_labs_connect()
    a.conf_code_replace_up()
else:
    pass