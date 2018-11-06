import json
import requests
from easygui import choicebox, enterbox

from helper import project_api_id, access_token, base_url

title = "JamaScript"
display = ""
artifact_result = ""
main_components_result = ""
component_ids = []
test_management_ids = []
target_item_id = 0
user_choice = 0
main_selection = 0
main2_selection = 0
total_items_imported = 0
original_count = 0
headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}


def add_components_to_root_level(root_cmp_names1):
    global original_count, main_components_result
    original_count = 9 * len(root_cmp_names1)
    url = base_url + "/rest/latest/items?setGlobalIdManually=false"
    for name in root_cmp_names1:
        data = {"project": project_api_id, "itemType": 30,
                "childItemType": 30, "fields": {"name": name}}

        response = requests.request("POST", url, headers=headers, data=json.dumps(data))
        global component_ids
        component_ids.append(response.json()["meta"]["id"])
    main_components_result += ("[" + str(len(component_ids)) + "/" + str(len(root_cmp_names1)) + "] Components "
                                                                                                 "created\n")
    global total_items_imported
    total_items_imported += len(component_ids)


def add_sets_to_components():
    count = []
    child_item_types = ["25", "87", "87", "87", "116"]
    set_names = ["Use Cases", "Functional Requirements", "Non-Functional Requirements", "Technical Requirements",
                 "Wireframes"]
    set_keys = ["UC", "FR", "NFR", "TR", "WF"]
    url = base_url + "/rest/latest/items?setGlobalIdManually=false"
    i = 0
    while 5 > i > -1:
        for item in component_ids:
            data = {"project": project_api_id, "itemType": 31,
                    "childItemType": child_item_types[i], "location":
                        {
                            "parent":
                                {
                                    "item": item
                                }
                        }, "fields": {"setKey": set_keys[i], "name": set_names[i]}
                    }
            response = requests.request("POST", url, headers=headers, data=json.dumps(data))
            count.append(response.json()["meta"]["id"])
        i += 1
    global main_components_result
    main_components_result += ("[" + str(5 * len(component_ids)) + "/" + str(len(count)) + "] Sets of Use Cases, "
                                                                                           "Functional "
                                                                                           "Requirements, "
                                                                                           "Non-Functional "
                                                                                           "Requirements, Technical "
                                                                                           "Requirements, "
                                                                                           "and Wireframes created\n")
    global total_items_imported
    total_items_imported += (5 * len(component_ids))


def add_test_management():
    url = base_url + "/rest/latest/items?setGlobalIdManually=false"
    for item in component_ids:
        data = {"project": project_api_id, "itemType": 30,
                "childItemType": 30, "location": {"parent": {"item": item}}, "fields": {"name": "Test Management"}}
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))
        global test_management_ids
        test_management_ids.append(response.json()["meta"]["id"])
    global main_components_result
    main_components_result += ("[" + str(len(component_ids)) + "/" + str(len(test_management_ids)) + "] Test "
                                                                                                     "Management Sub "
                                                                                                     "Components "
                                                                                                     "created\n")
    global total_items_imported
    total_items_imported += len(component_ids)


def add_test_cases_and_defects():
    count = []
    child_item_types = ["26", "27"]
    set_names = ["Test Cases", "Defects"]
    set_keys = ["TC", "DEF"]
    url = base_url + "/rest/latest/items?setGlobalIdManually=false"
    i = 0
    while 2 > i > -1:
        for item in test_management_ids:
            data = {"project": project_api_id,
                    "itemType": 31,
                    "childItemType": child_item_types[i],
                    "location": {
                        "parent": {
                            "item": item}
                    }, "fields": {"setKey": set_keys[i], "name": set_names[i]}
                    }
            response = requests.request("POST", url, headers=headers, data=json.dumps(data))
            count.append(response.json()["meta"]["id"])
        i += 1
    global main_components_result, total_items_imported
    main_components_result += ("[" + str(len(count)) + "/" + str(2 * len(component_ids)) + "] Sets of Test Cases and "
                                                                                           "Defects created\n")
    total_items_imported += (2 * len(component_ids))
    if original_count == total_items_imported:
        main_components_result += ("\nSuccess, imported [" + str(total_items_imported) + "] items!")
    else:
        main_components_result += ("Failed, only [" + str(total_items_imported) + "] items were imported.")


def get_user_choices():
    choices = ["Component", "Use Case", "Requirement", "Wireframe", "Document", "Go back"]
    global user_choice
    user_choice = choicebox("What artifact type would you like to add?", choices=choices)
    if user_choice == "Go back":
        main()
    else:
        msg = "Please enter the target item's ID"
        document_key = enterbox(msg, title)
        url = base_url + "/rest/latest/abstractitems?project=" \
              + str(project_api_id) + "&documentKey=" + document_key
        response = requests.request("GET", url, headers=headers)
        global target_item_id
        target_item_id = response.json()["data"][0]['id']


def add_uc(uc_data1):
    count = []
    url = base_url + "/rest/latest/items?setGlobalIdManually=false"
    for name, pre, main_flow, post, alt, blueprint_id in zip(uc_data1["Name"], uc_data1["PreCondition"],
                                                             uc_data1["MainFlow"],
                                                             uc_data1["PostCondition"], uc_data1["AlternateFlows"],
                                                             uc_data1["Blueprint_ID"]):
        data = {"project": project_api_id, "itemType": 25,
                "childItemType": 25, "location":
                    {
                        "parent":
                            {
                                "item": target_item_id
                            }
                    }, "fields": {"name": name, "precondition": pre,
                                  "mainflow": main_flow, "postcondition": post, "alternateflows": alt,
                                  "blueprint_id": blueprint_id}
                }
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))
        count.append(response.json()["meta"]["id"])
    global artifact_result
    if len(uc_data1["Name"]) == len(count):
        artifact_result = "Success, imported " + str(len(count)) + " Use Cases!"
    else:
        artifact_result = "Failed, only " + str(len(count)) + " Use Cases imported"


