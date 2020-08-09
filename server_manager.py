# Импортируем созданный нами класс Server
from server import Server
# Получаем из config.py наш api-token
from config import vk_api_token


server1 = Server('6ea0f22a765091ccc6efeb1c1c3211c1c74c2b3224e22d26fb304485d488eae2c5bd8f86179f0359bae7b', '154573014', "server1")
# vk_api_token - API токен, который мы ранее создали
# 172998024 - id сообщества-бота
# "server1" - имя сервера

server1.test()


def start(self):
    for event in self.long_poll.listen():
        print(event)