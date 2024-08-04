import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", None))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 1356469075))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Smaugopp/Voidmusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/botz_x_hub")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Alice_x_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "6be9f0b34c384ad097cc71b1c1fc5e8b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "2607415f99944cc6b24fa98018fb8c09")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFtP-gAb9FHeqvFniD1Ncxy6A25tHZEiwpmyRTHDTxX6D9lX1EOKzfTHbWVNKVc52CSefLNFbcVqZL-PEaeuVRx6s2MiKsbxM9dod00sc02-jiBEVlMV2I0zZr3PvkY3LZgH4x64Cw3sWcqgdfs4nr-ZnoRMWH1Ny4SK1mFjeYSuRH5OSGh4OC7ceN1Xjr3UDHHgrhnspL6XJvawEhFo5Nc8IotjZ2iWboOtHxJHq_U_lN0ntK100SMSB_NWVkmc7QOeD8opXxdpifD8EcAY5BxjVW5cAAM44TF_q5P-IJGDDjd04D844weC4UAzsO7gVPBB7fdd-ghzYQ1fRqtAd8_R-34wgAAAAFaybePAA")
STRING2 = getenv("STRING_SESSION2", "BQFtP-gAm_Z-YZg2YPJX-aePeQGAaegppT-KJ1wyfRqmhiNAggsRHXkAHF8U0Q9pPBLRqCLY7jL6iAjnYhAt5onoeCLeNGHlGqqS6uSOUG55uQu6Q5il6Q3Oc2lFWrzO8HdOZihJFHTo6mENn0TAe-W4oRHHSKcWUzihJqrJGgZiTiIMYT-NIMJPaDEiMIDNTEdUSLe8Jmw3DamAIrsp319pTEFOsbUJ-GTdvGxQkWhnaTYj1WgvrcA40bgM7Cf_Ycjll31aet0yzYZThEmnMRqNllYd8bNcwxkpmk1ctaKrBuvxVkyM3RmhgX2Ed3mNsIFhVMUbpLRgfjm52GdxCZmPoUFjVwAAAAGUzntfAA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/adb4c3fe1124461b023c4.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/531090c47c12e983bf731.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/6dd4127abb744a1c82ce9.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph//file/4f8a07408aacfff00f3de.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph//file/4f8a07408aacfff00f3de.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
