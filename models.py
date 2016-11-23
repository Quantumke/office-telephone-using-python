from sqlalchemy.engine import create_engine
from sqlalchemy import schema, types, Table, column, String, Integer
metadata = schema.MetaData()

def users():
	ben=Table('users', metadata,
		schema.Column('id', Integer()),
		schema.Column('firstname', String(100), nullable=False),
		schema.Column('lastname', String(100)),
		schema.Column('username', String(100)),
		schema.Column('email_address',String(100)),
		schema.Column('password', String(100)),
		schema.Column('status', Integer())
		)
	engine= create_engine("postgresql://root:master12!@localhost:5432/office_tel")
	metadata.bind= engine
	metadata.create_all(checkfirst=True)


if __name__=="__main__":
	users()