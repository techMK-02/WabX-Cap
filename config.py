# config.py

import os
from dotenv import load_dotenv

# This line loads the environment variables from a .env file.
# It's useful for local development. On Koyeb, you'll set these variables directly.
load_dotenv()

class Config:
    """
    Configuration class to hold all the environment variables.
    """
    # --- Telegram API Credentials ---
    # Get these from my.telegram.org
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")

    # --- Bot Token ---
    # Get this from @BotFather on Telegram
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    # --- Database ---
    # Your MongoDB connection string.
    # Get this from your MongoDB Atlas dashboard.
    MONGO_URI = os.environ.get("MONGO_URI")

    # --- Bot Owner ---
    # Your own Telegram User ID. The bot will grant you special privileges.
    # You can get your ID from @userinfobot on Telegram.
    OWNER_ID = int(os.environ.get("OWNER_ID", "0"))


# --- Verification ---
# A check to ensure that all necessary variables are set before starting the bot.
if not all([Config.API_ID, Config.API_HASH, Config.BOT_TOKEN, Config.MONGO_URI, Config.OWNER_ID != 0]):
    raise ValueError(
        "CRITICAL ERROR: One or more essential environment variables are missing. "
        "Please check API_ID, API_HASH, BOT_TOKEN, MONGO_URI, and OWNER_ID."
    )
