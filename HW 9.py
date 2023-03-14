#Напишіть клас автомобіля з атрибутами: марка, колір, об'єм двигуна.
# Та методами: їхати вперед, їхати назад. Напишіть ще один клас автомобіля,
# який є успадкованим від першого.
# Додайте до нього методи повороту праворуч та ліворуч.
class Car():
    '''Клас автомобіля'''
    def __int__(self, brand,color,v_engine):
        '''Ініціалізуємо атрибути марки, кольору, об'єму двигуна'''
        self.brand = brand
        self.color = color
        self.v_engine = v_engine

    def go_forward(self):
        '''Авто буде їхати вперед'''
        print("Авто їде вперед")

    def go_back(self):
        '''Авто буде їхати назад'''
        print("Авто їде назад")



class CarModern(Car):
    '''Новий функціонал авто'''
    def __int__(self, brand, color, v_engine):
        '''Ініціалізуємо атрибути  класа предка'''
        super().__init__(brand, color, v_engine)

    def turn_left(self):
        '''Авто буде повертати вліво'''
        print("Авто повертає на ліво")

    def turn_right(self):
        '''Авто буде повертати вправо'''
        print("Авто повертає на право")


#Напишіть клас TextProcessor для обробки текстових даних.
# Клас повинен мати публічний метод get_clean_string, який видалить усі знаки
# пунктуації із рядка, який передається йому аргументом, та приватним методом is_punktiantian,
# який безпосередньо перевіряє символ на рівність із знаками пунктуації та повертає True/False,
# який, у свою чергу, є приватним або захищенним атрибутом. Потом напишіть клас TextLoader, який має
# приватний атрибут text_processor, що є об'єктом класу TextProcessor. Клас TextLoader повинен мати
# приватний атрибут clean_string і публічний метод set_clean_text, який буде викликати метод класу
# TextProcessor, через свій атрибут text_processor і записує значення в clean_string. Створіть додатково
# property для clean_string , який буде виводити повідомлення в консоль про те , що виводиться вже очищенний
# текст. Напишіть клас DataInterface, в якому буде захищенний атрибут , що є екземпляром класу TextLoader,
# а також публічний метод process_text , який буде приймати список рядків , опрацьовувати їх у циклі і
# виводити значення в консоль.

class TextProcessor():
    '''Ініціалізуємо атрибути '''
    def __init__(self, line):
        self.line = line

    def __is_punktiantian(self, i):
        t={'.',',','!','?',':',';'}
        if i in t:
            return True
        else:
            return False

    def get_clean_string(self, line):
        for c in line:
            if self.__is_punktiantian(c)==True:
                line = line.replace(c, '')
                return line


class TextLoader(TextProcessor):
    '''Ініціалізуємо атрибути '''
    def __init__(self, clean_string,line):
        '''Ініціалізуємо атрибути  класа предка'''
        super().__init__(line)
        self.clean_string = clean_string
        self.__text_processor = TextProcessor(line)

    # @property
    def set_clean_text(self, line):
        clean_string = self.__text_processor.get_clean_string(line)
        return clean_string

class DataInterface(TextLoader):
    '''Ініціалізуємо атрибути '''
    def __init__(self,line):
        '''Ініціалізуємо атрибути  класа предка'''
        super().__init__(line,line)
        self._text = TextLoader(line,line)

    def process_text(self, lst_in):
        for line in lst_in:
            text_out = self._text.set_clean_text(line)
            print(text_out)


data = ['jjklkjjk./','mnb...','jkk,,,,,']
f=DataInterface(data)
f.process_text(data)

#
#
# print(f.process_text())

# 3. Напишіть клас Parallelogram, який приймає два аргумента
# width  hight і метод get_area, який вираховує площу паралелограма . Успадкуйте від нього клас
# Square, перевизначіть в ньому метод et_areaтаким чином , щоб він вираховував площу квадрату.

class Parallelogram():
    '''Ініціалізуємо атрибути '''
    def __init__(self,wight,hight):
        self.wight= wight
        self.hight = hight

    def get_area(self):
        return self.wight * self.hight


class Square(Parallelogram):
    '''Ініціалізуємо атрибути '''
    def __init__(self,wight,hight):
        '''Ініціалізуємо атрибути  класа предка'''
        super().__init__(wight,hight)

    def get_area(self):
        '''Переориділяємо метод'''
        return self.wight * self.wight

d=Parallelogram(5,6)
print(d.get_area())
b=Square(7,7)
print(b.get_area())
