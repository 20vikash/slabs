import sys
import time
import subprocess

def loading_animation(text):
    # Define the animation symbols
    symbols = ['/', '-', '\\', '|']
    # Get the length of the text
    text_length = len(text)
    # Define the maximum number of symbols
    max_symbols = 4
    # Define the number of symbols displayed
    num_symbols = 0
    # Define the current symbol index
    symbol_index = 0

    # Define the duration of the animation
    duration = 5.0

    # Loop until the animation is complete
    start_time = time.time()
    while True:
        # Get the current symbol
        symbol = symbols[symbol_index % max_symbols]
        # Print the animation and text on the same line
        sys.stdout.write(f"\r{text} {symbol}")
        # Flush the output buffer
        sys.stdout.flush()
        # Pause for a short time
        time.sleep(0.3)
        # Increment the symbol index
        symbol_index += 1
        # If the animation has completed a full loop
        if symbol_index % max_symbols == 0:
            # Increment the number of symbols displayed
            num_symbols += 1
            # If the number of symbols displayed is equal to the length of the text
            if num_symbols == text_length:
                # Exit the loop
                break
        # Check if the animation has exceeded the duration
        elapsed_time = time.time() - start_time
        if elapsed_time > duration:
            # Exit the loop
            break

    # Print the final text
    sys.stdout.write(f"\r{' ' * (text_length + 2)}")
    sys.stdout.write(f"\r{text}... Done!\n")
    # Flush the output buffer
    sys.stdout.flush()

# Call the loading animation function with a duration of 5 seconds
# loading_animation()

def private_key_gen():
    command = 'wg genkey | sudo tee /etc/wireguard/private.key'
    command2 = 'sudo cat /etc/wireguard/private.key'
    print("-" * 20)
    private_checking = input("Did you already generate a WireGuard private key? (y/n): ")
    if private_checking == 'n':
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Successfully generated a new private key. Don't share this: " + result.stdout.decode('utf-8'))
    elif private_checking == 'y':
        result = subprocess.run(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Your existing private key. Don't share this: " + result.stdout.decode('utf-8'))
    else:
        print("Invalid input. Please enter either 'y' or 'n'.")

def public_key_gen():
    cmd1 = 'sudo cat /etc/wireguard/private.key | wg pubkey | sudo tee /etc/wireguard/public.key'
    cmd2 = 'sudo cat /etc/wireguard/public.key'
    print("-" * 20)
    public_checking = input("Did you linked the private key to your public key ? (y/n): ")
    if public_checking == 'n':
        output = subprocess.run(cmd1,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print("Successfully generated a new private key. "+ output.stdout.decode('utf-8'))
    elif public_checking == 'y':
        output = subprocess.run(cmd2,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print("Your existing public key : " + output.stdout.decode('utf-8'))
    else:
        print("Invalid input. Please enter either 'y' or 'n'.")

def sna_labs_connect():
    print("-" * 20)
    lab_connect_checking = input("Have you added public key and created new device to Our labs ? (y/n): ")
    if lab_connect_checking == 'n':
        subprocess.run(["sudo", "sh", "-c", "echo '# Please add the configuration code of your device here' > /etc/wireguard/wg0.conf"])
        subprocess.run(["sudo", "nano", "/etc/wireguard/wg0.conf"])
    elif lab_connect_checking == 'y':
        pass
    else:
        print("Invalid input. Please enter either 'y' or 'n'.")
def conf_code_replace_up():
    output_of_conf = subprocess.run(['sudo','cat','/etc/wireguard/private.key'],stdout=subprocess.PIPE)
    private_key = output_of_conf.stdout.decode("utf-8")
    with open("/etc/wireguard/wg0.conf", "r") as f:
        confCode = f.read()
    confCode = confCode.replace("{private_key}", "{}".format(private_key))
    with open("/etc/wireguard/wg0.conf", "w") as f:
        f.write(confCode)
        subprocess.run(["sudo", "wg-quick", "up", "wg0"])

