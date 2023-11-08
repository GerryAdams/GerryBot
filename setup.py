from dotenv import set_key
from pathlib import Path

disctoke = input('Discord Token: ')

env_file_path = Path("DISCORD_TOKEN.env")
set_key(dotenv_path=env_file_path, key_to_set="DISCORD_TOKEN", value_to_set=disctoke)
