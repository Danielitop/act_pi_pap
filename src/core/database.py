from databases import Database
from core import config

database = Database(config.DATABASE_URL)

async def connect():
    await database.connect()

async def disconnect():
    await database.disconnect()
