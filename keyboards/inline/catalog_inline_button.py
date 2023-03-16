from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import catalog_id_callback, all_catalog_callback, delete_callback
from API.catalog_API import get_catalog_by_id


def inline_button(ctgrs, lan):
    catalog = []
    catalog_list = []
    for key, value in ctgrs.items():
        catalog.append(InlineKeyboardButton(text=f"{get_catalog_by_id(key, lan)}:{get_catalog_by_id(value, lan)}", callback_data=catalog_id_callback.new(item_name=value)))
        if len(catalog)==1:
            catalog_list.append(catalog)   
            catalog = []
    catalog_list.append(catalog)

    del_cat = [
        InlineKeyboardButton(text="📋 Catalog", callback_data=all_catalog_callback.new(item_name="0")),
        InlineKeyboardButton(text="❌ Delete", callback_data=delete_callback.new(item_name="delete"))
        ]
    catalog_list.append(del_cat)

    catalog_inline = InlineKeyboardMarkup(inline_keyboard=catalog_list)

    return catalog_inline

# back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
# catalog.insert(back_button)