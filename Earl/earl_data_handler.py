# Currently Mammaly only runs locally, but is to be migrated to a server.
import os
import json
import typing
from typing import List, Dict, Tuple, Optional, Union
from earl_entry import EarlEntry


#  TODO: Migrate to Firebase handling.
class EarlDataHandler:
    def __init__(self, json_path: str):
        """
        Class for handling the data in the Earl database
        :param json_path: Path to the json file. Format: string
        dict: all the data from the json file. Format: dict
        """
        self.json_path = json_path
        self.dict = self.get_json_data()

    def get_json_data(self) -> Dict:
        with open(self.json_path, 'r') as f:
            return json.load(f)

    def write_json_data(self, data: Dict):
        with open(self.json_path, 'w') as f:
            json.dump(data, f)

    def sort_data(self, data: Dict) -> Dict:
        """
        Function for sorting the data in self.dict by date
        :param data:
        :return:
        """
