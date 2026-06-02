# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery

API_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = '@jokertestik'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Проверка подписки
async def is_subscribed(user_id: int):
    try:
        member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            return True
        return False
    except:
        return False

# Кнопки
def main_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Перейти на канал", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")
        ],
        [
            InlineKeyboardButton(text="Проверить подписку", callback_data="check_sub")
        ]
    ])
    return keyboard

# /start
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Нажми кнопку ниже:", reply_markup=main_keyboard())

# Проверка по кнопке
@dp.callback_query(lambda c: c.data == "check_sub")
async def check(callback: CallbackQuery):
    if await is_subscribed(callback.from_user.id):
        await callback.answer("✅ Ты подписан!", show_alert=True)
    else:
        await callback.answer("❌ Подпишись на канал!", show_alert=True)

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())