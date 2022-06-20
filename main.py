nombre = input('¿Cual es tu nombre?')
apellido = input('¿Cuales son tus apellidos?')
edad = (input('¿Cuantos años tienes?'))
email = input('¿Cual es tu email?')
telefono = input('¿Cual es tu telefono?')
casado = input('¿Eres casado? (si/no)')
if casado == 'si':
    casado = True
else: casado = False
hijos = input('¿Tienes hijos? si/no')
if hijos == 'si':
    hijos = True
else: hijos = False
listAmigos = []
numeroDeAmigos = int(input('¿Cuantos amigos cercanos tienes?'))
print('Como se llaman')
for i in range(numeroDeAmigos):
    data = str(input())
    listAmigos.append(data)
numeroDePeliculas = int(input('¿Cuantas peliculas haz visto en los ultimos 6 meses? ?'))
nombreDePeliculas = {}
for i in range (numeroDePeliculas):
    key=numeroDePeliculas
    value=input('¿Como se llaman las pelicula/s')
    nombreDePeliculas[key]=value

    print ('Tu nombre completo es '+ nombre + ' ' + apellido)
    print('Tienes ' + edad + ' años')
    print('Tu correo es ' + email)
    print('Tu numero de telefono es ' + telefono)
    if casado == True:
        print('Estas Casado')
    else: print('No estas casado')

    if hijos == True:
        print('Tienes Hijos')
    else: print('No tienes hijos')

    print(listAmigos)
    print(nombreDePeliculas)
