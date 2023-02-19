import random as rd

class Game:
    def __init__(self):
        with open("puzzles.txt") as f:
            lvl = rd.randint(0, 17)
            lines = f.readlines()
            self.puzzle, self.solution = lines[lvl].split(":")
            self.puzzle = [i for i in self.puzzle]
            self.solution = [i for i in self.solution]
        self.current = self.puzzle

    def __repr__(self) -> str:
        out = ""
        for i in range(9*9):
            out += self.current[i]
            i += 1
            if i % 3 == 0:
                out += " "
            if i % 9 == 0:
                out += "\n"
                if (i // 9) % 3 == 0:
                    out += "\n"
        return out

    def check(self):
        for i in range(9*9):
            if self.current[i] != self.solution[i]:
                return False
        return True

    def mark(self, row, col, n):
        if n < 1 or n > 9:
            print("Le nombre doit être entre 1 et 9")
            return 0
        if row > 8 or row < 0:
            print("Coordonnées invalide")
            return 0
        if col < 0 or col > 8:
            print("Coordonnées invalide")
            return 0
        if self.puzzle[row * 9 + col] == ".":
            self.current[row * 9 + col] = str(n)
            return 1
        else:
            print("Ne peut pas modifier le nombre à cet emplacement")
            return 0



print("Jeux Sudoku")
print("Pour jouer veuiller entrer: num_ligne num_colonne nombre")
print("Les lignes et colonnes sont numéroter de 0 à 8")
g = Game()
while(not g.check()):
    print(g)
    try:
        r, c, n = input("Entrée: ").split(" ")
        i_r, i_c, i_n = int(r), int(c), int(n)
        g.mark(i_r, i_c, i_n)
    except:
        print("Veuiller entrée les coordonées et nombre correctement")
print("Puzzle résolu")