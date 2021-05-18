# YANDEX EDUCATION | LIBRARY (for robot)
Эта "библиотека" создана для упрощения выполнения заданий (только с "РОБОТОМ").

## Как пользоваться?
1. Просто откройте файл **main.py** или перейдите по ссылки на него в *ROW* режиме
2. Скопируете всё содержимое
3. Вставте в *Yandex Учебник*
4. Пользуйтесь всеми функциями на здоровье!

## Какие есть функции????
#### safe_move(move, check, amount\_cells=100)
Эта функция просто будет двигать робота в зависимости от `move`,
и не остановится пока `check` не вернет `False` или пока робот уже не пройдет `amount_cells`.

Пример:
```python
# Робот будет либо будет идти до левой стены, либо будет идти 5 клеток
safe_move(move_left, free_from_left, 5)
```

#### safe\_move\_and\_fill\_cells(move, check, amount\_cells=100, fill_first=True)
То же самое, что и `safe_move`, только будет красить каждое поле на своём шагу,
По умолчанию красит первую клетку, но если указать `fill_first=False`, тогда первая клетка
будет чиста!

Пример:

```python
# Робот всё раскрасит от текущей клетки до левой стены
safe_move_and_fill_cells(move_left, free_from_left)

# Робот всё раскрасит от текущей клетки до левой стены (кроме 1-ой клетки)
safe_move_and_fill_cells(move_left, free_from_left, fill_first=False)
```

#### safe\_move\_and\_fill\_cell\_if\_should(move, check, is\_should\_fill, amount\_cells=100, check\_last)

Похоже на `safe_move_and_fill_cells`, только Робот будет красить только те клетки, которые требуют условию `is_should_fill`.

Пример:
```python
# Этот код будет красить все клетки которые имеют стену и сверху, и снизу, начиная с нашей клетки, кончая правой стеной

safe_move_and_fill_cell_if_should(
    move_right,
    free_from_right,
    lambda: wall_from_right() and wall_from_down()
)
```

### move_while(move, check)
Двигаться в зависимости от `move` пока `check` - Правда

Пример:
```
# Этот код остановится на той клетке справ от нас, которая не имеет стен ни снизу, ни сверху.
move_while(
    move_right,
    lambda: free_from_up() and free_from_down()
)
```
