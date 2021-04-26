
import requests

def get_poet_names(parameters):
    s = requests.Session()
    url = 'https://www.stackmaps.com/api/login/'
    req = s.get(url)
    r = req.text[1411:1475]
    header = {'Referer': 'https://www.stackmaps.com/api/login/?next=/api/examples/poets/'}
    parameters['csrfmiddlewaretoken'] = r   
    req1 = s.post(url, data = parameters, headers = header)
    req2 = s.get('https://www.stackmaps.com/api/examples/poets/', data = parameters, headers = header).json()
    return req2


login_data = {'username': 'PD9W79','password': 'changepass'}
get_poet_names(login_data)

