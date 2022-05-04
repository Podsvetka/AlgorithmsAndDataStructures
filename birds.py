class Birds():
    def __init__(self, name, breed, color, wings, size, arial, flying):
        self.name = name
        self.breed = breed
        self.color = color
        self.size = size
        self.wings = wings
        self.arial = arial
        self.flying = flying

    def get_info(self):
        return f"{self.name} породы {self.breed} , что имеет {self.color} окрас, вырастает до  {self.size} см роста и размаха крыльев{self.wings} см, относится к крупным " \
                f" обитает в {self.arial} регионе, умеет летать {self.flying}."
    def size1(self):
        if self.size >= 140:
            print("крупный")
        elif 120 <= self.size <= 140:
            print("большой")
        elif self.size <= 100:
            print("средний")

    def arial1(self):
        if self.arial == "Северная или Южная Америка":
            print("Американский", birds.get_info(),)
        elif self.arial == "Европа и Азия":
            print("Евроазиатский", birds.get_info(),)
        elif self.arial == "Африка":
            print("Африканский", birds.get_info(), )
        elif self.arial == "Австралия":
            print("Австралийский", birds.get_info(), )
        elif self.arial == "Антарктида":
            print("Антарктический", birds.get_info(), )
        elif self.arial == "Арктика":
            print("Арктический", birds.get_info(), )


 if ...name... == "main":
    birds = Birds("Сэм", "розовый фламинго", "розовый", "большой", "100 см", "Африканский", "умеет летать")