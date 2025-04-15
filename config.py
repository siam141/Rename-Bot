import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "27752560"))
API_HASH = os.environ.get("API_HASH", "67d3ec64db8031189962b5d4804884c0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7728598881:AAF3evUl3YJw9dp4wm58Ad0oZu1CbeWgMMo")
ADMIN = int(os.environ.get("ADMIN", "7862181538"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "-1002530980008")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002589776901"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://andfreefirew:andfreefirew@cluster0.qufbkvn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "TechifyBots")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")
