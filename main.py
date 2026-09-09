#!/bin/python3

import platform
import os
import subprocess
import argparse

def windows():
    print("[!] Started scanning...")
    script_path = "Windows/scan.ps1"
    
    if os.path.exists(script_path):
        # Read the contents of your script
        with open(script_path, "r", encoding="utf-8") as f:
            ps_script_code = f.read()
        
        # Run powershell without any execution policy flags
        process = subprocess.Popen(
            ["powershell.exe", "-NoProfile", "-Command", "-"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Send the script code and get the output
        stdout, stderr = process.communicate(input=ps_script_code)
        print(stdout)
    else:
        print(f"[X] Error: {script_path} not found.")


def main():
    parser = argparse.ArgumentParser(description="Persistence Scanner")
    args = parser.parse_args()

    current_os = platform.system()

    print(f"[-] Detected operating system: {current_os}")
    print("=" * 40)
    
    if current_os == "Windows":
        windows()
    elif current_os == "Linux":
        print("[!] Linux detected. Support is not implemented yet.")
    elif current_os == "Darwin":
        print("[!] macOS detected. Support is not implemented yet.")
    else:
        print("[X] Unknown operating system. Could not scan")



if __name__ == "__main__":
    main()