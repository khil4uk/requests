import requests
from pprint import pprint

def ability_get(search_name, ability='intelligence'):
    url = "https://superheroapi.com/api/2619421814940190/"
    ability_list = list() # создаем список из информации о id, имени и intelligence героя
    for i in search_name:
        final_url = url + "search/" + i # формируем итоговый путь для осуществления запроса по адресу
        superhero = requests.get(final_url, timeout=5).json()["results"][0]
        ability_list.append({'id': superhero["id"], # формируем словарь и наполняем созданный ранее список
                           'name': superhero["name"],
                           'intelligence': int(superhero["powerstats"][ability])}) # приводим к типу integer для последующего сравнения
    return ability_list

if __name__ == '__main__':
    superhero = ['Hulk', 'Captain America', 'Thanos']
    superpower = 'intelligence'
    results = ability_get(superhero, superpower)
    #pprint(results)
    max_intelligence = {'id': 0, 'name': 'none', superpower: 0} # создаем пустой словарь для последующей работы цикла
    for person in results:
        if max_intelligence[superpower] < person[superpower]:
            max_intelligence = person
    print(f'\nСамым умным супергероем является {max_intelligence["name"]}. Уровень его {superpower} равен {max_intelligence[superpower]}.')