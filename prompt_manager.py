

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

    produci un json e un markdown
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
    crea un testo con questa struttura:

    
        contenuto del json

        $$$

        contenuto del markdown
    
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