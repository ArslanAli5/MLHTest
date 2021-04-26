import requests,json
#from requests import get
#from requests.auth import HTTPBasicAuth

from requests import get
from requests.auth import HTTPBasicAuth

#req = requests.get('https://api.github.com/user', auth=('ArslanAli5', '*/*8aj4L>$)'))
# Do not add any import statements


try: 
    #cookie = {'csrftoken':'55TWHxdvu9FB1u407FNS0JFd0hYr5Croh1pdL9gftExHUodDTtptGXQOTqzEGG2Z'} 
    r1 = requests.get('https://www.stackmaps.com/api/login/?next=/api/examples/poets/',auth=('PD9W79', 'D3D75/Cs?C'))
    #print(r1.content)
    response = requests.get('https://www.stackmaps.com/api/examples/poets/',cookies=r1.cookies) 
    print(response.content)
except requests.exceptions.HTTPError as httpErr: 
    print ("Http Error:",httpErr) 
except requests.exceptions.ConnectionError as connErr: 
    print ("Error Connecting:",connErr) 
except requests.exceptions.Timeout as timeOutErr: 
    print ("Timeout Error:",timeOutErr) 
except requests.exceptions.RequestException as reqErr: 
    print ("Something Else:",reqErr)