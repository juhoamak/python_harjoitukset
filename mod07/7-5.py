# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
# Ohjelma palauttaa toisen listan, muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.


def parittomat_pois(kokonaisluvut):
    ei_parittomia =[]

    for i in kokonaisluvut:
        if i % 2 == 0:
            ei_parittomia.append(i)

    return ei_parittomia


## pääohjelma

testi_lista = [1,1,2,3,5,8,13,21,34]

karsittu = parittomat_pois(testi_lista)

print(f"alkuperäinen lista: {testi_lista}")

print(f"karsittu lista: {karsittu}")


