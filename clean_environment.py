import requests

def stopRestServer():
    try:
        requests.get('http://127.0.0.1:5000/stop_server')
        # res = requests.get('http://localhost:5000')
        # if res.status_code == 200:
        #     requests.get('http://127.0.0.1:5000/stop_server')
    except requests.exceptions.RequestException as ex:
        return 'rest server didnt stop because: ', str(ex)

def stopWebServer():
    try:
        requests.get('http://127.0.0.1:5001/stop_server')
    except requests.exceptions.RequestException as ex:
        return 'web server didnt stop because: ', str(ex)

if __name__ == "__main__":
    stopRestServer()
    stopWebServer()