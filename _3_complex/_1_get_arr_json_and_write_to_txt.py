import json

# TODO 1st decision


# with open('temp/data.json', mode='r', encoding='utf-8') as file:
#     data = json.load(file)
#     print(data)
#
# formatted_data = []
#
# for item in data:
#     id = item['id']
#     userId = item['userId']
#     title = item['title']
#
#     formatted_item = f'{id} | {userId} | {title} | {title}'
#
#     formatted_data.append(formatted_item)

# TODO 2nd decision

with open('temp/data.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)
    print(data)

with open('temp/data.txt', mode='w', encoding='utf-8') as file:
    for item in data:
        completed = item.get('completed', 0)
        data_string = f"{item['id']} | {item['userId']} | {item['title']} | {completed}\n"
        file.write(data_string)
