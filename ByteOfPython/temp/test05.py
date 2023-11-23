import requests


class GetContent:
    def __init__(self, url):
        self.url = url

    def get(self):
        res = requests.get(self.url)
        return res.content

url = 'https://www.baidu.com'
con = GetContent(url)
print(con)