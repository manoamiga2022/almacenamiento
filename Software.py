mensaje_inicio='mensaje de bienvenida y anuncio de derchos y políticas de\ntratamiento de datos'
mensaje_info_clinica='Esta información que llenará a continuación, corresponde a la información clínica.\n\n¿Cuénta usted con la historia clínica?\n\nResponda:\n1 Sí\2 No'
def mensaje_de_error(n):
    """Esta función genera un mensaje de error y solicita que se ingrese un valor entre 1 y n"""
    print(f'No he comprendido tu inquietud, por favor, intenta digitando sólo un número entre 1 y {n} de acuerdo a las siguentes opciones:')
print(mensaje_inicio)
def ver_num(b,n):
    """Esta función verifica que la respuesta sea siempre un número entero, en caso de no serlo, la función solicita que se corrija y se ingrese un valor entero."""
    a=input(f'{b}') # b es un mensaje que da la instrucción del mensaje que debe ingresar el usuario.
    while not a.isdigit():
        a=input('Por favor, digite el número sin pustos, comas ni espacios. Respuesta: ')
    while not int(a) in range(1,n):# n es el enésimo término de una lista de valores que el usuario debe seleccionar.
        mensaje_de_error(n-1)
        a=ver_num(b,n)
    return int(a)
def historia_clinica():
    hc=ver_num(mensaje_info_clinica,3)
    causa=0
    if hc==1:
        print('Adjunte a este chat la historia clínica.')
        #Aquí se debe crear una función que reciba el archivo y lo almacene.
    else:
        print('\n¿Las razones por las cuales no posee historia clinica es alguna de las siguientes?')
        causas='No la ha solicitado/No sabe qué es ni cómo se solicita/La ha solicitado, pero se la han negado/Otra'.split('/')#Posibles causas de no tener HC
        for i in range(len(causas)):
            print(f'{i+1} {causas[i]}')
        causa=ver_num('\nRespuesta: ',len(causas)+1)
    return causa
def personal_data():
    """Esta función permite recolectar los datos del usuario. Dichos datos son Nombre completo, número de documento, tipo de documento."""
    name=input('Ingrese primer nombre y segundo nombre: ').upper()
    last_name1=input('Ingrese primer apellido: ').upper()
    last_name2=input('Ingrese segundo apellido: ').upper()
    tipo=['Cédula de ciudadanía','Tarjeta de identidad','Registro civil de nacimiento','Pasaporte']
    def documento():
        """Esta función imprime una lista de los datos que debe ingresar el usuario."""
        print('Digite el valor correspondiente al tipo de documento que aparece en la siguiente lista:')
        for i in range(len(tipo)):
            print(f'{i+1} {tipo[i]}')
    documento()
    t=ver_num('Respuesta: ',5)-1
    num=ver_num('Ingrese su número de documento: ',10000000000)
    print(f'Sus datos son los siguientes:\n\nNombre completo: {last_name1} {last_name2} {name}\nTipo de documento: {tipo[t]}\nNúmero de documento: {num}\n\n¿Desea corregir algún dato?\n1 SÍ\n2 NO')
    res=ver_num('Respuesta: ',3)
    while res == 1:
        """Este ciclo permite corregir la información básica del usuario"""
        print('¿qué dato desea corregir?')
        def corrija():
            datos='Primer y segundo nombre,Primer apellido,Segundo Apellido,Tipo de documento,Número de documento,Salir'.split(',')
            for i in range(len(datos)):
                print(f'{i+1} {datos[i]}')
            print('Digite el número de la lista anterior, que corresponda al dato a corregir')
            r=ver_num('Respuesta: ',7)
            return r
        x=corrija()
        if x==1:
            name=input('Ingrese primer nombre y segundo nombre: ').upper()
        elif x==2:
            last_name1=input('Ingrese primer apellido: ').upper()
        elif x==3:
            last_name2=input('Ingrese segundo apellido: ').upper()
        elif x==4:
            documento()
            t=ver_num('Respuesta: ',3)-1
        elif x==5:
            num=ver_num('Ingrese su número de documento: ',10000000000)
        else:
            while not x in range(7):
                mensaje_de_error(6)
                documento()
                x=corregir(ver_num('Respuesta: ',7))
                if x==6:
                    break
            
        print(f'\nSus datos son los siguientes:\n\nNombre completo: {last_name1} {last_name2} {name}\nTipo de documento: {tipo[t]}\nNúmero de documento: {num}\
\n¿Desea corregir algún otro dato?\n1 SÍ\n2 NO')
        res=ver_num('Respuesta: ',3)
    return [last_name1,last_name2,name,tipo[t],num]
    

def aceptar_TyC():
    a=ver_num('¿Acepta usted los términos y condiciones?\nResponda:\n1 para SÍ\n2 para NO\nRespuesta: ',3)
    if a==1:
        return personal_data()
    elif a==2:
        print('Para poder continuar, es necesario que acepte los Términos y Condiciones')
        aceptar_TyC()
    else:
        mensaje_de_error(2)
        aceptar_TyC()
    
sal=aceptar_TyC()
print(sal)
#La prueba ha sido un éxito
#La segunda prueba ha sido un éxito
#La tercera prueba ha sido un éxito


