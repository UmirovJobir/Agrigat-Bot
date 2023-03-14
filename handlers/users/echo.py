from aiogram_media_group import media_group_handler
from aiogram import types, filters
from aiogram import Dispatcher, Bot
from loader import dp
from keyboards.inline.callback_data import catalog_callback
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
    fullnamedata = ['fullname']
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
    """This handler will receive a complete album of any type."""
    media_group = types.MediaGroup()
    for obj in album:
        caption = obj.caption
        if caption != None:
                caption = json.loads(caption)
                message_text = caption["message_text"]
                print(message_text)
                catalog_options = caption['catalog_options']
                lan = caption["lan"]

        if obj.photo:
            file_id = obj.photo[-1].file_id
        else:
            file_id = obj[obj.content_type].file_id

        try:
            # We can also add a caption to each file by specifying `"caption": "text"`
            media_group.attach({"media": file_id, "type": obj.content_type})
        except ValueError:
            return await message.answer("This type of album is not supported by aiogram.")

    a = json.loads(media_group.as_json())
    for i in a:
        print(i)

    await message.answer_media_group(media_group)
    await message.answer(message_text, reply_markup=inline_button(catalog_options, lan))
    
    # await message.answer_media_group(chat_id=-1001763109051, media=media_group)
    # await message.answer(chat_id=-1001763109051, text=message_text, reply_markup=inline_button(catalog_options, lan))

# 
# Echo photo bot

# @dp.message_handler(content_types=types.ContentType.ANY)
# async def album_handler(message: types.Message):
    
    
    
    # await messages[-1].reply_media_group(
    #     [
    #         types.InputMediaPhoto(
    #             media=m.photo[-1].file_id,
    #             caption=m.caption,
    #             caption_entities=m.caption_entities,
    #         )
    #         for m in messages
    #     ]
    # )



# Echo bot
# @dp.message_handler(state=None, content_types=types.ContentType.ANY)
# async def bot_echo(message: types.Message):
    # data = message.text
    # data = json.loads(data)

    # user_id = data['user_id']
    # fullnamedata = ['fullname']
    # group_id = data['group_id']
    # group_title = data['group_title']
    # group_link = data['group_link']
    # message_id = data['message_id']
    # message_text = data['message_text']
    # message_link = data['message_link']
    # catalog_options = data['catalog_options']
    # lan = data["lan"]

    # if message.media_group_id != None:
    #     album = types.MediaGroup()
        
        
        # id = message.photo[0]
        # print(id)
        # album.attach_photo(photo=id)
        # for i in message:
        #     print(i'photo')
        # await message.reply_media_group(media=album)
    # elsie:
    #     prnt(message)
    # if message.media_group_id != None:
    #     if len(message_text.split()) > 3:
    #         categories = get_language(
    #             data['message_text'], response_ru, response_cyrl, response_uz)
    #         print(categories)   

    # await message.answer_photo(id)#, reply_markup=inline_button(catalog_options, lan))



@dp.callback_query_handler(text_contains="catalog")
async def buy_books(call: types.CallbackQuery):
    callback_data = call.data.split(":")
    print(callback_data[1])

    await call.message.answer(callback_data)


# @dp.callback_query_handler(text="cancel")
# async def cancel_buying(call: CallbackQuery):
#     # Oynada javob qaytaramiz

#     await call.message.edit_reply_markup(reply_markup=inline_button(catalog_options))
#     await call.answer()
