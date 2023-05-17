import requests

def stopRestServer():
    msg = ''
    try:
        requests.get('http://127.0.0.1:5000/stop_server')
        msg = 'Rest server stopped\n'
    except requests.exceptions.RequestException as ex:
        msg = 'rest server didnt stop because: \n' + str(ex) + '\n'
    return msg

def stopWebServer():
    msg = ''
    try:
        requests.get('http://127.0.0.1:5001/stop_server')
        msg = 'Web server stopped\n'
    except requests.exceptions.RequestException as ex:
        msg = 'web server didnt stop because: \n' + str(ex)
    return msg

if __name__ == "__main__":
    print(stopRestServer())
    print(stopWebServer())