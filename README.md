# JamaScript

Meet JamaScript, your personal assistant, ready to migrate your data!

## Table of Contents:
- [Required](https://github.com/arthurosipyan/JamaScript#required) 
- [Setup](https://github.com/arthurosipyan/JamaScript#setup) 
- [Running JamaScript](https://github.com/arthurosipyan/JamaScript#running-jamascript)
- [Excel File Format](https://github.com/arthurosipyan/JamaScript#excel-file-format)
- [Additional Notes](https://github.com/arthurosipyan/JamaScript#additional-notes)
- [Author](https://github.com/arthurosipyan/JamaScript#author)
- [License and Code of Conduct](https://github.com/arthurosipyan/JamaScript#license-and-code-of-conduct)
- [Feedback](https://github.com/arthurosipyan/JamaScript#feedback)


## Required:
- [Jama Account](https://www.jamasoftware.com/get-started/) 
- [Client Credentials](http://help.jamasoftware.com/ah/en/get-started/manage-your-profile/set-api-credentials.html) 
- [Python (3.7 or greater or greater)](https://www.python.org/downloads/)
- [Microsoft Excel](https://www.microsoft.com/en-us/store/b/excel-2016?&OCID=AID718530_SEM_xnbrT3OI&gclid=EAIaIQobChMIrq6vo7eS3QIVl1cNCh2kFAvLEAAYASAAEgJdYfD_BwE)


## Setup:

1. Download and unzip [JamaScript](https://github.com/arthurosipyan/JamaScript/archive/master.zip)
2. Open your preferred Python IDE ([PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) is recommended)
3. Navigate to where you saved JamaScript and open it
4. Run ```main.py``` and login with your client credentials
5. Say hello to JamaScript, your personal migrate assistant!

**Note:** Make sure you have the proper packages installed and have "JamaScript" as your "Sources Root"

| Packages        | Version    |
| ----------------|:----------:|
| PyYAML          | 3.13+      |
| certifi         | 2018.4.16+ |
| chardet         | 3.0.4+     |
| docutils        | 0.14+      |
| et-xmlfile      | 1.0.1+     |
| get             | 1.0.3+     |
| idna            | 2.7+       |
| jdcal           | 1.4+       |
| numpy           | 1.15.0+    |
| openpyxl        | 2.5.4+     |
| pandas          | 0.23.3+    |
| pip             | 10.0.1+    |
| post            | 1.0.2+     |
| public          | 1.0.3+     |
| python-dateutil | 2.7.3+     |
| pytz            | 2018.5+    |
| query-string    | 1.0.2+     |
| request         | 1.0.2+     |
| requests        | 2.19.1+    |
| setuptools      | 39.0.1+    |
| six             | 1.11.0+    |
| urllib3         | 1.23+      |
| xlrd            | 1.1.0+     |

## Running JamaScript:
- Once logged in, you will be asked for a ```Project API_ID```. This can be found when viewing one of your projects.
- After confirming that's the project you'd like to work on, you will be prompt with a few options:

1. Add main components with their sets
    - This will ask for a components file and do a basic setup, which includes a set of:
        - Use Cases
        - Functional Requirements
        - Non-Functional Requirements
        - Technical Requirements
        - Test Cases and Defects linked to a Test Management Sub Component

2. Add specific artifacts
    - This will ask you to select what type of artifact you'd like to import
    - After selecting a valid artifact option, you will be asked for the target item's ```ID```, which is where everything will be imported
    - Finally, you'll be asked for a file to be read. Make sure to follow the correct [file format](https://github.com/arthurosipyan/JamaScript#excel-file-format)!

3. Change project
    - Change the current project

4. Exit
    - Terminate

## Excel File Format:

| Artifact Types     | Col 1 | Col 2        | Col 3        | Col 4         | Col 5          | Col 6        |
| -------------------|:-----:|:------------:|:------------:|:-------------:|:--------------:|:------------:|
| **Components**     | Name  |              |              |               |                |              |
| **Use Cases**      | Name  | PreCondition | MainFlow     | PostCondition | AlternateFlows | Blueprint_ID |
| **Requirements**   | Name  | Description  | Blueprint_ID |               |                |              |
| **Wireframes**     | Name  | Blueprint_ID |              |               |                |              |
| **Documents**      | Name  | Description  | Blueprint_ID |               |                |              |
    
**Note:** Blank cells need to have some data for the file to be read. This can be fixed with some placeholder text.


## Additional Notes:

- Image and Attachment imports are **not** available
- While this was developed for the migration process from Blueprint to Jama, it can create new items as well


## Author

* **Arthur Osipyan** - *Developer and Photographer* - [Instagram](https://www.instagram.com/arty.nyc/) [Twitter](https://twitter.com/arty_nyc) [GitHub](https://github.com/arthurosipyan)


## License and Code of Conduct

- This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/arthurosipyan/JamaScript/blob/master/LICENSE) file for details
- This project's Code of Conduct can be found [here](https://github.com/arthurosipyan/JamaScript/blob/master/CODE_OF_CONDUCT.md)

## Feedback

- Found a bug or want to imporve JamaScript? Submit [here](https://github.com/arthurosipyan/JamaScript/issues)!


[Top of Page](https://github.com/arthurosipyan/JamaScript#jamascript)
