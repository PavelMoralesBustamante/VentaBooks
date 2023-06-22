import funciones as fu

while True:
    fu.limpiarpantalla()
    fu.printv("SISTEMA VENTABOOKS")
    fu.printv("******************")
    print("1) Guardar Libros")
    print("2) Buscar Libros")
    print("3) Certificados de Libros")
    print("0) Salir")
    opcion = int(input("Seleccione : "))

    #validamos la opción
    if opcion==0:
        fu.printv("Adios :D")
        break
    elif opcion==1:
        fu.printv("Guardar Libro")
    elif opcion==2:
        fu.printv("Buscar Libro")
    elif opcion==3:
        fu.printv("Certificados")
        print("1) Críticas de libro")
        print("2) Detalles de ventas")
        cert = int(input("Seleccione : "))

        if cert==1:
            fu.printv("Certificado Críticas")
        elif cert==2:
            fu.printv("Certificado Detalle de ventas")
        else:
            fu.printr("Certificado no valido")
    else:
        fu.printr("Opción no valida")

