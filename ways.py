import json
from itertools import chain


def recursive_a(source_object, specs, potential_paths=[], begin_path=''):
    if specs.get(source_object, None):
        for value in specs[source_object]:
            path = f'{begin_path}/{value.__name__}'
            potential_paths.append(path)
            if specs.get(value, None):
                recursive_a(value, specs, potential_paths, path)
    return potential_paths


def recursive_b(source_object, specs):
    alg_dict = {source_object.__name__: 'NOT IMPLEMENTED YET'}
    return alg_dict


class Component:
    def __init__(self, *algorithm_list):
        self.algorithm_list = algorithm_list

    def __call__(self, source_object):
        result = []
        queue = [source_object]
        while queue:
            result.extend(queue)
            queue = list(chain.from_iterable(
                algorithm(item)
                for item in queue
                for algorithm in self.algorithm_list
            ))
        return result

    def find_potential_paths(self, source_object):
        path = f'/{source_object.__name__}'
        potential_paths = [path]
        for algorithm in self.algorithm_list:
            specs = algorithm.SPECIFICATION
            recursive_a(source_object, specs, potential_paths, path)
        return potential_paths

    def my_method(self, source_object):
        potential_paths = self.find_potential_paths(source_object)
        algorithm_paths = {}
        for algorithm in self.algorithm_list:
            specs = algorithm.SPECIFICATION
            alg_dict = {}
            if specs:
                alg_dict = recursive_b(source_object, specs)
            algorithm_paths[algorithm.__class__.__name__] = alg_dict

        return {'Potential': potential_paths, 'Algorithm': algorithm_paths}


class Apple:
    pass


class Orange:
    def __init__(self, number):
        self.number = number


class Lemon:
    pass


class FirstAlgorithm:
    SPECIFICATION = {
        Orange: [Apple],
        Lemon: [Orange, Apple]
    }

    def __call__(self, source_object):
        if isinstance(source_object, Orange):
            return [Apple() for _ in range(source_object.number)]
        if isinstance(source_object, Lemon):
            return [Orange(3), Apple()]
        return []


class EmptyAlgorithm:
    SPECIFICATION = {}

    def __call__(self, source_object):
        return []


if __name__ == '__main__':
    component = Component(FirstAlgorithm(), EmptyAlgorithm())
    print(json.dumps(
        component.my_method(Lemon),
        indent=4
    ))
