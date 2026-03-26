# 🎲 Código da Transformação - EAD 🐍☁️💻
Nosso primeiro repositório do Código da Transformação.

---

## 🏗️ Panorama Geral: O Sistema de Pedidos

Independentemente de ser uma Hamburgueria ou um Açaí, o programa precisa seguir esta lógica:

1.  **Exibir um Menu:** Mostrar ao cliente o que está disponível.
2.  **Receber a Escolha:** O usuário digita o que deseja.
3.  **Processar o Pagamento:** Calcular o total e informar ao usuário.

### 🛠️ O que vamos usar?

* **Variáveis:** Para guardar os nomes e preços.
* **Print:** Para exibir informações na tela.
* **Input:** Para o usuário interagir com o código.
* **Condicionais (if/else):** Para decidir o que o programa faz baseando-se na escolha do cliente.

---

## 👥 Participantes Organizados

### 🌅 Manhã (Segunda e Terça)
* | Anthony Bezerra | Beatriz Borges | C. Adriano | Cauã José | Diego Farias | Gabriel Lima
* | Gabriele Campos | Henrique Souza | Juan Pablo | Laís Renata | Luan Seiji | Marcos Nobre
* | Maria Matos | Pedro Henrique | Rafael Araújo | Rychard Rodrigues | Samuel Paiva
* | Vinicius Batista

### 🌆 Tarde (Segunda e Terça)
* | Alicya Duarte | Allan Costa | Ana Nascimento | Claudomiro Santos | Davi Lima | Fellipe Lima
* | Gustavo Jesus | Igor Batista | João Teles | Julio Ilidio | Lana Reis | Larissa Silva
* | Leandro Xavier | Lorenzo Carmo | Luis Gentil | Luiz Silva | Miguel Alves | Milena Oliveira
* | Nicolly Gonçalves | Paulo Nascimento | Richard Pimenta | Thalya Alcantara | Thierry Duarte
* | Yuri Santana

---

## 📂 Projetos por Tema

### 🍔 Hamburgueria / Burguer
* **Grupos:**
* | Marcos Nobre, Samuel Paiva, Diego Farias
* | Gabriel Lima, Gabriele Campos, Maria Matos, Vinicius Batista
* | Gabriela Leite, Henrique Souza, Laís Renata, Rychard Rodrigues
* | Beatriz Oliveira, Clara, João, Maria Ferreira
* | Claudomiro Santos, Richard Pimenta | Julio Ilidio, Miguel Alves.

### 🍧 Açaí
* **Grupos:**
* | Anthony Bezerra, C. Adriano, Luan Seiji
* | Cauã José, Juan Pablo, Pedro Henrique
* | Guilherme Firmino, Gustavo Rodrigues, Leonardo Santana, Wilson
* | Lorenzo Carmo, Luis Gentil, Maxuel Xavier.

### 🥖 Padaria
* **Grupos:**
* | Kauã, Miguel Marcondes | Fellipe Lima, Gustavo Jesus, Juliana Lima, Lana Reis.

### 🍽️ Restaurante
* **Grupo:**
* | Alicya Duarte, Ana Nascimento, Larissa Silva, Nicolly Gonçalves, Thalya Alcantara, Thierry Duarte.

### ✂️ Barbearia
* **Grupo:**
* | Allan Costa, Igor Batista, Milena Oliveira, Yuri Santana.

### 💄 Salão de Beleza
* **Grupo:**
* | Michelle Andrade, Rafaela, Stefani Santos.

---

## 💻 Exemplos de Código (Python)

Abaixo, temos três níveis de complexidade para os sistemas.

### 1️⃣ Exemplo Básico: Pedido Único
Focado em variáveis e exibição simples.

