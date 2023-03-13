from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import catalog_callback
from API.catalog_API import get_catalog, get_catalog_by_id



def inline_button(ctgrs, lan):
    catalog = InlineKeyboardMarkup(row_width=1)
    for key, value in ctgrs.items():
        catalog.insert(InlineKeyboardButton(text=f"{get_catalog_by_id(key, lan)}:{get_catalog_by_id(value, lan)}", callback_data=catalog_callback.new(item_name=value)))
    return catalog

# back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
# catalog.insert(back_button)