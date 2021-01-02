import time
import networkx as nx
import matplotlib.pyplot as p
import networkx.algorithms.dag as nxd

with open("cities") as file:
    city_list = file.read().split(",")
graph = nx.DiGraph()


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


def get_graph(city, array):
    graph.add_node(city)
    if city in array:
        array.pop(city)
    chain = get_chain(get_last_char(city), array)
    if len(chain) == 0:
        return 0
    else:
        for index in chain:
            graph.add_edge(city, index)
            graph.add_weighted_edges_from([(city, index, 1)])
            get_graph(index, array)


if __name__ == "__main__":
    time_now = time.time()

    for i in city_list:
        graph_map = {i: 0 for i in city_list}
        get_graph(i, graph_map)

    nx.draw(graph, with_labels=True, font_weight='light')

    # pos = nx.spectral_layout(graph)
    # nx.draw(graph, pos)
    # nx.draw_networkx_labels(graph, pos)
    # nx.draw_networkx_edge_labels(graph, pos)

    p.show()

    # Longest
    # value: 6
    # ['Новосибирск', 'Уфа', 'Ульяновск']
    # Красноярск # Краснодар # Ростов - на - Дону # Уфа # Архангельск # Кострома

    for n, nbrs in graph.adj.items():
        for nbr, eattr in nbrs.items():
            wt = eattr['weight']
            print('%s, %s, %.3f' % (n, nbr, wt))

    print(graph['Новосибирск'])

    # p2 = nx.johnson(graph, weight='weight')
    # for i in city_list:
    #     for j in city_list:
    #         if nx.has_path(graph, i, j) and i != j:
    #             print('{} - {} : {} value {}'.format(i, j, p2[i][j], len(p2[i][j])-1))

    # lngst = nxd.dag_longest_path_length(pos)
    # lng_path = nxd.dag_longest_path(pos)
    # print(lngst)
    # print(lng_path)

    shortest_paths = dict(nx.all_pairs_shortest_path(graph))

    chains = []
    for from_name, path_dict in shortest_paths.items():
        for to_name, path in path_dict.items():
            if from_name != to_name:
                chains.append(path)

    max_chain_len = 0
    for i in chains:
        if max_chain_len < len(i):
            max_chain_len = len(i)

    long_chains = []
    cities_set = set()
    for i in chains:
        if len(i) == max_chain_len:
            long_chains.append(i)
            cities_set.add(i[0])

    print("Cities: {}".format(len(cities_set)))
    print("Longest value: {}".format(max_chain_len))
    for i in cities_set:
        print(i, end=" ")
    print()
    # print("-->", long_chains[0])
    time_after = time.time() - time_now
    print("%6.2f sec" % time_after)
