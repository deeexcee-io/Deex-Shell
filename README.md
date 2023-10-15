# Edit

Now getting detected. It was fun while it lasted ⚰️


# Deex-Shell
Obfuscated PowerShell Reverse Shell Executable. Unashamedly made with assistance from chatgpt 🧠 💻

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
Enter your IP and Port Number

![image](https://github.com/deeexcee-io/Deex-Shell/assets/130473605/7288c047-32f4-4f5e-88be-e4250df798c5)

It outputs a file called `temp.exe` which can be executed on Windows.

Currently undectable 14/10/2023

![image](https://github.com/deeexcee-io/Deex-Shell/assets/130473605/92dd3499-c5d1-42b3-903b-c2f5e8d7e96e)

