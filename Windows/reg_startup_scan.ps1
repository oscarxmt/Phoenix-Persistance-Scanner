# Define registry hives to look at
$RunKeys = @(
    "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run",
    "HKCU:\Software\Microsoft\Windows\CurrentVersion\RunOnce",
    "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run",
    "HKLM:\Software\Microsoft\Windows\CurrentVersion\RunOnce"
)

Write-Host "[*] Checking Registry Run Keys..."
foreach ($Key in $RunKeys) {
    if (Test-Path $Key) {
        Get-ItemProperty -Path $Key | Get-Member -MemberType NoteProperty | ForEach-Object {
            $Name = $_.Name
            $Value = (Get-ItemProperty -Path $Key).$Name
            [PSCustomObject]@{
                Location = $Key
                Name     = $Name
                Path     = $Value
            }
        }
    }
}

