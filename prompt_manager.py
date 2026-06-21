

def genera_prompt(scheda):

    argomento = scheda.argomento
    livello = scheda.livello

    istruzioni = f'''
    Sei un professore di {argomento} 
    La lingua di riferimento è l'Italiano.
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
    Se i dati di input non sono chiare e ben definite, 
    indica la miglior risposta possibile ma segnala che ci sono state problematiche
    e suggerisci possibili soluzioni

    Devi restituire DUE file scaricabili come definito nella sezione output 
    NON aggiungere commenti né prima, né dopo
    Inserisci nella risposta SOLO le indicazioni presenti nella struttura
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
    crea:
    1. un file json scaricabile con struttura chiave-valore evidenziata nelle istruzioni
    
    2. un file markdown scaricabile
    
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