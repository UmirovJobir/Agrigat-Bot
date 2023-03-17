from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import catalog_id_callback, all_catalog_callback, delete_callback
from API.catalog_API import get_catalog_by_id, get_catalog


def inline_button(ctgrs, lan):
    catalog = []
    catalog_list = []
    for key, value in ctgrs.items():
        catalog.append(InlineKeyboardButton(text=f"{get_catalog_by_id(key, lan)}:{get_catalog_by_id(value, lan)}", callback_data=catalog_id_callback.new(item_name=value, lan_name=lan)))
        if len(catalog)==1:
            catalog_list.append(catalog)   
            catalog = []
    catalog_list.append(catalog)

    del_cat = [
        InlineKeyboardButton(text="📋 Catalog", callback_data=all_catalog_callback.new(item_name=0, lan_name=lan)),
        InlineKeyboardButton(text="❌ Delete", callback_data=delete_callback.new(item_name="delete"))
        ]
    catalog_list.append(del_cat)

    catalog_inline = InlineKeyboardMarkup(inline_keyboard=catalog_list)

    return catalog_inline


def all_catalogs(ctgrs, lan):
    catalog = []
    catalog_list = []

    all_ctlg = get_catalog(ctgrs, lan)

    for ctlg in all_ctlg:
        catalog.append(InlineKeyboardButton(text=ctlg['name'], callback_data=all_catalog_callback.new(item_name=ctlg['id'], lan_name=lan)))
        if len(catalog)==1:
            catalog_list.append(catalog)   
            catalog = []
    catalog_list.append(catalog)

    back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="back")
    catalog_list.append(back_button)

    catalog_inline = InlineKeyboardMarkup(inline_keyboard=catalog_list)

    return catalog_inline

# back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
# catalog.insert(back_button)