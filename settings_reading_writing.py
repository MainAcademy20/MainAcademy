

def recording(sets):
    """ Запись  файла настроек"""
    try:
        with open('Settings.txt', '+w') as f:
            sets_rec = f.write(sets)

    except (OSError, IOError):

        sets_rec = str("Settings.txt [CNTTOWRITE] can not to write ")  # [WARNING] не могу обработать
    return sets_rec


def reading():
    """ Чтение с файла настроек"""
    try:
        with open('Settings.txt', '+r') as f:
            sets_read = f.read()

    except (OSError, IOError):

        sets_read = str("Settings.txt [CNTTOREAD] can not to read ")   #"""[WARNING] не могу обработать  [CNTTOREAD]

                                                                       # def count_event(log_text) log_reading """

    return sets_read


def list_generator (string_tolist, count ):
    """ Группировка элементов последовательности(списка) по count элементов ,разделить его на несколько частей,"""
    start = 0
    for i in range(count):
        stop = start + len(string_tolist[i::count])
        yield string_tolist[start:stop]
        start = stop


def list_creator():
    """Создание вложенного списка на 2 уровня на 2 элемента после лист_генератора"""
    trylist = []
    for elem in test:
        trylist.append(elem)
    return trylist


def string_creator(norm_list):
    """Выводит все вложенные списки на 1 этаж"""
    from itertools import chain
    ready_tostring = list(chain(*norm_list))
    tostring = slice_string(ready_tostring)
    return tostring


def slice_string(ready_tostring):
    """Операция на строкой (удаление элементов обозначения списка стринговой строки)"""
    ready_tostring = str(ready_tostring)
    ready_tostring = ready_tostring[1:]  # slice []
    ready_tostring = ready_tostring[:-1]
    return ready_tostring


def formating(index1,index2):
    """ Оформление єлементов списка для вывода на запрос"""
    format_list = 'Параметр {}, значение : {}'.format(index1,index2)
    return format_list


def midle_data(data):
     """ Не продумал логику изменения настроек в Settings.txt"""
                                    # Температурный режим почвы тоже важен и должен находиться в пределах 14 – 25 °С
     data_min = data - 3          # дневная температура воздуха в теплице должна быть 16 – 25 °С
     data_max = data + 3          # важно проветривать теплицу в солнечные дни, температура при этом составляет
     return data_min, data_max    # 28 – 30 °С, а в пасмурные должна колебаться в районе 20 – 22 °С


def change_value_setting():
    """ Не продумал логику изменения настроек в Settings.txt"""
    pass

# testmin = 0
# testmax = 0
# data = 16
# test = midle_data(data)
# print(test, type(test))


sets_read = slice_string(reading())           # чтение стринг строка из файла Settings после обрезания slice []
print('String from Settings\n',sets_read, type(sets_read))

string_tolist = sets_read.split(',')          # разбивание строки в список
count = len(string_tolist)// 2                #(2 этаж)   # определяется глубина разбития списков от кол-ва єлементов на этажах

test = list_generator(string_tolist,count)   # test - формируется счетчик для постороения 1 или многоэтажных списков
norm_list = list_creator()
print('\n2х этаж список\n',norm_list, type(norm_list))      # [["'air_temp_min'", ' 0']
                                                            # prints the string by removing geeks
                                                            # print(string.strip(' geeks')) :first reference
                                                            # много лишних ковычек в списке, требуется обработка

t01 = formating(norm_list[0][0],norm_list[0][1] )
t23 = formating(norm_list[1][0],norm_list[1][1] )
t45 = formating(norm_list[2][0],norm_list[2][1] )
t67 = formating(norm_list[3][0],norm_list[3][1] )
t89 = formating(norm_list[4][0],norm_list[4][1] )
t1011 = formating(norm_list[5][0],norm_list[5][1] )
t1213 = formating(norm_list[6][0],norm_list[6][1] )
t1415 = formating(norm_list[7][0],norm_list[7][1] )


#print('1\n',t01, type(t01),'\n2\n',t23,'\n3\n',t45,'\n4\n',t67,'\n5\n',t89,'\n6\n',t1011,'\n7\n',t1213,'\n8\n',t1415)
# t1 = auto_formating(norm_list)
# print('1\n',t1, type(t1))

# norm_list = list_creator()
# norm_list1 = (string_creator(norm_list))
# last_rec = recording(norm_list1)            # запись стринга строка в сетинги
# norm_list = list_creator()
# print('\ntest',norm_list1, type(norm_list1))
# new_set_read = sets_read.split(",")

# test_norm_list = str(decor)
# print('~~~~~~~~~~~~~~~~', test_norm_list)

# test = decor_reading()
# test2 = decor_reading(sets_read)
# print('==========',test, type(test),'==========\n', norm_list[2][1],norm_list [3][0], "test[3]")
# print('===',test2, type(test2))
# print('\n ',sets_read, type(sets_read))
# print('##########',sets_read[3][0])