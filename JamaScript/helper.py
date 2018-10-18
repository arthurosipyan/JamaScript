import requests
from easygui import multpasswordbox, ynbox, integerbox

access_token = ""
base_url = ""
project_api_id = ""
title = "JamaScript"
welcome = ""
current_project = ""


def get_access_token():
    msg = "Please enter your client credentials and company base url"
    field_names = ["Client ID", "Client Secret", "Base URL"]
    field_values = multpasswordbox(msg, title, field_names)
    # make sure that none of the fields was left blank
    while 1:
        if field_values is None:
            break
        errmsg = ""
        for i in range(len(field_names)):
            if field_values[i].strip() == "":
                errmsg = errmsg + ('"%s" is a required field.\n\n' % field_names[i])
        if errmsg == "":
            break  # no problems found
        field_values = multpasswordbox(errmsg, title, field_names, field_values)
    global access_token, base_url
    username = field_values[0]
    password = field_values[1]
    base_url = field_values[2]
    data = {"grant_type": "client_credentials"}
    response = requests.post(base_url + "/rest/oauth/token", data=data, auth=(username, password))
    try:
        access_token = response.json()['access_token']
        user = response.json()['application_data']["JAMA_CORE"]
        global welcome
        welcome = ("Welcome, " + user)
    except KeyError:
        print('Status: ' + str(response.json()['status']) + ' ' + response.json()['error'] + '\n'
              + 'Message: ' + response.json()['message'] + '\nPlease enter the correct client credentials.')
        get_access_token()


def get_project_name():
    msg = welcome + "\n Please enter the Project API-ID"
    global project_api_id
    project_api_id = integerbox(msg, title)
    url = base_url + "/rest/latest/projects/" + str(project_api_id)
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    response = requests.request("GET", url, headers=headers)
    try:
        project_name = response.json()['data']['fields']['name']
        global current_project
        current_project = ("Current project: " + project_name)
        project_confirmation()
    except KeyError:
        print('Status: ' + response.json()['meta']['status'] + '\nMessage: ' + response.json()['meta']['message']
              + '\nPlease enter the correct Project API-ID.\n')
        exit()


def project_confirmation():
    msg = current_project + "\n Is this the project you'd like to work on?"
    if ynbox(msg, title):
        pass
    else:
        get_project_name()


get_access_token()
get_project_name()
