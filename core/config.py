import os
import yaml

config_file_path = os.path.abspath("config.yml")

with open(config_file_path, "r") as file:
    config = yaml.safe_load(file)

print(
    f"✅ Loaded config for project: {config['project']['name']} (v{config['project']['version']})"
)
