def merge(*dicts):
    result = {}
    for dictionary in dicts:
        result.update(dictionary)
    return result

dict1 = {'a': 1, 'b': 2}
dict2 = {'f': 6, 'g': 7}
dict3 = {'d': 4, 'e': 5}
dict4 = {'h': 8, 'c': 3}

merged = merge(dict1, dict2, dict3, dict4)
sort = dict(sorted(merged.items())) #reverse=True
print("Объединённый отсортированный словарь:", sort)