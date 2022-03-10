import gspread
from datetime import date

gs = gspread.service_account(filename='abon.json')  # подключаем файл с ключами и пр.
sh = gs.open_by_key('19LBStaP31DZLTPpLtqqMGXo2mPYUN5roy_68uIUI_3o')  # подключаем таблицу по ID
worksheet = sh.sheet1  # получаем первый лист
#  res = worksheet.get_all_records()
#  res = worksheet.get_all_values()
#  print(res)
#  ['идентификатор абонемента', 'клиента', 'дата создания', 'цена', 'кол-во занятий', 'пройденных занятий',
#  ' дата и время последней тренировки']

# ps = gspread.service_account(filename='название файла')  # подключаем файл с ключами и пр.
# hs = gs.open_by_key('id таблицы клиентов')  # подключаем таблицу по ID
# client_list = hs.sheet1  # получаем первый лист таблицы клиентов

r = worksheet.col_values(1)  # 1 столбец таблицы, в котором записываются id абонемента
abon_id = len(r)

client_list = sh.sheet1  # лист с таблицей клиентов
client_id_list = client_list.col_values(1)  # столбец с id клиентов

if __name__ == '__main__':
    client_id = str(input())
    if client_id in client_id_list:
        today = date.today()
        t = "{}.{}.{}".format(today.day, today.month, today.year)  # текущая дата
        price_abon = str(input('введите цену '))  # цену я получаю
        sum = int(input('введите кол-во занятий '))  # количество занятий я получаю
        passed = 0  # 0 по умолчанию, далее рассчитываются при регистрации тренировки
        past_tren = str(input('введите дату и время последней тренировки '))  # рассчитывается при регистрации тренировки
        newAbon = [abon_id, client_id, t, price_abon, sum, passed, past_tren]  # новые данные
        worksheet.append_row(newAbon)
        print('Абонемент добавлен')
    else:
        print('Клиент не найден')
    #  worksheet.insert_row(newAbon, 2)  # добавляет новые данные во 2 строку

