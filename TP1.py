def word_count():
    count = str(input("écrit quelque chose\n"))
    count = count.split(" ")
    nombre_mot = len(count)
    print(nombre_mot)
word_count()