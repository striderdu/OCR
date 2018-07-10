import requests

def upload(pic):

    fileName = pic.split('/')[-1]
    file = {
        'logo' :(fileName, open(pic,'rb'), 'image/jpeg')
    }

    url1 = 'http://106.15.201.54:8080/sixGod/getMessage'
    #url2 = 'http://192.168.119.37:3000/upload'
    r = requests.post(url=url1, files=file)
    return r.content.decode()