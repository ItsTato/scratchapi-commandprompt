# MIT License
# 
# Copyright (c) 2021 ItsTato
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os,sys,time

os.system("cls")

try:
    from colorama import Fore, Back, Style
    print(f"{Back.LIGHTGREEN_EX}{Fore.BLACK} GOOD {Fore.RESET}{Back.RESET} Imported {Fore.LIGHTYELLOW_EX}colorama{Fore.RESET}")
except ImportError as e:
    os.system("pip3 install colorama")
    sys.exit(1)

try:
    from scratchclient import *
    print(f"{Back.LIGHTGREEN_EX}{Fore.BLACK} GOOD {Fore.RESET}{Back.RESET} Imported {Fore.LIGHTYELLOW_EX}scratchclient{Fore.RESET}")
except ImportError as e:
    os.system("pip3 install scratchclient")
    sys.exit(1)

os.system("cls")

while True:
    maincommand = input(f"{Fore.LIGHTYELLOW_EX}ScratchAPI{Fore.RESET}{Fore.GREEN}${Fore.RESET} ")
    if maincommand == "login":
        os.system("cls")
        username = input("Username: ")
        password = input("Password: ")
        os.system("cls")
        print("Logging in to Scratch...")
        session = ScratchSession(username=username, password=password)
        print(f"Logged in to Scratch account {username} successfully")
        time.sleep(1)
        os.system("cls")
        notquit = False
        mainnotquit = True
        
        while mainnotquit == True:
            option = input(f"{Fore.LIGHTYELLOW_EX}{username}{Fore.RESET}{Fore.GREEN}@{Fore.RESET}{Fore.LIGHTYELLOW_EX}ScratchSite{Fore.RESET}{Fore.GREEN}#{Fore.RESET} ")
            if option == "cloudconnect":
                print("Please enter a Project ID.")
                projectid = input("Project ID: ")
                connection = session.create_cloud_connection(projectid)
                notquit = True
                while notquit == True:
                    command = input(f"{Fore.LIGHTYELLOW_EX}{username}{Fore.RESET}{Fore.GREEN}@{Fore.RESET}{Fore.LIGHTYELLOW_EX}{session.get_project(projectid).title}{Fore.RESET}{Fore.GREEN}#{Fore.RESET} ")
                    if command == "changevar":
                        vartochange = input("Cloud variable to change: ")
                        vartochange1 = vartochange
                        newvarval = input("New value for the variable: ")
                        newvarval1 = newvarval
                        connection.set_cloud_variable(vartochange1, newvarval1)
                        print("Changed variable value.")
                    if command == "getlatestcomment":
                        print(f"Latest comment for {session.get_project(projectid).title}")
                        print(session.get_project(projectid).get_comments()[0].content)
                    if command == "exit":
                        notquit = False
                        os.system("cls")
            if option == "postcomment":
                usertopostcomment = input("Username of the user to post the comment at: ")
                comment = input("Comment to post (500 characters max): ")
                session.get_user(f"{usertopostcomment}").post_comment(f"{comment}")
            if option == "logout":
                mainnotquit = False
                os.system("cls")
    if maincommand == "help":
            print("• help -- Shows this list")
            print("• login -- Starts login procedure")
