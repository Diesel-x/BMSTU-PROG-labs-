import os
import asyncio
import requests
from telethon import TelegramClient, functions
from datetime import datetime, timedelta

# Введите ваши данные Telegram API
api_id = ''
api_hash = ''

# Папка с изображениями
avatar_folder = 'avatars/'
# Файл для записи истории смен аватарок
log_file = 'avatar_change_log.txt'

if not os.path.exists(avatar_folder):
    os.makedirs(avatar_folder)
    print(f"Папка '{avatar_folder}' была создана. Положите туда изображения и перезапустите программу.")

async def get_current_date():
    try:
        response = requests.get('http://worldtimeapi.org/api/timezone/Etc/UTC')
        response.raise_for_status()
        return datetime.fromisoformat(response.json()['utc_datetime'][:-1])
    except Exception as e:
        print(f"Ошибка получения текущей даты из интернета: {e}")
        return datetime.utcnow()

async def change_avatar():
    # Создаем клиент
    async with TelegramClient('session_name', api_id, api_hash) as client:
        while True:
            # Получаем список изображений из папки
            avatars = [f for f in os.listdir(avatar_folder) if f.endswith((".jpg", ".png"))]

            if not avatars:
                print("Нет доступных изображений в папке")
                break

            # Загружаем историю смены аватарок
            used_avatars = set()
            if os.path.exists(log_file):
                with open(log_file, 'r') as file:
                    used_avatars = set(file.read().splitlines())

            # Выбираем первое доступное изображение, которое не использовалось
            avatar_path = None
            for avatar in avatars:
                if avatar not in used_avatars:
                    avatar_path = os.path.join(avatar_folder, avatar)
                    break

            if not avatar_path:
                print("Все изображения из папки уже были использованы")
                break

            try:
                # Устанавливаем новое фото профиля
                await client(functions.photos.UploadProfilePhotoRequest(
                    file=await client.upload_file(avatar_path)
                ))

                # Логируем изменение аватарки
                with open(log_file, 'a') as file:
                    file.write(f"{os.path.basename(avatar_path)}\n")

                print(f"Аватарка обновлена: {avatar_path}")
            except Exception as e:
                print(f"Ошибка при обновлении аватарки: {e}")

            # Получаем текущую дату и ждем до следующего дня
            current_date = await get_current_date()
            next_day = current_date.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
            sleep_duration = (next_day - current_date).total_seconds()

            print(f"Следующая смена аватарки через {sleep_duration // 3600:.0f} часов")
            await asyncio.sleep(sleep_duration)

if __name__ == "__main__":
    asyncio.run(change_avatar())
