from pathlib import Path

from tclogger import OSEnver

configs_root = Path(__file__).parents[1] / "configs"
envs_path = configs_root / "envs.json"

ENVS_ENVER = OSEnver(envs_path)
BILI_DATA_ENVS = ENVS_ENVER["bili_data"]
BILI_DATA_ROOT = Path(BILI_DATA_ENVS["root"])

secrets_path = configs_root / "secrets.json"
SECRETS = OSEnver(secrets_path)

COOKIES_DICT = SECRETS["cookies"]
COOKIES = "; ".join(f"{key}={val}" for key, val in SECRETS["cookies"].items())
