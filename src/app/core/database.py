import asyncio

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://lab_sult_db:27017/test")
client.get_io_loop = asyncio.get_running_loop

database = client["lab_sult"]

user_collection = database.get_collection("user_collection")
