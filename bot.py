import json
import asyncio
from pathlib import Path
from datetime import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

bot = Bot(token=TOKEN,parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

db_file = Path('db.json')

def read_db():
    if not db_file.exists():
        return {}
    with db_file.open('r',encoding='utf-8') as f:
        return json.load(f)

def write_db(data):
    with db_file.open('w',encoding='utf-8') as f:
        return json.dump(data,f,indent=2, ensure_ascii=False)

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(KeyboardButton("/new"), KeyboardButton("/notes"))

class NoteForm(StatesGroup):
    title = State()
    description = State()
    remind_at = State()


