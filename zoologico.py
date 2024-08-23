class Animal:
    def __init__(self, nome, idade, horas_comer, vizinho):
        self.nome = nome
        self.idade = idade
        self.horas_comer = horas_comer
        self.vizinho = vizinho

    def fazer_barulho(self):
        pass
    
    def alimentacao_dieta(self):
        pass
    
    def movimento_locomocao(self):
        pass
    
    def categorias_aves(self):
        return "Águia, Coruja, Pinguim"
    print(f"Aves: {categorias_aves}")
    
class Leao(Animal):
    def fazer_barulho(self):
        return "Rugido"
    def alimentacao_dieta(self):
        return "Carníviro"
    def movimento_locomocao(self):
        return "Quadrupede"
    def vizinhos_animais(self):
        print(f"Os vizinhos são: {Coruja.nome()}")

class Coruja(Animal):
    def fazer_barulho(self):
        return "Corujar"
    def alimentacao_dieta(self):
        return "Carníviro"
    def movimento_locomocao(self):
        return "Bípede e Vôo"
    def vizinhos_animais(self):
        print(f"Os vizinhos são: {Leao.nome()}")












# Lista de animais com polimorfismo
animais = [Leao("Lion", 6, "Manhã", "Coruja"), 
           Coruja("Owl", 4, "Noite", "Leão")]

#animais[0].set_vizinho(animais[1])

for animal in animais:
    print(f"O {animal.nome}, tem {animal.idade}!")
    print(animal.categorias_aves)
