from backend_testing import postRequest, getRequest, checkPostUserStoredInDB
from fronted_testing import checkIfIDExistOnBrowser

# inputUserID = input('enter a user ID: ')
# inputUserName = input('enter a user name: ')

# api_url = 'http://127.0.0.1:5000/users/' + inputUserID
api_url = 'http://127.0.0.1:5000/users/1'
userData = {'user_name': 'yosi1'}

def TestCombined():
    # Post any new user data to the REST API using POST method.
    print('\n*********** postRequest ***********\n')
    apiUserName = postRequest(api_url, userData)

    # Submit a GET request to make sure data equals to the posted data
    print('\n*********** getRequest ***********\n')
    getRequest(api_url, apiUserName)

    # Using pymysql, check posted data was stored inside DB (users table)
    print('\n*********** checkPostUserStoredInDB ***********\n')
    checkPostUserStoredInDB('1', apiUserName)

    # Navigate to web interface URL using an existing user id
    # Check that the userName element is showing (web element exists)
    # Print userName (using locator)
    print('\n*********** checkIfIDExistOnBrowser ***********\n')
    # url = 'http://127.0.0.1:5001/users/get_user_data/' + inputUserID
    url = 'http://127.0.0.1:5001/users/get_user_data/1'
    browserUserName = checkIfIDExistOnBrowser(url)
    msg = f'browserUserName: {browserUserName} \n' \
          f'apiUserName: {apiUserName} \n\n'
    if (browserUserName == apiUserName):
        print(msg + 'names are equal')
    else:
        print(msg + 'names are NOT equal (browserUserName != apiUserName)')

try:
    TestCombined()
except Exception as e:
    print('test failed because: ', str(e))
    raise Exception('test failed')

# import clean_environment
# print('\n*********** stopRestServer ***********\n')
# clean_environment.stopRestServer()
# print('\n*********** stopWebServer ***********\n')
# clean_environment.stopWebServer()