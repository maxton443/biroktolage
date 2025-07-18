from telegram.ext import ApplicationBuilder
from handlers.start import start_handler
from handlers.menu import menu_handler, content_handler
from handlers.admin import admin_handler, message_all_handler

BOT_TOKEN = "7849662626:AAGd5KBsWduBl740xIw09lAyFPUFs4XqpFI"  # এখানে নিজের বট টোকেন বসাও

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # হ্যান্ডলারগুলো যুক্ত করো
    app.add_handler(start_handler)
    app.add_handler(menu_handler)
    app.add_handler(content_handler)
    app.add_handler(admin_handler)
    app.add_handler(message_all_handler)

    print("Bot is running...")
    app.run_polling()
