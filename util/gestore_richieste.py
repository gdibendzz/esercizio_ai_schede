from model.scheda import Scheda
import json

def get_argomenti():

    scheda_list = []
    scheda_dict = []
    
    while True:
        n = input("Quante schede vuoi creare? ")

        try:
            numero = int(n)
            break
        except ValueError:
            print("Inserire un valore intero\n")
            continue

    for i in range(numero):

        arg = ""
        
        while len(arg.strip()) == 0:
            arg = input("Inserire l'argomento: ")

            if(len(arg.strip()) == 0):
                print("Argomento obbligatorio\n")
                
            
        lvl = input("Inserire il livello (oppure lasciare vuoto per default basso): ")

        if(len(lvl.strip()) == 0):
            scheda_list.append(Scheda(arg))
        else:
            scheda_list.append(Scheda(arg, lvl))


    for s in scheda_list:
        scheda_dict.append(
            {

                "argomento": s.argomento,
                "livello": s.livello

            }
        )

        

    return json.dumps(scheda_dict, indent=4)






