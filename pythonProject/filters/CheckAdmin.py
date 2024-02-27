import os
from aiogram.filters import BaseFilter
from aiogram.types import Message
from utils.database import Database


class CheckAdmin(BaseFilter):
    async def __call__(self, message: Message):
        try:
            db = Database(os.getenv('DATABASE_NAME'))
            users = db.select_user_id(message.from_user.id)
            admin_ids_str = os.getenv('ADMIN_ID', '')
            admin_ids = admin_ids_str.split(',') if admin_ids_str else []
            for admin_id in admin_ids:
                return users[3] in admin_id
        except Exception as e:
            print(f"Error in CheckUser filter: {e}")
            return False
