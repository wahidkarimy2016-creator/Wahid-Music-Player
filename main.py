
import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 به وحید موزیک پلیر خوش آمدید!\n\n"
        "یک ربات موسیقی برای گروه‌ها و کانال‌های تلگرام.\n\n"
        "برای مشاهده دستورات، /help را بزنید."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎧 راهنمای وحید موزیک پلیر\n\n"
        "/play - پخش موسیقی\n"
        "/search - جستجوی آهنگ\n"
        "/pause - توقف موقت\n"
        "/resume - ادامه پخش\n"
        "/skip - آهنگ بعدی\n"
        "/stop - قطع پخش\n"
        "/queue - صف موسیقی\n\n"
        "بعضی قابلیت‌ها هنوز در حال ساخت هستند."
    )


async def coming_soon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 این قابلیت در حال آماده‌سازی است."
    )


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is not configured!")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    for command in ["play", "search", "pause", "resume",
                    "skip", "stop", "queue"]:
        app.add_handler(CommandHandler(command, coming_soon))

    print("Wahid Music Player is running!")
    app.run_polling()


if __name__ == "__main__":
    main()
  
