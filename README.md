# JamaScript

Meet JamaScript, your personal assistant, ready to migrate your data!

## Table of Contents:
- [Required](https://github.com/arthurosipyan/JamaScript#required) 
- [Setup](https://github.com/arthurosipyan/JamaScript#setup) 
- [Running JamaScript](https://github.com/arthurosipyan/JamaScript#running-jamascript)
- [Excel File Format](https://github.com/arthurosipyan/JamaScript#excel-file-format)
- [Additional Notes](https://github.com/arthurosipyan/JamaScript#additional-notes)
- [Authors](https://github.com/arthurosipyan/JamaScript#authors)
- [License](https://github.com/arthurosipyan/JamaScript#license)
- [Feedback](https://github.com/arthurosipyan/JamaScript#feedback)


## Required:
- [Jama Account](https://www.jamasoftware.com/get-started/) 
- [Client Credentials](http://help.jamasoftware.com/ah/en/get-started/manage-your-profile/set-api-credentials.html) 
- [Python (3.7 or greater or greater)](https://www.python.org/downloads/)

## Setup:

1. Download and unzip [JamaScript](https://github.com/arthurosipyan/JamaScript/archive/master.zip)
2. Open your preferred Python IDE ([PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) is recommended)
3. Navigate to where you saved JamaScript and open it
4. Run ```main.py``` and login with your client credentials
5. Say hello to JamaScript, your personal migrate assistant!

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
| **Documents**      | Name  | Blueprint_ID |              |               |                |              |
    
**Note:** Blank cells need to have some data for the file to be read. This can be fixed with some inserted whitespaces.


## Additional Notes:

- There is a ```templates``` folder for reference
- Image and Attachment imports are **not** available
- While this was developed for the migration process from Blueprint to Jama, it can create new items as well


## Author

* **Arthur Osipyan** - *Developer and Photographer* - [Instagram](https://www.instagram.com/arty.nyc/) [Twitter](https://twitter.com/arty_nyc) [GitHub](https://github.com/arthurosipyan)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/arthurosipyan/JamaScript/blob/master/LICENSE) file for details

## Feedback

- Found a bug? Submit [here](https://github.com/arthurosipyan/JamaScript/blob/master/.github/ISSUE_TEMPLATE/bug_report.md)!
- Help make JamaScript better! Submit your ideas [here](https://github.com/arthurosipyan/JamaScript#feedback)!


[Top of Page](https://github.com/arthurosipyan/JamaScript#jamascript)
