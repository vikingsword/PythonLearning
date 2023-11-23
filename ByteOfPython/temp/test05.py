import requests


class GetContent:
    def __init__(self, url):
        self.url = url

    def get(self):
        return requests.get(self.url).content

url = 'https://www.baidu.com'
con = GetContent(url).get()
print(con)