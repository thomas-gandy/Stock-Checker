import sys, requests, mailSender, re
from time import sleep
from datetime import datetime

if len(sys.argv) < 7:
    print("Usage: <productName> <url> <textToFind> <subject> <body> <email1> <email...> <emailn>")
    sys.exit(1)

productName = sys.argv[1]
url = sys.argv[2]
textToFind = sys.argv[3]
subject = sys.argv[4]
body = sys.argv[5]
emailList = sys.argv[6:]

headers = {
"Accept": "*/*",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
}

while True:
    try:
        r = requests.get(url, headers=headers)
    except:# Exception could occur if server rejects connection
        sleep(600)# In this case wait for a while and try again
        continue

    webpage = r.content.decode("utf-8")

    if re.search(textToFind, webpage) != None:
        print("Stock Found! | " + datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        mailSender.sendMail(emailList, subject, body)
        sleep(600)# If content found, sleep for a while to avoid notification spam

    else: print("Not Found | " + datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    sleep(20) # Wait to avoid spamming server and risk getting blocked
