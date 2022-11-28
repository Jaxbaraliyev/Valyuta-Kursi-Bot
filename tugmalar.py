from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup, ReplyKeyboardRemove

sotish = InlineKeyboardButton(text="Valyuta sotish", callback_data="sotish")
sotish_olish = InlineKeyboardButton(text="Valyuta sotib olish", callback_data="sotib_olish")

natijai = InlineKeyboardMarkup().add(sotish,sotish_olish)

aqsh = KeyboardButton(text="🇺🇸 AQSH dollori(USD)")
rubl = KeyboardButton(text="🇷🇺 Rubl(RUB)")
yevro = KeyboardButton(text="🇪🇺 Yevro(EUR)")
funt = KeyboardButton(text="🏴󠁧󠁢󠁥󠁮󠁧󠁿 Funt sterling(GBP)")
yena = KeyboardButton(text="🇯🇵󠁧󠁢󠁥󠁮󠁧󠁿 Yena(JPY)")

natija = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(aqsh,rubl,yevro,funt,yena)