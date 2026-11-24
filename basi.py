posts = [{
"title" : "dizionario",
"views" : 10,
"author" : { "name" : "Luigi" ,
            "surname" : "Bianchi" } 
},
{
"title" : "dizionario2",
"views" : 50,
"author" : { "name" : "Antonio" ,
            "surname" : "Rossi" } 
},
{
"title" : "dizionario3",
"views" : 30,
"author" : { "name" : "Marco" ,
            "surname" : "Verdi" } 
}
]
print(posts[1]["author"]["surname"])
def popolari(lista, soglia):
    risultato=[]
    for post in lista :
        if post ["views"]>soglia:
            risultato.append(post)
    return risultato
for post in popolari(posts,20):
    print(f'{post["title"]} di {post["author"]["name"]} {post["author"] ["surname"]} - {post["views"]} views')

