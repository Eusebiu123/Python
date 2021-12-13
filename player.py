import math, random


class Jucator():
    def __init__(self, litera):
        self.litera = litera

    def mutare1(self, joc):
        pass

    def mutare2(self, joc):
        pass


class Om(Jucator):
    def __init__(self, litera):
        super().__init__(litera)

    def mutare1(self, joc):
        loc_liber = False
        valoare = None
        while not loc_liber:
            patratel = input(self.litera + ' alege. Scrie in ce patratel (0-9): ')
            try:
                valoare = int(patratel)
                if valoare not in joc.mutari_posibile():
                    raise ValueError
                loc_liber = True
            except ValueError:
                print('Patratel invalid sau deja ocupat. Alege altul!')
        return valoare

    def mutare2(self, joc):
        loc_liber = False
        valoare = None
        while not loc_liber:
            patratel = input(self.litera + ' alege. Scrie in ce patratel (0-9): ')
            try:
                valoare = int(patratel)
                if valoare not in joc.mutari_posibile():
                    raise ValueError
                loc_liber = True
            except ValueError:
                print('Patratel invalid sau deja ocupat. Alege altul!')
        return valoare


class Random(Jucator):
    def __init__(self, litera):
        super().__init__(litera)

    def mutare1(self, joc):
        patratel = random.choice(joc.mutari_posibile())
        return patratel

    def mutare2(self, joc):
        patratel = random.choice(joc.mutari_posibile())
        return patratel


class Ai(Jucator):
    def __init__(self, litera):
        super().__init__(litera)

    def mutare1(self, joc):
        if len(joc.mutari_posibile()) == 9:
            patratel = random.choice(joc.mutari_posibile())
        else:
            patratel = self.minimax(joc, self.litera)['pozitie']
        return patratel

    def mutare2(self, joc):
        if len(joc.mutari_posibile()):
            patratel = random.choice(joc.mutari_posibile())
            return patratel

    def minimax(self, state, jucator):
        max_jucator = self.litera
        oponent = 'O' if jucator == 'X' else 'X'
        if state.castigatorcurent == oponent:
            return {'pozitie': None, 'scor': 1 * (state.nrspatiilibere() + 1) if oponent == max_jucator else -1 * (state.nrspatiilibere() + 1)}
        elif not state.locuri_libere():
            return {'pozitie': None, 'scor': 0}
        if jucator == max_jucator:
            mutare_buna = {'pozitie': None, 'scor': -math.inf}  # vrem sa maximizam
        else:
            mutare_buna = {'pozitie': None, 'scor': math.inf}  # vrem sa minimizam
        for mutare_posibila in state.mutari_posibile():
            state.fa_mutare(mutare_posibila, jucator)
            simulare = self.minimax(state, oponent)
            # aici dam undo la mutare
            state.tabla[mutare_posibila] = ' '
            state.castigatorcurent = None
            simulare['pozitie'] = mutare_posibila  # aici reprezinta viitoarea mutarea optima
            if jucator == max_jucator:
                if simulare['scor'] > mutare_buna['scor']:
                    mutare_buna = simulare
            else:
                if simulare['scor'] < mutare_buna['scor']:
                    mutare_buna = simulare
        return mutare_buna
