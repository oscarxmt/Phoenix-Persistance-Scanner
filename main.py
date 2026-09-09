#!/usr/bin/env python3

import platform
import os
import argparse

def windows():
    print("[!] Started scanning...")
    script_path = "Windows/win_main.ps1"
    
    if not os.path.exists(script_path):
        print(f"[X] Error: {script_path} not found. Please ensure the script is in the correct location.")
    
    #print(f"[!] Found {script_path}. Executing...")

    ## Here you would add the code to execute the PowerShell script if needed.
    # os.system(f"powershell -ExecutionPolicy Bypass -File {script_path}")¨
    

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