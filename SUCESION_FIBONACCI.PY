#  Este codigo calcula e imprime**
# los N numeros de la sucesion de fibonacci**
#********************************************
#  Parametros de entredad:**
#  N = cantidad de N numeros de la sucesion a imprimir**
#********************************************
#  Autor: Juan Felipe Corrales Toro **
#  ULTIMA ACTUALIZACION: 12 de agosto/2021 **



N=int(input("ingrese el N "))#ESTE INPUT LO PUSE PARA PEDIR EL N NUMEROS DE LA SUCESSION
PRIMERO=0#DAMOS VALOR AL PRIMERO 
SEGUNDO=1#DAMOS VALOR AL SEGUNDO
SUMA=0#INICIALIZAMOS LA SUMA 
CONTEO=1#INICIAMOS EL CONTEO
while(CONTEO<=N):# MIENTRAS SE CUMPLA ESTA CONDICION SE EJECUTARA EL CODIGO    
  print(SUMA)#IMPRIMIMOS CADA RESULTADO SUMA
  CONTEO=CONTEO+1#SUMAMOS 1 MAS AL CONTEO COMO UNA BANDERILLA 
  PRIMERO=SEGUNDO#IGUALDAD PARA PODER INICIAR DE NUEVO
  SEGUNDO=SUMA
  SUMA=PRIMERO+SEGUNDO


    


