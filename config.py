import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "18013154"))
API_HASH = os.environ.get("API_HASH", "93c6f3c43ede0082aceebfff185cf5ff")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8668760056:AAHOi8qW854ValNEeIB1bsLFMlu3_H2LZI8")
ADMIN = int(os.environ.get("ADMIN", "8530165612"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "-1004411647916")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1004411647916"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://siamvai:siamvai@cluster0.1bungtm.mongodb.net/?appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "TechifyBots")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")
