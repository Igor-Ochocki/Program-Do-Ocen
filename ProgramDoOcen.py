default_key = {
    "5":[99.00, 100.0],
    "5-":[97.0, 98.99],
    "4+":[91, 96.99],
    "4":[85, 90.99],
    "4-":[80, 84.99],
    "3+":[75, 79.99],
    "3":[69, 74.99],
    "3-":[63, 68.99],
    "2+":[58, 62.99],
    "2":[53, 57.99],
    "2-":[50, 52.99],
    "1+":[48, 49.99],
    "1":[0, 47.99]
}

def beetween(a, b, value):
    return value >= a and value <= b

students = []

def programRunning():

    max_score = int(input("Wprowadź maksymalną liczbę punktów : "))

    while max_score < 22:
        max_score = int(input("Wprowadzona liczba punktów jest zbyt mała. Minimalna ilość 22 punkty. Wprowadź poprawne dane : "))

    key = {
        "5":[default_key["5"][0]*max_score/100, default_key["5"][1]*max_score/100],
        "5-":[default_key["5-"][0]*max_score/100, default_key["5-"][1]*max_score/100],
        "4+":[default_key["4+"][0]*max_score/100, default_key["4+"][1]*max_score/100],
        "4":[default_key["4"][0]*max_score/100, default_key["4"][1]*max_score/100],
        "4-":[default_key["4-"][0]*max_score/100, default_key["4-"][1]*max_score/100],
        "3+":[default_key["3+"][0]*max_score/100, default_key["3+"][1]*max_score/100],
        "3":[default_key["3"][0]*max_score/100, default_key["3"][1]*max_score/100],
        "3-":[default_key["3-"][0]*max_score/100, default_key["3-"][1]*max_score/100],
        "2+":[default_key["2+"][0]*max_score/100, default_key["2+"][1]*max_score/100],
        "2":[default_key["2"][0]*max_score/100, default_key["2"][1]*max_score/100],
        "2-":[default_key["2-"][0]*max_score/100, default_key["2-"][1]*max_score/100],
        "1+":[default_key["1+"][0]*max_score/100, default_key["1+"][1]*max_score/100],
        "1":[0, default_key["1"][1]*max_score/100],
    }
    maxPoints(key, students, 1, max_score)

def maxPoints(key, students, num, max_score): 

    command = int(input("Wybierz operację : \n1. Wyświetlenie ocen według klucza \n2. Wpisanie ilości punktów i wyświetlenie oceny według klucza\n"))  
    
    if command == 1:
            print("Klucz ocen w schemacie : \nOcena : Minimalna ilość punktów - Maksymalna ilość punktów : ")
            for grade, points in key.items():
                if points[0] % 0.5 != 0:
                    points = [int(round(points[0])), points[1]]
                if points[1] % 0.5 != 0:
                    points = [points[0], round(points[1])]
                print("{} : {} - {}".format(grade, points[0] , points[1]))
            submit = input("Czy chcesz zapisać wyniki do pliku txt?\nTak // Nie\n").lower()
            if submit == "tak":
                file = open("Klucz ocen.txt", "w+")
                file.write("Klucz ocen w schemacie : \nOcena : Minimalna ilość punktów - Maksymalna ilość punktów : \n")
                for grade, points in key.items():
                    if points[0] % 0.5 != 0:
                        points = [int(round(points[0])), points[1]]
                    if points[1] % 0.5 != 0:
                        points = [points[0], round(points[1])]
                    file.write("{} : {} - {}\n".format(grade, points[0] , points[1]))
                file.close()
            operation = int(input("Co chcesz zrobić dalej? (w przypadku podania nieprawidłowej komendy, program zostanie zamknięty)\n1. Uruchomić program od nowa\n2. Ponownie wybrać opcję z obecną maksymalną punktacją\n3. Zamknąć program."))
            if operation == 1: 
                programRunning()
            elif operation == 2:
                maxPoints(key, students, num, max_score)
            elif operation == 3:
                pass
            

    if command == 2:
            obtained_points = int(input("W wypadku podania punktacji więcej niż jednego ucznia, będzie możliwość zapisania wyników do pliku txt\nPodaj ilość punktów otrzymaną przez ucznia : "))
            if beetween(0, max_score, obtained_points):
                obtained_grade = 0
                for grade, points in key.items():
                        if beetween(points[0], points[1], obtained_points):
                            print("Uczeń powinien otrzymać {}.".format(grade))
                            obtained_grade = grade
                students.append([obtained_grade, num])
                num += 1
                if len(students) > 1:
                    if input("Czy chcesz zapisać oceny obecnie wpisanych uczniów?\nTak//Nie\n").lower() == "tak":
                        file = open("Oceny uczniów.txt", "w+")
                        file.write("Oceny obecnie wpisanych uczniów : \n")
                        for student, numb in students:
                            file.write("Uczeń numer {} powinien otrzymać {}.\n".format(numb, student))
                        file.close()
            else:
                print("Podałeś nieprawidłową liczbę punktów.")
            operation = int(input("Co chcesz zrobić dalej? (w przypadku podania nieprawidłowej komendy, program zostanie zamknięty)\n1. Uruchomić program od nowa\n2. Ponownie wybrać opcję z obecną maksymalną punktacją\n3. Zamknąć program.\n"))
            if operation == 1: 
                programRunning()
            elif operation == 2:
                maxPoints(key, students, num, max_score)
                    

programRunning()