import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")  # ⚠️ Required

    # premium 4g renaming client
    STRING_API_ID = os.environ.get("STRING_API_ID", "")
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "")
    DB_URL = os.environ.get("DB_URL", "")  # ⚠️ Required

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "")
    ADMIN = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMIN', '').split()]  # ⚠️ Required
    
    FORCE_SUB = os.environ.get("FORCE_SUB", "") # ⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))  # ⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get(
        "BANNED_USERS", "1234567890").split())

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


class Txt(object):
    # part of text configuration
    START_TXT = """✨ **Wᴇʟᴄᴏᴍᴇ, {}!** 👋



🌟 **Advanced Rename Bot** 🌟

🔄 This bot allows you to **rename files** and **change their thumbnails** with ease.

📦 You can also **convert videos to files** and **files to videos**, providing maximum flexibility.

🖼️ **Custom Thumbnails** and **Custom Captions** are fully supported, allowing you to personalize your content.



Start exploring the powerful features and let the renaming magic happen! ✨
"""

    ABOUT_TXT = """╭━━━───[ 🌟 𝔸𝕓𝕠𝕦𝕥 𝕄𝕖 🌟 ]───━━━╮
┃ 
┃ 🤖 𝕄𝕪 𝕟𝕒𝕞𝕖    : {}
┃ 👨‍💻 ℙ𝕣𝕠𝕘𝕣𝕒𝕞𝕞𝕖𝕣  : <a href="https://t.me/TamilxLinks">TamilxLinks</a>
┃ ❄️ 𝔽𝕠𝕦𝕟𝕕𝕖𝕣 𝕠𝕗  : <a href="https://t.me/TNTamilLinks">TNTamilLinks</a>
┃ 📚 𝕃𝕚𝕓𝕣𝕒𝕣𝕪   : <a href="https://github.com/pyrogram">ℙ𝕪𝕣𝕠𝕘𝕣𝕒𝕞</a>
┃ 🖋️ 𝕃𝕒𝕟𝕘𝕦𝕒𝕘𝕖  : <a href="https://www.python.org">ℙ𝕪𝕥𝕙𝕠𝕟 𝟛</a>
┃ 💾 𝔻𝕒𝕥𝕒𝕓𝕒𝕤𝕖   : <a href="https://cloud.mongodb.com">𝕄𝕠𝕟𝕘𝕠 𝔻𝔹</a>
┃ ☁️ 𝕄𝕪 𝕊𝕖𝕣𝕧𝕖𝕣  : <a href="https://dashboard.heroku.com">ℍ𝕖𝕣𝕠𝕜𝕦</a>
┃ 
╰━━━━━━[ 𝔽𝕠𝕣 𝕄𝕠𝕣𝕖 𝕀𝕟𝕗𝕠 ]━━━━━━╯
 """

    CMD_LIST="""
/start - Aʟɪᴠᴇ Cʜᴇᴄᴋɪɴɢ 
/view_thumbᴠɪᴇᴡ -Vɪᴇᴡ Tʜᴜᴍʙɴᴀɪʟ 
/del_thumb - Dᴇʟᴇᴛᴇ Tʜᴜᴍʙɴᴀɪʟ 
/set_caption - Sᴇᴛ A Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ 
/see_caption - Sᴇᴇ Yᴏᴜʀ CᴜsᴛᴏᴍCᴀᴘᴛɪᴏɴ 
/del_caption - Dᴇʟᴇᴛᴇ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ 
/metadata - Tᴏ Sᴇᴛ & Cʜᴀɴɢᴇ ʏᴏᴜʀ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴄᴏᴅᴇ 
/set_prefix - Tᴏ Sᴇᴛ Yᴏᴜʀ Pʀᴇғɪx 
/del_prefix - Dᴇʟᴇᴛᴇ Yᴏᴜʀ Pʀᴇғɪx 
/see_prefix - Tᴏ Sᴇᴇ Yᴏᴜʀ Pʀᴇғɪx
/set_suffix - Tᴏ Sᴇᴛ Yᴏᴜʀ Sᴜғғɪx 
/see_suffix - Tᴏ Sᴇᴇ Yᴏᴜʀ Sᴜғғɪx 
/del_suffix - Dᴇʟᴇᴛᴇ Yᴏᴜʀ Sᴜғғɪx
/help
"""




    
    HELP_TXT = """
🌌 **How to Set a Thumbnail**

1. **Start the Bot**: Use the /start command, then send any photo to automatically set it as your thumbnail.
\n2. **Delete Thumbnail**: Use /del_thumb to remove your current thumbnail.
\n3. **View Thumbnail**: Use /view_thumb to see your existing thumbnail.

📑 **How to Set a Custom Caption**

1. **Set a Custom Caption**: Use /set_caption to create a personalized caption for your files.
\n2. **See Custom Caption**: Use /see_caption to view your current custom caption.
\n3. **Delete Custom Caption**: Use /del_caption to remove your custom caption.

**Example for setting a caption:**
   ```markdown
   /set_caption 
   📕 File Name: {filename}
   💾 Size: {filesize}
   ⏰ Duration: {duration}
"""

    SEND_METADATA = """
**Set Your Custom METADATA**

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @RoyalxMoviesOfficial" -metadata author="@TamilxLinks" -metadata:s:s title="Subtitled By :- @UHD4KxMovies" -metadata:s:a title="By :- @RoyalxMoviesOfficial" -metadata:s:v title="By:- @TamilxLinks" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @Cute_Boy_Saravana
"""

    PROGRESS_BAR = """<b>\n
╭━━━━━❰ 𝙋𝙧𝙤𝙜𝙧𝙚𝙨𝙨 𝘽𝙖𝙧 ❱━━━━━➣
┃ 
┣⪼ 📦 **Size**     : {1} / {2}
┃ 
┣⪼ ⏳️ **Completed**: {0}%
┃ 
┣⪼ 🚀 **Speed**    : {3}/s
┃ 
┣⪼ ⏰️ **ETA**      : {4}
┃ 
╰━━━━━━━━━━━━━━━━━━━➣
</b>
"""
