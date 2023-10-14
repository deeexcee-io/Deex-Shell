# Deex-Shell
Obfuscated PowerShell Reverse Shell Executable

# Simple-C#/PowerShell-Reverse-Shell-Executable
FUD Executable Reverse Shell .exe

Utilises an unique obfuscated Powershell Reverse Shell One Liner each time.

The One Liner is then utilised in the executable which calls PowerShell and executes the obfuscated string.

## Pre-requisites

It uses mono to compile the C# code in the python script into an executable.

On Kali
```
sudo apt install mono-mcs

sudo apt install mono-devel
```

Then simply run 
```
python3 PowerShell-Executable.py

```
Enter your IP and Port Number

![image](https://github.com/deeexcee-io/Deex-Shell/assets/130473605/7288c047-32f4-4f5e-88be-e4250df798c5)

It outputs a file called `temp.exe` which can be executed on Windows.

Currently undectable 14/10/2023
