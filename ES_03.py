#dato un dizionario, scambio chiave con valore
dizionario = {"a": 1, "b": 2, "c": 3}

#la funzione dict.items() restituisce tante tuple quante sono le coppie chiave valore
# quindi posso ciclare per la lista di tuple che si genera e salvare i due valori della tupla in due variabili differenti
# facendo come sotto, il corpo del ciclo sarebbe valore : chiave, eseguito per tutte le chiavi e valori che si hanno nel dizionario 
scambiato = {valore : chiave for chiave, valore in dizionario.items()}

print(scambiato)