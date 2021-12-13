import math,time
from player import Om,Ai

class X_0:
    def __init__(self):
        self.tabla=self.fa_tabla()
        self.castigatorcurent=None
    def fa_tabla(self):
        return [' ' for _ in range(9)]
    def afiseaza(self):
        for linie in [self.tabla[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(linie) + ' |')
    def afiseaza_mutari(self):
        numar_tabla = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for linie in numar_tabla:
            print('| ' + ' | '.join(linie) + ' |')
    def fa_mutare(self,patratel,litera):
        if self.tabla[patratel] == ' ':
            self.tabla[patratel] = litera
            if self.castigatorul(patratel, litera):
                self.castigatorcurent = litera
            return True
        return False
    def castigatorul(self, patratel, litera):
        linie_i = math.floor(patratel / 3)
        linie = self.tabla[linie_i*3:(linie_i+1)*3]
        if all([k == litera for k in linie]):
            return True
        col_i = patratel % 3
        coloana = [self.tabla[col_i+i*3] for i in range(3)]
        if all([k == litera for k in coloana]):
            return True
        if patratel % 2 == 0:
            diag1 = [self.tabla[i] for i in [0, 4, 8]]
            if all([k == litera for k in diag1]):
                return True
            diag2 = [self.tabla[i] for i in [2, 4, 6]]
            if all([k == litera for k in diag2]):
                return True
        return False
    def locuri_libere(self):
        return ' ' in self.tabla
    def nrspatiilibere(self):
        return self.tabla.count(' ')
    def mutari_posibile(self):
        return [i for i, k in enumerate(self.tabla) if k == " "]

def joaca(dif, joc, x_jucator, o_jucator, afis_joc):
    if afis_joc:
        joc.afiseaza_mutari()

    litera = 'X'
    if dif == '3':
        while joc.locuri_libere():
            if litera == 'O':
                patratel = o_jucator.mutare1(joc)
            else:
                patratel = x_jucator.mutare1(joc)
            if joc.fa_mutare(patratel, litera):

                if afis_joc:
                    print(litera + ' a facut o mutare in patratelul {}'.format(patratel))
                    joc.afiseaza()
                    print('')

                if joc.castigatorcurent:
                    if afis_joc:
                        print(litera + ' a castigat!')
                    return litera
                litera = 'O' if litera == 'X' else 'X'

            time.sleep(.10)

        if afis_joc:
            print('Este egalitate!')
    elif dif == '1':
        while joc.locuri_libere():
            if litera == 'O':
                patratel = o_jucator.mutare2(joc)
            else:
                patratel = x_jucator.mutare2(joc)
            if joc.fa_mutare(patratel, litera):

                if afis_joc:
                    print(litera + ' a facut o mutare in patratelul {}'.format(patratel))
                    joc.afiseaza()
                    print('')

                if joc.castigatorcurent:
                    if afis_joc:
                        print(litera + ' a castigat!')
                    return litera
                litera = 'O' if litera == 'X' else 'X'

            time.sleep(.10)

        if afis_joc:
            print('Este egalitate!')
    if dif == '2':
        contor = 0
        while joc.locuri_libere():
            contor = contor + 1
            if litera == 'O':
                if contor % 2 == 0:
                    patratel = o_jucator.mutare2(joc)
                else:
                    patratel = o_jucator.mutare1(joc)
            else:
                if contor % 2 == 0:
                    patratel = x_jucator.mutare2(joc)
                else:
                    patratel = x_jucator.mutare1(joc)
            if joc.fa_mutare(patratel, litera):

                if afis_joc:
                    print(litera + ' a facut o mutare in patratelul {}'.format(patratel))
                    joc.afiseaza()
                    print('')

                if joc.castigatorcurent:
                    if afis_joc:
                        print(litera + ' a castigat!')
                    return litera
                litera = 'O' if litera == 'X' else 'X'

            time.sleep(.10)

        if afis_joc:
            print('Este egalitate!')



if __name__ == '__main__':
    gata = False
    contorx = 0
    contory = 0
    while gata != True:
        dificultate = input('Ce dificultate vrei? [1/2/3]  ')
        dif=dificultate
        x_jucator = Om('X')
        o_jucator = Ai('O')
        t = X_0()
        final = joaca(dif,t,x_jucator,o_jucator,afis_joc=True)
        if final == 'X':
            contorx = contorx + 1
        else:
            contory = contory + 1
        raspuns = input('Mai joci inca o data? [y/n]  ')
        if raspuns.lower() == 'y':
            gata = False
        else:
            print("Papa")
            gata = True
    s = 'Ai castigat de '
    s1 = ' ori, iar el de '
    s2 = ' ori!'
    print(s + str(contorx) + s1 + str(contory) + s2)