def Harjutus_5(): #Упорядочить зарплаты в порядке возрастания и убывания вместе с именами,
    print("Harjutus 5.")
    palgad = [1200, 2500, 750, 395, 1200]
    inimesed = ["A", "B", "C", "D", "E"]

    kasvavad_palgad = sorted(palgad) #Происходит сортировка списка зарплат и сохраняется в переменной.
    kasvavad_inimesed = [inimesed[palgad.index(p)] for p in kasvavad_palgad] #Происходит сортировка людей по зарплате. Он смотрит список зарплат,
        #и каждый индекс зарплаты он сохраняет. и применяет к именам.
    print("Kasvavad palgad: " + ", ".join(str(p) for p in kasvavad_palgad))
    print("Kasvavad inimesed: " + ", ".join(kasvavad_inimesed))
    #for p in kasvavad_palgad -  Здесь перебираются элементы списка kasvavad_palgad. P - это переменная индекса человека, а значит что его зарплата стоит на том же индексе.
    kahanemine_palgad = sorted(palgad, reverse=True)
    kahanemine_inimesed = [inimesed[palgad.index(p)] for p in kahanemine_palgad]

    print("Kahanevad palgad: " + ", ".join(str(p) for p in kahanemine_palgad)) 
    print("Kahanevad inimesed: " + ", ".join(kahanemine_inimesed))
    # используется для преобразования списка kasvavad_palgad в строку, разделенную запятыми.
# join() объединяет элементы списка в одну строку, используя заданный разделитель (в данном случае запятую и пробел ", ")
def Harjutus_1():
    print("Harjutus 1.")
    palgad = [1200, 2500, 750, 395, 1200]
    inimesed = ["A", "B", "C", "D", "E"]
    n = int(input("Kui palju inimesi soovite lisada? "))
    for i in range(n):
        inimene = input(f"Sisestage isiku nimi {i+1}: ")
        palk = float(input(f"Sisestage töötasu {inimene}: "))
        inimesed.append(inimene)
        palgad.append(palk)
    print(palgad)
    print(inimesed)
