# используется для сортировки
from operator import itemgetter


class Comp:
    """Компьютер"""
    def __init__(self, id, brand, price, disp_cls_id):
        self.id = id
        self.brand = brand
        self.price = price
        self.disp_cls_id = disp_cls_id


class Disp_cls:
    """Дисплейный класс"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class CompDisp_cls:
    """
    'Компьютеры дисплейного класса' для реализации
    связи многие-ко-многим
    """
    def __init__(self, disp_cls_id, comp_id):
        self.disp_cls_id = disp_cls_id
        self.comp_id = comp_id


# Дисплейные классы
disp_classes = [
    Disp_cls(1, 'А-класс'),
    Disp_cls(2, 'Б-класс'),
    Disp_cls(3, 'В-класс'),
    Disp_cls(11, 'Г-класс'),
    Disp_cls(22, 'Д-класс'),
    Disp_cls(33, 'Е-класс'),

]

# Компьютеры
comps = [
    Comp(1, 'HP', 1168390, 1),
    Comp(2, 'Asus', 55390, 1),
    Comp(3, 'Vaio', 78940, 3),
    Comp(4, 'Acer', 97450, 2),
    Comp(5, 'Lenovo', 86980, 3),
]

# Компьютеры и Дисплейные классы для связи многие-ко-многим
comps_disp_classs = [
    CompDisp_cls(1, 1),
    CompDisp_cls(1, 2),
    CompDisp_cls(3, 3),
    CompDisp_cls(2, 4),
    CompDisp_cls(3, 5),

    CompDisp_cls(33, 1),
    CompDisp_cls(22, 2),
    CompDisp_cls(11, 3),
    CompDisp_cls(33, 4),
    CompDisp_cls(22, 5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(c.brand, c.price, d.name)
                   for d in disp_classes
                   for c in comps
                   if c.disp_cls_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, dc.disp_cls_id, dc.comp_id)
                         for d in disp_classes
                         for dc in comps_disp_classs
                         if d.id == dc.disp_cls_id]

    many_to_many = [(c.brand, c.price, disp_class_name)
                    for disp_class_name, disp_cls_id, comp_id in many_to_many_temp
                    for c in comps if c.id == comp_id]

    print('Задание Б1')
    res_1 = sorted(one_to_many, key=itemgetter(0))
    print(res_1)

    print('\nЗадание Б2')
    res_2_unsorted = []
    for c in disp_classes:
        # Все компьютеры дисплейного класса
        c_comps = list(filter(lambda i: i[2] == c.name, one_to_many))
        if len(c_comps) > 0:
            res_2_unsorted.append((c.name, len(c_comps)))

    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    print(res_2)

    print('\nЗадание Б3')
    res_3 = {}
    # Перебираем все компьютеры
    for s in comps:
        if s.brand.endswith("o"):
            c_comps = list(filter(lambda i: i[0] == s.brand, many_to_many))
            c_comps_brands = [x[2] for x in c_comps]
            res_3[s.brand] = c_comps_brands

    print(res_3)


if __name__ == '__main__':
    main()