from Package.main import *


async def start_notify(dp):
    await dp.bot.send_message(-4004433009, "Бот запущен")

#started?
print("started?")

if __name__ == '__main__':
    from Package.main import dp
    
    # scheduler.start()
    executor.start_polling(dp, on_startup=start_notify, skip_updates=True)