import os
import datetime

def write_log(info, stato, messaggio):
        now_date = datetime.datetime.now()
        format_date = now_date.strftime("%d/%m/%Y %H:%M:%S")

        if not os.path.exists("log"):
            os.mkdir("log")

        with open("log/indice_elaborazioni.txt", "a") as f:
              log_line = f"Log del giorno {format_date}\n{stato}\n{info}\n{messaggio}\n\n"


              f.write(log_line)


        

