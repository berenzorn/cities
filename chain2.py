import time
from multiprocessing import Pool

with open("cities") as file:
    # city_list - список городов
    city_list = file.read().split(" ")
# city_map - словарь город:длина цепочки
city_map = {}
city_text = ""


def get_length(city):
    global city_map
    city_string = ""
    city_count = 0
    array = city_list[:]
    array.remove(city)
    last_char = city[-1]
    bad_char = -2

    while last_char in 'ъьый':
        last_char = city[bad_char]
        bad_char -= 1
    i = 0

    while i < len(array):
        choice = array[i]
        first_char = choice[0].swapcase()
        if first_char == last_char:
            city_string += choice + " "
            city_count += 1
            last_char = choice[-1]
            bad_char = -2
            while last_char in 'ъьый':
                last_char = choice[bad_char]
                bad_char -= 1
            array.remove(choice)
            i = 0
        else:
            i += 1
    return city, city_count, city_string


def get_key(value, array):
    names = []
    for i in array:
        if i[1] == value:
            names.append(i[0])
    return names


if __name__ == "__main__":
    # список кортежей из названия, длины цепи и цепи
    clist = []
    time_now = time.time()
    p = Pool(8)
    clist = p.map(get_length, city_list)
    p.close()
    p.join()
    # city_values - список длин всех цепочек
    city_values = []
    for i in clist:
        city_values.append(i[1])
    city_values.sort(reverse=True)
    print("Longest value: {}".format(city_values[0]))
    # city_final - словарь городов с самой длинной цепью
    city_final = get_key(city_values[0], clist)
    print(city_final)
    cstring = get_length(city_final[0])[2]
    print(cstring)
    time_after = time.time() - time_now
    print("%6.2f sec" % time_after)
#    print("Time to remove:", cstring.split()[-1])
#    city_list.remove(cstring.split()[-1])
#    with open("cities", 'w') as file:
#        file.write(" ".join(city_list))
