import os
from dotenv import load_dotenv

class EnvManager:

    def __init__(self):
        pass

    def load_from_key(self, key_var_name):

        try:
            load_dotenv()

            value = os.getenv(key_var_name)

            if not value:
                raise ValueError("Errore nel caricamento del valore", key_var_name)
            
            return value
            
        except Exception as  e:
            raise(e)