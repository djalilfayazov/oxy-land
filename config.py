from os import getenv
from dotenv import load_dotenv


load_dotenv()


class Settings:
    def __init__(self) -> None:
        self.token = getenv('TOKEN')
        self.db = getenv('DB_NAME')

        self.ranks = {
            'grey': ('серый', 1),
            'green': ('зеленый', 2),
            'blue': ('голуюбой', 3),
            'violet': ('фиолетовый', 4),
            'pink': ('розовый', 5),
            'red': ('красный', 6),
            'gold': ('золотой', 7)
        }


    def get_msg(self, name:str):
        with open(f'msgs/{name}.txt', 'r', encoding='utf-8') as file:
            return str(
                file.read()
            )