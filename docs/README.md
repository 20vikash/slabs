
# SNAWGCONNET

This Python script allows you to manage your Wireguard VPN connections on your Linux machine. With this script, you can start, stop, and check the status of your Wireguard connection.

# Prerequisites

This script requires Python 3 to be installed on your system, as well as the following packages:

* `WGMO`
* `subprocess`
* `urllib.request`
* `sys`
* `os`
## Installation

Install my-project with npm

```
git clone https://github.com/20vikash/slabs.git
```
Clone or download the repository to your local machine.
Open a terminal and navigate to the directory where the script is located.
Run the following command to install the required packages: 

`pip install -r requirements.txt`
## Usage

* Open a terminal and navigate to the directory where the script is located.

* Run the following command to start the Wireguard connection:

` python3 wireguard_manager.py up `

* Run the following command to stop the Wireguard connection:

` python3 wireguard_manager.py down `

* Run the following command to check the status of the Wireguard connection:

` python3 wireguard_manager.py status `

If you have not configured Wireguard yet, the script will guide you through the installation and configuration process.


## Demo

Insert gif or link to demo


## Screenshots

* File Location 
![App Screenshot](https://i.imgur.com/28l7RB4.png)

* New Configration
![new conf](https://imgur.com/qSq7I4S.png)

* Wire Guard installation 
![wireguardistallcompleted](https://imgur.com/tUNPE3e.png)


* Private keygen 
![Privatekey](https://imgur.com/tJKc0ed.png)

* Public keygen 

![pulicjeygen](https://i.imgur.com/Ud30sBL.png)

* After generating the public key, add it to Essential Labs by navigating to the "Add new" panel and pasting it in the designated area.

* Add new and add the Public key in this panel 
![labsconfig](https://imgur.com/NADgAX8.png)

* After  added the Configration click three dots and copy and paste the conf in this nano edit and save it
![Configration](https://imgur.com/Gm7n056.png)

* Once the configuration is saved, the device will become available in Essential Labs and show as online.

![deviceoline](https://imgur.com/MxDISeN.png)

* To connect to the device via SSH, use the allocated IP address and run the following command:
![Lab ssh ](https://imgur.com/AhmYv1X.png)


* After that if you think disconnect the device use this command like this 

![showdown](https://imgur.com/ygiHyQb.png)

It will down the device and show like this

![showdownsate](https://imgur.com/gbgKPG4.png)
its goes offline with few minitues

* Now when everyyou can simply up the device and connect like this 

![labup](https://imgur.com/4LZ8jPI.png)
- By SNA Students
![Logo](data:image/png;base64,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)


## License


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Authors

- [@20vikash](https://github.com/20vikash/slabs)
- [@mrintroverrt](https://github.com/mrintroverrt)

Our mentor Grand wizard of technology [@Sibidharan](https://sibidharan.me/)

