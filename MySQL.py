import getpass

from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import Session,  DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy_utils import create_database, database_exists
import pymysql


# The Database Model
class PrositeBase(DeclarativeBase):
    pass

class Entry(PrositeBase):
    __tablename__ = "Entry"

    Accession_Num: Mapped[str] = mapped_column(String(7),primary_key=True)
    id: Mapped[str] = mapped_column(String(30))
    entry_type : Mapped[str] = mapped_column(String(7))
    Description : Mapped["Description"] = relationship(back_populates="Entry")


class Description(PrositeBase):
    __tablename__ = "Description"

    Doc_ac : Mapped[str] = mapped_column(String(9), primary_key=True)
    description: Mapped[str] = mapped_column(String(10000))
    last_update_date : Mapped[str] = mapped_column(String(14))
    last_update_type: Mapped[str] = mapped_column(String(50))
    Entry : Mapped[list["Entry"]] = relationship(back_populates="description")






# A DataBase Connection
class DBConnection:
    def __init__(self):
        self._username = input("Enter your DataBase User Name: ")
        print(f"Let's connect {self._username}!\n(If you're on IDE and the code stop running from here, make sure you enabled terminal emulation!")
        self.engine = self.CreateEngine()


    # get the URL of the database (for security purposes, shouldn't be used outside the class methods)
    def __URL__(self):
        return f"mysql+pymysql://{self._username}:{getpass.getpass(prompt=f"Enter database password for user {self._username} :")}@localhost/PrositeLocalDB"

# Create the DB engine to connect to a DB
    def CreateEngine(self):
        if not database_exists(self.__URL__()):
            self.__CreateDB__()

        return create_engine(self.__URL__())


    # Create the database
    def __CreateDB__(self):
        create_database(self.__URL__())
        tempEngine = create_engine(self.__URL__())
        thisDB = PrositeBase()
        thisDB.metadata.create_all(tempEngine)


    def con(self):
        return self.engine.connect()

    def begin(self):
        return self.engine.begin()