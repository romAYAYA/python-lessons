def search_target_name(target_name: str, list_names: list):
    for i in list_names:
        if i == target_name:
            return True
    return False


def search_target_name2(target_name: str, list_names: list):
    return target_name in list_names


print(search_target_name('Anime', ['Roma', 'Oleg', 'Anime']))
print(search_target_name2('Danila', ['Roma', 'Oleg', 'Anime']))