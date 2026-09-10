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
    
    with open(config_path, 'r') as f:
        return json.load(f)


def windows():
    print("[!] Started scanning...")
    scripts_path = "Windows"
    registry_run_keys = "Windows/reg_startup_scan.ps1"
    startup_folders_scan = "Windows/startup_folders.ps1"
    
    if not os.path.exists(scripts_path):
        print(f"[X] Error: {scripts_path} not found. Please ensure the Windows folder within this repo, is in the correct location.")

    config = json_config()

    if config and config["checks"]["registry_run_keys"]:
        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", registry_run_keys])
        # bro just run the powershell script for scanning registry run keys
        # I love debugging :3¨
    if config and config["checks"]["startup_folders"]:
        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", startup_folders_scan])

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