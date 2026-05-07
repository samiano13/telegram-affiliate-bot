import re
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8779692069:AAFDi6b_gllplBbhI_wZroJ9bwaaGnGYTbc"
AFF_SHORT_KEY = "_c3KHLXzD"

def convert_to_affiliate(url):
    return f"https://s.click.aliexpress.com/deep_link.htm?aff_short_key={AFF_SHORT_KEY}&dl_target_url={url}"

def extract_url(text):
    if not text:
        return None

    urls = re.findall(r"(https?://[^\s]+)", text)

    for u in urls:
        if "aliexpress" in u.lower():
            return u

    return None

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    text = (message.text or "") + " " + (message.caption or "")

    url = extract_url(text)

    if not url and "aliexpress" in text.lower():
        url = text

    if url:
        aff_link = convert_to_affiliate(url)
        await message.reply_text(f"🔗 رابطك:\n{aff_link}")
    else:
        await message.reply_text("❌ أرسل رابط AliExpress فقط")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, handle))

app.run_polling()
