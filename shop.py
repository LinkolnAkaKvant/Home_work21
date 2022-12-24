from typing import Dict

from base_storage import BaseStorage


class Shop(BaseStorage):
    def __init__(self, items: Dict[str, int], capacity=20):
        super().__init__(items, capacity)
        self._items = items

    def add(self, title, qnt):
        if self.get_unique_items_count() >= 5:
            raise Exception(f"На складе не хватает места")
        else:
            super().add(title, qnt)