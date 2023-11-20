# Deex-Shell
Interactive Python Program that creates a Windows Executable which utilises an Obfuscated PowerShell One Liner to get a reverse shell. 
## Update
Line 117 in the code which is part of the C# Code had a static string which I believe was getting picked up and classing the PE as malicious. If testing, please turn off automatic sample submission. 
That being said, it should be random now but if you get any issues change any of the numbers after exit to a different number between 1 and 10. `{5}.StandardInput.WriteLine("exit;{1}{9}{2}{10}{3}{1}{2}`

!!! Dont change {5} it is a variable name that is required elsewhere in the code !!!

# C#/PowerShell Reverse Shell Executable
Currently Undetected (Defender) Executable Reverse Shell Windows PE. 

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

https://github.com/deeexcee-io/Deex-Shell/assets/130473605/81c69cf0-4906-4b7e-af1f-74f4bded7234



![image](https://github.com/deeexcee-io/Deex-Shell/assets/130473605/528d5efe-282e-4fea-b2b7-a019f9b5ab54)

 
Currently undetectable but behavioural detections can class it as "malicious". What I mean by that is if the executable is transferred over and then executed immediatley, the fact it reaches out to a remote address and calls PowerShell is suspicious.

![image](https://github.com/deeexcee-io/Deex-Shell/assets/130473605/b58ca73a-864c-4f20-b118-cb4c44625f4e)

Made with assistance from chatgpt 🧠 💻



