from ecuaciones.ecdiff import ec1, ec2, ec3, ec4
seleccion = input("Seleccione la ecuación a resolver: ")
def lanzar():
    if seleccion == "1":
        ec1()
    elif seleccion == "2":
        ec2()
    elif seleccion == "3":
        ec3()
    elif seleccion == "4":
        ec4()
    else:
        print("Opción no válida")
