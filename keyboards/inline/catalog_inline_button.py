from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import catalog_callback
from API.catalog_API import get_catalog


for i in get_catalog(key):
            for j in get_catalog(value):
                print(i, j)

def inline_button(ctgrs):
    catalog = InlineKeyboardMarkup(row_width=1)
    for key, value in ctgrs.items():
        catalog.insert(InlineKeyboardButton(text=f"{key}:{value}", callback_data=catalog_callback.new(item_name=f"{key}/{value}")))
    return catalog

# back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
# catalog.insert(back_button)