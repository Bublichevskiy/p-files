class Pet(object):
    """Виртуальный питомец"""
    total = 0

    @staticmethod
    def status():
        print("Общее число зверюшек", Pet.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Pet.total += 1

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def talk(self):
        print("Меня зовут", self.__name,
             ", и сейчас, я чувствую себя", self.mood)

    def eat(self, food = 4):
        print("Мррр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
 
    def play(self, fun = 4):
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
    def __str__(self):
        ans = 'Объект класса Pet\n'
        ans += "имя: " + self.name + "\n"
        return ans

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверушки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать что хорошо"
        else:
            m = "ужасно"
        return m

    def main():
        pet_name = input("Как вы назовете свою зверушку?: ")
        pet = Pet(pet_name)

        choice - None
        while choice != "0":
            print \
            ("""
            Моя зверюшка

            0 - Выйти
            1 - Узнать о самочувстии зверюшки
            2 - Покормить зверюшку
            """)

            choice = input("Ваш выбор: ")
            print()

        if choice == "0":
            print("До свидания.")
