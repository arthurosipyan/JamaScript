import json
import requests

from helper import project_api_id, access_token

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
    global original_count
    original_count = 9 * len(root_cmp_names1)
    url = "https://fitchratings.jamacloud.com/rest/latest/items?setGlobalIdManually=false"
    print("*** Attempting to create [" + str(original_count) + "] items...")
    for name in root_cmp_names1:
        data = {"project": project_api_id, "itemType": 30,
                "childItemType": 30, "fields": {"name": name}}

        response = requests.request("POST", url, headers=headers, data=json.dumps(data))
        global component_ids
        component_ids.append(response.json()["meta"]["id"])
    print("*** [" + str(len(component_ids)) + "/" + str(len(root_cmp_names1)) + "] Components created")
    global total_items_imported
    total_items_imported += len(component_ids)


def add_sets_to_components():
    count = []
    child_item_types = ["25", "87", "87", "87", "116"]
    set_names = ["Use Cases", "Functional Requirements", "Non-Functional Requirements", "Technical Requirements",
                 "Wireframes"]
    set_keys = ["UC", "FR", "NFR", "TR", "WF"]
    url = "https://fitchratings.jamacloud.com/rest/latest/items?setGlobalIdManually=false"
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
    print("*** [" + str(5 * len(component_ids)) + "/" + str(len(count)) + "] sets of Use Cases, Functional "
                                                                          "Requirements, "
                                                                          "Non-Functional Requirements, Technical "
                                                                          "Requirements, "
                                                                          "and Wireframes created")
    global total_items_imported
    total_items_imported += (5 * len(component_ids))


def add_test_management():
    url = "https://fitchratings.jamacloud.com/rest/latest/items?setGlobalIdManually=false"
    for item in component_ids:
        data = {"project": project_api_id, "itemType": 30,
                "childItemType": 30, "location": {"parent": {"item": item}}, "fields": {"name": "Test Management"}}
        response = requests.request("POST", url, headers=headers, data=json.dumps(data))
        global test_management_ids
        test_management_ids.append(response.json()["meta"]["id"])
    print("*** [" + str(len(component_ids)) + "/" + str(len(test_management_ids)) + "] Test Management Sub Components "
                                                                                    "created")
    global total_items_imported
    total_items_imported += len(component_ids)


def add_test_cases_and_defects():
    count = []
    child_item_types = ["26", "27"]
    set_names = ["Test Cases", "Defects"]
    set_keys = ["TC", "DEF"]
    url = "https://fitchratings.jamacloud.com/rest/latest/items?setGlobalIdManually=false"
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
    print("*** [" + str(len(count)) + "/" + str(2 * len(component_ids)) + "] sets of Test Cases and Defects created")
    print("______________________________________________________")
    global total_items_imported
    total_items_imported += (2 * len(component_ids))
    if original_count == total_items_imported:
        print("*** Success, imported [" + str(total_items_imported) + "] items!")
    else:
        print("*** Failed, only [" + str(total_items_imported) + "] items were imported.")
        exit()


def confirm_artifact_choice():
    user_confirm = input("Is this the artifact you'd like to add? (y/n) ")
    print("______________________________________________________\n")
    if user_confirm.lower() == 'n':
        get_user_choices()
    elif user_confirm.lower() != 'y':
        print("Error: Please enter a valid option.")
        print("______________________________________________________\n")
        confirm_artifact_choice()


def get_user_choices():
    print("______________________________________________________\n"
          "What artifact type would you like to add?\n"
          "______________________________________________________\n"
          "[1] Component\n"
          "[2] Use Case\n"
          "[3] Requirement\n"
          "[4] Wireframe\n"
          "[5] Document\n"
          "[6] Go back\n"
          "[7] Exit\n"
          "______________________________________________________\n")
    global user_choice
    user_choice = int(input("______________________________________________________\n"
                            "Enter the number choice: "))
    if user_choice == 7:
        quit()
    elif user_choice == 6:
        main()
    elif user_choice not in range(1, 7):
        print("______________________________________________________\n"
              "Error: Please enter a valid number.\n"
              "______________________________________________________\n")
        get_user_choices()
    else:
        confirm_artifact_choice()
        document_key = input("Enter item's ID: ")
        print("______________________________________________________\n")
        url = "https://fitchratings.jamacloud.com/rest/latest/abstractitems?project=" \
              + project_api_id + "&documentKey=" + document_key
        response = requests.request("GET", url, headers=headers)
        global target_item_id
        target_item_id = response.json()["data"][0]['id']


