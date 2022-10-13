from ecuaciones.ecdiff import EDO

seleccion = input("Seleccione la ecuación a resolver: ")
def lanzar():
    if seleccion == "1":
        EDO.ec1()
    elif seleccion == "2":
        EDO.ec2()
    elif seleccion == "3":
        EDO.ec3()
    elif seleccion == "4":
        EDO.ec4()
    else:
        print("Opción no válida")
