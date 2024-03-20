from sqlalchemy import Integer, and_, func, insert, select, text, update
from sqlalchemy.orm import aliased
from models import worker_t

from database import sync_engine
from models import metadata_obj

def create_table():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)

def insert_data():
    with sync_engine.connect() as conn:
        # stmt = """INSERT INTO workers VALUES (NULL, 'evgen', 'evgen@mail.ru')"""
        stmt = insert(worker_t).values(username='evgen2', email="evgen2@mail.ru")
        conn.execute(stmt)
        conn.commit()