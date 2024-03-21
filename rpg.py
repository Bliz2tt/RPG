import random
import time
#Данные о персонаже
name = 'Маша'
power = 100
health = 100
money = 0
day = 1

situations = ['Монстр', 'Удача', 'Еда', 'Подарок']
monsters = ['Риптозавр', 'Змеекрыл', 'Хель', 'Грам', 'Нидхегг', 'Фафнир', 'Валькирия']
presents = ['Кольчуга', 'Оружие', 'Черный дух ночи']
vibe = ['Вы наступаете в лужу', 'Проход становится уже', 'Вы слышите странный шелест сзади', 'Вы видите просвет справа. Это небольшая дыра в стене', 'Вы наступили на что - то склизское', 'Вас обвевает прохладный сквозняк', 'Проход расширяется. Вдали вы видите что - то темное']

#начало
print("Добро пожаловать в игру! \nВы играете за персонажа, \nкоторый охотится за монстрами и получает за это монеты. \nСейчас у него силы: ", power, '\nденег: ', money, '\nздоровья: ', health )

#цикл игры
while health > 0:
#начало дня
    print('День', day)
    print(f'Сила: {power} \nЗдоровье: {health} \nМонеты: {money}')
    time.sleep(5)
#Выбор ситуации
    situation = random.choice(situations)
#ситуация монстр
    if situation == 'Монстр':
#данные о монстре
        name_m = random.choice(monsters)
        power_m = random.randint(1, 100)
        health_m = random.randint(1, 100)
        print(f'Имя монстра: {name_m} \nСила монстра:{power_m} \nЗдоровье монстра:{health_m}')

        time.sleep(5)
#сражение с монстром цикл повторяется пока здоровье участников больше 0
        while health_m > 0 and health > 0:
#удары участников
            your_bunch = random.randint(50, power)
            monster_bunch = random.randint(0, power_m)
#здоровье участников
            health = health - monster_bunch
            health_m = health_m - your_bunch
            print(f'Вы наносите удар с силой {your_bunch}. \nЗдоровье монстра: {health_m}')
            time.sleep(4)
            if health_m <=0:
                print(f'Вы одержали победу в этой битве! \nВаша награда: {monster_bunch} монет')
                money += monster_bunch
                time.sleep(4)
            else:
                print(f'Монстер наносит удар с силой {monster_bunch} \nВаше здоровье: {health}')
                time.sleep(4)
                if health_m <= 0 and health <= 0:
                    print('Вы победили монстра ценой собстренной жизни. Вы погибли, но слава о вас гремит в веках')
                    time.sleep(4)
                elif health > health_m:
                    print(f'Вы одержали победу в этой битве! \nВаша награда: {monster_bunch} монет')
                    money += monster_bunch
                    time.sleep(4)
                else:
                    print('Монстер съел вас. Игра окончена!')
                    time.sleep(2)
                    print(
                        f'Ваше здоровье: 0 \nВаша сила: 0 \nВаши монеты: {money}')
                    time.sleep(4)

#ситуация удача
    elif situation == 'Удача':
        print('Преред вами два коридора. \nОдин ведет направо, другой - налево.')
        answer = input('Выберите, в какой коридор вы пойдете (введите 1 или 2): ')
        lucky_door = random.randint(1, 2)
#удачный выбор
        if int(answer) == lucky_door:
            new_money = random.randint(1, 1000)
            print(f'Поздравляем! Вы нашли {new_money} монет!')
            money += new_money
#неудачный выбор
        else:
            print('Вы долго шли по коридору, но так ничего и не нашли')
        time.sleep(5)

#ситуация еда
    elif situation == 'Еда':
        if health < 100:
            print('Поздравляем! Вы нашли еду! Ваше здоровье восстановилось до 100!')
            health = 100
        else:
            print('Поздравляем! Вы нашли еду! Ваше здоровье пополнилось на 20')
            health = health + 20

        time.sleep(5)

#ситуация с коробочкой
    elif situation == 'Подарок':
        print('Вы нашли в земле коробочку. Что же в ней? Будем открывать?')
        box = input('Введите да или нет: ')
        present = random.choice(presents)
#если пользователь решает открыть коробку
        if box.lower() == 'да':
#если попадается кольчуга
            if present == 'Кольчуга':
                health = health + random.randint(1, 100)
                print(f'Поздравляем! Вы нашли кольчугу! Ваше здоровье поднимается до {health}')
#если попадается оружие
            elif present == 'Оружие':
                power = power + random.randint(1, 100)
                print(f'Поздравляем! Вы нашли оружие! Ваша сила поднимается до {power}')
#если попадается дух прошлого
            else:
                damage = random.randint(1, 50)
                health -= damage
                print('Берегись! Дух прошлого вылетает из коробки и наносит вам удар: -',damage, f'. Ваше здоровье: {health}')
#если дух сносит все здоровье
                if health <= 0:
                    print('Вы умерли. Игра окончена')
#если пользователь не открыл корробку
        else:
#если в коробке была кольчуга
            if present == 'Кольчуга':
                print(f'Жаль. В коробке была {present}')
            #если в коробке было оружие
            elif present == 'Оружие':
                print(f'Жаль. В коробке было {present}')
#если в коробке был дух
            else:
                print(f'Вам повезло! В коробке был {present}')
        time.sleep(5)

#увеличивает количество дней на 1
    day = day + 1
