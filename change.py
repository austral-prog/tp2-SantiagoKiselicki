def change ():
     expense = 23.75
     money = 100
     vuelto = money - expense
     pesos = int(vuelto)
     centavos = vuelto - pesos
     resultado_centavo = int(centavos*100)
     print (f"Ingresar gasto:")
     print (expense)
     print (f"Dinero recibido")
     print (money)
     print ("")
     print ("Vuelto")
     print ("")
     print (f"Pesos:")
     print (pesos)
     print (f"Centavos:")
     print (resultado_centavo)

change()
