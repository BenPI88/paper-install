#d8888b.  .d8b.  d8888b. d88888b d8888b.      d888888b d8b   db .d8888. d888888b  .d8b.  db      db      d88888b d8888b. 
#88  `8D d8' `8b 88  `8D 88'     88  `8D        `88'   888o  88 88'  YP `~~88~~' d8' `8b 88      88      88'     88  `8D 
#88oodD' 88ooo88 88oodD' 88ooooo 88oobY'         88    88V8o 88 `8bo.      88    88ooo88 88      88      88ooooo 88oobY' 
#88~~~   88~~~88 88~~~   88~~~~~ 88`8b           88    88 V8o88   `Y8b.    88    88~~~88 88      88      88~~~~~ 88`8b   
#88      88   88 88      88.     88 `88.        .88.   88  V888 db   8D    88    88   88 88booo. 88booo. 88.     88 `88. 
#88      YP   YP 88      Y88888P 88   YD      Y888888P VP   V8P `8888Y'    YP    YP   YP Y88888P Y88888P Y88888P 88   YD 
#
#Made By Benji (https://github.com/BenPI88)

import os
import time

print("d8888b.  .d8b.  d8888b. d88888b d8888b.      d888888b d8b   db .d8888. d888888b  .d8b.  db      db      d88888b d8888b.\n88  `8D d8' `8b 88  `8D 88'     88  `8D        `88'   888o  88 88'  YP `~~88~~' d8' `8b 88      88      88'     88  `8D \n88oodD' 88ooo88 88oodD' 88ooooo 88oobY'         88    88V8o 88 `8bo.      88    88ooo88 88      88      88ooooo 88oobY' \n88~~~   88~~~88 88~~~   88~~~~~ 88`8b           88    88 V8o88   `Y8b.    88    88~~~88 88      88      88~~~~~ 88`8b   \n88      88   88 88      88.     88 `88.        .88.   88  V888 db   8D    88    88   88 88booo. 88booo. 88.     88 `88. \n88      YP   YP 88      Y88888P 88   YD      Y888888P VP   V8P `8888Y'    YP    YP   YP Y88888P Y88888P Y88888P 88   YD ")
def menu(title,opt,funcalls):
    print(title + "\n\n")
    menusel=0
    menuopt=opt
    i=0
    while not i == menusel + 1:
        print(str(i + 1) + " " + opt[i])
        i += 1
    print("\nWhich Option Would You Like?\n")
    optsel=input("")
    optsel = optsel - 1
    funcalls[int(optsel)]
def step():
    print("Please Use Automatic! As Stepped Is Not Ready Yet!")
    exit()
def auto():
    print("Dropping Server Files...")
    os.system("cp paper.jar ~/paper.jar && cd ~ && mkdir minecraft && cp ~/paper.jar ~/minecraft/paper.jar && rm -rf ~/paper.jar")
    print("Populating Server Files...")
    os.system("java -Xms2G -Xmx2G -jar paper.jar --nogui")
    print("Please Click Enter To Accept The EULA")
    input("")
    os.system("nano ~/minecraft/eula.txt")
    os.system("clear")
    print(".d8888. db    db  .o88b.  .o88b. d88888b .d8888. .d8888. db \n88'  YP 88    88 d8P  Y8 d8P  Y8 88'     88'  YP 88'  YP 88 \n`8bo.   88    88 8P      8P      88ooooo `8bo.   `8bo.   YP \n  `Y8b. 88    88 8b      8b      88~~~~~   `Y8b.   `Y8b.    \ndb   8D 88b  d88 Y8b  d8 Y8b  d8 88.     db   8D db   8D db \n`8888Y' ~Y8888P'  `Y88P'  `Y88P' Y88888P `8888Y' `8888Y' YP")
    time.sleep(2)
    print("You have installed Paper on your computer! Good work!\n")
    menu("Would You Like To Put Start Scripts In ~/minecraft ?",{Yes, No},{os.system(cp run.sh ~/minecraft/run.sh && cp run-headless.sh ~/minecraft/run-headless.sh), exit()})
menu("\nWelcome To BenPI88's Paper Installer!\n\nWould You Like To Install Paper Automatically, Or Stepped?", {"Automatically", "Stepped"}, {auto(), step()})