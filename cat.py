from project_exam.animal import Animal


class Cat(Animal):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {str(self.age)} year old {self.gender} {self.__class__.__name__}"

    def make_sound(self):
        return "Meow meow!"