from sqlalchemy import Column, Integer, String

from Database import db


class ListEntry(db.Model):
    __table_name__ = "list_entries"

    id = Column(Integer, primary_key=True)

    title = Column(String)
