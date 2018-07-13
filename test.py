import requests
import

def upload(pic):

    fileName = pic.split('/')[-1]
    file = {
        'logo' :(fileName, open(pic,'rb'), 'image/jpeg')
    }


    url1 = 'http://106.15.201.54:8080/sixGod/getMessage'
    #url2 = 'http://192.168.119.37:3000/upload'
    r = requests.post(url=url1, files=file)
    return r.content.decode()

for i in range(2):
    plj = 'C:/Users/Strider/PycharmProjects/untitled/pic/'+str(i+1)
    tlj = 'C:/Users/Strider/PycharmProjects/untitled/gt/'+str(i+1)
    shiji = upload(plj+'.jpg')
    f = open(tlj+'.txt', 'r')
    gt = f.read()
    print(type(gt))
    print(type(shiji))
    print(gt==shiji)
    print(gt)
    print(shiji)
