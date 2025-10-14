import requests
from send_email import send_email

api_key = "f178f2ad6e35440eb18d2779a0c7f416"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2025-09-14&"
       "sortBy=publishedAt&apiKey=f178f2ad6e35440eb18d2779a0c7f416")

# Make Request
request = requests.get(url, verify=False)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
   if article["title"] is not None:
       body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body  = body.encode("utf-8")
send_email(message=body)

