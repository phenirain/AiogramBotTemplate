from aiogram import types, Router, F, Bot
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.state import StatesGroup, State
import os
from filters.chat_types import ChatTypeFilter
from typing import Any


class AnyState(StatesGroup):
    any = State()


any_router = Router()
any_router.message.filter(ChatTypeFilter(['private', 'superuser']))

@any_router.message(StateFilter('*'), CommandStart)
async def start(message: Message, state: FSMContext):
    pass