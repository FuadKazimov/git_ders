
#Task1
def count_repeated(soz):
    unique_chars = set(soz)
    repeated_count = 0

    for char in unique_chars:
        if soz.count(char) > 1:
            repeated_count += 1

    return repeated_count

string = input("Soz daxil et: ")
print(count_repeated(string))          

#Task2
def tekrarlanan(soz):
    tekrar_olunan_elementler =[]
    for i in soz:
        if i in tekrar_olunan_elementler:
            continue
        count = soz.count(i)
        if count > 1:
            tekrar_olunan_elementler.append(i)
    return len(tekrar_olunan_elementler)
print(tekrarlanan())


#Task 3.

products = []
prchased_products = []
while True:
    print("Magazaya xos gelmisiniz!")
    print("Emeliyyati secin: ")
    print("1. Mehsul elave edin")
    print("2. Mehsulu silin")
    print("3. Mehsula baxin")
    print("4. Mehsulun sayina baxin")
    print("5. Mehsullari alinmis kimi qeyd edin")
    print("6. Cixin")
    
    secim = int(input("Seciminizi daxil edin: "))
    if secim == 1:
        product = input("Mehsulu daxil edin: ")
        products.append(product)
        print(f"{products} siyahiya elave edildi! ")

    elif secim == 2:
        products = input("Silinecek mehsulu elave edin: ")
        
        if product in products:
            products.remove(product)
            print(f"{product} siyahinizdan silindi! ")
        else:
            print(f"{products} tapilmadi")
    elif secim == 3:
        print("Alinacaq mehsullar")
        print(products)
        print("alinmis mehsullar")
        print(prchased_products)
    elif secim == 4:
        print(f"Siyahidaki mehsullar {products}")
        
    elif secim == 5:
        product = input("Alinmis mehsulu qeyd edin: ")
        if product in products:


            prchased_products.append(product)
            product.remove(product)
            print(f"{product} alinmis kimi qeyd olundu. ")
        else:
            print(f"{product} siyahida tapilmadi. ")


    elif secim == 6:
        print("Proqram dayandirildi. Tesekkur edirik! ")
        break

#Task4
movies = [
    ("Inception", 9),
    ("The Dark Knight", 8),
    ("Interstellar", 10),
    ("The Matrix", 7),
    ("Avengers: Endgame", 8),
    ("Parasite", 9)
]
for i in range(len(movies)):
    for j in range(i + 1, len(movies)):
        if movies[i][1] < movies[j][1]:
            movies[i],movies[j] = movies[j],movies[i]

yuksek_reytingli_film = []
for movie in movies:
    if movie[1] >= 8:
        yuksek_reytingli_film.append(movie[0])

ortalama = 0
for movie in movies:
    ortalama += movie[1]

ortalama_reyting = ortalama / len(movies)
filimler = []
for movie in movies:
    if True:
        filimler.append(movie[0])

print("reyting:", movies)
print("reyting +8",yuksek_reytingli_film)
print("ededi orta",ortalama_reyting)
print("filimin adi",filimler)
