import json

""" Crear una funció que mostri, per consola, i guardi en un arxiu extern, 
un JSON amb una key de nom book que contindrà titel, cover, year i pages. 
Dintre del JSON hi hauran 4 de cada book (s’ha d’omplir amb values). 
"""
def cearJson():
    libros = """
        {
        "book":[
            {"title": "Nosotros en la luna",
            "cover": "Soft cover",
            "year": "2019",
            "pages": "202"
            }
            {"title": "Adiós Pequeño",
            "cover": "Soft cover",
            "year": "2020",
            "pages": "136"
            }
            {"title": "Aquí empieza todo",
            "cover": "Hard cover",
            "year": "2021",
            "pages": "267"
            }
            {"title": "Qué pasaría si ...?",
            "cover": "Soft cover",
            "year": "2017",
            "pages": "87"
            }
        ]
    }    
    """
    with open("libro1.json",'w') as file:
        json.dump(libros,file)

"""Crear una funció que llegeixi el JSON de l’exercici 2 i surti el resultat (en format json) per consola."""
def imprimirJson():
    with open("libro1.json",'r') as file:
        resultat = json.load(file)
        print(resultat)
