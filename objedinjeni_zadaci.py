"""I ZADATAK - Napiši program koji unosi ime i ispisuje poruku da li je upisano ime muško ili žensko. Ako se ime završava na a,
ispisaće se poruka 'Ime je žensko ime', u suprotnom će se ispisati poruka 'Ime je muško ime’."""
ime = input("Unesite Vase ime: ")
if ime[-1] == "a": #proveravamo samo poslednje slovo u imenu
    print("Ime je zensko ime.")
else:
    print("Ime je musko ime.")
    
    
"""II ZADATAK - Napiši program koji omogućava unos dve reči i ispisuje poruku koja reč je duža.
Ako su reci iste duzine ispisi Unete reci su iste duzine."""
prva_rec = input("Unesite prvu rec: ")
druga_rec = input("Unesite drugu rec: ")
if len(prva_rec)>len(druga_rec):
    print("Duza je prva rec koja glasi",prva_rec)
elif len(prva_rec)==len(druga_rec): #u slucaju da su reci iste duzine
    print("Unete reci su iste duzine.")
else:
    print("Duza je druga rec koja glasi",druga_rec)
    
    
"""III Zadatak - Napiši program koji unosi rečenicu na srpskom jeziku i ispisuje
je tako što će svako malo slovo i da zameni velikim slovom I.
Ukoliko ne postoji slovo i u recenici, ispisi recenica ne sadrzi slovo i"""
recenica = input("Unesite recenicu: " )
if "i" in recenica:
    nova_recenica = recenica.replace("i", "I")
    print("Izmenjena recenica glasi: ",nova_recenica)
else: 
    print("Uneta recenica ne sadrzi slovi i.") 
    

#IV ZADATAK - Napiši program koji omogućava unos nekog broja i ispisuje cifre tog broja.
#prvi nacin, ispis cifara bez pozicije u visecifrenom broju.
a = input("Unesite neki visecifreni broj: ")
for x in a:
    print(x)
    
#drugi nacin, ispis cifara sa pozicijama u visecifrenom broju
for x in range(0, len(a), 1): #range broji od pocetne do krajnje vrednosti sa zeljenim korakom.
    print(x+1,"cifra je",a[x])
    
    
#V ZADATAK -  Napiši program koji omogućava unos nekog broja i izračunava zbir njegovih cifara.
broj = input("Unesite zeljeni visecifreni broj: ")
s = 0
for i in range(0, len(broj), 1):
    s = s + int(broj[i])
print("Suma cifara broja",broj,"iznosi",s)


"""VI ZADATAK - Napiši program koji omogućava unos nekog broja i ispisuje broj 
obrnutim redosledom cifara od unetog."""
broj = input("Unesite zeljeni visecifreni broj: ")
#prvi nacin
print("Obrnuti redosled cifara unetog broja je",broj[::-1],",prvi nacin.")
#drugi nacin
a = len(broj)
s = "" #da pamti cifre
for i in range(-1, -a-1, -1): # mora -a-1 jer se ne racuna krajnja vrednost
    s = s + broj[i]
print("Obrnuti redosled cifara unetog broja je",s,",drugi nacin.")


#VII ZADATAK - Napisi program koji stampa ukupan broj slova 'a' u recenici.
recenica = input("Unesite neku recenicu: ")
brojac = 0
for x in recenica:
    if x == "a":
        brojac = brojac + 1
print("U recenici koju je korisnik uneo imamo",brojac,"slova a")


"""VIII ZADATAK - Napisi program koji stampa ukupan broj pojavljivanja slova
po zelji korisnika, u recenici koju korisnik unosi."""
recenica = input("Unesite neku recenicu: ")
slovo = input("Unesite slovo koje zelite da prebrojite u recenici: ")
brojac = 0
for x in recenica:
    if x == slovo:
        brojac += 1
print("U recenici koju je uneo korisnik, slovo",slovo,"imamo",brojac,"puta")


"""IX ZADATAK - . Napišite program koji traži od korisnika da unese string, a onda štampa sve
pozicije na kojima se nalazi slovo ’a’ u stringu."""
recenica = input("Unesite neku recenicu: ")
duzina = len(recenica)
s = ""
for x in range(0, duzina, 1): #kada zelimo da radimo sa indeksima koristimo range
    if recenica[x] == "a":
        s = s + str(x) +","
print("Slovo a  se u recenici pojavljuje na sledecim lokacijama",s,"kao poslednja lokacija indeksa")


