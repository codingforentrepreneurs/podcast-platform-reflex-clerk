import os
import reflex as rx
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

config = rx.Config(
    app_name="podcast_discovery",
    plugins=[rx.plugins.TailwindV3Plugin()],
    db_url=DATABASE_URL
)