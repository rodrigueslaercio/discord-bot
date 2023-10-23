import requests, os
import re
from dotenv import load_dotenv

load_dotenv()

class Bible:
    __code = 0
    __API_KEY = os.getenv('API_KEY')

    def __init__(self):
        pass

    # TODO
    def get_verse(self):
        url = f"https://api.scripture.api.bible/v1/bibles/de4e12af7f28f599-01/verses/"
        header = {'api-key': f"{self.__API_KEY}"}
        response = requests.get(url, headers=header)

        self.__code = response.status_code

        response_json = response.json()
        
        return response_json
    
    def status(self):
        return self.__code
    
    # searchs for the existence of a book and returns it's ID with it's chapter
    def check_book(self, name):
        arr = name.split(' ', 1)
        name_part = arr[0]
        chapter_part = f".{arr[1].replace(':', '.')}"

        url = "https://api.scripture.api.bible/v1/bibles/de4e12af7f28f599-01/books"
        header = {'api-key': f"{self.__API_KEY}"}
        response = requests.get(url, headers=header)

        response_json = response.json()

        for book in response_json['data']:
            if name_part in book['name']:
                return book['id'] + chapter_part
        
        return 'Not found'