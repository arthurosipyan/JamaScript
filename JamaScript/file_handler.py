import pandas as pd
from easygui import fileopenbox


def get_file():
    return fileopenbox(msg="Please select the excel file you'd wish to migrate", title="JamaScript", default='*', filetypes=".xlsx", multiple=False)


def root_components_file():
    while True:
        root_cmp_file_name = get_file()
        try:
            cmp_excel_file = pd.ExcelFile(root_cmp_file_name)
            df = cmp_excel_file.parse("Sheet1")
            return df.iloc[:, 0].tolist()
        except FileNotFoundError:
            print("Error: File not found")
            root_components_file()


def components_file():
    while True:
        cmp_file_name = get_file()
        try:
            cmp_excel_file = pd.ExcelFile(cmp_file_name)
            df = cmp_excel_file.parse("Sheet1")
            return df.iloc[:, 0].tolist()
        except FileNotFoundError:
            print("Error: File not found")
            components_file()


def use_cases_file():
    while True:
        uc_file_name = get_file()
        try:
            uc_excel_file = pd.ExcelFile(uc_file_name)
            df = uc_excel_file.parse("Sheet1")
            uc_data = dict()
            uc_data["Name"] = df.iloc[:, 0].tolist()
            uc_data["PreCondition"] = df.iloc[:, 1].tolist()
            uc_data["MainFlow"] = df.iloc[:, 2].tolist()
            uc_data["PostCondition"] = df.iloc[:, 3].tolist()
            uc_data["AlternateFlows"] = df.iloc[:, 4].tolist()
            uc_data["Blueprint_ID"] = df.iloc[:, 5].tolist()
            return uc_data
        except FileNotFoundError:
            print("Error: File not found")
            use_cases_file()


def wireframes_file():
    while True:
        wf_file_name = get_file()
        try:
            wf_excel_file = pd.ExcelFile(wf_file_name)
            df = wf_excel_file.parse("Sheet1")
            wf_data = dict()
            wf_data["Name"] = df.iloc[:, 0].tolist()
            wf_data["Blueprint_ID"] = df.iloc[:, 1].tolist()
            return wf_data
        except FileNotFoundError:
            print("Error: File not found")
            wireframes_file()


def requirements_file():
    while True:
        rq_file_name = get_file()
        try:
            rq_excel_file = pd.ExcelFile(rq_file_name)
            df = rq_excel_file.parse("Sheet1")
            rq_data = dict()
            rq_data["Name"] = df.iloc[:, 0].tolist()
            rq_data["Description"] = df.iloc[:, 1].tolist()
            rq_data["Blueprint_ID"] = df.iloc[:, 2].tolist()
            return rq_data
        except FileNotFoundError:
            print("Error: File not found")
            requirements_file()


def documents_file():
    while True:
        rq_file_name = get_file()
        try:
            rq_excel_file = pd.ExcelFile(rq_file_name)
            df = rq_excel_file.parse("Sheet1")
            doc_data = dict()
            doc_data["Name"] = df.iloc[:, 0].tolist()
            doc_data["Description"] = df.iloc[:, 1].tolist()
            doc_data["Blueprint_ID"] = df.iloc[:, 2].tolist()
            return doc_data
        except FileNotFoundError:
            print("Error: File not found")
            documents_file()
