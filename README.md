# Thief Raccoon - Login Phishing Tool

Thief Raccoon is a tool designed for educational purposes to demonstrate how phishing attacks can be conducted on various operating systems. This tool is intended to raise awareness about cybersecurity threats and help users understand the importance of security measures like 2FA and password management.

## Features

- Phishing simulation for Windows 10, Windows 11, Windows XP, Windows Server, Ubuntu, Ubuntu Server, and macOS.
- Capture user credentials for educational demonstrations.
- Customizable login screens that mimic real operating systems.
- Full-screen mode to enhance the phishing simulation.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- ngrok (for exposing the local server to the internet)

### Download and Install

1. **Clone the repository:**

   ```bash
   git clone https://github.com/davenisc/thief_raccoon.git
   cd thief_raccoon

2. **Install the required libraries:**
   
   ```bash
   pip install -r requirements.txt

**Usage**

1. **Run the main script:**
   
   ```bash
   python app.py

2. **Select the operating system for the phishing simulation:**

   After running the script, you will be presented with a menu to select the operating system. Enter the number corresponding to the OS you want to simulate.

3. **Access the phishing page:**

   If you are on the same local network (LAN), open your web browser and navigate to http://127.0.0.1:5000.
   
   If you want to make the phishing page accessible over the internet, use ngrok.

Using ngrok

1. **Download and install ngrok**

Download ngrok from ngrok.com and follow the installation instructions for your operating system.

2. **Expose your local server to the internet:**

3. **Get the public URL:**

After running the above command, ngrok will provide you with a public URL. Share this URL with your test subjects to access the phishing page over the internet.

**Example**

1. **Run the main script:**
   
   ```bash
   python app.py


2. **Select Windows 11 from the menu:**

   ```bash
   Select the operating system for phishing:
   1. Windows 10
   2. Windows 11
   3. Windows XP
   4. Windows Server
   5. Ubuntu
   6. Ubuntu Server
   7. macOS
   Enter the number of your choice: 2

3. **Access the phishing page:**

Open your browser and go to http://127.0.0.1:5000 or the ngrok public URL.

**Disclaimer**

**This tool is intended for educational purposes only. The author is not responsible for any misuse of this tool. Always obtain explicit permission from the owner of the system before conducting any phishing tests.**

**License**

This project is licensed under the MIT License. See the LICENSE file for details.

**Credits**

Developer: @davenisc
Web: https://davenisc.com
