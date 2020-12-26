<# Computer Serial number and name retrieve v1.1 (2020/12/15)

 - added easier way to enter email. v1.1
 - auto login after Run *in progres* (get user detail as only one is logged on device)
 - find out the best option to prevent changes *if required* #>

$first_name = Read-Host "Enter your first name: "
$second_name = Read-Host "Enter your surname: "
$prompt_login = $first_name + "." + $second_name + "@domain.name"
$c = Get-Credential -credential $prompt_login
$c.Username

$name = $env:COMPUTERNAME
$serial = Get-WmiObject win32_bios | Format-List SerialNumber
cd C:\
mkdir C:\!_IT_TEST
cd !_IT_TEST
New-Item serial_number.txt
Add-Content -Path .\serial_number.txt -Value (Out-String -InputObject 'Computer name: ', $name)
Add-Content -Path .\serial_number.txt -Value (Out-String -InputObject $serial)
Get-Content -Path .\serial_number.txt

$From = $prompt_login

# type correct email for receiver between quotation marks
$To = ".........@domain.name"

$Attach = "C:\!_IT_TEST\serial_number.txt"
$Subject = "Computer serial number"
$Body = "Serial number and computer name added to attachement."
$SMTP = "smtp.office365.com"  # office365 as an example
$Port = "587"
Send-MailMessage -From $From -to $To -Subject $Subject -Body $Body `
-SmtpServer $SMTP -port $Port -UseSsl `
-Credential ($c) -Attachments $Attach