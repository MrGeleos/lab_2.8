#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_train(list_trains):
    destination = input("Пункт назначения? ")
    number = input("Номер поезда? ")
    timer = input("Время отправления (ЧЧ:ММ)? ")

    train = {
        'destination': destination,
        'number': number,
        'timer': timer,
    }

    list_trains.append(train)
    if len(list_trains) > 1:
        list_trains.sort(key=lambda item: item.get('timer', ''))
    return list_trains


def display_train(list_trains):
    if list_trains:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                "№",
                "Пункт",
                "Номер поезда",
                "Время отпраления"
            )
        )
        print(line)

        for idx, train in enumerate(list_trains, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                    idx,
                    train.get('destination', ''),
                    train.get('number', ''),
                    train.get('timer', '')
                )
            )
        print(line)
    else:
        print("Список пуст")


def select(command_a, list_trains):
    parts = command_a.split(' ', maxsplit=1)
    des = parts[1]
    count = 0

    for train in list_trains:
        if train.get('destination') == des:
            count += 1
            print(
                '{:>4}: {}'.format(count, train.get('destination', '')),
            )
            print('Номер поезда: ', train.get('number', '')),
            print('Время отправления: ', train.get('timer', ''))

    if count == 0:
        print("Поезд с таким пунктом не найден.")


def help_1():
    print("Список комaнд:\n")
    print("add - добавить поезд;")
    print("list - вывести список поезда;")
    print("select - запросить поезд с пунктом назначения;")
    print("exit - завершить работу с программой.")


if __name__ == '__main__':
    trains = []
    while True:
        command = input(">>> ").lower()
        if command == "exit":
            break
        elif command == "add":
            trains = get_train(trains)
        elif command == "list":
            display_train(trains)
        elif command.startswith('select '):
            select(command, trains)
        elif command == "help":
            help_1()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
