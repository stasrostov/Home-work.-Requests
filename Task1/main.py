import requests

url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
names = ['Hulk', 'Captain America', 'Thanos']
intellegence_dict = {}
response = requests.get(url=url)


def get_intellegence_by_names(names_list):
    for name in names_list:
        for element in response.json():
            if element['name'] == name:
                intellegence_dict[name] = element['powerstats']["intelligence"]
    max_intellegence_name = max(intellegence_dict, key=intellegence_dict.get)
    print(max_intellegence_name)


if __name__ == '__main__':
    get_intellegence_by_names(names)
