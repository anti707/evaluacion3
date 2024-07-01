import os
os.system("")

vehiculos = []
marca = ["jack, suzuki, toyota"]


menu = """
1.ingresar vehiculo
2.listar vehiculo
3.imprimir orden de resgristro
4.salir
"""

def invehiculos():
            mar = input("ingrese marca del vehiculo (jack/suzuki/toyota): ")
            año = input("ingrese año del vehiculo: ")
            kil = input("ingrese su kilometraje:")
            cos = int(input("costo de reparacion estimado: "))
            if len(año)>0 and mar in kil and cos>0:
                imp = round(cos*0,8)
                total = int(input(cos+imp))
                vehiculos.append([mar, año, kil, cos, imp, total])
            
def listar():
        texto = """
    ----------------------------------------------------------------------------
    |           |         |               |              |            |          |
    |   marca   |   año   |  kilometraje  |  costo r.    |  impuesto  |  total   |
    |           |         |               |              |            |          |
    ----------------------------------------------------------------------------

    """ 
        
        for i in range(len(vehiculos)):
            texto += f"{vehiculos[i][0]:13s}"
            texto += f"{vehiculos[i][1]:10s}"
            texto += f"{vehiculos[i][2]:16s}"
            texto += f"{vehiculos[i][3]:15s}"
            texto += f"{vehiculos[i][4]:14s}"
            texto += f"{vehiculos[i][5]:13s}"
            texto += f"{vehiculos[i][6]:11s}"

        for i in range(len(vehiculos)):
            if vehiculos == [i][0]:
                texto += f"{vehiculos[i][0]:13s}"
                texto += f"{vehiculos[i][1]:10s}"
                texto += f"{vehiculos[i][2]:16s}"
                texto += f"{vehiculos[i][3]:15s}"
                texto += f"{vehiculos[i][5]:13s}"
                texto += f"{vehiculos[i][6]:11s}"
        return texto

def imprimir():
        try:
                opc = int(input("""
                1.todas las marcas
                2. solo (jack/suzuki/toyota)         

                """))
                if opc == 1:
                    reporte=listar(0)
                    with open ("lista.txt","w") as archivo:
                        archivo.write(reporte)
        except:
            input("error")

def salir():
        input("usted ha salido.")

while True:
        opc = int(input(menu))
        if opc == 1:
            invehiculos()
        elif opc == 2:
            print(listar())
        elif opc == 3:
            imprimir()
        elif opc ==4:
             salir()
