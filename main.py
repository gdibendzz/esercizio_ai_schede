from util.env_manager import EnvManager
from util.gestore_richieste import get_argomenti
from google import genai
from openai import OpenAI
import os
import json
from model.scheda import Scheda
from prompt_manager import genera_prompt
from util.log_manager import write_log

#commit di prova
#terzo commit
km = EnvManager()

try:

    api_key = km.load_from_key("API_KEY")
    api_model = km.load_from_key("MODEL")


    json_input = get_argomenti()

    with open("argomenti.json", "w") as f:
        f.write(json_input)

    
    with open("argomenti.json", "r") as f1:
        json_out = f1.read()

    scheda_list = json.loads(json_out)

    for s in scheda_list:
        try:

            prompt = genera_prompt(Scheda(s["argomento"], s["livello"]))
        

            #client = OpenAI(api_key=api_key)

            #response = openai_client.responses.create(input=prompt, model=api_model, temperature=0, max_output_tokens=500)

            client = genai.Client(api_key=api_key)

            chat = client.chats.create(model=api_model)

            response = chat.send_message(prompt)

            if not os.path.exists("output"):
                os.mkdir("output")

            text = response.text

            res = json.loads(text)

            data = res["dati"]
            esito = res["esito"]

            print(data)

            if esito =="ERROR":
                raise(Exception(data))
            
            files = data.split("$$$")


            json = files[0]
            md = files[1]

            filename = s["argomento"].strip().lower().replace(" ", "_")
            file_names = [f"{filename}.json", f"{filename}.md"]
            

            with open(f"output/{filename}.json", "w") as jf:
                jf.write(json)
            
            with open(f"output/{filename}.md", "w") as mf:
                mf.write(md)

            write_log(f"{s["argomento"]}\n{s["livello"]}\n{",".join(file_names)}", "OK", "Successo")
               

        except Exception as e:
            write_log("Errore API", "ERROR", str(e))
        



except Exception as e:
    write_log("Errore Generico", "ERROR", str(e))
    print("Errore: ", e)