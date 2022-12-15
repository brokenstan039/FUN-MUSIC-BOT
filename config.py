import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("20632724"))
API_HASH = os.getenv("fcb71f66e685e3ece3c4c36b87ec19de")
SESSION = os.getenv("1BVtsOHgBu21v1Bhgi7dMbVPdgFwhS2X0nryPuShT7Jh0MktpXFmpszVZ1lS4M_NlxBzFCkElAqtIGhm1OdK3kATfCAIuXfmZOxllXjybY4GfZS2zFyrGgOMBAbjURDUJWovCn59-KZ04VkN_q5FmpA5bGH2HrBRtdcvTlBVGF05SUowiLAKfdtSwXgXPJt5h_F6VIlWye82Rs3b8TvKV-b63ew22zmMKj-z9OMUkiXNfvuQ03j54FV5Sj3Rc-inFg7HdQJTiZdIMn09h0kCXDn-wHCP4PvfrIWdbiPegUFESrDHDeEIJ3fILmX4EM3HMDTkJ-KbfBuD7SJr2HCExCrdGvEM6ZkE=")
HNDLR = os.getenv("HNDLR", "/")
SUDO_USERS = list(map(int, os.getenv("1780355297").split()))


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
