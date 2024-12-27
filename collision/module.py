from itertools import combinations

class RectCorrectError(Exception): #исключение(ошибка) при неправильном вводе координат
    def __init__(self, num):
        super().__init__(f"{num}й прямоугольник некоректный")

def isCorrectRect(rectangle): #функция проверяет, может ли быть такой прямоугольник
    if(rectangle[0][0] < rectangle[1][0] and rectangle[0][1] < rectangle[1][1]):
        return True
    else:
        return False
    
def intersectionAreaRect(fir_rect, sec_rect):
    if isCorrectRect(fir_rect) and isCorrectRect(sec_rect): #если ввод корректный
        if min(sec_rect[0][0], sec_rect[1][0]) < max(fir_rect[0][0], fir_rect[1][0]) and min(fir_rect[0][1], fir_rect[1][1]) < max(fir_rect[0][1], fir_rect[1][1]):
            return (min(fir_rect[1][0], sec_rect[1][0]) - max(fir_rect[0][0], sec_rect[0][0])) * (min(fir_rect[1][1], sec_rect[1][1]) - max(fir_rect[0][1], sec_rect[0][1])) #если пересекаются находит площадь
        else:
            return 0 #если не пересекаются площадь = 0
    elif(not isCorrectRect(fir_rect)): #если 1 прямоугольник некорректный - ошибка
        raise RectCorrectError(1)
    elif (not isCorrectRect(sec_rect)): #если 2 прямоугольник некорректный- ошибка
        raise RectCorrectError(2)

def intersectionAreaMultiRect(rectangles):

    def get_intersection(rects):
        x1 = max(rect[0][0] for rect in rects)
        y1 = max(rect[0][1] for rect in rects)
        x2 = min(rect[1][0] for rect in rects)
        y2 = min(rect[1][1] for rect in rects)
        if x1 < x2 and y1 < y2:
            return [(x1, y1), (x2, y2)]
        return None
    
    total_area = 0 # уникальная площадь
    all_intersections = [] # массив всех пересечений

    
    for combination in combinations(rectangles, 2):# суммарная площадь всех пересечений двух фигур
            intersection = get_intersection(combination)
            if intersection:
                all_intersections.append(intersection)
    
    for k in range(1, len(all_intersections) + 1):# итоговая площадь пересечений двух и более фигур
        sign = (-1) ** (k + 1)  # Чередование знаков
        for combination in combinations(all_intersections, k):
            intersection = get_intersection(combination)
            total_area += sign * intersectionAreaRect(intersection)
    return total_area