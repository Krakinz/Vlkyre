# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡| 
#             (𝐜)𝐕𝐥𝐤𝐲𝐫𝐞 𝐢𝐬 𝐚 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐌𝐮𝐥𝐭𝐢𝐏𝐮𝐫𝐩𝐨𝐬𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧,𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝟏𝟎𝟎+ 𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬!
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡|
import os
import psutil
import shutil
import logging
import pathlib
import platform
import git as 𝖛
import subprocess
from loguru import *
from datetime import *
from termcolor import *
from os import getenv
from dotenv import load_dotenv
load_dotenv("./ᴠʟᴋʏʀᴇ™.env")
ᴠʟᴋʏʀᴇ = getenv("HEROKU", None)
𝖈𝖔𝖗𝖑𝖊𝖝 = getenv("HEROKU", None)
ᴠʟᴋʏʀᴇi = getenv("CODE", None)
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡| 
#             (𝐜)𝐕𝐥𝐤𝐲𝐫𝐞 𝐢𝐬 𝐚 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐌𝐮𝐥𝐭𝐢𝐏𝐮𝐫𝐩𝐨𝐬𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧,𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝟏𝟎𝟎+ 𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬!
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡|
class InterceptHandler(logging.Handler):
    LEVELS_MAP = {
        logging.CRITICAL: "CRITICAL",
        logging.ERROR: "ERROR",
        logging.WARNING: "WARNING",
        logging.INFO: "INFO",
        logging.DEBUG: "DEBUG",
    }

    def _get_level(self, record):
        return self.LEVELS_MAP.get(record.levelno, record.levelno)

    def emit(self, record):
        logger_opt = logger.opt(
            depth=6, exception=record.exc_info, ansi=True, lazy=True
        )
        logger_opt.log(self._get_level(record), record.getMessage())


logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)
LOGS = logging.getLogger(__name__)
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡| 
#             (𝐜)𝐕𝐥𝐤𝐲𝐫𝐞 𝐢𝐬 𝐚 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐌𝐮𝐥𝐭𝐢𝐏𝐮𝐫𝐩𝐨𝐬𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧,𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝟏𝟎𝟎+ 𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬!
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡|
pkgFl = pathlib.Path("package-lock.json")
if pkgFl.exists ():
    os.remove("package-lock.json")
    if ᴠʟᴋʏʀᴇ == "HEROKU":
        LOGS.info(str(f"🐍𝐏𝐲꧂ package-lock.json has been cleaned!"))
    else:
        cprint(f"🐍𝐏𝐲꧂ package-lock.json has been cleaned!", "yellow")
else:
    if ᴠʟᴋʏʀᴇ == "HEROKU":
        LOGS.info(str(f"🐍𝐏𝐲꧂ package-lock.json File does not exist!"))
    else:
        cprint(f"🐍𝐏𝐲꧂ package-lock.json File does not exist!", "green")
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡| 
#             (𝐜)𝐕𝐥𝐤𝐲𝐫𝐞 𝐢𝐬 𝐚 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐌𝐮𝐥𝐭𝐢𝐏𝐮𝐫𝐩𝐨𝐬𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧,𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝟏𝟎𝟎+ 𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬!
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡|
try:
    subprocess.run(["node", "ᴠʟᴋʏʀᴇ🀄ᴇxʜᴀᴜꜱᴛ/dirDash.js"], check=True, stdout=subprocess.PIPE).stdout
except Exception as Error:
    if ᴠʟᴋʏʀᴇ == "HEROKU":
        LOGS.info(str(f"🐍𝐏𝐲꧂ {Error}"))
    else:
        cprint(f"🐍𝐏𝐲꧂ {Error}")
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡| 
#             (𝐜)𝐕𝐥𝐤𝐲𝐫𝐞 𝐢𝐬 𝐚 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐌𝐮𝐥𝐭𝐢𝐏𝐮𝐫𝐩𝐨𝐬𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧,𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝟏𝟎𝟎+ 𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬!
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡|
pkgFl = pathlib.Path("package.json")
if pkgFl.exists ():
    os.remove("package.json")
    if ᴠʟᴋʏʀᴇ == "HEROKU":
        LOGS.info(str(f"🐍𝐏𝐲꧂ package.json has been cleaned!"))
    else:
        cprint(f"🐍𝐏𝐲꧂ package.json has been cleaned!", "yellow")
else:
    if ᴠʟᴋʏʀᴇ == "HEROKU":
        LOGS.info(str(f"🐍𝐏𝐲꧂ package.json File does not exist!"))
    else:
        cprint(f"🐍𝐏𝐲꧂ package.json File does not exist!", "green")       
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡| 
#             (𝐜)𝐕𝐥𝐤𝐲𝐫𝐞 𝐢𝐬 𝐚 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐌𝐮𝐥𝐭𝐢𝐏𝐮𝐫𝐩𝐨𝐬𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧,𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝟏𝟎𝟎+ 𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬!
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡|
try:
    subprocess.run(["git", "config", "--global", "user.name", "KryKnz"], check=True, stdout=subprocess.PIPE).stdout
    subprocess.run(["git", "config", "--global", "user.email", "KryKnz@yandex.com"], check=True, stdout=subprocess.PIPE).stdout
    subprocess.run(["git", "config", "pull.rebase", "false"], check=True, stdout=subprocess.PIPE).stdout
    subprocess.run(["git", "init", "--initial-branch=🛰️KryTek"], check=True, stdout=subprocess.PIPE).stdout
    subprocess.run(["git", "fetch", "origin", "🛰️KryTek"], check=True, stdout=subprocess.PIPE).stdout
    subprocess.run(["git", "reset", "--hard", "origin/🛰️KryTek"], check=True, stdout=subprocess.PIPE).stdout
    subprocess.run(["git", "pull"], check=True, stdout=subprocess.PIPE).stdout
    if ᴠʟᴋʏʀᴇ == "HEROKU":
        LOGS.info(str("🐍𝐏𝐲꧂ git sync done!"))
    else:
        cprint("🐍𝐏𝐲꧂ git sync done!", "green")
