from bs4 import BeautifulSoup
from aiogram import Bot,Dispatcher,types, executor
import requests
import logging
from tugmalar import natija, natijai


logging.basicConfig(level=logging.INFO)

bot = Bot(token="5677218742:AAH1MndTG89fK3LjRmR1zbQamAplp-7q7Vg")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    ism = message.from_user.full_name
    await message.answer(f"Assalomu alaykum <b>{ism}</b>.Valyuta kursi botimizga xush kelibsiz😊!\n "
                         f"Valyuta kurslarini bilish  uchun quydagi tugmalardan birini tanlang👇:", parse_mode="HTML",reply_markup=natijai)


@dp.message_handler(commands=['admin'])
async def admin(message:types.Message):
    await message.answer("Bot admini: @Ramziddin_17_17")

@dp.message_handler(commands=['help'])
async def help(message:types.Message):
    await message.answer("Bu bot orqali siz Valyuta kurslari haqida ma`lumotlar olishingiz mumkin!")


@dp.callback_query_handler(lambda c: c.data == "sotish")
async def sotish(call:types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id,"Siz Valyuta sotishni tanladingiz✅. Endi esa pul birligini kiriting!👇", reply_markup=natija)

@dp.message_handler()
async def sotish_aqsh(message:types.Message):
        if message.text == "🇺🇸 AQSH dollori(USD)":
            url = f"https://hamkorbank.uz/uz/exchange-rate/"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(url, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            sotish = part.findAll("span")
            await message.answer(f"1 AQSH🇺🇸 dollori sotilishi, bizning pulga {sotish[14].text} so`mga🇺🇿 ga teng!")

        elif message.text == "🇷🇺 Rubl(RUB)":
            url = f"https://hamkorbank.uz/uz/exchange-rate/"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(url, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            sotish = part.findAll("span")
            await message.answer(f"1 Rossiya🇷🇺 rubli  sotilishi, bizning pulga {sotish[42].text} so`mga🇺🇿 ga teng!")

        elif message.text == "🇪🇺 Yevro(EUR)":
            url = f"https://hamkorbank.uz/uz/exchange-rate/"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(url, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            sotish = part.findAll("span")
            await message.answer(f"1 Yevro🇪🇺  sotilishi, bizning pulga {sotish[21].text} so`mga🇺🇿 ga teng!")

        elif message.text == "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Funt sterling(GBP)":
            url = f"https://hamkorbank.uz/uz/exchange-rate/"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(url, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            sotish = part.findAll("span")
            await message.answer(f"1 Angilya🏴󠁧󠁢󠁥󠁮󠁧󠁿 funt-serlingi sotilishi, bizning pulga {sotish[28].text} so`mga🇺🇿 ga teng!")

        elif message.text == "🇯🇵󠁧󠁢󠁥󠁮󠁧󠁿 Yena(JPY)":
            url = f"https://hamkorbank.uz/uz/exchange-rate/"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(url, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            sotish = part.findAll("span")
            await message.answer(f"1 Yaponiya🇯🇵󠁧󠁢󠁥󠁮󠁧󠁿 yenasi sotilishi, bizning pulga {sotish[35].text} so`mga🇺🇿 ga teng!")

        else: await message.answer("Afsuski bunday Valyuta mavjud emas☹")


@dp.callback_query_handler(lambda f: f.data == "sotib_olish")
async def sotish(call:types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id,"Siz Valyuta sotib olishni tanladingiz✅. Endi esa pul birligini kiriting!👇", reply_markup=natija)


@dp.message_handler()
async def kurs(message:types.Message):
        if message.text == "🇺🇸 AQSH dollori(USD)":
            url = f"https://hamkorbank.uz/uz/exchange-rate/"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(url, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            sotib_olish_aqsh = part.findAll("span")
            await message.answer(f"1 AQSH🇺🇸 dollori sotib olinishi, bizning pulga {sotib_olish_aqsh[12].text} so`mga🇺🇿 ga teng!")

        elif message.text == "🇷🇺 Rubl(RUB)":
            url = f"https://hamkorbank.uz/uz/exchange-rate/"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(url, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            sotib_olish_aqsh = part.findAll("span")
            await message.answer(f"1 Rossiya🇷🇺 rubli sotib olinishi, bizning pulga {sotib_olish_aqsh[40].text} so`mga🇺🇿 ga teng!")

        elif message.text == "🇪🇺 Yevro(EUR)":
            url = f"https://hamkorbank.uz/uz/exchange-rate/"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(url, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            sotib_olish_aqsh = part.findAll("span")
            await message.answer(f"1 Yevro🇪🇺 sotib olinishi, bizning pulga {sotib_olish_aqsh[19].text} so`mga🇺🇿 ga teng!")

        elif message.text == "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Funt sterling(GBP)":
            url = f"https://hamkorbank.uz/uz/exchange-rate/"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(url, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            sotib_olish_aqsh = part.findAll("span")
            await message.answer(f"1 Angliya🏴󠁧󠁢󠁥󠁮󠁧󠁿 funt-sterlingi sotib olinishi, bizning pulga {sotib_olish_aqsh[26].text} so`mga🇺🇿 ga teng!")

        elif message.text == "🇯🇵󠁧󠁢󠁥󠁮󠁧󠁿 Yena(JPY)":
            url = f"https://hamkorbank.uz/uz/exchange-rate/"
            agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            full_page = requests.get(url, headers=agent)
            part = BeautifulSoup(full_page.content, "html.parser")
            sotib_olish_aqsh = part.findAll("span")
            await message.answer(f"1 Yaponiya🇵󠁧󠁢󠁥󠁮󠁧󠁿 yenasi sotib olinishi, bizning pulga {sotib_olish_aqsh[33].text} so`mga🇺🇿 ga teng!")

        else: await message.answer("Afsuski bunday Valyuta mavjud emas☹")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)