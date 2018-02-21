import requests

s = requests.Session()
dic = {
    'myName': 'junbumlee',
    'pw': 1234
}
res = s.post('http://httpbin.org/post', data=dic)
print(res.json())
