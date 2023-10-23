# Deex-Shell
Interactive Python Wrapper that creates an Executable which utilises an Obfuscated PowerShell Reverse Shell One Liner. 

# C#/PowerShell-Reverse-Shell-Executable
Currently Undetected Executable Reverse Shell Windows PE. 

The program generates a unique, obfuscated Powershell Reverse Shell One Liner each time.
The One Liner is then utilised in the executable which executes the obfuscated Powershell Reverse Shell when run. 

The C# code and PowerShell Script are dynamically generated each time so no 2 files should be the same.

Perfect for CTF or Pen Testing purposes if Defender is running. 

# Motivation 

Back when I was learning Pen Testing, it was fun. Smashing boxes and exploiting issues with Meterpreter Shells raining down upon you. But AV was never a consideration. Enter the real world and any decent AV will shutdown script kiddie tactics, kill a meterpreter shell and ruin your day. I wanted, or accurately needed something I could use as a PoC when testing and for reporting purposes. Having not enough knowledge of the windows api and coding in C or C# to make one from scratch, I took what I did know enough of i.e bash, python, powershell and some C# and mixed it all together to create this. It's clunky, it's not stealthy but if you need to execute an .exe to get a shell, then this works quite well. 

Any and all feedback is appreciated. 

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

Creates an Obfuscated and currently undetected (Defender) PowerShell Reverse Shell Script and PE. The program then launches a HTTP server to host the PowerShell Script which the executable grabs during execution. A netcat listener is then setup which catches the shell. 

## Option 2

Outputs the PE and PowerShell Script to host to allow you to excute when needed.

## Option 3 

Outputs the Obfuscated PowerShell Script only

## Deex-Shell in Action

![image](https://github.com/deeexcee-io/Deex-Shell/assets/130473605/528d5efe-282e-4fea-b2b7-a019f9b5ab54)

 
Currently undetectable but behavioural detections can class it as "malicious". What I mean by that is if the executable is transferred over and then executed immediatley, the fact it reaches out to a remote address and calls PowerShell is suspicious.

![image](https://github.com/deeexcee-io/Deex-Shell/assets/130473605/b58ca73a-864c-4f20-b118-cb4c44625f4e)

Made with assistance from chatgpt 🧠 💻



