$currentdir = cmd.exe /C cd C:

Write-Host "`n[*] Checking Scheduled Tasks..."

$user = $env:username 

$finalfilename = $user + "_ScheduledTask"

Write-Host "`n[*] Checking Startup Folders..."
Get-ChildItem "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"
Get-ChildItem "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"