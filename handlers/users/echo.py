from aiogram import types
from loader import dp
from aiogram.types import Message, CallbackQuery
from keyboards.inline.callback_data import catalog_callback
from keyboards.inline.catalog_inline_button import inline_button
from API.catalog_API import get_catalog
import json
from pprint import pprint

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    data = message.text
    data = json.loads(data)

    user_id = data['user_id']
    fullnamedata = ['fullname']
    group_id = data['group_id']
    group_title = data['group_title']
    group_link = data['group_link']
    message_id = data['message_id']
    message_text = data['message_text']
    message_link = data['message_link']
    catalog_options = data['catalog_options']

    await message.answer('Katalog', reply_markup=inline_button(catalog_options))
    
@dp.callback_query_handler(text_contains="catalog")
async def buy_books(call: CallbackQuery):
    callback_data = call.data.split(":")
    print(callback_data)
    
    await call.message.answer(callback_data)

# @dp.callback_query_handler(text="cancel")
# async def cancel_buying(call: CallbackQuery):
#     # Oynada javob qaytaramiz

#     await call.message.edit_reply_markup(reply_markup=inline_button(catalog_options))
#     await call.answer()

    