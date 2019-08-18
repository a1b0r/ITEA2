# Создать свою структуру данных Список, которая поддерживает индексацию.
# Методы pop, append, insert, remove, clear.
# Перегрузить операцию сложения для списков, которая возвращает новый расширенный объект.

# Указанные методы описываем самостоятельно, без использования стандартных.


class DataList:

    def __init__(self):
        self._list_indexes = []
        self._list_data = []

    def __setitem__(self, value):
        list_len = self.len()
        self._list_indexes += [list_len + 1]
        self._list_data += [value]

    def append(self, value):
        self.__setitem__(value)

    def __getitem__(self):
        list_len = self.len()
        result = self._list_data[list_len-1:]
        self._list_indexes = self._list_indexes[:list_len-1]
        self._list_data = self._list_data[:list_len-1]
        return result

    def pop(self):
        return self.__getitem__()

    def insert(self, index, value):
        list_len = self.len()
        index -= 1
        if list_len >= index >= 0:
            list_end = self._list_indexes[index:]
            for idx in list_end:
                list_end[idx-1] += 1
            self._list_indexes = self._list_indexes[:index] + [index+1] + list_end[:]
            self._list_data = self._list_data[:index] + [value] + self._list_data[index:]
        else:
            raise Exception('Out of range')

    def remove(self, index):
        list_len = self.len()
        index -= 1
        if list_len >= index >= 0:
            list_end = self._list_indexes[index+1:]
            for idx in list_end:
                print(idx)

                list_end[idx-1] -= 1
            self._list_indexes = self._list_indexes[:index] + list_end[:]
            self._list_data = self._list_data[:index] + self._list_data[index - 1:]
        else:
            raise Exception('Out_of_range')

    def __len__(self):
        return len(self._list_indexes)

    def len(self):
        return self.__len__()

    def __str__(self):
        print_list = '['
        for idx in range(self.len()):
            if idx > 0:
                print_list += ','
            print_list += f'({self._list_indexes[idx]},{self._list_data[idx]})'
        print_list += ']'
        return print_list


new_list = DataList()

new_list.append('a')
new_list.append('b')
new_list.append('c')
print(new_list)
new_list.pop()
print(new_list)
new_list.insert(1, 'd')
print(new_list)
new_list.append('f')
print(new_list)
new_list.remove(3)
print(new_list)
