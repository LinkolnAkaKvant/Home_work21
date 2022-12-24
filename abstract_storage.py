from abc import ABC, abstractmethod
from typing import Dict


class AbstractStorage(ABC):
    @abstractmethod
    def __init__(self, items: Dict[str, int], capacity: int):
        self._items = items
        self._capacity = capacity


    @abstractmethod
    def add(self, title, qnt):
        pass

    @abstractmethod
    def remove(self, title, qnt):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
