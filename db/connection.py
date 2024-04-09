# app/db/connection.py
from functools import lru_cache
from motor.motor_asyncio import AsyncIOMotorClient

from config.settings import get_settings

class connectToDB():
    def __init__(self) -> None:
        client = AsyncIOMotorClient(get_settings().mongodb_uri)
        self.db = client[get_settings().mongodb_db_name]
        print("db connected")

    def getDbInstance(self):
        return self.db

connection = connectToDB().getDbInstance()

