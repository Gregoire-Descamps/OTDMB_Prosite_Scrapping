## Prosite project
### Hemery Maxence & Descamps Gregoire
# Goals of the project

The goal of the project is to scrap content from an online HTML page, and more specifically a grid containing information about prosite motifs.
The fields to be output are "AC", "ID", "entry_type" and "Description". 
Once those have been retrieved after scrapping the html pages, they must be stored in a mySQL database.

# Methodology

In order to work easily together on this project, a github repository has been set up.
We decided to use modules for this project in order to make it clear and more organized. 
It was also made with the user's comfort in mind, for instance:
- installation of necessary resources are automated and can be easily modified by said-user.
- the database is automatically generated and the user is prompted to register themselves (using secure terminal input) to access it.

These modules include:

### - A main.py script

Runs all of the other scripts located in this project.
Automates installation of APIs and any other resources required for the code to work.

### - A BeautifulSoup.py script

Scraps the content from the prosite website, and successfully retrieves the required data inside of a list, which is used to copy this data over to the database.

### - A ScrapPySQL.py script

Responsible for creating the mySQL database, generating and managing the database connection and population.
It's based on the [SQLAlchemy](https://www.sqlalchemy.org/) package and the ORM( Object Relationnal Mapper) approach.


### - A requirements.txt file

This file contains the name of every python APIs required. 
The user can install other APIs if needed by adding their name in this file, and then running the main.py script again.


# Reached/Unreached Goals (+ Discussion)

### Reached Goals:

Every goal set here have been reached: we managed to make a project which can be easily modified and understood by an user.


### Discussion:

While we cannot ensure for how long the beautifulsoup script will work, it was made to last as long as possible. 
For instance, columns of the required fields are not retrieved using the index as we see it on the page, but by searching for the actual name of the field, and only then retrieving the index. 
However, one of the main downside of this project is the time it takes to successfully retrieves all the required information as it can easily take between 5 and 10 minutes.
On top of that, to reduce database transaction time, the scrapped data get loaded separately instead of creating the objects "on the fly". 
This requires creating a data list and duplicate its content in the database objects. Here we made the choice of database performance over program and system memory.
Aside from this downside, the project is suited for any user thanks to its clarity and its user-friendly interface.


