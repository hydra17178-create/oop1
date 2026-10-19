from abc import ABC, abstractmethod
from datetime import datetime

class AbstractEntity(ABC):
    @abstractmethod
    def get_info(self):
        pass


class CustomPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class CustomMap:
    def __init__(self):
        self._data = []

    def put(self, key, value):
        self._data.append(CustomPair(key, value))

    def get(self, key):
        for pair in self._data:
            if pair.key == key:
                return pair.value
        return None

class CalendarEvent(AbstractEntity):
    def __init__(self, e_id, title, date_str, desc):
        self._id = e_id
        self._title = title
        self._date = date_str
        self._description = desc

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        self._title = val

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, val):
        self._date = val

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, val):
        self._description = val

    @property
    def event_id(self):
        return self._id

    def get_info(self):
        return f"{self._date} - {self._title}"

    def __eq__(self, other):
        if isinstance(other, CalendarEvent):
            return self._id == other._id
        return False

    def __lt__(self, other):
        if isinstance(other, CalendarEvent):
            d1 = datetime.strptime(self._date, "%d.%m.%Y")
            d2 = datetime.strptime(other._date, "%d.%m.%Y")
            return d1 < d2
        return False

    def __repr__(self):
        return f"Event(id={self._id}, title='{self._title}')"

    def __str__(self):
        return f"{self._date} - {self._title}"

    def __hash__(self):
        return hash(self._id)

    def __len__(self):
        return len(self._title)