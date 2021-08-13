#  Este codigo calcula e imprime**
# la razon aurea**
#********************************************
#  Parametros de entredad:**
#  N = el numero de veces que se va repetir el codigo**
#  para que la razon aurea sea mas exacta**
#********************************************
#  Autor: Juan Felipe Corrales Toro **
#  ULTIMA ACTUALIZACION: 12 de agosto/2021 **

N=int(input("ingrese el N ENTRE MAS GRANDE MAS EXACTO! "))#ESTE INPUT LO PUSE PARA PEDIR EL N 
RAZONAUREA=1.61803398874989
PRIMERO=0#DAMOS VALOR AL PRIMERO 
SEGUNDO=1#DAMOS VALOR AL SEGUNDO
SUMA=0#INICIALIZAMOS LA SUMA 
CONTEO=1#INICIAMOS EL CONTEO
while(CONTEO<=N):# MIENTRAS SE CUMPLA ESTA CONDICION SE EJECUTARA EL CODIGO    
  CONTEO=CONTEO+1#SUMAMOS 1 MAS AL CONTEO COMO UNA BANDERILLA 
  PRIMERO=SEGUNDO#IGUALDAD PARA PODER INICIAR DE NUEVO
  SEGUNDO=SUMA
  SUMA=PRIMERO+SEGUNDO

E=SUMA/SEGUNDO#REALIZAMOS LA OPERACION DEL NUMERO AUREO
RAZ=RAZONAUREA-E
print("La diferencia con la proporcion aurea es de  ",RAZ)
print(E)#LO IMPRIMOS PARA VERLO 
