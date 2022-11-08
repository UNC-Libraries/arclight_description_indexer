import os
from pathlib import Path

import yaml


class Config:

	def __init__(self):
		if 'DESCRIPTION_INDEXER_CONFIG_FILE' in os.environ:
			base_path = os.environ['DESCRIPTION_INDEXER_CONFIG_FILE']
		else:
			base_path = Path.home() / ".description_indexer.yml"
		with open(base_path, "r") as f:
			config = yaml.safe_load(f)

			for k in config.keys():
				setattr(self, k, config[k])
