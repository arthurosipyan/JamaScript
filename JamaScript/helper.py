import requests
from easygui import multpasswordbox, ynbox, integerbox, ccbox

access_token = ""
base_url = ""
project_api_id = ""
title = "JamaScript"
welcome = ""
current_project = ""


def get_access_token():
    data = {"grant_type": "client_credentials"}
    msg = "Please enter your client credentials and company base url.\nIf you need help finding your credentials, " \
          "please visit:\n" \
          "https://arthurosipyan.github.io/JamaScript/"
    field_names = ["Base URL", "Client ID", "Client Secret"]
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
    base_url = field_values[0]
    username = field_values[1]
    password = field_values[2]
    try:
        requests.post(base_url + "/rest/oauth/token", data=data, auth=(username, password))
    except:
        msg = 'ERROR: Please enter the correct base url.'
        if ccbox(msg, title):
            get_access_token()
        else:
            exit()

    try:
        response = requests.post(base_url + "/rest/oauth/token", data=data, auth=(username, password))
        access_token = response.json()['access_token']
        user = response.json()['application_data']["JAMA_CORE"]
        global welcome
        welcome = ("Welcome, " + user)
    except KeyError:
        response = requests.post(base_url + "/rest/oauth/token", data=data, auth=(username, password))
        msg = ('ERROR: Please enter the correct client credentials.\nSTATUS: ' + str(response.json()['status']) + ' '
               + response.json()['error'] + '\n' + 'MESSAGE: ' + response.json()['message'])
        if ccbox(msg, title):
            get_access_token()
        else:
            exit()


def get_project_name():
    msg = welcome + "\n Please enter the Project API-ID"
    global project_api_id
    project_api_id = integerbox(msg, title, upperbound=1000)
    url = base_url + "/rest/latest/projects/" + str(project_api_id)
    headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
    response = requests.request("GET", url, headers=headers)
    try:
        project_name = response.json()['data']['fields']['name']
        global current_project
        current_project = ("Current project: " + project_name)
        project_confirmation()
    except KeyError:
        msg = ('Please enter the correct Project API-ID.\nStatus: ' + response.json()['meta']['status'] + '\nMessage: '
               + response.json()['meta']['message'])
        if ccbox(msg, title):
            get_project_name()
        else:
            exit()


def project_confirmation():
    msg = current_project + "\n Is this the project you'd like to work on?"
    if ynbox(msg, title):
        pass
    else:
        get_project_name()


get_access_token()
get_project_name()
