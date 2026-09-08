$currentdir = cmd.exe /C cd C:

Write-Host "`n[*] Checking Scheduled Tasks..."

$user = $env:username 

$finalfilename = $user + "_ScheduledTask"

Get-ScheduledTask | Where-Object {$_.State -ne "Disabled"} | Select-Object TaskName, TazskPath, State > $currentdir\$finalfilename.txt

Write-Host "[*] Scheduled tasks saved to C:\Users\$user\Desktop\$finalfilename.txt" 