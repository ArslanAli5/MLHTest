import requests,json
from requests import get



try: 
    s = requests.Session()
    url = 'https://www.stackmaps.com/api/login/'
    req = s.get(url)
    r = req.text[1411:1475]
    header = {'Referer': 'https://www.stackmaps.com/api/login/?next=/api/examples/poets/'}
    login_data = {'csrfmiddlewaretoken': r,
                  'username': 'PD9W79',
                  'password': 'D3D75/Cs?C',
                  }
    
    req1 = s.post(url, data = login_data, headers = header)
    req2 = s.get('https://www.stackmaps.com/api/examples/poets/').json()
    print(req2['data'])
except:
    print("Failed")
