#This problem is about accessing API endpoints. 

#Stackmaps has an API endpoint you will access for this problem.  The address is:

#https://www.stackmaps.com/api/ping
#Please write a function called ping which uses the Python requests library to access the Stackmaps API endpoint given above.  Because you will be making a GET request, you will need to use the get() method from the requests library.  Your function should take in a single parameter.  If that parameter is an integer or a float, your function should pass it to the API endpoint using the parameter name x_value and return the value returned by the API.

#If your function is given a parameter which is not an integer and not a float, your function should return None.

#Please assume that the following import statement has already been made:

#from requests import get
#Do not add any additional import statements to your code.


#Spend five minutes skimming the documentation about the Python requests library.  You can access that documentation here:

#https://requests.readthedocs.io/en/master/

#and you can read about the get() method here:

#https://requests.readthedocs.io/en/master/api/#requests.get

#Note! Your function must be named ping



from requests import get

def get_poet_names(parameters):
    headers = {'Authorization':'Token f36460022a2cec6d0cbbc49df6e87d69bae856ec'}
    req2 = get('https://www.stackmaps.com/api/examples/poets/',headers=headers)
    return req2.text

apikey = "f36460022a2cec6d0cbbc49df6e87d69bae856ec"
print(get_poet_names(apikey))

