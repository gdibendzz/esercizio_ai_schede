

def genera_prompt(scheda):

    argomento = scheda.argomento
    livello = scheda.livello

    istruzioni = f'''

    La lingua di riferimento è l'Italiano.

    Valuta  {argomento}: 
    se non è un ambito tematico su cui non si può costruire un corso allora  ritorna esito ERROR e in dati la frase 'Input non valido' e non fare altro

    Se è un ambito tematico corretto allora procedi con le seguenti istruzioni

    ISTRUZIONI
    Sei un professore di {argomento} 

    Devi generare le seguenti sezioni per creare una scheda didattica:
    
    Ti fornisco le coppie di chiavi - valori separate da :
    Con * ti indico quelli obbligatori, con - quelli opzionali
   
    Inizio Struttura chiave-valore:

    * titolo:titolo della lezione ;
    * introduzione:introduzione;
    * obiettivi:almeno tre obiettivi didattici;
    * concetti:elenco dei concetti fondamentali;
    - esempio:un esempio di codice Python completo;
    - spiegazione_esempio:spiegazione dell’esempio;
    - esercizio:un esercizio da svolgere;
    - svolgimento_esercizio:soluzione dell’esercizio, da conservare nell’output del programma;
    - quiz: tre domande a risposta multipla con quattro opzioni per ogni domanda, evidenziando risposta corretta, con breve spiegazione;

    Fine struttura chiave-valore

    La risposta deve essere di almeno 5 pagine A4 standard

    ritorna esito OK e  in dati  un json e un markdown
    NON aggiungere alcun tipo di frase, né prima, né dopo
    Inserisci nella risposta SOLO le indicazioni presenti nella struttura, senza altro
    '''

    contesto = f'''
        Dobbiamo scrivere una scheda didattica di un corso basata su {argomento}
        La difficoltà del corso generato deve essere: {livello}
    '''

    input = f'''
        argomento: {argomento}
        livello: {livello}
    '''

    output = '''
    
    crea un json con questa struttura:


        {

        esito: esito dell'elaborazione,
    
        dati:
            contenuto del json

            $$$

            contenuto del markdown

        }
    
    '''

    prompt =  f"""

        CONTESTO
        {contesto}

        ISTRUZIONI
        {istruzioni}

        INPUT
        {input}

        OUTPUT
        {output}
    """

    return prompt