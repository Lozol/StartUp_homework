# Створіть три списки: int_list, float_list, str_list. Користуючись пакетами рандомізації,
# заповніть словник   int_list випадковими цілочисельними значеннями, у кількості 5000 елементів, в діапазоні
# від 0 до 1000. Заповніть словник float_list випадковими значеннями, у кількості 5000 елементів, в діапазоня
# від 0,1 до 100,0. Також заповніть словник str_list випадковими словами теж у кількості 5000 елементів.
import random
from random_word import RandomWords
import time

int_list=[]
float_list=[]
str_list=[]

w = RandomWords()

for i in range(0,5000):
    int_list.append(random.randint(0,1000))
    float_list.append(random.uniform(0.1,100.0))
    str_list.append(w.get_random_word())

# print("Int List:", int_list)
# print("Int List:", float_list)
# print("Int List:", str_list)
a = str_list
N = len(a)      # число элементов в списке

for i in range(0, N-1):     # N-1 итераций работы алгоритма
    for j in range(0, N-1-i):   # проход по оставшимся не отсортированным парам массива
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)
# Додайте до попередньої програми код, будь-якого алгоритму сортування. Додайте функцію яка б обраховувала
# середній час роботи алгоритму сортування. Функція повинна приймати список і кількість ітерацій циклів
# сортування, а повертати середній час роботи алгоритму сортування.

def get_time_for_working_function(x,y):
   start = time.time()
   for i in range(y):
        N = len(x)
        for i in range(0, N-1):
            for j in range(0, N-1-i):
               if x[j] > x[j+1]:
                   x[j], x[j+1] = x[j+1], x[j]
        # return x
   end = (time.time() - start)/y
   print(end)

p = get_time_for_working_function(str_list,10) # навіть не пробуй на 5000, бо на 50 комп сильно думав!

