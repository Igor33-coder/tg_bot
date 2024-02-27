from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='🚀 Запустити бота'
        ),
        BotCommand(
            command='help',
            description='🕘 Графік роботи та телефони ☎️'
        ),
        BotCommand(
            command='mail',
            description='✍️ Написати адміну'
        ),
        BotCommand(
            command='clear',
            description='🗑 Очистити ввід'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
