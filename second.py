def find_reachable_vertexes(data, target_vertex, reachable_vertexes=None):
    if reachable_vertexes is None:
        reachable_vertexes = []
    reachable_vertexes.append(target_vertex)
    if data.get(target_vertex, None):
        for vertex in data[target_vertex]:
            if vertex not in reachable_vertexes:
                find_reachable_vertexes(data, vertex, reachable_vertexes)
    return reachable_vertexes


def my_code(data, target_vertex):
    vertexes = find_reachable_vertexes(data, target_vertex)
    for vertex in vertexes:
        print(vertex)


if __name__ == '__main__':
    data = {
        1: [2, 3],
        2: [4]
    }
    my_code(data, 1)
    data = {
        1: [2, 3],
        2: [3, 4],
        4: [1]
    }
    my_code(data, 1)
