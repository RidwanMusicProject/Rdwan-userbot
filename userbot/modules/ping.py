import random
import time
from time import sleep

from datetime import datetime
from speedtest import Speedtest
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, StartTime, bot, DEVS
from userbot.events import register
from userbot.utils import edit_or_reply, humanbytes, poci_cmd

absen = [
    "**Hadir Bosquee** ๐",
    "**Hadir Bang** ๐",
    "**Hadir dong** ๐",
    "**Hadir ganteng** ๐ฅต",
    "**Hadir Bang Halbert** ๐",
    "**Hadir bang maap telat** ๐ฅบ",
]


ange = [
    "**Ayok vcs bareng aku** ๐",
    "**AW lagi Ange ya** ๐ฅต",
    "**Sama ni lagi Ange juga** ๐",
    "**Ayok Zaen privat** ๐",
    "**Yok Ange bareng aku** ๐ฅบ",
]




async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@poci_cmd(pattern="ping$")
async def _(ping):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(ping, "**๐ฅ**")
    sleep(1)
    await xx.edit("**P**")
    await xx.edit("**Po**")
    await xx.edit("**Pon**")
    await xx.edit("**Pong**")
    await xx.edit("**Pong!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await bot.get_me()
    await xx.edit(
        f"**HalbertโงUserbot!!**\n"
        f"โก **Ping**  `%sms`\n"
        f"โณ **BotUptime** `{uptime}` \n"
        f"๐ค **BotOf** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@poci_cmd(pattern="speedtest$")
async def _(speed):
    """For .speedtest command, use SpeedTest to check server speeds."""
    xxnx = await edit_or_reply(speed, "`Running speed test...`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    msg = (
        f"**Started at {result['timestamp']}**\n\n"
        "**Client**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Country :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Name :** `{result['server']['name']}`\n"
        f"**Country :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )
    await xxnx.delete()
    await speed.client.send_file(
        speed.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )


@poci_cmd(pattern="pong$")
async def _(pong):
    """For .ping command, ping the userbot from any chat."""
    start = datetime.now()
    xx = await edit_or_reply(pong, "`Gass!`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await xx.edit("๐ **Ping!**\n`%sms`" % (duration))


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK ๐ก
@register(incoming=True, from_users=DEVS, pattern=r"^.absen$")
async def pocong(ganteng):
    await ganteng.reply(random.choice(absen))

@register(incoming=True, from_users=2010825200, pattern=r"^.ange$")
async def Zaen(ganteng):
    await ganteng.reply(random.choice(ange))


CMD_HELP.update(
    {
        "ping": f"**Plugin : **`ping`\
        \n\n  โข  **Syntax :** `{cmd}ping`\
        \n  โข  **Function : **Untuk menunjukkan ping userbot.\
        \n\n  โข  **Syntax :** `{cmd}pong`\
        \n  โข  **Function : **Sama seperti perintah ping\
    "
    }
)


CMD_HELP.update(
    {
        "speedtest": f"**Plugin : **`speedtest`\
        \n\n  โข  **Syntax :** `{cmd}speedtest`\
        \n  โข  **Function : **Untuk Mengetes kecepatan server userbot.\
    "
    }
)
