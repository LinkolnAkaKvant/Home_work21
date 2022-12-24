from typing import Dict

from abstract_storage import AbstractStorage


class BaseStorage(AbstractStorage):
    def __init__(self, items: Dict[str, int], capacity: int):
        self._items = items
        self._capacity = capacity

    def add(self, title, qnt):
        if self.get_free_space() < qnt:
            raise Exception("Недостаточно места")
        else:
            self._items[title] = self._items.get(title, 0) + qnt

    def remove(self, title, qnt):
        if title not in self._items:
            raise Exception('Неизвестный товар')
        elif self._items[title] < qnt:
            raise Exception('Недостаточно места')
        else:
            self._items[title] -= qnt

        if self._items[title] == 0:
            self._items.pop(title)

    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)
