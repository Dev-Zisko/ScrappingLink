import queue
import urllib.request
import re
from urllib.parse import urljoin

def buscarUrl1(url):
  try:
    peticion = urllib.request.Request(url)
    html = urllib.request.urlopen(peticion).read()
    buscaEnlaces = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    enlaces = buscaEnlaces.findall(str(html))
    print("Contenido de la página: ")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print(html)
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("Fin del contenido de la página. ")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("Mostrando links encontrados en la página: ")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    for enlace in enlaces:
      print("Enlace: ", enlace)
    print("Todos los enlaces encontrados han sido mostrados. ")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
  except:
    print("Error al buscar la página.")
    
def buscarUrl2(url, n):
  try:
    peticion = urllib.request.Request(url)
    html = urllib.request.urlopen(peticion).read()
    buscaEnlaces = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    enlaces = buscaEnlaces.findall(str(html))
    cont = 1
    cont1 = 1
    print("Contenido de la página: ")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print(html)
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("Fin del contenido de la página. ")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("Mostrando links encontrados en la página: ")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    for enlace in enlaces:
      if cont <= int(n):
        print("URL[", cont, "]: ", enlace)
        peticion1 = urllib.request.Request(enlace)
        html1 = urllib.request.urlopen(peticion1).read()
        enlaces1 = buscaEnlaces.findall(str(html1))
        for enlace1 in enlaces1:
          if cont1 <= int(n):
            print("URL[", cont, "]-[", cont1, "]: ", enlace1)
          cont1 += 1
        cont1 = 1
      cont += 1
    print("Todos los enlaces encontrados han sido mostrados. ")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
  except:
    print("Error al buscar la página.")

tarea = input("Indique la tarea a probar (1 o 2): ")
if(tarea == "1"):  
  url = input("Introduce la url (wwww.example.com): ")
  buscarUrl1("http://"+url)
if(tarea == "2"):
  url = input("Introduce la url (wwww.example.com): ")
  n = input("Indique el numero de iteraciones (n): ")
  buscarUrl2("http://"+url, n) 