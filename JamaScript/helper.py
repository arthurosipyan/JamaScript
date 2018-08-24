import requests

access_token = ""
project_api_id = ""


def get_access_token():
    print("______________________________________________________\n")
    client_id = input('Enter your client id: ')
    client_secret = input('Enter your client secret: ')
    print("______________________________________________________\n")
    username = client_id
    password = client_secret
    base_url = "https://fitchratings.jamacloud.com/rest/oauth/token"
    data = {"grant_type": "client_credentials"}
    response = requests.post(base_url, data=data, auth=(username, password))
    global access_token
    try:
        access_token = response.json()['access_token']
        user = response.json()['application_data']["JAMA_CORE"]
        print("Welcome, " + user.split(".")[0].title() + " " + user.split(".")[1].title() + "\n"
              + "______________________________________________________\n")
    except KeyError:
        print('Status: ' + str(response.json()['status']) + ' ' + response.json()['error'] + '\n'
              + 'Message: ' + response.json()['message'] + '\nPlease enter the correct client credentials.')
        get_access_token()


def get_project_name():
    global project_api_id
    project_api_id = input("Enter the Project API-ID: ")
    print("______________________________________________________\n")
    url = "https://fitchratings.jamacloud.com/rest/latest/projects/" + project_api_id
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    response = requests.request("GET", url, headers=headers)
    try:
        project_name = response.json()['data']['fields']['name']
        print("Current project: " + project_name + "\n"
                                                   "______________________________________________________\n")
        project_confirmation()
    except KeyError:
        print('Status: ' + response.json()['meta']['status'] + '\nMessage: ' + response.json()['meta']['message']
              + '\nPlease enter the correct Project API-ID.\n'
                '______________________________________________________\n')
        get_project_name()


def project_confirmation():
    user_confirmation = input("Is this the project you'd like to work on? (y/n) ")
    print("______________________________________________________\n")
    if user_confirmation.lower() == 'n':
        get_project_name()
    elif user_confirmation.lower() != 'y':
        print("Error: Please enter a valid option.")
        print("______________________________________________________\n")
        project_confirmation()


get_access_token()
get_project_name()
