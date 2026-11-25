# Chat AI con memoria in MongoDB
Ho costruito una chat AI  con un modello open source in locale con Ollama, che salva lo storico delle conversazioni in MongoDB
## Tecnologie
- Python
- MongoDB (pymongo)
- Ollama con il modello qwen2.5:7b
## Come funziona
Scrivi un messaggio, tipo di presentazione , o comunque con dati, e in seguito fai una domanda su quei dati, i modelli sono stateless (non ricordano niente), quindi a ogni messaggio l'app rilegge tutta la conversazione da MongoDB e la rimanda al modello. Ogni nuovo messaggio viene aggiunto con $push
## Come avviarlo
Per essere avviato è necessario:
1. MongoDB acceso
2. Ollama con il modello scaricato
3. installare le librerie con pip install -r requirements.txt
4. lanciare python chat_ai.py
## Cosa ho imparato
-  i primi comandi in mongosh
-  documenti e collection
- modellare i dati
- annidati o  riferimenti e quando usare uno o l'altro
-  linguaggio di Python e la libreria pymongo
- modellare lo storico delle conversazioni in MongoDB con Python