import databases
import ormar
import sqlalchemy

url = 'sqlite:///crud_test.db'
metadata = sqlalchemy.MetaData()
database = databases.Database(url)
engine = sqlalchemy.create_engine(url)


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database