# -*- coding: utf-8 -*-


import sys, urllib as ul
import urllib2
import urlparse

"""Este script en python obtiene las fotos de la orla de todas las personas contenidas en el array personas """
ipersonas = [   "Hernández Cordero Alejandro",
                "Quiñones Grande Rocio",
                "Zamora Contreras Cristina",
                "Navarro Bosgos Juan",
                "González González María",
                "Aguado Jiménez Mariluz",
                "Barriga Villavicencio Darío",
                "García López Adrián",
                "Mayoral Vilches Víctor",
                "Barrena Romero Aurora",
                "Pérez López Javier",
                "Naranjo Martínez Manuel",
                "Lorenzo Servan Juanmanuel",
                "Fuillerat García Franciscojosé",
                "Alonso Sanchez Laura",
                "Valenzuela Velasco Sergio",
                "Arias Conde Estefanía",
                "Angulo Hernández Mªjosé",
                "Martín Barroso María",
                "Ruiz Tejero Ángelamaría",
                "Gálvez Sosa Maríapiedraescrita",
                "Garcia Jimenez Jaime",
                "García Nebreda Mónica",
                "Delafuente Barrio Christian",
                "Barragán Garnacho Aitor",
                "Fernández Pablo",
                "Horcajo Jerez Cintia",
                "Calvo Gago Rodrigo",
                "Villena Guerras Alberto",
                "Calderón Higuera Maya",
                "Muñoz Manso_Beatriz",
                "Pérez Comendador Jesús",
                "Verdugo Molano Carolina",
                "Hernández Pérez Bernard",
                "Merino López Fernando",
                "Díaz Delavega Israel",
                "Torres Mollejo Guillermo",
                "Alcañiz Medina Abel",
                "Shrestha Thapa Shweta",
                "Mazuelos Iván",
                "Rodriguez Lorenzo David",
                "Cañete Agudo Victor",
                "Delgado García Alberto",
                "Duque Mingo Víctor",
                "López Martín Alberto"]



personas = []
for p in ipersonas:
    personas.append(ul.quote(p))

html = "<html><head></head><body>"
for persona in personas:
    try:
        '''
        for indice in range(1,10):
            picurl = "http://miorla.es/ArchivoImagenes/URJCTeleco/"+persona+"00"+str(indice)+".jpg"
            picimg = '<img src="'+picurl+'" width="290" height="386">'
            conn = urllib2.urlopen(picurl)
            img = conn.read()                       # obtengo la imagen
            html+= picimg

        for indice in range(10,24):
            picurl = "http://miorla.es/ArchivoImagenes/URJCTeleco/"+persona+"0"+str(indice)+".jpg"
            picimg = '<img src="'+picurl+'" width="290" height="386">'
            conn = urllib2.urlopen(picurl)
            img = conn.read()                       # obtengo la imagen
            html+= picimg
        '''
        picurl = "http://miorla.es/ArchivoImagenes/URJCTeleco/"+persona+"019.jpg"
        picimg = '<img src="'+picurl+'" width="290" height="386">'
        conn = urllib2.urlopen(picurl)
        img = conn.read()                       # obtengo la imagen
        html+= picimg
    except urllib2.HTTPError:
        print "Error procesando "+persona
        
html+= "</body></html>"
#print html
f = open('fotosorla.html', 'w')
f.write(html)
f.close()





'''
Hay que arreglar:

Error procesando Hern%C3%A1ndez%20Cordero%20Alejandro
Error procesando Aguado%20Jim%C3%A9nez%20Mariluz
Error procesando Naranjo%20Mart%C3%ADnez%20Manuel
Error procesando Lorenzo%20Servan%20Juanmanuel
Error procesando Fuillerat%20Garc%C3%ADa%20Franciscojos%C3%A9
Error procesando Alonso%20Sanchez%20Laura
Error procesando Valenzuela%20Velasco%20Sergio
Error procesando Angulo%20Hern%C3%A1ndez%20M%C2%AAjos%C3%A9
Error procesando Ruiz%20Tejero%20%C3%81ngelamar%C3%ADa
Error procesando G%C3%A1lvez%20Sosa%20Mar%C3%ADapiedraescrita
Error procesando Garcia%20Jimenez%20Jaime
Error procesando Delafuente%20Barrio%20Christian
Error procesando Barrag%C3%A1n%20Garnacho%20Aitor
Error procesando Fern%C3%A1ndez%20Pablo
Error procesando Horcajo%20Jerez%20Cintia
Error procesando Calvo%20Gago%20Rodrigo
Error procesando Villena%20Guerras%20Alberto
Error procesando Mu%C3%91oz%20Manso%20Beatriz
Error procesando Merino%20L%C3%B3pez%20Fernando
Error procesando D%C3%ADaz%20Delavega%20Israel
Error procesando Mazuelos%20Iv%C3%A1n
Error procesando Rodriguez%20Lorenzo%20David
Error procesando Ca%C3%B1ete%20Agudo%20Victor
Error procesando Duque%20Mingo%20V%C3%ADctor
Error procesando L%C3%B3pez%20Mart%C3%ADn%20Alberto

'''
