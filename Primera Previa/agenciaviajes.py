
class Region:
    def __init__(self, nombreRegion, actividades):
        self.NombreRegion = nombreRegion
        self.Actividades = actividades
        

class Recomendacion:
    def __init__(self, nombreRecomendacion, region):
        self.NombreRecomendacion = nombreRecomendacion
        self.Region = region

class GeografiaMontañosa(Recomendacion):
    def recomendar(self):
        print("Le recomendamos visitar ",self.Region," por su región montañosa e ir a los siguientes lugares: ", self.NombreRecomendacion)

class GeografiaSelva(Recomendacion):
    def recomendar(self):
        print("Le recomendamos visitar ",self.Region," por su región selvática e ir a los siguientes lugares: ", self.NombreRecomendacion)

def agregarRegiones(nombreRegion,actividades):
    listaRegiones.append(Region(nombreRegion,actividades))

def agregarRecomendacion(nombreRecomendacion,region,tipo):
    if tipo == "Montañosa":
        listaRecomendaciones.append(GeografiaMontañosa(nombreRecomendacion,region))
    else:
        listaRecomendaciones.append(GeografiaSelva(nombreRecomendacion,region))

def preferenciasUsuario():
    condicional = True
    while condicional == True:
        preferencia = str(input("¿Cual es su clima de preferencia y que tipo de actividades prefiere hacer?: "))
        listaPreferencias.append(preferencia)
        condicional = bool(input("Si ya no desea ingresar actividades presione enter de lo contrario ingrese lo que sea: "))

def compararActividades_Region():
    contador_actividadesEjeCafetero = 0
    contador_actividadesAmazonas = 0
    for s in listaPreferencias:
        for e in listaRegiones:
            for se in e.Actividades:
                if s == se:
                    if e.NombreRegion == "EjeCafetero":
                        contador_actividadesEjeCafetero += 1
                    else:
                        contador_actividadesAmazonas += 1

    print("Debido a sus actividades preferidas, el sistema determina que: ")
    if contador_actividadesEjeCafetero > contador_actividadesAmazonas:
        for t in listaRecomendaciones:
            if t.Region == "EjeCafetero":
                print(t.recomendar())
    elif contador_actividadesAmazonas > contador_actividadesEjeCafetero:
        for t in listaRecomendaciones:
            if t.Region == "Amazonas":
                print(t.recomendar())
    elif contador_actividadesAmazonas == contador_actividadesEjeCafetero:
        print("No se puede determinar una región de su preferencia, se necesita más informacion")

def menu():
    agregarRegiones("EjeCafetero",['ClimaTemplado','PaisajeCafetero','Senderismo','AvistamientoDeAves'])
    agregarRegiones("Amazonas",['ClimaTropical','NavegacionPorRio','Senderismo','AvistamientoDeAves'])
    agregarRecomendacion("Valle del Cocora (Salento), Nevado del Ruiz y avistamiento de aves en Pereira y Dosquebradas ","EjeCafetero","GeografíaMontañosa")
    agregarRecomendacion("Selva amazonica, recorrido en lancha por el Rio Amazonas y avistamiento de aves en la selva","Amazonas","GeografíaSelvática")
    preferenciasUsuario()
    print("Sus preferencias son: ",listaPreferencias)
    compararActividades_Region()

if __name__ == "__main__":
    listaRegiones = []
    listaRecomendaciones = []
    listaPreferencias = []
    menu()