import time


def get_length(city, array, string=False):
    # string - или возвращаем длину и всю цепь, или только длину
    city_string = ""
    city_count = 0
    array.remove(city)
    last_char = city[-1]
    bad_char = -2
    while last_char in 'ъьый':
        last_char = city[bad_char]
        bad_char -= 1
    i = 0

    while i < len(array):
        choice = array[i]
        # print(choice)
        first_char = choice[0].swapcase()
        if first_char == last_char:
            if string:
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

    if string:
        city_string.rstrip()
        return city_count, city_string
    else:
        return city_count


def get_key(value, array):
    names = []
    for name, val in array.items():
        if val == value:
            names.append(name)
    return names


if __name__ == "__main__":
    time_now = time.time()
    with open("cities") as file:
        city_list = file.read().split(" ")  # city_list - список городов
    city_map = {}  # city_map - словарь город:длина цепочки
    for i in city_list:
        city_copy = city_list.copy()
        city_map[i] = get_length(i, city_copy)
    city_values = list(city_map.values())  # city_values - список длин всех цепочек
    city_values.sort(reverse=True)
    print("Longest value: {}".format(city_values[0]))
    city_final = get_key(city_values[0], city_map)  # city_final - словарь городов с самой длинной цепью
    print(city_final)
    # for i in city_final:
    #     city_copy = city_list.copy()
    #     print(get_length(i, city_copy, True)[1])
    city_copy = city_list.copy()  # ещё раз составляем самую длинную цепь
    print(get_length(city_final[0], city_copy, True)[1])
    time_after = time.time() - time_now
    print("%6.2f sec" % time_after)
