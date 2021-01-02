import time
from multiprocessing import Pool

with open("cities_s") as file:
    city_list = file.read().split(" ")
city_map = {}


def get_last_char(city):
    index = -1
    while city[index] in 'ьый':
        index -= 1
    return city[index]


def get_chain(first_char, array):
    chain = []
    for index in array:
        if index[0].lower() == first_char:
            chain.append(index)
    return chain


def get_length(city):
    city_string = ""
    city_count = 0
    array = city_list[:]
    array.remove(city)
    last_char = get_last_char(city)
    index = 0

    while index < len(array):
        option = array[index]
        first_char = option[0].swapcase()
        if first_char == last_char:
            city_string += option + " "
            city_count += 1
            last_char = get_last_char(option)
            array.remove(option)
            index = 0
        else:
            index += 1
    return city, city_count, city_string


def get_key(value, array):
    names = []
    for index in array:
        if index[1] == value:
            names.append(index[0])
    return names


if __name__ == "__main__":
    time_now = time.time()

    p = Pool(4)
    clist = p.map(get_length, city_list)
    p.close()
    p.join()

    city_values = []
    for i in clist:
        city_values.append(i[1])
    city_values.sort(reverse=True)
    print("Longest value: {}".format(city_values[0]))
    city_final = get_key(city_values[0], clist)
    print(city_final)
    cstring = get_length(city_final[0])[2]
    print(cstring)
    time_after = time.time() - time_now
    print("%6.2f sec" % time_after)
    # print("Time to remove:", cstring.split()[-1])
    # city_list.remove(cstring.split()[-1])
    # with open("cities_s", 'w') as file:
    #     file.write(" ".join(city_list))
