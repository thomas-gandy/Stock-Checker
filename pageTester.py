# This file is used to output the webpage of a given URL, to ensure the content is what expected

import sys, requests

if len(sys.argv) != 2:
    print("Usage: <url>")
    sys.exit(1)

url = sys.argv[1]

headers = {
"Accept": "*/*",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
}

r = requests.get(url, headers=headers)
webpage = r.content.decode("utf-8")
print(webpage)
