# Sistema de Gerenciamento de Zoológico (em python)

Este programa é um sistema simples para gerenciar um zoológico. Ele permite a inclusão, visualização e simulação de animais e suas características usando programação orientada a objetos em Python.

## Estrutura do Programa

### Classes

#### `Animal`
A classe base que representa um animal e suas características.

- **Atributos:**
  - `nome`: Nome do animal.
  - `idade`: Idade do animal.
  - `barulho`: Tipo de barulho que o animal faz.
  - `movimento`: Tipo de locomoção do animal.
  - `alimentacao`: Tipo de alimentação do animal.
  - `habitat`: Habitat natural do animal.
  - `vizinhos`: Lista de vizinhos (outros animais que estão próximos).
  - `horas_alimentacao`: Horário em que o animal é alimentado.

- **Métodos:**
  - `adicionar_vizinho(nome_vizinho)`: Adiciona um vizinho à lista (máximo de 2 vizinhos).
  - `detalhes()`: Retorna uma string com todas as informações do animal.
  - `alimentar()`: Retorna uma string simulando que o animal foi alimentado.

#### Mamifero, Ave, Reptil
Subclasses da classe **Animal** que representam categorias de animais (mamíferos, aves e répteis).

#### `Zoo`
Gerencia a lista de animais e fornece métodos para interagir com eles.

- **Atributos:**
  - `animais`: Lista de objetos do tipo `Animal`.

- **Métodos:**
  - `adicionar_animal(animal)`: Adiciona um animal à lista.
  - `listar_animais()`: Exibe o nome de todos os animais no zoológico.
  - `listar_categorias(categoria)`: Lista animais de uma categoria específica.
  - `listar_vizinhos(nome)`: Exibe os vizinhos do animal com o nome fornecido.
  - `buscar_animal(nome)`: Exibe detalhes do animal com o nome fornecido.
  - `simular_alimentacao()`: Simula a alimentação de todos os animais.

### Função Principal

#### `menu()`
Exibe um menu interativo para o usuário escolher entre diferentes operações:

1. **Listar Animais**: Mostra todos os animais no zoológico.
2. **Buscar Animal**: Permite buscar e ver detalhes de um animal pelo nome.
3. **Listar Animais por Categoria**: Lista todos os animais de uma categoria específica (Mamífero, Ave ou Réptil).
4. **Listar Vizinhos de um Animal**: Exibe quais animais são vizinhos do animal especificado.
5. **Simular Alimentação**: Simula a alimentação de todos os animais.
6. **Sair**: Encerra o programa.

## Exemplo de Uso

Ao executar o programa, o usuário verá um menu e pode escolher uma opção digitando o número correspondente. Por exemplo:

