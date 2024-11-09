import sqlalchemy, sqlalchemy_utils as sqlu

def CreateEngine( engineURL= None):
    if engineURL == None :
        engine = sqlalchemy.create_engine("postgresql://localhost/mydb")
        if not sqlu.database_exists(engine.url):
            sqlu.create_database(engine.url)