def add_uc(uc_data1):
    count = []
    print("*** Attempting to import [" + str(len(uc_data1["Name"])) + "] Use Cases...")
    url = "https://fitchratings.jamacloud.com/rest/latest/items?setGlobalIdManually=false"
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
    if len(uc_data1["Name"]) == len(count):
        print("*** Success, imported [" + str(len(count)) + "] Use Cases!")
    else:
        print("*** Failed, only [" + str(len(count)) + "] Use Cases imported.")


def add_cmp(cmp_name1):
    count = []
    print("*** Attempting to import [" + str(len(cmp_name1)) + "] Components...")
    url = "https://fitchratings.jamacloud.com/rest/latest/items?setGlobalIdManually=false"
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
    if len(cmp_name1) == len(count):
        print("*** Success, imported [" + str(len(count)) + "] Components!")
    else:
        print("*** Failed, only [" + str(len(count)) + "] Components imported.")


def add_rq(rq_data1):
    count = []
    print("*** Attempting to import [" + str(len(rq_data1["Name"])) + "] Requirements...")
    url = "https://fitchratings.jamacloud.com/rest/latest/items?setGlobalIdManually=false"
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
    if len(rq_data1["Name"]) == len(count):
        print("*** Success, imported [" + str(len(count)) + "] Requirements!")
    else:
        print("*** Failed, only [" + str(len(count)) + "] Requirements were imported.")


def add_document(doc_data1):
    count = []
    print("*** Attempting to import [" + str(len(doc_data1["Name"])) + "] Documents...")
    url = "https://fitchratings.jamacloud.com/rest/latest/items?setGlobalIdManually=false"
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
    if len(doc_data1["Name"]) == len(count):
        print("*** Success, imported [" + str(len(count)) + "] Documents!")
    else:
        print("*** Failed, only [" + str(len(count)) + "] Documents imported.")


def add_wf(wf_data1):
    count = []
    print("*** Attempting to import [" + str(len(wf_data1["Name"])) + "] Wireframes...")
    url = "https://fitchratings.jamacloud.com/rest/latest/items?setGlobalIdManually=false"
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
    if len(wf_data1["Name"]) == len(count):
        print("*** Success, imported [" + str(len(count)) + "] Wireframes!")
    else:
        print("*** Failed, only [" + str(len(count)) + "] Wireframes imported.")


def add_requirements():
    if user_choice == 1:
        from file_handler import components_file
        add_cmp(components_file())
        main2()
    elif user_choice == 2:
        from file_handler import use_cases_file
        add_uc(use_cases_file())
        main2()
    elif user_choice == 3:
        from file_handler import requirements_file
        add_rq(requirements_file())
        main2()
    elif user_choice == 4:
        from file_handler import wireframes_file
        add_wf(wireframes_file())
        main2()
    elif user_choice == 5:
        from file_handler import documents_file
        add_document(documents_file())
        main2()
    else:
        print("Error")
        get_user_choices()


def main2():
    global main2_selection
    main2_selection = int(input("______________________________________________________\n"
                                "_________ What else would you like to do? ____________\n"
                                "______________________________________________________\n"
                                "[1] Add artifacts\n"
                                "[2] Change project\n"
                                "[3] Exit\n"
                                "______________________________________________________\n"))

    if main2_selection == 1:
        get_user_choices()
        add_requirements()
    elif main2_selection == 2:
        from helper import get_project_name
        get_project_name()
        main()
    elif main2_selection == 3:
        quit()
    else:
        print("______________________________________________________\n"
              "Error: Please enter a valid number.\n"
              "______________________________________________________\n")
        main2()


def main():
    global main_selection
    main_selection = int(input("_____________ What would you like to do? _____________\n"
                               "______________________________________________________\n"
                               "[1] Add main components with their sets\n"
                               "[2] Add artifacts\n"
                               "[3] Change project\n"
                               "[4] Exit\n"
                               "______________________________________________________\n"))
    print("______________________________________________________")

    if main_selection == 1:
        main_cmp_confirm = input("Would you like to add main components and their sets (y/n): ")
        if main_cmp_confirm == 'y':
            from file_handler import root_components_file
            add_components_to_root_level(root_components_file())
            add_sets_to_components()
            add_test_management()
            add_test_cases_and_defects()
            main2()
        elif main_cmp_confirm == 'n':
            main()
        else:
            print("Please enter a valid option (y/n)")
            main()
    elif main_selection == 2:
        get_user_choices()
        add_requirements()
    elif main_selection == 3:
        from helper import get_project_name
        get_project_name()
        main()
    elif main_selection == 4:
        quit()
    else:
        print("Error: Please enter a valid number.\n"
              "______________________________________________________\n")
        main()


if __name__ == '__main__':
    main()
