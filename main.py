from collision import module

def main():
    while True:
        print("1 - Найти площадь пересечений\n2 - Выйти из программы\n")
        c = int(input("Выберите действие(введите число): ")) #запрашивает действие пользователя в переменную
    
        if c == 1:
            try:
                num = int(input("Введите количество прямоугольников: "))
            except:
                print("Некорректный ввод данных")
                num = 2
            rectangles = []
            for i in range(num):
                print(f"Прямоугольник {i + 1}:")
                x1 = float(input('Введите x1: '))
                y1 = float(input('Введите y1: '))
                x2 = float(input('Введите x2: '))
                y2 = float(input('Введите y2: '))
                if module.isCorrectRect([(x1, y1), (x2, y2)]):
                    rectangles.append([(x1, y1), (x2, y2)])
                else:
                    print("Некорректный ввод данных")
                    exit()
            try:
                print("Итоговая уникальная площадь: ",module.intersectionAreaMultiRect(rectangles))
            except module.RectCorrectError as e:
                print(e)
                return 0
                
        elif c == 2:#выход из программы
            exit()
        
        else: #при вводе некорректного значения
            print('Введите корректное значение')


if __name__=="__main__":
    main()