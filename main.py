from util.env_manager import EnvManager
from util.gestore_richieste import get_argomenti
from openai import OpenAI

#commit di prova
#terzo commit
km = EnvManager()

try:

    api_key = km.load_from_key("API_KEY")
    api_model = km.load_from_key("MODEL")

    print(api_key, api_model)

    json_input = get_argomenti()

    with open("argomenti.json", "w") as f:
        f.write(json_input)

    print(json_input)

    #openai_client = OpenAI(api_key=apy_key)

    
    #TODO controllare nel prompt se il livello è qualcosa di consono


except Exception as e:
    print("Errore: ", e)