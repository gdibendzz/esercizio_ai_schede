from util.env_manager import EnvManager
from util.gestore_richieste import get_argomenti
from openai import OpenAI
import json
from model.scheda import Scheda
from prompt_manager import genera_prompt

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
        prompt = genera_prompt(Scheda(s["argomento"], s["livello"]))
       

        openai_client = OpenAI(api_key=api_key)

        response = openai_client.responses.create(input=prompt, model=api_model, temperature=0, max_output_tokens=500)



except Exception as e:
    print("Errore: ", e)