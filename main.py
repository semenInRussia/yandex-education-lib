# Cool library for YANDEX EDUCATION
# Author: semenInRussia 
# 2021 (c)
# Hello, Smirnov, Yarik, Parizyan, Sasha!!!!

def safe_move(move, check, amount_cells=100):
    """Safe move, if check() is False stop.
    
    :param Callable move executed when should move
    :param Callable check check - is should move?
    :param int amount_cells minimum moved cells 
    """
    for i in range(amount_cells):
        if check():
            move()
        else:
            break

            
def safe_move_and_fill_cells(
    move, check, amount_cells=100,
    fill_first=True
):
    """
    Like on safe_move, but when move, fill_cell, 
    If fill_first is False, don't fill first cell.
    """

    if fill_first:
        fill_cell()
    
    def move_and_fill_cell():
        move()
        fill_cell()
    
    safe_move(move_and_fill_cell, check, amount_cells)

    
def safe_move_and_fill_cell_if_should(
    move, check, is_should_fill,
    amount_cells=100, fill_last=True
):
    """
    Like on safe_move_and_fill_cells, but this function fill cell,
    Only when is_should_fill() is True.
    """
    def move_and_fill_cell_if_should():
        if is_should_fill():
            fill_cell()
        move()
    
    safe_move(
        move_and_fill_cell_if_should, check, amount_cells
    )
    
    if check_last and is_should_fill():
        fill_cell()
        
    
def move_while(move, check):
    """
    Move while check() is True.
    """
    while check():
        move()
