from aiogram.utils.callback_data import CallbackData

catalog_id_callback = CallbackData("catalog_id", "word", "item_name","lan_name")
all_catalog_callback = CallbackData("all_catalog", "item_name", "lan_name")
delete_callback = CallbackData("delete", "item_name")
