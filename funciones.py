class calculator: 

    def suma ():
        n1 = int (input("escrime el primer numero "))
        n2 = int (input("escribe el segundo nunmero "))
    
        return n1 + n2

    def resta ():
        n1 = int (input("escrime el primer numero "))
        n2 = int (input("escribe el segundo nunmero "))
    
        return n1 -  n2

    def multiplicacion ():
        n1 = int (input("escrime el primer numero "))
        n2 = int (input("escribe el segundo nunmero "))
    
        return n1 * n2
    
    def division ():
        n1 = int (input("Escribe el primer numero "))
        n2 = int (input("Escribe el segundo numero "))

        return n1 / n2 

    while True:
        print("-------------------")
        print("    calculator     ")
        print("-------------------\n")

        print("1. suma    3. multiplicacion")
        print("2. resta   4. division \n")

        opcion = int(input("Elige una opcion "))

        if opcion == 1:
            print(suma())
            break

        elif opcion == 2 :
            print(resta())
            break
        
        elif opcion == 3 :
            print(multiplicacion())
            break

        elif opcion == 4 : 
            print(division())
            break



