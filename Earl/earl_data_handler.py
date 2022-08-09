import os
import json
import typing
from typing import List, Dict, Tuple, Optional, Union


class EarlDataHandler:
    def __init__(self, json_path: str):
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
        