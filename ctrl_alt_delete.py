#Program to ShutDown or Restart your system.

import os

def shut_down():
    os.system("shutdown /s /t 1")
    return "ShutDown Done"

def re_start():
    os.system("shutdown /r /t 1")
    return "Restart Done"

print("1 , Shut down Your System")
print("2 , Restart your System")


userChoice = input("\nEnter Option : ")

if userChoice == "1":
    confirmation = input("Want to Shut down your computer/PC ? (y/n): ")
    if confirmation.lower() == 'n':
        exit()
    else:
        shut_down()

elif userChoice == "2":
    confirmation = input("Want to Restart your computer/PC ? (y/n): ")
    if confirmation.lower() == 'n':
        exit()
    else:
        re_start()

else:
    print("Entered Invalid Option"+'\n'
          "Thank You")
    exit()