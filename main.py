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


today = date.today()  # дата через тире/дефисы
v = "{}.{}.{}".format(today.day, today.month, today.year)  # дата через точки

newRec = ['506', '203', v, '500 руб.', '2', '0', '']  # новые данные

#  worksheet.insert_row(newRec, 2)  # добавляет новые данные во 2 строку
worksheet.append_row(newRec)
