# [G. Клуб любителей винила](https://contest.yandex.ru/contest/24953/problems/G/)

**Ограничение времени:** 1 секунда \
**Ограничение памяти:** 64Mb \
**Ввод:** input.db \
**Вывод:** стандартный вывод или output.txt

В очередном заседании клуба любителей виниловых пластинок разгорелись нешуточные страсти – Михаил и Владимир поспорили, кто сможет перечислить как можно больше пар исполнитель-альбом, которые были записаны на студиях «Граммофон» или «Скрипичный ключ». При этом по правилам клуба принято считать, что пластинки с рейтингом «4 и ниже» не стоят внимания членов клуба, а упоминать пластинки с рейтингом «10 из 10» считается плохим тоном. \
Полемика Михаила и Владимира грозит расколом клуба.

К счастью, у вас под рукой оказался ноутбук и доступ к базе данных рейтингов.

Даны таблицы со следующим содержимым:
```sql
CREATE TABLE musicians ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name VARCHAR(20) 
); 
CREATE TABLE labels ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name VARCHAR(20) 
); 
CREATE TABLE albums ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name VARCHAR(20), 
  rating INTEGER, 
  musician_id INTEGER, 
  label_id INTEGER 
);
```

Нужно вывести все строки «музыкант» – «лэйбл» – «альбом» – «рейтинг», такие, что лэйбл равен «Граммофон» или «Скрипичный ключ», и альбомы имеют рейтинг от 5 до 9 включительно.

Сделать вывод в порядке возрастания имени музыканта.

На следующей базе данных:
```sql
INSERT INTO musicians VALUES
  (1, "Петя"),
  (2, "Маша")
;
INSERT INTO labels VALUES
  (1, "Граммофон"),
  (2, "Скрипичный ключ")
;
INSERT INTO albums VALUES
  (1, "Дебютный альбом", 8, 1, 1),
  (2, "Этюды", 10, 2, 1),
  (3, "Осень", 6, 2, 2)
;
```

Результат должен быть:
```
┌──────┬─────────────────┬─────────────────┬────────┐
│ name │      name       │      name       │ rating │
├──────┼─────────────────┼─────────────────┼────────┤
│ Маша │ Скрипичный ключ │ Осень           │ 6      │
│ Петя │ Граммофон       │ Дебютный альбом │ 8      │
└──────┴─────────────────┴─────────────────┴────────┘
```

## Формат вывода

В качестве ответа надо вывести запрос на языке SQL.

## Примечания
Пример какого-то корректного запроса на языке SQL, выводящего названия альбомов и их рейтинг в порядке возрастания рейтинга:
```sql
SELECT 
    albums.name, 
    albums.rating 
FROM 
    albums 
ORDER BY 
    albums.rating
```