import requests , os , time , sys
from os import system, path
from colorama import Fore
u=Fore.LIGHTRED_EX
y=Fore.LIGHTYELLOW_EX
asd=Fore.LIGHTMAGENTA_EX
sd=Fore.LIGHTBLUE_EX
done = 1
reaper = input ("Enter Password : ")
if reaper == "EYE" :
        print ("Thanks..."*4)
else :
        print ("ERROR... ENTER PASSWORD...")
        os.system("exit")
print("loding")
time.sleep(0.3)
print("10%■□□□□□□□□□")
time.sleep(0.3)
print("20%■■□□□□□□□□")
time.sleep(0.3)
print("30%■■■□□□□□□□")
time.sleep(0.3)
print("40%■■■■□□□□□□")
time.sleep(0.3)
print("50%■■■■■□□□□□")
time.sleep(0.3)
print("60%■■■■■■□□□□")
time.sleep(0.3)
print("70%■■■■■■■□□□")
time.sleep(0.3)
print("80%■■■■■■■■□□")
time.sleep(0.3)
print("90%■■■■■■■■■□")
time.sleep(0.3)
print("100%■■■■■■■■■")
time.sleep(0.3)
os.system("clear")
print(f"{asd}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
 
print(f"""{u}
 
 
 
 __   __         _______  _______  __    _ 
|  | |  |       |  _    ||   _   ||  |  | |
|  | |  | ____  | |_|   ||  |_|  ||   |_| |
|  |_|  ||____| |       ||       ||       |
|       |       |  _   | |       ||  _    |
|       |       | |_|   ||   _   || | |   |
|_______|       |_______||__| |__||_|  |__|
 
------------------------------------
orginal by:6g7r_here
  updated by:343o8
 
  make sure to follow us on instagram
------------------------------------                           
""")
print(f"{asd}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
name = input(' (-) Name > : ')
user = input('(-) User >  : ')
email = input('(-) Email > : ')
phone = int(input("P-N: "))
bio = input("Contact Message (Leave It Empty To Use Default Message): ")
if bio == "":
    bio = "‏My account has been disabled by accident, I didn’t broke any instagram rules , and i hope you help me reactive it my account"
 
def Unbanned():
    url_Unbanned = "https://help.instagram.com/ajax/help/contact/submit/page"
    headers = {
                "Host": "help.instagram.com",
                "Accept": "*/*",
                "X-FB-LSD": "AVr_Dx9PS9A",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-us",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "https://help.instagram.com",
                "User-Agent": "Mozilla/5.0 (Linux; Android 11; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
                "Connection": "keep-alive",
                "Referer": "https://help.instagram.com/contact/606967319425038?helpref=page_content"
            }
    data = {
                "jazoest": 2890,
                "lsd": "AVr_Dx9PS9A",
                "name": name,
                "instagram_username": user,
                "email": email,
                "mobile_number": phone,
                "appeal_reason": bio,
                "support_form_id": 606967319425038,
                "support_form_hidden_fields": "{}",
                "support_form_fact_false_fields": "[]",
                "__user": 0,
                "__a": 1,
                "__dyn": "7xe6Fo4OQ1PyWwHBWo5O12wAxu13wqovzEy58ogbUuw9-3K4o1j8hwem0nCq1ewcG0KEswaq1xwEw7BKdwnU1e42C220qu1TwoU2swdq0Ho2ew",
                "__csr": "",
                "__req": "h",
                "__beoa": 0,
                "__pc": "PHASED:DEFAULT",
                "__bhv": 2,
                "dpr": 3,
                "__ccg": "EXCELLENT",
                "__rev": 1003521343,
                "__s": "8x0mgw:dal0sr:s5g412",
                "__hsi": "6943937313156005653-0",
                "__comet_req": 0,
                "__spin_r": 1003521343,
                "__spin_b": "trunk",
                "__spin_t": 1616761394
            }
    while True:
 
        done = +1
        req = requests.post(url_Unbanned,headers=headers,data=data)
        print('Done Send/تم ارسال!{}'.format(done))
    else:
        print('Error Send/خطأ! ')
 
Unbanned()
 