"""X ZADATAK - Napisi program koji vraca ukupan broj slova i znakova interpukcije u recenici koju unosi korisnik.
Napomena: u ukupna broj nisu ukljuceni razmaci tj. space"""
#od ukupne duzine recenice, oduzimamo broj razmaka u recenici
recenica = input("Unesite neku zeljenu recenicu: ")
ukupna_duzina = len(recenica)
brojac_space = 0
for x in recenica:
    if x == " ":
        brojac_space += 1
ukupno = ukupna_duzina - brojac_space
print("U recenici se nalazu ukupno",ukupno,"slova i znakova interpukcije.")


"""XI ZADATAK - Napisi program koji od 2 uneta broja ispisuje zbir, razliku, proizvod, kolicnik, stepne,
binarni zapis prvog broja i heksadecimalni zapis drugog broja"""
a = int(input("Unesite prvi ceo broj: "))
b = int(input("Unesite drugi ceo broj: "))
zbir = a + b
razlika = a - b
proizvod = a * b
kolicnik = a / b
pr_na_dr = a ** b
dr_na_pr = b ** a
binarni = bin(a)
heksa = hex(b)
print("{0:^4} + {1:^4} = {2:^4}".format(a,b,zbir))
print("{0:^4} - {1:^4} = {2:^4}".format(a,b,razlika))
print("{0:^4} * {1:^4} = {2:^4}".format(a,b,proizvod))
print("{0:^4} / {1:^4} = {2:^4}".format(a,b,kolicnik))
print("{0:^4} na {1:^4} = {2:^4}".format(a,b,pr_na_dr))
print("{1:^4} na {0:^4} = {2:^4}".format(a,b,dr_na_pr))
print("{0:^4} binarno {1}".format(a,binarni))
print("{0:^4} heksadecimalno {1}".format(b,heksa))


#XII ZADATAK - Unos koliko zelimo brojeva i racunanje aritmeticke sredine
#korisnik unosi ukupan broj brojeva za koje zeli da racuna aritmeticku sredinu
duzina = input("Unesite ukupan broj brojeva za koje zelite da racunate aritmeticku sredinu: ")
sum = 0
for x in range(0,int(duzina)):
  print("Unesite",x+1,"broj:")
  ad = int(input(""))
  sum += ad
print("Aritmeticka sredina je {0:.2f}".format(sum/int(duzina)))


"""XIII ZADATAK - Bacanje novcica. Korisnik baca novcic zeljeni broj puta, 
resenje treba da nam ispise broj pojavljivanja pisma kao i glave.
Ispisati i procente pojavljivanja """
import random
broj_bacanja = int(input("Koliko puta zelite da bacate novcic: "))
pismo = 0
glava = 0
for x in range(0,broj_bacanja,1):
    a = random.randint(0,1) #dogadjaj ce biti ili 0 ili 1
    if a == 0:
        pismo += 1
    else:
        glava += 1
print("Broj pojavljivanja pisma je {0}({1:.2f}%) puta, broj pojavljivanja glave je {2}({3:.2f}%) puta.".format(pismo, pismo/broj_bacanja * 100, glava, glava/broj_bacanja * 100))


"""XIV ZADATAK - Ispitivanje da li je uneti broj pozitivan, negativan, deljiv sa sedam i 
odstampati sve parne brojeve od 0 do tog unetog broja kao i taj broj ako je taj broj pozitivan.
Ako je negativan odstampati sve parne brojeve od tog broj do 0, kao i nulu  i taj broj."""
pozicija = ""
broj = int(input("Unesite zeljeni broj: "))
if broj>0:
    print("Uneti broj je POZITIVAN.")
    for x in range(0,broj+1,2):
       pozicija += str(x)+","
    print("Pozitivni parni brojevi od 0 do {} su: {} zakljucno sa unetim brojem.".format(broj,pozicija))       
elif broj == 0:
    print("Uneti broj je NULA.")
else:
    print("Uneti broj je NEGATIVAN.")
    for x in range(broj,1,2):
        pozicija += str(x)+","
    print("Negativni parni brojevi od {} do 0 su: {} zakljucno sa brojem 0.".format(broj,pozicija))     
if broj % 7 == 0:
    print("Uneti broj JESTE deljiv sa sedam.")
else:
    print("Uneti broj NIJE deljiv sa sedam.")


