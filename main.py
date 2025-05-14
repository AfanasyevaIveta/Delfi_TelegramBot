import json
import asyncio
import feedparser
from datetime import datetime
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.constants import ParseMode
from telegram.error import TelegramError
import nest_asyncio

# Iestatījumi
TOKEN = '7534228860:AAELAPad3M-pfMzrVqKb9fuR3aA9Ze_e5Ls'
RSS_FEED_URL = 'https://www.delfi.lv/rss/?channel=delfi'
STATE_FILE = 'state.json'
SUBSCRIBERS_FILE = 'subscribers.json'
CHECK_INTERVAL_SECONDS = 60  # jaunu ziņu pārbaude

bot = Bot(token=TOKEN)

# Jaunākās ziņas pārbaude
def load_last_news_id(): # jaunākās ziņas ID salīdzinājums
    try:
        with open(STATE_FILE, 'r') as f:
            return json.load(f).get('last_id')
    except FileNotFoundError:
        return None

def save_last_news_id(news_id): # saglabā jaunākās ziņas ID
    with open(STATE_FILE, 'w') as f:
        json.dump({'last_id': news_id}, f)

# SUBSCRIBERS
def load_subscribers():
    try:
        with open(SUBSCRIBERS_FILE, 'r') as f:
            return set(json.load(f)) # atkārtošanās pārbaude
    except FileNotFoundError:
        return set()

def save_subscribers(subscribers): # saglabā abonentu kopu
    with open(SUBSCRIBERS_FILE, 'w') as f:
        json.dump(list(subscribers), f)

# TELEGRAM KOMANDAS
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): # Sekot  
    user_id = update.effective_chat.id
    subscribers = load_subscribers()
    if user_id not in subscribers:
        subscribers.add(user_id)
        save_subscribers(subscribers)
        await update.message.reply_text("Paldies par sekošanu!")
    else:
        await update.message.reply_text("Jūs jau sekojat līdzi jaunumiem.")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE): # Beigt sekošanu
    user_id = update.effective_chat.id
    subscribers = load_subscribers()
    if user_id in subscribers:
        subscribers.remove(user_id)
        save_subscribers(subscribers)
        await update.message.reply_text("Jūs vairs nesaņemsiet ziņojumus no šī bota.")
    else:
        await update.message.reply_text("Jūs nesaņemsiet ziņojumus no šī bota")

# Ziņu sūtīšana
async def send_news_to_all(message):
    subscribers = load_subscribers()
    for user_id in subscribers:
        try:
            await bot.send_message(chat_id=user_id, text=message, parse_mode=ParseMode.HTML)
        except TelegramError as e:
            print(f"Error sending to {user_id}: {e}")

# RSS pārbaude --> ja ir atklāta, nosūta jaunu ziņu
async def check_news():
    feed = feedparser.parse(RSS_FEED_URL)
    if not feed.entries:
        print("No news in RSS.")
        return

    latest = feed.entries[0] # nosūta jaunāko ziņu
    last_id = load_last_news_id()

    if latest.id != last_id: # ja tas ir jaunā ziņa -> nosūta
        message = (
            f"📰 <b>{latest.title}</b>\n"
            f"📅 {latest.published}\n"
            f"🔗 <a href=\"{latest.link}\">Atvērt rakstu</a>"
        )
        await send_news_to_all(message)
        save_last_news_id(latest.id)
        print(f"The news has been sent {datetime.now().strftime('%H:%M:%S')}")
    else:
        print(f"There is no new news ({datetime.now().strftime('%H:%M:%S')})")

# Ziņu pārbaudes cikls
async def run_news_checker():
    while True:
        await check_news()
        await asyncio.sleep(CHECK_INTERVAL_SECONDS)

# Galvēna ASYNC funkcija
async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stop", stop))

    # Ziņu pārbaude
    asyncio.create_task(run_news_checker())

    print("The bot has started working. Stay tuned for updates...")
    await app.run_polling()

if __name__ == '__main__':
    nest_asyncio.apply()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\nAction aborted")
