import names
import random

class Flamingo():
    name: str
    breed: str
    color: str
    wings: str
    size: int
    arial: str
    flying: str

    def __init__(self, name: str, breed: str, color: str, wings: str, size: int, arial: str, flying: str = "умеет летать"):
        self.name = name
        self.breed = breed
        self.color = color
        self.size = size
        self.wings = wings
        self.arial = arial
        self.flying = flying

    def get_info(self) -> str:
        return f"{self.name} породы {self.breed} , что имеет {self.color} окрас, вырастает до  {self.size} см роста и размаха крыльев{self.wings} см, относится к крупным " \
                f" обитает в {self.arial} регионе, умеет летать {self.flying}."
    def __repr__(self) ->str:
        return f'flamingo {self.name} {self.breed} {self.color} {self.size} {self.wings} {self.arial} {self.flying}'


    def size1(self):
        if self.size >= 140:
            return "крупный"
        elif 120 <= self.size <= 140:
            return "большой"
        elif self.size <= 100:
            return"средний"

    def arial1(self):
        if self.arial == "Северная или Южная Америка":
            return "Американский"
        elif self.arial == "Европа и Азия":
            return "Евроазиатский"
        elif self.arial == "Африка":
            return "Африканский"
        elif self.arial == "Австралия":
            return "Австралийский"
        elif self.arial == "Антарктида":
            return "Антарктический"
        elif self.arial == "Арктика":
            return "Арктический"
        assert False

    class Generator:
        def __create_breed(self) -> str:
            self.breed = random.choice(['малый', 'чилийский', 'красный', 'розовый'])
            return self.breed

        def __create_sizes(self):
            self.size = random.randint(20, 250)
            return self.size

        def __create_size(self) -> str:
            if self.size >= int(140):
                return "крупный"
            elif int(120) <= self.size <= int(140):
                return "большой"
            elif self.size <= int(100):
                return "средний"

        def __create_area(self) -> str:
            self.area = random.choice(['Северная Америка', 'Южная Америка', 'Европа', 'Азия',
                                       'Австралия', 'Антарктида', 'Арктика'])
            return self.area

        def __create_areal(self) -> str:
            if self.area == "Северная Америка":
                return "американском"
            elif self.area == "Южная Америка":
                return "американском"
            elif self.area == "Европа":
                return "европоазиатском"
            elif self.area == "Азия":
                return "европоазиатском"
            elif self.area == "Африка":
                return "африканском"
            elif self.area == "Австралия":
                return "австралийском"
            elif self.area == "Арктика":
                return "арктическом"
            elif self.area == "Антарктида":
                return "антарктический"

            assert False

        def __create_flying(self) -> str:
            self.flying = random.choice(['умеет летать', 'не умеет летать'])
            return self.flying

        def generate_single(self):
            name = names.get_first_name()
            return [name, self.__create_breed(), self.__create_sizes(), self.__create_size(), self.__create_area(),
                    self.__create_areal(), self.__create_flying()]

        def generate_1000(self) -> list:
            flamingolist = list()
            for i in range(1001):
                flamingolist.append(self.generate_single())
            return flamingolist

        def generate_10000(self) -> list:
            flamingolist = list()
            [flamingolist.append(self.generate_single()) for i in range(10000)]
            return flamingolist

    if __name__ == "__main__":
        flamingo = Flamingo("Ник", "розовый", str(60), "Европа")
        print(flamingo.get_info())

        flamingo = Flamingo("Сэм", "красный", str(105), "Северная Америка")
        print(flamingo.get_info())

        flamingo = Flamingo("Рик", "чилийский", str(80), "Южная Америка")
        print(flamingo.get_info())

        g = Generator()
        print(g.generate_single())
        print(g.generate_1000())
        print(g.generate_10000())