except Exception as Error:
    if ᴠʟᴋʏʀᴇ == "HEROKU":
        LOGS.info(str(f"🐍𝐏𝐲꧂ {Error}"))
        LOGS.info(str("🐍𝐏𝐲꧂ Error In git sync!"))
        LOGS.info(str("🐍𝐏𝐲꧂ Trying TO Stash and ReTry!"))
    else:
        cprint("🐍𝐏𝐲꧂ Error In git sync!", "red")
        cprint("🐍𝐏𝐲꧂ Trying TO Stash and ReTry!", "yellow")
    # |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡| 
    #             (𝐜)𝐕𝐥𝐤𝐲𝐫𝐞 𝐢𝐬 𝐚 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐌𝐮𝐥𝐭𝐢𝐏𝐮𝐫𝐩𝐨𝐬𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧,𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝟏𝟎𝟎+ 𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬!
    # |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡|
    try:
        subprocess.run(["git", "config", "--global", "user.name", "KryKnz"], check=True, stdout=subprocess.PIPE).stdout
        subprocess.run(["git", "config", "--global", "user.email", "KryKnz@yandex.com"], check=True, stdout=subprocess.PIPE).stdout
        subprocess.run(["git", "config", "pull.rebase", "false"], check=True, stdout=subprocess.PIPE).stdout
        subprocess.run(["git", "init", "--initial-branch=🛰️KryTek"], check=True, stdout=subprocess.PIPE).stdout
        subprocess.run(["git", "fetch", "origin", "🛰️KryTek"], check=True, stdout=subprocess.PIPE).stdout
        subprocess.run(["git", "reset", "--hard", "origin/🛰️KryTek"], check=True, stdout=subprocess.PIPE).stdout
        subprocess.run(["git", "stash"], check=True, stdout=subprocess.PIPE).stdout
        subprocess.run(["git", "stash", "drop"], check=True, stdout=subprocess.PIPE).stdout
        subprocess.run(["git", "pull"], check=True, stdout=subprocess.PIPE).stdout
    except Exception as Error:
        if ᴠʟᴋʏʀᴇ == "HEROKU":
            LOGS.info(str(f"🐍𝐏𝐲꧂ {Error}"))
            LOGS.info(str("🐍𝐏𝐲꧂ Nothing To Stash and Drop!"))
        else:
            cprint(f"🐍𝐏𝐲꧂ {Error}")
            cprint("🐍𝐏𝐲꧂ Nothing To Stash and Drop!", "blue")
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡| 
#             (𝐜)𝐕𝐥𝐤𝐲𝐫𝐞 𝐢𝐬 𝐚 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐌𝐮𝐥𝐭𝐢𝐏𝐮𝐫𝐩𝐨𝐬𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧,𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝟏𝟎𝟎+ 𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬!
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡|
try:
    subprocess.run(["npm", "install", "--force", "--save"], check=True, stdout=subprocess.PIPE).stdout
    if ᴠʟᴋʏʀᴇ == "HEROKU":
        LOGS.info(str(f"🐍𝐏𝐲꧂ npm install done using python subprocess!"))
    else:
        cprint(f"🐍𝐏𝐲꧂ npm install done using python subprocess!")
except Exception as Error:
    if ᴠʟᴋʏʀᴇ == "HEROKU":
        LOGS.info(str(f"🐍𝐏𝐲꧂ {Error}"))
    else:
        cprint(f"🐍𝐏𝐲꧂ {Error}")
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡| 
#             (𝐜)𝐕𝐥𝐤𝐲𝐫𝐞 𝐢𝐬 𝐚 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐌𝐮𝐥𝐭𝐢𝐏𝐮𝐫𝐩𝐨𝐬𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧,𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝟏𝟎𝟎+ 𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬!
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡|
pkgFl = pathlib.Path("package-lock.json")
if pkgFl.exists ():
    os.remove("package-lock.json")
    if ᴠʟᴋʏʀᴇ == "HEROKU":
        LOGS.info(str(f"🐍𝐏𝐲꧂ package-lock.json has been cleaned!"))
    else:
        cprint(f"🐍𝐏𝐲꧂ package-lock.json has been cleaned!", "yellow")
else:
    if ᴠʟᴋʏʀᴇ == "HEROKU":
        LOGS.info(str(f"🐍𝐏𝐲꧂ package-lock.json File does not exist!"))
    else:
        cprint(f"🐍𝐏𝐲꧂ package-lock.json File does not exist!", "green")
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡| 
#             (𝐜)𝐕𝐥𝐤𝐲𝐫𝐞 𝐢𝐬 𝐚 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐌𝐮𝐥𝐭𝐢𝐏𝐮𝐫𝐩𝐨𝐬𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧,𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝟏𝟎𝟎+ 𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬!
# |⬡════════════════════════════════════════════|❝ Ⓒ𝐕𝐥𝐤𝐲𝐫𝐞 ☊ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋʀᴀᴋɪɴᴢʟᴀʙ™ ❞|═══════════════════════════════════════════⬡|
