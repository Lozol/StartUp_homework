#1.Напишіть функцію, яка б приймала номер місяця  і вертала його назву. Реалізуйте
#у функії  декільк обробок виключень:
def month_name(num):
    try:
        if (num >= 1) & (num <= 12):
            en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
              'october', 'november', 'december']
        print(en[num - 1])
    except TypeError:
        print('Помилка в значенні')
    except UnboundLocalError:
        print('Це щось з календаря майя')
    else:
        print('Помилок не має')

a = month_name(13)



#2.Напишіть программу , яка сприймала список  з числами та перевіряла  чи всі числа в ньому унікальні .
#еалізуйте у функції декілька обробок виключень.
def unicum_number(list):
    try:
        col = 0
        for i in range(len(list)):
            for j in range(len(list)):
                if i != j and list[i] == list[j]:
                   col+=1
        if col==0:
            print("Всі числа унікальні")
        else:
            print("Є не унікальні числа")
    except ValueError:
        print('Помилка в значенні')
    except TypeError:
        print('Нема введення')

p1 = unicum_number(list)


#3.Напишіть користувацький клас виключення з функціоналом на свій вибір.
#Викличте його за допомогою інструкції raise

class MyErrorSendPost(Exception):
    '''Клас виключення при відправленні пошти'''
    def __int__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"MyErrorSendPost: {self.message}"


class SendPost:
    def print(self,text):
        self.send_text(text)
        print(f"Send: str(text)")

    def send_text(self,text):
        if not self.send_post(text):
            raise MyErrorSendPost("Post not available")

    def send_post(self, text):
        return False

p = SendPost()
p.print('hhjkjhh')