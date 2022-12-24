from courier import Courier
from shop import Shop
from store import Store
from reguest import Request

shop = Shop(items={'хлеб': 3, 'молоко': 2, 'конфеты': 4, 'сыр': 1})
store = Store(
    items={'сыр': 8, 'молоко': 10, 'хлеб': 4, 'конфеты': 11, 'печенье': 6, 'яблоки': 13, 'игрушки': 13, 'сок': 9})

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    while True:
        for storage_name in storages:
            print(f"в {storage_name} хранится: {storages[storage_name].get_items()}")

        user_input = input(
            'Введите строку в формате: "Доставить 3 печенье из склад в магазин".\n'
            'Введите "стоп" или "stop", чтобы закончить:\n',
        )

        if user_input in ('стоп', 'stop'):
            break

        request = Request(request_str=user_input, storages=storages)
        courier = Courier(request=request, storages=storages)
        courier.move()


if __name__ == '__main__':
    main()
