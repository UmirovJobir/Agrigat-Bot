from aiogram_media_group import media_group_handler
from aiogram import types, filters
from aiogram import Dispatcher, Bot
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from keyboards.inline.catalog_inline_button import inline_button
from API.langugages import get_language
from API.catalog_API import (
    get_catalog,
    response_uz,
    response_ru,
    response_cyrl
)
import json
from typing import List, Union
from pprint import pprint

def caption_data(message):
    data = json.loads(message)

    user_id = data['user_id']
    fullname = data['fullname']
    group_id = data['group_id']
    group_title = data['group_title']
    group_link = data['group_link']
    message_id = data['message_id']
    message_text = data['message_text']
    message_link = data['message_link']
    catalog_options = data['catalog_options']
    lan = data["lan"]



@dp.message_handler(is_media_group=True, content_types=types.ContentType.ANY)
async def handle_albums(message: types.Message, album: List[types.Message]):
    media_group = types.MediaGroup()
    for obj in album:
        caption = obj.caption
        if caption != None:
                caption = json.loads(caption)

                username = caption["username"]
                user_id = caption["user_id"]
                fullname = ["fullname"]

                group_id = caption["group_id"]
                group_title = caption['group_title']
                group_username = caption['group_username']

                message_id = caption['message_id']
                message_text = caption['message_text']
                message_link = caption["message_link"]

                catalog_options = caption['catalog_options']
                lan = caption["lan"]
                channel = caption["channel"]
  
        if obj.photo:
            file_id = obj.photo[-1].file_id
        else:
            file_id = obj[obj.content_type].file_id

        try:
            # We can also add a caption to each file by specifying `"caption": "text"`
            media_group.attach({"media": file_id, "type": obj.content_type})
        except ValueError:
            return await message.answer("This type of album is not supported by aiogram.")

    if channel=="False": 
        txt  = f"Statusi: Bazaga #joylanmadi\n"
        txt += f"User {username}\n"
        txt += f"Group {group_username}\n"
        txt += f"Message: {message_text}\n"
        txt += f"Message_link: {message_link}"
    
    else:
        txt = "True"


    media_files_id = json.loads(media_group.as_json())
    
    # await bot.send_media_group(-1001578600046, media=media_group)
    await bot.send_message(-1001578600046, text=txt, reply_markup=inline_button(catalog_options, lan), parse_mode=types.ParseMode.HTML)



@dp.message_handler(state=None)
async def bot_echo(message: types.Message, state: FSMContext):
    caption = json.loads(message.text)
    message_text = caption["message_text"]
    catalog_options = caption['catalog_options']
    lan = caption["lan"]

    await state.update_data(lan=lan)
    await message.answer(message_text)



@dp.callback_query_handler(text_contains="catalog_id")
async def buy_books(call: types.CallbackQuery, state: FSMContext):
    callback_data = call.data.split(":")
    
    async with state.proxy() as data:
        print(data)

    await call.message.answer(callback_data)


@dp.callback_query_handler(text_contains="all_catalog")
async def buy_books(call: types.CallbackQuery):
    callback_data = call.data[1]
    catalog = get_catalog(callback_data)

    print(catalog)
    await call.message.answer(catalog)