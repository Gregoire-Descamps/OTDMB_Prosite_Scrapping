import getpass

from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy_utils import create_database, database_exists
import pymysql


# The Database Model
class PrositeBase(DeclarativeBase):
    pass

# The Entry table model
class Entry(PrositeBase):
    __tablename__ = "Entry"

    Accession_Num: Mapped[str] = mapped_column(String(7),primary_key=True)
    id: Mapped[str] = mapped_column(String(30))
    entry_type : Mapped[str] = mapped_column(String(7))
    description : Mapped["Description"] = relationship(back_populates="entry")

# The Description table model
class Description(PrositeBase):
    __tablename__ = "Description"

    Accession_Num: Mapped[str] = mapped_column(String(7), ForeignKey(Entry.Accession_Num), primary_key=True)
    description: Mapped[str] = mapped_column(String(10000))
    entry : Mapped["Entry"] = relationship(back_populates="description")

# A DataBase Connection
# Initialize a connection to the DataBase prompting for user credentials.
# If the DB doesn't exist, automatically generate one.
class DBConnection:

    # Password is retrieved using getpass.
    # It allows to hide the user typed characters but require access to the terminal output
    def __init__(self):
        self._username = input("Enter your DataBase User Name: ")
        print(f"Let's connect {self._username}!\n(If you're on IDE and the code stop running here, make sure you enabled terminal emulation!)")
        self.__psw = getpass.getpass(prompt=f"Enter database password for user {self._username} :")
        self.engine = self.CreateEngine()


    # get the URL of the database (for security purposes, shouldn't be used outside the class methods)
    def __URL__(self):
        return URL.create(drivername="mysql+pymysql", username=self._username,password=self.__psw,  host="localhost", database="PrositeLocalDB")

    # Create the DB engine to connect to a DB
    def CreateEngine(self):

        # Check for DB, if it doesn't exist, create one
        if not database_exists(self.__URL__()):
            print("Prosite DataBase were not found, creating one...")
            self.__CreateDB__()
            print("DataBase Prosite successfully created!")

        return create_engine(self.__URL__())


    # Create the database.
    # Use temporary connection engine and PrositeBase() defined Class and childs to create the DB
    def __CreateDB__(self):
        create_database(self.__URL__())
        tempEngine = create_engine(self.__URL__())
        thisDB = PrositeBase()
        thisDB.metadata.create_all(tempEngine)

    # "Commit as you go" method
    def con(self):
        return self.engine.connect()

    # "Begin once" method
    def begin(self):
        return self.engine.begin()

    # Session method, allow to initialize a session and instantiate entry objects for the DB
    def session(self):
        return Session(self.engine)

    #Load Prosite Scrapped data into the database
    def PrositeLoader(self, EntryList):
        DBObjects = []
        with self.session() as session:
            for item in EntryList:
                DBObjects.append(Entry(Accession_Num = item['AC'], id= item['ID'], entry_type=item['entry_type'] , description = Description(description =item['description'])))
            session.add_all(DBObjects)
            session.commit()

