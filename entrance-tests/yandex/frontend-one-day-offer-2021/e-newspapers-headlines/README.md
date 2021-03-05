# [E. Заголовки газет [100 баллов]](https://contest.yandex.ru/contest/24470/problems/E/)

**Ограничение времени:** 5 секунд \
**Ограничение памяти:** 512Mb \
**Ввод:** input.json \
**Вывод:** output.json

Петя работает старшим верстальщиком в газете «Московский фронтендер». Для вёрстки газеты Петя использует стек веб-технологий. Самая сложная задача, с которой столкнулся Петя — это вёрстка заголовков в газетных статьях: колонки в газете в каждом выпуске имеют разную ширину, а заголовки — разный шрифт и разное количество символов.

Пете нужно подбирать свой размер шрифта для каждого заголовка так, чтобы размер шрифта был максимальным, но при этом весь текст заголовка влез в отведённое ему место.

Помогите Пете: реализуйте функцию `calcFontSize`, которая позволяет вписать переданный текст в контейнер таким образом, чтобы он влезал в контейнер целиком и имел максимально возможный шрифт, при этом если оптимальнее разместить текст в несколько строк, то так и нужно сделать. Если же это не удаётся сделать, то решение должно возвращать null. Максимальная длина строки на вход - 100 символов. Входная строка не может быть пустой. Ваше решение должно содержать код функции целиком и не использовать внешних зависимостей, чтобы Петя мог скопировать её в своей проект и вызывать в своём коде.

Мы будем проверять, насколько оптимально работает ваше решение, и штрафовать его, если оно производит слишком большое количество манипуляций с DOM.

## Заготовка функции

Ваше решение должно содержать функцию, соответствующую следующей сигнатуре:
```javascript
/***  
 * @param container {Node} ссылка на DOM-node, в которую нужно вписать строку ‘str‘  
 * @param str {string} строка, которую необходимо вписать. Максимальная длина равняется 100 символам  
 * @param min {number} минимальный размер шрифта (целое число, min >= 1)  
 * @param max {number} максимальный размер шрифта (целое число, max >= min >= 1)  
 * @return {number | null} искомый размер шрифта (целое число) или null, если текст вписать нельзя  
 */  
function calcFontSize(container, str, min, max) {  
  // ваш код  
}
```

## Примеры

Для такого контейнера:
```html
<div id="container" style="width: 300px; height: 50px"></div>
```
и таких входных параметров
```javascript
calcFontSize(
    document.getElementById("container"),
    "Топ-10 jQuery-плагинов недели",
    10,
    100,
)
```
функция должна вернуть `22` _(на вашем компьютере это число может быть другим из-за различий в отрисовке шрифтов)_.

![](./statement-image.jpeg)

## Примечания

Ваше решение будет тестироваться в браузере Google Chrome 69.
Если ваше решение проходит не все тесты (получает вердикт WA), то оно может
- возвращать неправильный ответ в каких-то случаях
- выполнять слишком много манипуляций с DOM