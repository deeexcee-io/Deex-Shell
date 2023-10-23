# Deex-Shell
Interactive Python Program that creates a Windows Executable which utilises an Obfuscated PowerShell One Liner to get a reverse shell. 

# C#/PowerShell Reverse Shell Executable
Currently Undetected Executable Reverse Shell Windows PE. 

The program generates a unique, obfuscated Powershell Reverse Shell One Liner each time.
The One Liner is then utilised in the executable which executes the obfuscated Powershell Reverse Shell when ran. 

The C# code and PowerShell Script are dynamically generated each time so no 2 files should be the same, even with the same IP Address and Port.
```python
[+] Enter 1 to Create PE and start Listeners
[+] Enter 2 to simply create a PE
[+] Enter 3 to simply create a Obfuscated PowerShell Reverse Shell One Liner


<--Deex--># : 2
Enter IP address: 192.168.227.128
Enter port: 55555
[+] PE has been saved as CHIoWmocNR.exe and Remote PowerShell Reverse Shell Script has been saved as maDWQUYjzg in the current directory
Returning to Main Menu....

[+] Enter 1 to Create PE and start Listeners
[+] Enter 2 to simply create a PE
[+] Enter 3 to simply create a Obfuscated PowerShell Reverse Shell One Liner


<--Deex--># : 2
Enter IP address: 192.168.227.128
Enter port: 55555
[+] PE has been saved as jsUcXGaUhW.exe and Remote PowerShell Reverse Shell Script has been saved as KyKzkOlXyV in the current directory
Returning to Main Menu....

[+] Enter 1 to Create PE and start Listeners
[+] Enter 2 to simply create a PE
[+] Enter 3 to simply create a Obfuscated PowerShell Reverse Shell One Liner

┌──(kali㉿kali)-[/opt/Deex-Shell]
└─$ md5sum CHIoWmocNR.exe 
894d03e8c5a9f2fb49a4f8fe8180e8bf  CHIoWmocNR.exe
                                                                                                                                                     
┌──(kali㉿kali)-[/opt/Deex-Shell]
└─$ md5sum jsUcXGaUhW.exe 
2d07a03856acf334e878be35c079613e  jsUcXGaUhW.exe
```

Perfect for CTF or Pen Testing purposes if Defender is running. 

# Motivation 

Back when I was learning Pen Testing, it was fun. Smashing boxes and exploiting issues with Reverse/Meterpreter Shells raining down upon you. But AV was never a consideration. Enter the real world and any decent AV will shutdown script kiddie tactics, kill a reverse shell and ruin your day. I wanted, or accurately needed something I could use as a PoC when testing and for reporting purposes. Having not enough knowledge of the windows sysinternals and coding in C or C# to make one from scratch, I took what I did know enough of i.e bash, python, powershell, some C# and a healthy dose of asking chatgpt questions, I mixed it all together and created this. It's clunky, it's not stealthy, but if you need to execute an .exe to get a shell and bypass AV (Only tested on Defender), then this works quite well. 

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



