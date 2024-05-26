import asyncio
import importlib
import logging
import time

from telegram.ext import ApplicationBuilder
from config import TOKEN
from AsuX.modules import ALL_MODULES
from AsuX.handlers.chatbot import add_chatbot_handlers

StartTime = time.time()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

# Create the application
application = ApplicationBuilder().token(TOKEN).build()

# Load all modules
for module_name in ALL_MODULES:
    importlib.import_module(f"AsuX.modules.{module_name}")

# Add chatbot handlers
add_chatbot_handlers(application)

async def main():
    # Run the bot until the user sends a signal to stop
    await application.start()
    await application.updater.start_polling()
    await application.idle()

if __name__ == '__main__':
    asyncio.run(main())
