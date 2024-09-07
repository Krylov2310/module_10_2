from threading import Thread
from time import sleep

print('\033[30m\033[47mДомашнее задание по теме "Потоки на классах"\033[0m')
print('\033[30m\033[47mЗадача "За честь и отвагу!":\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.start_power = 100

    def start_battle(self):
        print(f'\33[31m{self.name}, на нас напали!\33[0m')

    def end_battle(self):
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!\n')

    def battle(self):
        print(f'{self.name} сражается {self.days} день(дня)..., осталось {self.start_power} войнов.\n')

    def run(self):
        self.start_battle()
        for i in range(self.start_power):
            if self.start_power > 0:
                self.start_power -= self.power
                self.days += 1
                self.battle()
                sleep(1)
                if self.start_power <= 0:
                    self.end_battle()


# Алгоритм выполнения кода:
first_knight = Knight('\33[34mSir Lancelot\33[0m', 10)
second_knight = Knight('\33[35mSir Galahad\33[0m', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print(f'\33[32mВсе битвы закончились!\33[0m')
print()
print(thanks)
