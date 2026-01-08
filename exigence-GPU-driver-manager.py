#Startup message
print("Welcome to Exegence-OS-GPU-driver-installer version 0.1.0 alpha")

#modules/libraries
import os
import platform
import subprocess

#variables
commands = ""

#gpu name
gpu = ""

#functions
def install_nvidia_gpu_driver():
    print("installing nvidia gpu driver")

def install_intel_gpu_driver():
    print("installing intel gpu driver")

def install_amd_gpu_driver():
    print("installing amd gpu driver")

def detect_GPU():
    print("detecting gpu")

def show_GPU_driver_options():
    print(f"It has been detected that your system has an {platform.uname}")

def command_input(command_input):
    if commands == "1":
        print("Driver Option 1")

#show driver options
show_GPU_driver_options()

#call functions
while commands != "quit" and commands != "exit":
    command_input(commands)

