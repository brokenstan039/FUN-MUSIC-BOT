import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("29653892"))
API_HASH = os.getenv("9a9c203c27ccb3a6d3982ecdab9c54ad")
SESSION = os.getenv("1AZWarzwBuwZTbkHcFLip-nqNtQDhUlBtCaxoZLy4HqjpUlfDB8vDql_Up5AomnSuYy9vMPdbO2rkR81eDsICZiNpmtpbHTJFmnNRQnjJiuSq1hGMo2D7NdhhB1uOckRXpPo1NNv6EpH6CImK0CrdIHmlQhJW3gG9_V5Ovj57MrCvCw-nhGxW-3XinH3yCR8M-kSlwIRbmkeLmV3Qh_3QZfAfW0uvBMG0yiDwYLOxvqH1d-e91dODu5Y02F5m2xp1hL50cvyZgY1GxVsNh4nqdACCNzaxEs4JMA0bSuIfhEbIdu9CssJhDL9MzUuvmZLup6BsUVokR8ZXumYqF6M2LEJ5w4BfmlM=")
HNDLR = os.getenv("HNDLR", "/")
SUDO_USERS = list(map(int, os.getenv("5663329994").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicRioUserbot"))
call_py = PyTgCalls(bot)
# © 2022 GitHub, Inc.
# Terms
# Privacy
# Security
