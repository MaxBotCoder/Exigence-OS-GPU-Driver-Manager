#Startup message
print("Welcome to Exegence-OS-GPU-driver-installer version 0.1.2 alpha")

#root confirmation
if os.geteuid != 0:
    print("This application requires root privaleges please enable root privaleges via su on debian or sudo su on ubuntu.")

#modules/libraries
import os

#variables
commands = ""

#gpu name
#gpu = ""

#functions
def install_nvidia_gpu_driver():
    print("installing nvidia gpu driver")

def install_amd_gpu_driver():
    print("installing amd gpu driver")

#def detect_GPU():
#    print("detecting gpu")

def show_GPU_driver_options():
    #print(f"It has been detected that your system has an {platform.uname}")
    print("Drivers are provided for amd, intel and nvidia gpus.\nTo install your desired driver please type in the letter allocated to the driver!")
    print("""
        A) Nvidia Open Kernel Modules driver (Dedicated GPU Only)
        B) AMD ROcm driver (Dedicated GPU Only)
    """)

def command_input(command_input):
    yn = ""
    if commands.lower() == "a":
        if yn == y:
        elif yn == n:
    elif commands.lower() == "b":
        if yn == y:
        elif yn == n:
        
#show driver options
show_GPU_driver_options()

#call functions
while commands != "quit" and commands != "exit":
    command_input(commands)
