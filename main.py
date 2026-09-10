#!/usr/bin/env python3

import platform
import os
import argparse
import json
import subprocess

def json_config():
    config_path = "config.json"
    
    if not os.path.exists(config_path):
        print(f"[X] Error: {config_path} not found. Please check if the configuration file is in the correct location.")
        return None
    
    with open(config_path, 'r') as f:
        return json.load(f)


def windows():
    print("[!] Started scanning...")
    scripts_path = "Windows"
    registry_run_keys = "Windows/reg_startup_scan.ps1"
    
    
    if not os.path.exists(scripts_path):
        print(f"[X] Error: {scripts_path} not found. Please ensure the Windows folder within this repo, is in the correct location.")

    config = json_config()

    if config and config["checks"]["registry_run_keys"]:
        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", registry_run_keys])
        # run the powershell script for scanning registry run keys
    #print(f"[!] Found {script_path}. Executing...")

    ## Here you would add the code to execute the PowerShell script if needed.
    # subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path])

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