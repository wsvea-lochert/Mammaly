import typing
import datetime
from typing import List, Dict, Tuple, Optional, Union


class EarlEntry:
    def __init__(self, date: datetime, country: str, site: str, start: str, time_in_water: int, depth: int, tank_volume: int, weights: int, bar_in: int, bar_out: int, o2, notes: str):
        """
        Class for storing the data of one entry in the Earl database
        :param date: The date of the dive. Format: YYYY-MM-DD
        :param country: The country of the dive. Format: string
        :param site: The dive site. Format: string
        :param start: When the dive started. Format: string (HH:MM)
        :param time_in_water: Time spent in the water. Format: int (minutes)
        :param depth: The maximum depth reached. Format: int (meters)
        :param tank_volume: The volume of the tank. Format: int (liters)
        :param weights: The weights used. Format: int (Kilos)
        :param bar_in: How many bars were in the tank when the dive started. Format: int (bars)
        :param bar_out: How many bars were in the tank when the dive ended. Format: int (bars)
        :param o2: What oxygen mix was used? 21%, 32%, etc. Format: string (percentage)
        :param notes: Dive notes, did you see a cool fish or something else? Format: string
        """
        self.date = date
        self.country = country
        self.site = site
        self.start = start
        self.time_in_water = time_in_water
        self.depth = depth
        self.tank_volume = tank_volume
        self.weights = weights
        self.bar_in = bar_in
        self.bar_out = bar_out
        self.o2 = o2
        self.notes = notes
