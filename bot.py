from aiogram import *
from aiogram.types import *
from aiogram.filters import *
import asyncio
import os
from aiogram.types.input_file import FSInputFile
import shutil

API_TOKEN = 'YOUR_TOKEN'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()
__name__ = "__main__"
ids = []
with open('users.txt', 'r') as f:
    c = f.read()
    ids = c.split('\n')

print('============================\n'
      '||                        ||\n'
      '||   BOT IS WORKING NOW   ||\n'
      '||                        ||\n'
      '============================\n')

@dp.message(Command('start'))
async def welcome(message: types.Message):
    ids = []
    with open('users.txt', 'r') as f:
        c = f.read()
        ids = c.split('\n')
    idd = str(message.from_user.id)

    if idd not in ids:
        ids = ids.append(idd)
        with open('users.txt', 'a') as f:
            f.write(idd+'\n')
        os.mkdir(f'files/{idd}')
    
    await message.answer(
        f"Hello! This is cloud storage bot! Just send file here to upload it. Type /help for manual\n"
        f"Creator: t.me/Ismail_Omani\n"
        f"Привет! Это бот для управления облачным хранилищем! Просто пришли файл, чтобы выгрузить его. Напиши /help для получения мануала\n"
        f"Creator: t.me/Ismail_Omani"
    )

@dp.message(Command('help'))
async def welcome(message: types.Message):
    ids = []
    with open('users.txt', 'r') as f:
        c = f.read()
        ids = c.split('\n')
    idd = str(message.from_user.id)

    await message.answer(f"Commands:\n/start - starting bot\n"
    f"/help - shows that list\n"
    f"/ls - shows list of your files\n"
    f"/dlall - download all your files\n"
    f"/dl file - downloads file\n"
    f"/rm file - removes file from the cloud\n"
    f"/rn oldname newname - changes filename from oldname to newname\n"
    f"/share file - other will see this file using next command\n"
    f"/lsh - show list of all shared files\n"
    f"/dlallh - download all shared files(not recommended)\n"
    f"/dlh file - downloads file from shared\n"
    f"/rmh - removes file from shared\n"
    f"/rnh oldname newname - changes shared file's filename from oldname to newname\n"
    f"Bot doesn't support circles!!! Works better with ucompressed files\n\n"
    f"Команды:\n/start - запускает бота\n"
    f"/help - показывает этот список\n"
    f"/ls - показывает список всех ваших файлов\n"
    f"/dlall - скачивает все ваши файлы\n"
    f"/dl file - скачивает файл file\n"
    f"/rm file - удаляет файл file из облака\n"
    f"/rn oldname newname - меняет имя файла с oldname на newname\n"
    f"/share file - все будут видеть файл file используя следующую команду(файл всегда можно удалить из общедоступных)\n"
    f"/lsh - показывает список общедоступных файлов\n"
    f"/dlallh - скачивает все общедоступные файлы(не рекомендовано)\n"
    f"/dlh file - скачивает кокретный общедоступный файл\n"
    f"/rmh - удаляет общедоступный файл\n"
    f"/rnh oldname newname - меняет имя общедоступного файла с oldname на newname\n"
    f"Бот не поддерживает кружки!!! Работает лучше с несжатыми файлами\n"
    )

@dp.message(Command('ls'))
async def ls(message: types.Message):
    ids = []
    with open('users.txt', 'r') as f:
        c = f.read()
        ids = c.split('\n')
    idd = str(message.from_user.id)
    dirr = 'files/'+idd
    files = os.listdir(dirr)
    ms = ''
    for i in files:
        ms = ms + i + '\n'
    await message.answer(f'Your files:\n\n{ms}')

@dp.message(Command('lsh'))
async def lsh(message: types.Message):
    ids = []
    with open('users.txt', 'r') as f:
        c = f.read()
        ids = c.split('\n')
    idd = str(message.from_user.id)
    dirr = 'files/shared'
    files = os.listdir(dirr)
    ms = ''
    for i in files:
        ms = ms + i + '\n'
    await message.answer(f'Shared files:\n\n{ms}')

@dp.message(Command('dlall'))
async def ls(message: types.Message):
    ids = []
    with open('users.txt', 'r') as f:
        c = f.read()
        ids = c.split('\n')
    idd = str(message.from_user.id)
    dirr = 'files/'+idd
    files = os.listdir(dirr)
    for i in files:
        name = 'files/' + idd + i
        document = FSInputFile(f'files/{idd}/{i}')
        await bot.send_document(idd, document)

