import requests #http requests
import socket #check whether localhost is connected

def check_localhost():
        localhost = socket.gethostbyname('localhost')
        if localhost == "127.0.0.1":
                return True
        else:
                return 0

def check_connectivity():
        request = requests.get("http://www.google.com")
        status_code = request
        print(status)
        # if status_code == "200":
        #         return True
        # else:
        #         return 0

#print(check_localhost() and check_connectivity())
request = requests.get("http://www.google.com")

print(request.status_code)