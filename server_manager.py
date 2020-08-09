# Импортируем созданный нами класс Server
from server import Server
# Получаем из config.py наш api-token
from config import vk_api_token


server1 = Server('тут токен', 'тут id', "server1")

server1.test()


def start(self):
    for event in self.long_poll.listen():
        print(event)
