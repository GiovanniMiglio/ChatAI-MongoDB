from pymongo import MongoClient
import ollama
client = MongoClient("mongodb://localhost:27017")
conversazioni = client["chatDb"]["conversations"]
id_chat = conversazioni.insert_one({"user": "giovanni", "title": "Chat con l'AI", "messages": []}).inserted_id
while True:
    domanda = input("Tu: ")
    if domanda == "esci":
        break
    conversazioni.update_one({"_id": id_chat},
        {"$push": {"messages": {"role": "user", "content" : domanda }}})
    chat = conversazioni.find_one({"_id": id_chat})
    storico = chat["messages"]
    risposta = ollama.chat(model="qwen2.5:7b", messages=storico)
    testo = risposta["message"]["content"]
    conversazioni.update_one({"_id": id_chat},
        {"$push": {"messages": {"role": "assistant", "content" : testo }}})
    print(f"AI: {testo}")


