import requests

api_key = "f178f2ad6e35440eb18d2779a0c7f416"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2025-09-14&"
       "sortBy=publishedAt&apiKey=f178f2ad6e35440eb18d2779a0c7f416")

# Make Request
request = requests.get(url, verify=False)

# Get a dictonary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
