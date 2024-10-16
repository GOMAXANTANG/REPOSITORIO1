meme_dict = {
            "cringe": "Algo excepcionalmente raro o embarazoso",
            "lol": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "creepy": "aterrador, siniestro"
            "AGGRO": "ponerse agresivo/enojado"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
   print("")