"""XV ZADATAK - Ispitivanje da li su date stranice stranice trougla.
Ako jesu, ispitati da li je u pitanju jednakokraki, jednakostranicni ili raznovrsni trougao.
Ako date stranice nisu stranice trougla, ispisati Date stranice ne mogu biti stranice trougla."""
#ispistujemo da li je u pitanju trougao, ako jeste da li je jednakokraki, jednakostranican, raznostranican
a = int(input("Unesite stranicu a: "))
b = int(input("Unesite stranicu b: "))
c = int(input("Unesite stranicu c: "))
if a+b>c and a+c>b and b+c>a:
    print("Unete stranice jesu stranice trougla.")
    if a == b or a == c or c == b:
        print("Jednakokraki trougao.")
    if a == b and b == c: #po automatizmu znamo da je a == c jer je a == b a  b == c
        print("Jednakostranicni trougao.")
    if a != b  and b!= c and a!=c: #ovde moramo sve da ispitamo
        print("Raznovrsni trougao.")
else:
    print("Date stranice ne mogu biti stranice trougla.")  
    

"""XVI ZADATAK - Ispisivanje ocene na osnovu osvojenih bodova studenta.
Ipsisati brojevnu kao i opisnu ocenu."""
p = int(input("Unesite broj bodova: "))
if p in range(0,100):
    if p <= 50:
        print("1 (NEDOVOLJAN)")
    elif p<=63: #ovo pisemo umesto if p>50 and p<=63
        print("2 (DOVOLJAN)")
    elif p<=76:
        print("3 (DOBAR)")
    elif p<=89:
        print("4 (VRLO DOBAR)")
    elif p<=100:
        print("5 (ODLICAN)")
else:
    print("Broj bodova mora biti u opsegu od 0 do 100")
    
"""XVII ZADATAK - Napraviti jelku od zvezdica.
Koristiti while petlju
a = 5
b = "*"
print(a*b)"""
j = 1
while j<=8:
    print(" "*(8-j)+"*"*(2*j-1))
    j = j+1


"""XVII ZADATAK - Papir, kamen, makaze
Igrate protiv kompjutera, pobednik je ko prvi stigne do 3 pobede.
"""
import random
ja = 0
kompa = 0
odgovor = input("Da li zelite da igra pocne: -->  ")
if odgovor.upper() == "DA":
    print("Srecno!")
    opcije = ["papir", "kamen", "makaze"]
    while ja<3 and kompa<3:
        korisnik = input("Unesite vas odgovor: ")
        random_broj = random.randint(0,2)
        kompjuter = opcije[random_broj]
        print("Kompjuter bira: ",kompjuter)
        if korisnik.lower() == "papir" and kompjuter == "papir":
            print("Nereseno")
        if korisnik.lower() == "papir" and kompjuter == "makaze":
            kompa += 1
        if korisnik.lower() == "papir" and kompjuter == "kamen":
            ja += 1
        if korisnik.lower() == "kamen" and kompjuter == "kamen":
            print("Nereseno")
        if korisnik.lower() == "kamen" and kompjuter == "papir":
            kompa += 1
        if korisnik.lower() == "kamen" and kompjuter == "makaze":
            ja += 1
        if korisnik.lower() == "makaze" and kompjuter == "makaze":
            print("Nereseno")
        if korisnik.lower() == "makaze" and kompjuter == "kamen":
            kompa += 1
        if korisnik.lower() == "makaze" and kompjuter == "papir":
            ja += 1
    if ja>kompa:
        print("Cestitam, pobedili ste rezultatom {} naprema {}!!!".format(ja, kompa))
    else:
        print("Nazalost, kompjuter je pobedio rezultatom {} naprema {}!!!".format(kompa, ja))   
else:
    print("Vratite se kada budete spremni da se igramo!!!")

#II NACIN - LAKSI SA MANJE KODA
#papir, kamen, makaze:
import random
dogadjaji = ["papir", "kamen", "makaze"]
ja_score = 0
kompa_score = 0
while True:
    ja = input("Unesi papir kamen ili makaze:  ")
    ja = ja.lower()
    if ja not in dogadjaji:
        print("Niste dobro uneli. Unesite ponovo.")
        continue
    racunar = random.randint(0,2)
    izbor_kompjutera = dogadjaji[racunar]
    print("Kompjuter je odabrao:",izbor_kompjutera)
    if ja == izbor_kompjutera:
        print("Nereseno.")
        continue
    if ja == "papir" and izbor_kompjutera == "kamen":
        ja_score += 1
    elif ja == "kamen" and izbor_kompjutera == "makaze":
        ja_score += 1
    elif ja == "makaze" and izbor_kompjutera == "papir":
        ja_score += 1
    else:
        kompa_score += 1
    if ja_score == 3 or kompa_score == 3:
        break
if ja_score>kompa_score:
    print("CESTITAM, pobedili ste rezultatom {} naprema {}.".format(ja_score,kompa_score))
else:
     print("IZGUBILI STE, kompjuter je pobedio rezultatom {} naprema {}.".format(kompa_score,ja_score))


