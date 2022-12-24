from typing import Dict

from abstract_storage import AbstractStorage
from reguest import Request


class Courier:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request

        self.__from = storages[self.__request.departure]
        self.__to = storages[self.__request.destination]

    def move(self):
        self.__from.remove(title=self.__request.product, qnt=self.__request.qnt)
        print(f"Курьер забрал {self.__request.qnt} {self.__request.product} из {self.__request.departure}")

        print(f"Курьер везет {self.__request.qnt} {self.__request.product}")

        self.__to.add(title=self.__request.product, qnt=self.__request.qnt)
        print(f"Курьер доставил {self.__request.qnt} {self.__request.product} в {self.__request.destination}")