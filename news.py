import requests
from send_email import send_email

topic = "tesla"

api_key = "f178f2ad6e35440eb18d2779a0c7f416"
url = ("https://newsapi.org/v2/everything?"\
       f"q={topic}&sortBy=publishedAt"\
       f"&apiKey=f178f2ad6e35440eb18d2779a0c7f416&"\
       "language=en")

# Make Request
request = requests.get(url, verify=False)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
   if article["title"] is not None:
       body = "Subject: Today's news"\
               +"\n" + body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body  = body.encode("utf-8")
send_email(message=body)

