class figure: #1сначала научимся сосздавать доску заданного размера и создавать на ней фигуры (пока только пешки)
    def __init__(self, col, pos):
        self.color = col
        self.pos = pos
    def pond_move(self): #3по сути это альфа того как мы будем ходить - пока это просто изменение координаты X на 1
        self.pos[0] += (1 if self.color == 'white' else -1) #4 движение есть, но как оно вызывается? нужен поиск - если я всегда знаю позиции фигур, то буду выбирать элемент по координатам и двигать его

class board: 
    def __init__(self, width = 8, height = 8):
        self.width = width
        self.height = height
    whites = []
    blacks = []
    def add(self, pos, color): 
        if color == 'white':
            self.whites.append(figure(color, pos))
        else: 
            self.blacks.append(figure(color, pos))
    def outboard(self):
        for element in self.whites: 
            print('цвет - {}, позиция - {}'.format(element.color, element.pos))
        for element in self.blacks: 
            print('цвет - {}, позиция - {}'.format(element.color, element.pos))
        print('Это всё на доске {} на {}'.format(self.width, self.height)) #2 теперь я могу поставить фигуры и они все хранятся в переменной доски. Дальше учу фигуру ходить
    def move(self, pos, colour): #5 получаю позицию и в белых и черных до упора ищу такую же. совпало - двигаю по методу фигуры.
        for element in self.whites if colour == 'white' else self.blacks: 
            if element.pos == pos: element.pond_move() 



a = board()
a.add([1,1], 'white')
a.add([3, 4], 'white')
a.move([3,4], 'white')
a.add([5,5], 'black')
a.move([5,5], 'black')
a.outboard()

