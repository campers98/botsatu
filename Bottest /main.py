"""
ɢɪᴛʜᴜʙ -: Abishnoi69
ᴛᴇʟᴇɢʀᴀᴍ -: @Abishnoi1M / @Abishnoi_bots 
"""


import importlib

from telegram import Update

from Bottest import Per
from Bottest.modules import ALL_MODULES


def main():
    rani.run_polling(
        timeout=15,
        drop_pending_updates=True,
        allowed_updates=Update.ALL_TYPES,
        stop_signals=None,
    )


if __name__ == "__main__":
    for Abishnoi in ALL_MODULES:
        importlib.import_module("Bottest.modules." + Abishnoi)
    main()
    print("ᴏ ғᴜ*ᴋ  ᴡʜᴇɴ ᴛᴜʀɴ ᴏɴ ᴍᴇ ᴀɢᴀɪɴ 🤔")
