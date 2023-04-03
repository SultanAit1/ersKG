from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import text

start_markup = InlineKeyboardMarkup(row_width=6)

one = InlineKeyboardButton(text='О компании ERSAG✅', callback_data="one")
three = InlineKeyboardButton(text='Продукция ERSAG🌿', callback_data='three')
two = InlineKeyboardButton(text='Маркетинг план💹', callback_data='two')
four = InlineKeyboardButton(text='О системе продвижения ERSAG✳', callback_data='four')
five = InlineKeyboardButton(text='Стать партнером ERSAG❇', callback_data='five')
last = InlineKeyboardButton(text='Хочу такого бота себе♻️', callback_data='last', url="https://t.me/Demonstrationsbot")
start_markup.add(one, )
start_markup.add(three, two)
start_markup.add(four)
start_markup.add(five)
start_markup.add(last)



main_markup = InlineKeyboardMarkup(row_width=1)
exit_1 = InlineKeyboardButton(text="Вернуться в Меню", callback_data='exit_1')
main_markup.add(exit_1)


url_markup = InlineKeyboardMarkup(row_width=5)
kyrg = InlineKeyboardButton(text='Каталог: Кыргызстан 🇰🇬 ', callback_data='kyrg', url='https://goo.su/ZZu4dty')
russia = InlineKeyboardButton(text='Каталог: Казахстан 🇰🇿 ', callback_data='russia', url='https://goo.su/uM5a2pT')
kazax = InlineKeyboardButton(text='Каталог: Узбекистан 🇺🇿 ', callback_data='kazax', url="https://goo.su/lAzUR4B")
uzb = InlineKeyboardButton(text='Каталог: Россия  🇷🇺 ', callback_data='uzb',url="https://goo.su/lqwJz3")
url_markup.add(kyrg
)
url_markup.add(russia)
url_markup.add(kazax)
url_markup.add(uzb)
url_markup.add(exit_1)

