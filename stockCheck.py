import sys, requests, mailSender, re
from time import sleep
from datetime import datetime

if len(sys.argv) < 6:
    print("Usage: <url-of-product> <text-to-find-in-page-for-match> <subject-of-email> <body-of-email> <recipient-email1> ...")
    sys.exit(1)

url = sys.argv[1]
textToFind = sys.argv[2]
subject = sys.argv[3]
body = sys.argv[4]
emailList = sys.argv[5:]

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
        try: mailSender.sendMail(emailList, subject, body)
        except: print("Error Sending Notification")
        sleep(600)# If content found, sleep for a while to avoid notification spam

    else: print("Not Found | " + datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    sleep(20) # Wait to avoid spamming server and risk getting blocked