```python
# Objetivo: Registrar o pedido de um cliente e exibir o valor total.
print("--- Bem-vindo à Nossa Hamburgueria! ---")

# 1. Definição do Menu
hamburguer_simples = 15.00
hamburguer_duplo = 25.00
refrigerante = 7.00

# 2. Exibição das opções
print("Cardápio:")
print(f"1. Hambúrguer Simples - R$ {hamburguer_simples}")
print(f"2. Hambúrguer Duplo - R$ {hamburguer_duplo}")
print(f"3. Refrigerante - R$ {refrigerante}")

# 3. Entrada de dados
escolha = input("\nDigite o número do item que deseja pedir: ")

# 4. Processamento do Pedido
if escolha == "1":
    print(f"Você escolheu o Simples. Total: R$ {hamburguer_simples}")
elif escolha == "2":
    print(f"Você escolheu o Duplo. Total: R$ {hamburguer_duplo}")
elif escolha == "3":
    print(f"Você escolheu o Refrigerante. Total: R$ {refrigerante}")
else:
    print("Opção inválida.")
```

### 2️⃣ Exemplo Intermediário: Atendimento Personalizado
Focado em interação amigável e boas-vindas.

```python
# Objetivo: Simular a recepção de um cliente com F-Strings.
nome_cliente = input("Olá! Qual é o seu name? ")

print("\n" + "="*30)
print(f"BEM-VINDO(A) À VOCA-BURGER, {nome_cliente.upper()}!")
print("="*30)

print("Confira nossas opções:")
print("1 - Combo Clássico ..... R$ 25.00")
print("2 - Combo Duplo ........ R$ 35.00")
print("3 - Batata Suprema ..... R$ 15.00")
print("4 - Sair")

opcao = input("\nO que você deseja pedir? ")

if opcao == "1":
    print(f"\nÓtima escolha, {nome_cliente}! Preparando seu Combo.")
elif opcao == "4":
    print(f"\nAté logo, {nome_cliente}!")
else:
    print("\nOpção processada com sucesso.")
```

### 3️⃣ Exemplo Avançado: Carrinho de Compras (Loop While)
Este código permite selecionar múltiplos itens e soma o total automaticamente.

```python
# Objetivo: Permitir múltiplos pedidos e somar o total.
# Conceitos: While (Loop), Acumuladores e Operadores Matemáticos.

nome_cliente = input("Qual o seu nome? ")
total_conta = 0.0  
continuar = True   

print(f"\nOlá {nome_cliente}! Monte seu pedido (Digite 0 para finalizar):")

while continuar:
    print("\n--- MENU SEJA SUA VOCAÇÃO ---")
    print("1. Item A (Hambúrguer/Açaí/Corte) - R$ 20.00")
    print("2. Item B (Batata/Adicional/Barba) - R$ 10.00")
    print("3. Item C (Bebida/Suco/Sobrancelha) - R$ 7.00")
    print("0. FINALIZAR PEDIDO")
    
    escolha = input("\nEscolha o número do item: ")

    if escolha == "1":
        total_conta += 20.00
        print("Item adicionado!")
    elif escolha == "2":
        total_conta += 10.00
        print("Item adicionado!")
    elif escolha == "3":
        total_conta += 7.00
        print("Item adicionado!")
    elif escolha == "0":
        continuar = False 
    else:
        print("Opção inválida!")

print("\n" + "="*30)
print(f"RESUMO DO PEDIDO - CLIENTE: {nome_cliente}")
print(f"TOTAL A PAGAR: R$ {total_conta:.2f}")
print("Obrigado e volte sempre!")
print("="*30)
```

---

## 📚 Método Educativo: Estrutura de Dados
Na programação, o que acabamos de fazer foi transformar uma **Lista Desordenada** em uma **Lista Estruturada**.

* **Agrupamento:** Em linguagens como Python, poderíamos usar um **Dicionário**
* para salvar esses dados, onde a "Chave" é o **Tema** e o "Valor" é a **Lista de Alunos**.
* **Markdown:** É a linguagem que estamos usando para formatar este texto.
* Ela é essencial para programadores documentarem seus projetos no GitHub de forma clara e profissional.

### 📖 O que aprendemos com os códigos?
1.  **Variáveis Acumuladoras:** A `total_conta` guarda a soma dos valores usando o operador `+=`.
2.  **O Laço `while`:** Cria uma repetição que só para quando a variável `continuar` vira `False`.
3.  **Boas Práticas de UX:** Feedback imediato e formatação de moeda (`:.2f`).