@dp.message(Command('dlallh'))
async def ls(message: types.Message):
    ids = []
    with open('users.txt', 'r') as f:
        c = f.read()
        ids = c.split('\n')
    idd = str(message.from_user.id)
    dirr = 'files/shared'
    files = os.listdir(dirr)
    for i in files:
        name = 'files/' + idd + i
        document = FSInputFile(f'files/shared/{i}')
        await bot.send_document(idd, document)

@dp.message()
async def save(message: types.Message):
    ids = []
    with open('users.txt', 'r') as f:
        c = f.read()
        ids = c.split('\n')
    idd = str(message.from_user.id)

    try:
        

        if message.text.split(maxsplit=1)[0] == '/dl':
            sp = message.text.split(maxsplit=1)
            t = sp[1]
        
            try:
                document = FSInputFile(f'files/{idd}/{t}')
                await bot.send_document(idd, document)
            except Exception as e:
                await message.answer("File doesn't exists or wrong syntax.\nТакого файла не существует или неправильный ввод")
        
        if message.text.split(maxsplit=1)[0] == '/dlh':
            sp = message.text.split(maxsplit=1)
            t = sp[1]
        
            try:
                document = FSInputFile(f'files/shared/{t}')
                await bot.send_document(idd, document)
            except Exception as e:
                await message.answer("File doesn't exists or wrong syntax.\nТакого файла не существует или неправильный ввод")


        elif message.text.split(maxsplit=1)[0] == '/rm':
            sp = message.text.split(maxsplit=1)
            t = sp[1]

            try:
                os.remove(f'files/{idd}/{t}')
                await message.answer(f'File {t} has been removed.\nФайл {t} был удален.')
            except Exception as e:
                await message.answer("File doesn't exists or wrong syntax.\nТакого файла не существует или неправильный ввод")

        elif message.text.split(maxsplit=1)[0] == '/rmh':
            sp = message.text.split(maxsplit=1)
            t = sp[1]

            try:
                os.remove(f'files/shared/{t}')
                await message.answer(f'File {t} has been removed.\nФайл {t} был удален.')
            except Exception as e:
                await message.answer("File doesn't exists or wrong syntax.\nТакого файла не существует или неправильный ввод")


        elif message.text.split(maxsplit=2)[0] == '/rn':
            sp = message.text.split(maxsplit=2)
            t = sp[1]
            tt = sp[2]
            try:
                os.rename(f'files/{idd}/{t}', f'files/{idd}/{tt}')
                await message.answer(f'File {t} has been renamed to {tt}.\nФайл {t} был переименован в {tt}.')
            except Exception as e:
                await message.answer("File doesn't exists or wrong syntax.\nТакого файла не существует или неправильный ввод")

        elif message.text.split(maxsplit=2)[0] == '/rnh':
            sp = message.text.split(maxsplit=2)
            t = sp[1]
            tt = sp[2]
            try:
                os.rename(f'files/shared/{t}', f'files/shared/{tt}')
                await message.answer(f'File {t} has been renamed to {tt}.\nФайл {t} был переименован в {tt}.')
            except Exception as e:
                await message.answer("File doesn't exists or wrong syntax.\nТакого файла не существует или неправильный ввод")


        elif message.text.split(maxsplit=1)[0] == '/share':
            sp = message.text.split(maxsplit=1)
            t = sp[1]

            try:
                shutil.copy(f'files/{idd}/{t}', f'files/shared/{t}')
                await message.answer(f'File {t} is shared with everyone now.\nФайл {t} теперь виден всем.')
            except Exception as e:
                await message.answer("File doesn't exists or wrong syntax.\nТакого файла не существует или неправильный ввод")




    except Exception as e:
        file_info = None
        file_name = "file"
    
    
        if message.document:
            file_info = message.document
            file_name = file_info.file_name
        elif message.photo:
            file_info = message.photo[-1]
            file_name = f"{file_info.file_unique_id}.jpg"
        elif message.video:
            file_info = message.video
            file_name = f"{file_info.file_unique_id}.mp4"
        elif message.audio:
            file_info = message.audio
            file_name = f"{file_info.file_unique_id}.mp3"
        elif message.voice:
            file_info = message.voice
            file_name = f"{file_info.file_unique_id}.ogg"
        else:
            await message.answer("Send file or voice message.\nОтправьте файл или голосовой сообщение.")
    
    
        file = await bot.get_file(file_info.file_id)
        await bot.download_file(file.file_path, f"files/{idd}/{file_name}")
    
        await message.answer(f"File saved to/файл сохранен в: {file_name}")







async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
