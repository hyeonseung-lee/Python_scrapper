import requests

base_url = "http://hn.algolia.com/api/v1"
url = f"{base_url}/search?tags=story"
request = requests.get(url)


jsons = request.json()
hits = jsons["hits"]
for hit in hits:
    print({"title": hit['title'],
           "url": hit['url'],
           "author": hit['author'],
           "points": hit['points'],
           "comments": hit['num_comments']})
# i need : title, url, author, point, num_comments
