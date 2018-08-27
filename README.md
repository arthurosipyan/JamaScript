# JamaScript

Meet JamaScript, your personal assistant, ready to migrate your data!

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

2. Add specific requirements/components
    - This will ask you to select what type of artifact you'd like to import
    - After selecting a valid artifact option, you will be asked for the target item's ```ID```, which is where everything will be imported
    - Finally, you'll be asked for a file to be read. Make sure to follow the correct [file format](https://github.com/arthurosipyan/JamaScript#file-format)!

3. Change project
    - Change the current project

4. Exit
    - Terminate

## File Format:

* Components:
    * Col 1 = Name
    
* Use Cases:
    * Col 1 = Name
    * Col 2 = PreCondition
    * Col 3 = MainFlow
    * Col 4 = PostCondition
    * Col 5 = AlternateFlows
    * Col 6 = Blueprint_ID
    
* Requirements:
    * Col 1 = Name
    * Col 2 = Description
    * Col 3 = Blueprint_ID
    
* Wireframes:
    * Col 1 = Name
    * Col 2 = Blueprint_ID

* Documents:
    * Col 1 = Name
    * Col 2 = Blueprint_ID
    
**Note:** Blank cells need to have some data for the file to be read. This can be fixed with some inserted whitespaces.


## Additional Notes:

- There is a ```templates``` folder for reference
- Image and Attachment imports are **not** available
- While this was developed for the migration process from Blueprint to Jama, it can create new items as well


## Authors

* **Arthur Osipyan** - *Developer and Photographer* - [Instagram](https://www.instagram.com/arty.nyc/) [Twitter](https://twitter.com/arty_nyc) [GitHub](https://github.com/arthurosipyan)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/arthurosipyan/JamaScript/blob/master/LICENSE) file for details

