nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'], 'h', False, [1, 2, 3, 4, 5],
    [1, 2, None]
]


class Flatiterator:

    def __init__(self, nested_list):
        self.nested_list = self.flattern(nested_list)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < len(self.nested_list):
            self.result = self.nested_list[self.count]
            self.count += 1
            return self.result
        else:
            raise StopIteration

    def flattern(self, nested_list):
        flatted_list = []
        for item in nested_list:
            if isinstance(item, list):
                flatted_list.extend(self.flattern(item))
            else:
                flatted_list.append(item)
        return flatted_list


def flat_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            for i in flat_generator(item):
                yield i
        else:
            yield item


if __name__ == '__main__':

    for item in Flatiterator(nested_list):
        print(item)

    for item in flat_generator(nested_list):
        print(item)
