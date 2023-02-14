import random
import argparse

SKILLS = ['Оружие языка пламени', 'Быстродействующий яд', 'Воскрешение союзника', 'Старый портал в Даларан',
          'Первозданная волна', 'Молот правосудия', 'Приручение лесного зверька', 'Духовное путешествие', 'Охотник',
          'Взмах', 'Призыв большого кодо Служителя Солнца', 'Прерывание', 'Вспышка Света', 'Обнаружение ловушек',
          'Поступь смерти', 'Призыв охотника Скверны', 'Героический бросок', 'Мясорубка', 'Прославление',
          "Портал в Дазар'алор", 'Нокаутирующий удар', 'Камень души', 'Притвориться мертвым', 'Руна истерии',
          'Облик птицы', 'Портал в Каменор', 'Пробудитель', 'Монах', 'Телепортация: Лунная поляна', 'Призрачное зрение',
          'Закаленная чешуя', 'Облик Бездны', 'Портал в Терамор', 'Кровавая чума', 'Сверкающая нефритовая молния',
          'Осколки души', 'Слово Тьмы: Боль', 'Алый фиал', 'Подрезать крылья', 'Оживить', 'Телепортация: Орибос',
          'Казнь', 'Чародейский интеллект', 'Слово силы: Стойкость', 'Коварный удар', 'Призыв кодо Служителя Солнца',
          'Выслеживание великанов', 'Критические удары', 'Врата смерти', 'Хождение по воде', 'Шакрамы',
          'Телепортация: Экзодар', 'Телепортация: Вальдраккен', 'Оживление', 'Размах', 'Дубовая кожа', 'Щит молний',
          'Шакрам смерти', 'Удар по почкам', 'Глубокие раны', 'Увечье', 'Телепортация: Даларан (Расколотые острова)',
          'Портал в Боралус', 'Будоражащий жар', 'Облик ездового животного', 'Блок щитом', 'Исчезновение',
          'Ледяное дыхание', 'Телепортация: Терамор', 'Лик смерти', 'Призыв сайаада', 'Пронизывающая стужа',
          'Двойной прыжок', 'Дезинтеграция', 'Гнойная язва', 'Бесконечное дыхание', 'Таинственное прикосновение',
          'Крадущийся зверь', 'Призывает аргусского скитальца озаренных', 'Призрачный волк', 'Пинок', 'Антимагия',
          'Стрела Тьмы', 'Астральное возвращение', 'Рывок Скверны', 'Молитва отчаяния', 'Выслеживание нежити',
          'Превращение', 'Паладин', 'Телепортация: Оплот Хранителя', 'Портал в Копье Войны',
          'Телепортация: Копье Войны', 'Внутреннее зрение', 'Тотем ветряного порыва', 'Сила дикой природы', 'Гнев',
          'Создание источника душ', 'Маг', 'Беглый огонь', 'Выслеживание механических существ', 'Жажда крови',
          'Возрождение', 'Рывок', 'Божественный скакун', 'Устранение вреда', 'Облик лунокрылой совы верховного друида',
          'Кормление питомца', 'Планирование', 'Искупление', 'Жрец', 'Метаморфоза', 'Телепортация: Вечноцветущий дол',
          'Верный выстрел', 'Призыв элекка экзарха', 'Облик кошки', 'Телепортация: Тол Барад', 'Правосудие',
          'Волшебное переливание', 'Солнечный огонь', 'Обшаривание карманов', 'Реинкарнация', 'Губительное касание',
          'Походный облик', 'Ложная смерть', 'Живой жар', 'Бреющий полет', 'Кувырок', 'Воин', 'Портал в Подгород',
          'Провокация', 'Спринт', 'Левитация', 'Заступничество', 'Огненное дыхание', 'Руна каменной горгульи',
          'Портал в Луносвет', 'Дух хамелеона', 'Портал в Громовой Утес', 'Создание камня здоровья',
          'Телепортация: Даларан (старая)', 'Страх', 'Телепортация', 'Портал в Даларан (Нордскол)',
          'Руна режущего льда', 'Конус холода', 'Замедленное падение', 'Портал в Оргриммар',
          'Телепортация: Преграда Ветров', 'Взбучка', 'Хватка смерти', 'Руна вечной жажды', 'Дух черепахи',
          'Искажение времени', 'Лунный огонь', 'Потрошение', 'Полоснуть', 'Кошачья грация', 'Портал на Тол Барад',
          'Разбойник', 'Ментальный крик', 'Око Килрогга', 'Успокоение разума', 'Выслеживание драконов', 'Иллюзия',
          'Бой с оружием в каждой руке', 'Портал в Преграду Ветров', 'Скачок', 'Духовное путешествие: возвращение',
          'Стихийный удар', 'Телепортация: Дарнас', 'Ритуал призыва', 'Молния', 'Труповзрыватель', 'Канал здоровья',
          'Твердая решимость', 'Портал в Штормград', 'Порабощение демона', 'Атака', 'Телепортация в Каменор',
          'Чернокнижник', 'Портал в Стальгорн', 'Глубокий вдох', 'Телепортация: Штормград', 'Круговой удар ногой',
          'Ясность мысли', 'Поглощение души', 'Замораживающая ловушка', 'Разрубатель душ', "Телепортация: Дазар'алор",
          'Метка охотника', 'Рык', 'Облик медведя', 'Средоточие воли', 'Ярость Аспектов', 'Отрыв',
          'Выслеживание элементалей', 'Призыв барана Рассветной кузни', 'Подпитка для пламени', 'Полет дзен',
          'Портал: Вальдраккен', 'Бросок боевого клинка', 'Выслеживание животных', 'Уход в тень', 'Руна полнокровия',
          'Отвлечение', 'Управление питомцем', 'Дух гепарда', 'Гнев деревьев', 'Аура рыцаря', 'Телепортация: Луносвет',
          'Лазурный удар', 'Победный раж', 'Удар воина Света', 'Озноб', 'Огненный шок', 'Скороход', 'Уловка',
          'Изумрудный цветок', 'Телепортация: Подгород', 'Осветительная ракета', 'Взлом замка',
          'Призыв элекка великого экзарха', 'Телепортация: Шаттрат', 'Знание зверя', 'Телепортация: Боралус',
          'Исцеляющий всплеск', 'Восстановление', 'Выслеживание демонов', 'Ячейка быстрого доступа 01',
          'Призыв скакуна', 'Мощный удар щитом', 'Быстрое исцеление', 'Живость', 'Созерцание', 'Чародейский выстрел',
          'Знак дикой природы', 'Чародей-полиглот', 'Телепортация: Громовой Утес', 'Перерождение', 'Призыв беса',
          'Кольцо льда', 'Вихрь', 'Приручение животного', 'Танцующий журавль', 'Поиск нежити', 'На коне бледном',
          'Дальнее зрение', 'Подлый трюк', 'Выслеживание скрытых', 'Призыв барана Темной кузни', 'Ярость орла',
          'Дикорог рыцаря', 'Рыцарь смерти', 'Героизм', 'Скрывающий покров', 'Смертельное касание', 'Кара',
          'Портал: Орибос', 'Стенающая стрела', 'Дар бронзовых драконов', 'Руна апокалипсиса', 'Парирование',
          'Телепортация: Оргриммар', 'Портал в Экзодар', 'Лапа тигра', 'Укус демона', 'Звериный гнев', 'Освящение',
          'Друид', 'Гнев карателя', 'Смерть и разложение', 'Матрица импринтинга меха-привязки', 'Пожирание',
          'Фейерверк', 'Портал в Шаттрат', 'Воскрешение питомца', 'Команда питомцу', 'Порча', 'Сотворение яств',
          'Водный облик', 'Внезапный удар', 'Аура благочестия', 'Призыв демона Бездны', 'Щит праведника', 'Мощный удар',
          'Конь Скверны', 'Телепортация: Стальгорн', 'Зуботычина', "Валь'кира", 'Жертвенное благословение',
          'Телепортация: Даларан (Нордскол)', 'Лечение питомца', 'Ритуал рока', 'Обжигающий жар', 'Шаман',
          'Стрелы ветра', 'Портал', 'Боевой крик', 'Блок', 'Огненный взрыв', 'Нейтрализующий яд', 'Удар Хаоса',
          'Льдистый путь', 'Призыв боевого коня', 'Рунический удар', 'Взрыв разума', 'Дух предков', 'Молот гнева',
          "Призыв кель'таласского боевого коня", 'Свирепый укус', 'Капкан', 'Длань расплаты',
          "Призыв кель'таласского скакуна", 'Калечащий яд', 'Слово силы: Щит', 'Портал в Вечноцветущий дол',
          'Печать хаоса', 'Избавление Тира', 'Ледяная стрела', 'Похищение жизни', 'Отпустить питомца',
          'Руна павшего рыцаря', 'Безопасное падение', 'Сноходец', 'Скакун погибели', 'Аура воздаяния', 'Сбор добычи',
          'Очищение', 'Мучение', 'Гравирование', 'Порыв', 'Руна защиты от магии', 'Темная власть', 'Чародейский взрыв',
          'Управление демоном', 'Вызов', 'Подрезать сухожилия', 'Воскрешение', 'Выслеживание гуманоидов',
          'Божественный щит', 'Родство с гибридами', 'Древняя мудрость зандаларов', 'Обнаружение', 'Глаза зверя',
          'Успокаивающий туман', 'Возвращение', 'Элементаль огня', 'Пробуждение', 'Тотем оков земли', 'Незаметность',
          'Сглаз', 'Безграничное убеждение', 'Проклятие слабости', 'Стрела Бездны', 'Орлиный глаз', 'Торжество',
          'Портал в Дарнас']


def read_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', help="Counter of jokes that gonna be generated", default=1)
    return parser.parse_args()


def generate_joke(setup: list, idx: int) -> str:
    joke: str = f"[{setup[idx].title()}]"
    joke += b' \xd0\x90\xd0\xbd\xd1\x83\xd1\x81\xd0\xb0'.decode()
    return joke


def main():
    try:
        args = read_args()
        joke_counter = int(args.count)
        if joke_counter < 0 or joke_counter > len(SKILLS):
            print(f'-c/--counter argument must be integer value in [0:{len(SKILLS)}]')
            return
        jokes = [generate_joke(SKILLS, idx) for idx in random.sample(range(len(SKILLS)), joke_counter)]
        for joke in jokes:
            print(joke)
    except ValueError:
        print("-c/--count argument must be integer!")


if __name__ == '__main__':
    main()
