#this problem is about accessing api endpoints. 

#stackmaps has an api endpoint you will access for this problem.  the address is:

#https://www.stackmaps.com/api/ping
#please write a function called ping which uses the python requests library to access the stackmaps api endpoint given above.  because you will be making a get request, you will need to use the get() method from the requests library.  your function should take in a single parameter.  if that parameter is an integer or a float, your function should pass it to the api endpoint using the parameter name x_value and return the value returned by the api.

#if your function is given a parameter which is not an integer and not a float, your function should return none.

#please assume that the following import statement has already been made:

#from requests import get
#do not add any additional import statements to your code.


#spend five minutes skimming the documentation about the python requests library.  you can access that documentation here:

#https://requests.readthedocs.io/en/master/

#and you can read about the get() method here:

#https://requests.readthedocs.io/en/master/api/#requests.get

#note! your function must be named ping      


from requests import get
# Do not add any import statements

def ping(x_value):
    # your code goes here
    try:
        url = "https://www.stackmaps.com/api/ping/?x_value="+str(x_value)
        req = get(url)
        r = req.json()
        rr = r['result_value']
        return rr
    except:
        return None

print(ping(2))

