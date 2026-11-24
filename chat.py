from pymongo import MongoClient

client = MongoClient ("mongodb://localhost:27017")
db = client["chatDb"]
conversazioni = db["conversations"]

nuova={
    "user" : "giovanni",
    "title" : "Domanda sul contratto",
    "messages":[{"role":"user", "text":"Quando scade il mio contratto?"}]
}
risultato = conversazioni.insert_one(nuova)
print(f"Conversazione creata con id: {risultato.inserted_id}")
conversazioni.update_one(
    {"_id": risultato.inserted_id},
    {"$push": {"messages": {"role": "assistant", "text": "Il tuo contratto scade il 31/12/2026."}}}
)
conversazioni.update_one(
    {"_id": risultato.inserted_id},
    {"$push": {"messages": {"role": "user", "text": "C'e' la possibilta' di rinnovo?"}}}
)
chat = conversazioni.find_one({"_id": risultato.inserted_id})
for messaggio in chat["messages"]:
    print(f'{messaggio["role"]} : {messaggio["text"]}')   