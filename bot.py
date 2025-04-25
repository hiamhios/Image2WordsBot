from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import pytesseract
from PIL import Image

# توکن ربات شما
TOKEN = "8025883792:AAFX5v66q4-4qEJ70RkRA4q43F7rXcU57Wg"

# تابعی که به فرمان /start پاسخ می‌دهد
async def start(update: Update, context):
    await update.message.reply_text("سلام! لطفاً عکسی ارسال کن تا متن آن استخراج شود.")

# تابعی که پیام‌های تصویر را پردازش می‌کند
async def handle_image(update: Update, context):
    # دریافت عکس از پیام
    photo_file = await update.message.photo[-1].get_file()
    photo_path = "temp.jpg"
    await photo_file.download(photo_path)

    # پردازش عکس با Tesseract OCR
    img = Image.open(photo_path)
    text = pytesseract.image_to_string(img)

    # ارسال متن استخراج شده
    await update.message.reply_text(f"متن استخراج شده: {text}")

# تابع اصلی که ربات را راه‌اندازی می‌کند
def main():
    # ایجاد اپلیکیشن ربات با توکن
    application = Application.builder().token(TOKEN).build()

    # اضافه کردن handler‌ها برای فرمان‌ها و تصاویر
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, handle_image))

    # شروع ربات
    application.run_polling()

# اجرای ربات
if __name__ == "__main__":
    main()
