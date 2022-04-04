import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_upload_link(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"  # запрос на получение ссылки (из документации)
        name = file_path.split('/', )[-1]  # имя загружаемого файла
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)} # определяем формат заголовков запроса
        params = {"path": f"Загрузки/{name}", "overwrite": "true"} # параметры запроса
        _response = requests.get(upload_url, headers=headers, params=params).json()
        href = _response.get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status() # статус отправки
        if response.status_code == 201: # проверка выполнения запроса
                print(f"Файл {file_path.split('/', )[-1]} успешно загружен на Яндекс.Диск")
        else:
            return f"Ошибка выполнения запроса. Код ошибки: {responce.status_code}"

if __name__ == '__main__':
    file_path = 'Example.txt' # ссылку на файл помещаем в переменную
    token = '...'
    uploader = YaUploader(token) # вносим собственный токен
    result = uploader.get_upload_link(file_path)  # Используя функцию get_upload_link, загружаем файл на яндекс диск
    print(result)