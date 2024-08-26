class Animal:
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao):
        self.nome = nome
        self.idade = idade
        self.barulho = barulho
        self.movimento = movimento
        self.alimentacao = alimentacao
        self.habitat = habitat
        self.vizinhos = []  # Lista dos animais vizinhos
        self.horas_alimentacao = horas_alimentacao

    def adicionar_vizinho(self, nome_vizinho):
        if len(self.vizinhos) < 2:
                self.vizinhos.append(nome_vizinho)
        else:
            print(f"{self.nome} já tem o máximo de vizinhos.")

    def detalhes(self):
        return (f"Nome: {self.nome}\nIdade: {self.idade}\nBarulho: {self.barulho}\n"
                f"Movimento: {self.movimento}\nAlimentação: {self.alimentacao}\n"
                f"Habitat: {self.habitat}\nVizinhos: {', '.join(self.vizinhos) or 'Nenhum'}\n"
                f"Horário de Alimentação: {self.horas_alimentacao}")

    def alimentar(self):
        return f"{self.nome} foi alimentado às {self.horas_alimentacao} horas."


class Mamifero(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao):
        super().__init__(nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao) # super() ajuda a utilizar item da classe principal (nesse caso a class Amnimal)


class Ave(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao):
        super().__init__(nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao)


class Reptil(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao):
        super().__init__(nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao)


class Zoo:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def listar_animais(self):
        for animal in self.animais:
            print(animal.nome)

    def listar_categorias(self, categoria):
        for animal in self.animais:
            if isinstance(animal, categoria):  # Verifica se o animal é da categoria especificada
                print(animal.nome)

    def listar_vizinhos(self, nome):
        for animal in self.animais:
            if animal.nome == nome:
                print(f"Vizinhos de {nome}: {', '.join(animal.vizinhos) or 'Nenhum'}") 
                return
        print("Animal não encontrado!")

    def buscar_animal(self, nome):
        for animal in self.animais:
            if animal.nome == nome:
                print(animal.detalhes())
                return
        print("Animal não encontrado.")

    def simular_alimentacao(self):
        for animal in self.animais:
            print(animal.alimentar())


def menu():
    zoo = Zoo()

    zoo.adicionar_animal(Mamifero("Leão", 6, "Rugido", "Caminhar/Quadrúpede", "Carnívoro", "Savana", "12:00"))
    zoo.adicionar_animal(Ave("Águia", 4, "Grasnar", "Voar/Bípede", "Carnívoro", "Montanhas", "13:00"))
    zoo.adicionar_animal(Reptil("Cobra", 3, "Nenhum", "Rastejar", "Carnívoro", "Planícies/Florestas", "14:00"))
    zoo.adicionar_animal(Mamifero("Elefante", 10, "Bramido", "Caminhar/Quadrúpede", "Herbívoro", "Savana/Florestas", "15:00"))
    zoo.adicionar_animal(Ave("Coruja", 5, "Piar", "Voar/Bípede", "Carnívoro", "Cerrados/Florestas", "21:00"))
    zoo.adicionar_animal(Reptil("Tartaruga", 15, "Grunhido", "Caminhar/Nadar/Quadrúpede", "Onívoro", "Rios/Lagos/Zonas Áridas", "12:00"))

    while True:
        print("\nMenu:")
        print("1. Listar Animais")
        print("2. Buscar Animal")
        print("3. Listar Animais por Categoria")
        print("4. Listar Vizinhos de um Animal")
        print("5. Simular Alimentação")
        print("6. Sair")

        escolha = input("Escolha a operação (1/2/3/4/5/6): ")

        if escolha == '1':
            zoo.listar_animais()

        elif escolha == '2':
            nome = input("Busque por algum animal: ")
            zoo.buscar_animal(nome)

        elif escolha == '3':
            categoria_animal = input("Escolha uma categoria (Mamífero/Ave/Reptil): ")
            categorias = {
                'Mamifero': Mamifero, 'Ave': Ave, 'Reptil': Reptil
            }
            categoria = categorias.get(categoria_animal)
            if categoria:
                zoo.listar_categorias(categoria)
            else:
                print("Categoria não existe!")

        elif escolha == '4':
            nome = input("Digite o nome do animal: ")
            zoo.listar_vizinhos(nome)

        elif escolha == '5':
            zoo.simular_alimentacao()

        elif escolha == '6':
            exit()

        else:
            print("Escolha inválida, tente outra opção!")

if __name__ == "__main__":
    menu()
