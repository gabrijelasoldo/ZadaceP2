rijec = input("Unesite rijec:")
def obrnuto_rekurzija(rijec):
        if len(rijec)==1:
            return rijec
        return obrnuto_rekurzija(rijec[1::]) + rijec[0]

print(obrnuto_rekurzija(rijec))
