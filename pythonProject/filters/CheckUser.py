import os
from aiogram.filters import BaseFilter
from aiogram.types import Message
from utils.database import Database


class CheckUser(BaseFilter):
    async def __call__(self, message: Message):
        try:
            user_id = message.from_user.id
            db = Database(os.getenv('DATABASE_NAME'))
            users = db.select_user_id(message.from_user.id)
            user = int(users[3])
            return user == user_id
        except Exception as e:
            print(f"Error in CheckUser filter: {e}")
            return False
