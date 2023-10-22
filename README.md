# Deex-Shell
Small program that creates an onfiscated PowerShell Reverse Shell One Liner and PE. Unashamedly made with assistance from chatgpt 🧠 💻

# Simple-C#/PowerShell-Reverse-Shell-Executable
Current Undetected Executable Reverse Shell Windows PE. 

The script generates a unique, obfuscated Powershell Reverse Shell One Liner each time.
The One Liner is then utilised in the executable which executes the obfuscated string when run. 


Perfect for CTF or Pen Testing purposes if Defender is running. 

## Pre-requisites

It uses mono to compile the C# code in the python script into an executable so must be installed prior to running the script. 

On Kali
```
sudo apt install mono-mcs

sudo apt install mono-devel
```

Then simply run 
```
python3 deex-shell.py
```
## Option 1

Creates an Obfuscated and currently undetected (Defender) PowerShell Reverse Shell Script and PE. The program then launches a HTTP server to host the PowerShell Script which the executable grabs during execution.

## Option 2

Outputs the PE and PowerShell Script to host and excute when needed.

## Option 3 

Outputs the Obfuscated PowerShell Script

![image](https://github.com/deeexcee-io/Deex-Shell/assets/130473605/528d5efe-282e-4fea-b2b7-a019f9b5ab54)

Currently undetectable but behavioural detections can class it as "malicious". What I mean by that is if the executable is transferred over and then executed immediatley, the fact it reaches out to a remote address and calls PowerShell is suspicious.

![image](https://github.com/deeexcee-io/Deex-Shell/assets/130473605/b58ca73a-864c-4f20-b118-cb4c44625f4e)