def add_cmp(cmp_name1):
    count = []
    url = base_url + "/rest/latest/items?setGlobalIdManually=false"
    for name in cmp_name1:
        data = {"project": project_api_id, "itemType": 30,
                "childItemType": 30, "location":
                    {
                        "parent":
                            {
                                "item": target_item_id
                            }
                    }, "fields": {"name": name}
                }
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))
        count.append(response.json()["meta"]["id"])
    global artifact_result
    if len(cmp_name1) == len(count):
        artifact_result = "Success, imported [" + str(len(count)) + "] Components!"
    else:
        artifact_result = "Failed, only [" + str(len(count)) + "] Components imported."


def add_rq(rq_data1):
    count = []
    url = base_url + "/rest/latest/items?setGlobalIdManually=false"
    for name, description, blueprint_id in zip(rq_data1["Name"], rq_data1["Description"], rq_data1["Blueprint_ID"]):
        data = {"project": project_api_id, "itemType": 87,
                "childItemType": 87, "location":
                    {
                        "parent":
                            {
                                "item": target_item_id
                            }
                    }, "fields": {"name": name, "description": description, "blueprint_id": blueprint_id}
                }
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))
        count.append(response.json()["meta"]["id"])
    global artifact_result
    if len(rq_data1["Name"]) == len(count):
        artifact_result = "Success, imported [" + str(len(count)) + "] Requirements!"
    else:
        artifact_result = "Failed, only [" + str(len(count)) + "] Requirements were imported."


def add_document(doc_data1):
    count = []
    url = base_url + "/rest/latest/items?setGlobalIdManually=false"
    for name, description, blueprint_id in zip(doc_data1["Name"], doc_data1["Description"], doc_data1["Blueprint_ID"]):
        data = {"project": project_api_id, "itemType": 87,
                "childItemType": 87, "location":
                    {
                        "parent":
                            {
                                "item": target_item_id
                            }
                    }, "fields": {"name": name, "description": description, "blueprint_id": blueprint_id}
                }
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))
        count.append(response.json()["meta"]["id"])
    global artifact_result
    if len(doc_data1["Name"]) == len(count):
        artifact_result = "Success, imported [" + str(len(count)) + "] Documents!"
    else:
        artifact_result = "Failed, only [" + str(len(count)) + "] Documents imported."


def add_wf(wf_data1):
    count = []
    url = base_url + "/rest/latest/items?setGlobalIdManually=false"
    for name, blueprint_id in zip(wf_data1["Name"], wf_data1["Blueprint_ID"]):
        data = {"project": project_api_id, "itemType": 116,
                "childItemType": 116, "location":
                    {
                        "parent":
                            {
                                "item": target_item_id
                            }
                    }, "fields": {"name": name, "blueprint_id": blueprint_id}
                }
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))
        count.append(response.json()["meta"]["id"])
    global artifact_result
    if len(wf_data1["Name"]) == len(count):
        artifact_result = "Success, imported [" + str(len(count)) + "] Wireframes!"
    else:
        artifact_result = "Failed, only [" + str(len(count)) + "] Wireframes imported."


def add_requirements():
    global display
    if user_choice == "Component":
        from file_handler import components_file
        add_cmp(components_file())
        display = artifact_result
        main2()
    elif user_choice == "Use Case":
        from file_handler import use_cases_file
        add_uc(use_cases_file())
        display = artifact_result
        main2()
    elif user_choice == "Requirement":
        from file_handler import requirements_file
        add_rq(requirements_file())
        display = artifact_result
        main2()
    elif user_choice == "Wireframe":
        from file_handler import wireframes_file
        add_wf(wireframes_file())
        display = artifact_result
        main2()
    elif user_choice == "Document":
        from file_handler import documents_file
        add_document(documents_file())
        display = artifact_result
        main2()
    else:
        print("Error")
        get_user_choices()


def main2():
    choices = ["Add artifacts", "Change project"]
    global main2_selection
    main2_selection = choicebox(display + "\n\n What else would you like to do?", choices=choices, title=title)
    if main2_selection == "Add artifacts":
        get_user_choices()
        add_requirements()
    elif main2_selection == "Change project":
        from helper import get_project_name
        get_project_name()
        main()
    else:
        exit()


def main():
    choices = ["Add main components with their sets", "Add artifacts", "Change project"]
    global main_selection, display
    main_selection = choicebox("What would you like to do?", choices=choices, title=title)
    if main_selection == "Add main components with their sets":
        from file_handler import root_components_file
        add_components_to_root_level(root_components_file())
        add_sets_to_components()
        add_test_management()
        add_test_cases_and_defects()
        display = main_components_result
        main2()
    elif main_selection == "Add artifacts":
        get_user_choices()
        add_requirements()
        display = artifact_result
    elif main_selection == "Change project":
        from helper import get_project_name
        get_project_name()
        main()
    else:
        exit()


if __name__ == '__main__':
    main()
