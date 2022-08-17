import requests
import re

def get_idfb(link):
    payload={"link": link}
    headers = {
    "Host": "id.traodoisub.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4495.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "51",
    "Origin": "https://id.traodoisub.com",
    "Alt-Used": "id.traodoisub.com",
    "Connection": "keep-alive",
    "Referer": "https://id.traodoisub.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    }
    url = "https://id.traodoisub.com/api.php"
    response = requests.request("POST", url, headers=headers, data=payload) 
    # print(response.text)
    return response.json()


# txt = """c_user=123;xs=xxx;sb=xxx;datr=xxx
# c_user=289;xs=yyy;sb=yyy;datr=yyy"""

def cookie_to_uid(cookies: str):
    if "\n" in cookies:
        cookies_array = cookies.split("\n")
        uid_array = list()
        for i in cookies_array:
            uid = re.search('(?i)c_user=(.*?);', i).group(0)
            uid = uid.replace("c_user=","")
            uid = uid.replace(";","")
            uid_array.append(uid)
        return "\n".join(uid_array)
    else:
        uid = re.search('(?i)c_user=(.*?);', cookies).group(0)
        uid = uid.replace("c_user=","")
        uid = uid.replace(";","")
        return uid

# with open("test.txt", "w") as f:
#     f.write(cookie_to_uid(txt))
# print(cookie_to_uid(txt))