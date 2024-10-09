import requests

url = "https://docs.google.com/spreadsheets/d/1S3kj0zo_QDERJu7O2QU1J4gMRx-K381m/export?format=xlsx"

def download(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open("spreadsheet.xlsx", "wb") as file:
            file.write(response.content)
        print("Скачать!")
    else:
        print("Код ошибки :", response.status_code)

download(url)