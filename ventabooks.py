import funciones as fu

while True:
    fu.limpiarpantalla()
    fu.printv("SISTEMA VENTABOOKS")
    fu.printv("******************")
    print("1) Guardar")
    print("2) Buscar")
    print("3) Certificados")
    print("0) Salir")
    opcion = int(input("Seleccione : "))

    #validamos la opción
    if opcion==0:
        fu.printv("Adios :D")
        break
    elif opcion==1:
        fu.printv("Guardar")
    elif opcion==2:
        fu.printv("Buscar")
    elif opcion==3:
        fu.printv("Certificados")
        print("1) Críticas")
        print("2) Detalles")
        cert = int(input("Seleccione : "))

        if cert==1:
            fu.printv("Certificado Críticas")
        elif cert==2:
            fu.printv("Certificado Detalle de ventas")
        else:
            fu.printr("Certificado no valido")
    else:
        fu.printr("Opción no valida")

