import requests, os, re
from dotenv import load_dotenv

load_dotenv()

class Bible:
    __code = 0
    __API_KEY = os.getenv('API_KEY')
    __HEADER = {'api-key': f"{__API_KEY}"}

    def __init__(self):
        pass

    def get_verse(self, name):
        verse_id = self.check_book(name)
        response = requests.get(self.__url('verses') + verse_id, headers = self.__HEADER)
        self.__code = response.status_code
        response_json = response.json()
        
        return self.__format_content(response_json['data']['content'])
    
    # searchs for the existence of a book and returns it's ID with it's chapter
    def check_book(self, name):
        response = requests.get(self.__url('books'), headers = self.__HEADER)
        response_json = response.json()
        
        tuple = self.__format_verse(name)
        
        if tuple == None:
            return 'Not a well formed verse, please try again.'
        else:
            name_part = tuple[0]
            chapter_part = tuple[1]

        for book in response_json['data']:
            if name_part in book['name']:
                return book['id'] + chapter_part
            
    def status(self):
        return self.__code
    
    # removes the html from the content 
    def __format_content(self, content):
       return re.sub('<[^<]+?>','',str(content)).strip()
   
   # formats the verse: John 3:16 > (John, 3.16) required for check_book() call
    def __format_verse(self, verse):
       arr = verse.split(' ', 1)
       
       try:
           name_part = arr[0]
           chapter_part = f".{arr[1].replace(':', '.')}"
    
           return name_part, chapter_part
       except IndexError:
           return None
    
    # returns differents url for http requests based on choice
    def __url(self, choice):
        match choice:
            case 'verses':
               return "https://api.scripture.api.bible/v1/bibles/de4e12af7f28f599-01/verses/"
            case 'books':
                return "https://api.scripture.api.bible/v1/bibles/de4e12af7f28f599-01/books"