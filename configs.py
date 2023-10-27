import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "21377679"))
  API_HASH = os.environ.get("API_HASH", "359ed998392d773cc1e0cefb3ca697d6")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6768471833:AAFXUoLkmj1Kpa9grHz7vXblzef-67d5f7o")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "PublicFileStorageBot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002064336451"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "MoneyKamalo.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "0eefb93e1e3ce9470a7033115ceb1bad13a9d674")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6642047024"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://publicfilestore:publicfilestore@cluster0.8unkb0e.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001682319978")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002064336451"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

   ⍟────[ File Store Bot]────⍟

🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})

🔸 Language: [Python 3](https://www.python.org)

🔸 Library: [Pyrogram](https://docs.pyrogram.org)
"""
  ABOUT_DEV_TEXT = f"""
Developer: [@THExAkib](https://t.me/THExAkib)
<b>○ Bot Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <a href='https://www.python.org/'>Python3</a>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram [Asyncio {__version__}]</a>\n○ Source Code : <a href='https://github.com/MExAkib/FileStoreBot2'>Click Here</a>\n○ Contact : @THExAkib\n○ Channel : <a href='https://t.me/+_CwryvJtzGA0NTk1'>Join Us</a>\n ⭐[Follow Me Here]⭐\n [<a href='https://github.com/MExAkib'>GitHub</a>] [<a href='https://www.facebook.com/MExAk1b'>Facebook</a>] [<a href='https://www.instagram.com/ig_4k1b'>Instagram</a>] [<a href='https://www.twitter.com/__4k1b__'>Twitter</a>]</b>",
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **File Store Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a Telegram Movie Channel or Any Copyright Channel, Then It's Useful for Daily Usage, You can Send Me Your File(s) & I will Send Permanent Link(s)s to You & Channel will be Safe from **Copygight Infringement Issues**. Check **About Bot** Section For More Details.
"""
