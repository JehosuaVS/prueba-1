meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Rolling on Floor Laughing-una respuesta a una broma ",
            "SHEESH": "ligera desaprobación ",
            "CREEPY": "aterrador, siniestro ",
            "AGGRO": "ponerse agresivo/enojado ",
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print=(meme_dict[word]) 
else:
    print("no se encontro")