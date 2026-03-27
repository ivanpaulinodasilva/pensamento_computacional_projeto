
# 🎲 Pensamento Computacional - Projeto 🐍☁️💻
Nosso primeiro repositório oficial do Código da Transformação. Um espaço para aprender, praticar e documentar o desenvolvimento de sistemas reais em Python.

---

## 💇‍♂️ Projeto em Destaque: Sistema de Gerenciamento - Salão de Beleza

Este projeto foi desenvolvido para facilitar a gestão de um salão ou barbearia, utilizando estruturas de dados para organizar o fluxo de trabalho.

### 🚀 Funcionalidades Principais
1. **Fila de Espera (FIFO):** Registro de clientes por ordem de chegada.
2. **Agenda de Atendimento:** Transição da espera para o serviço confirmado.
3. **Tabela de Preços Dinâmica:** Uso de **Dicionários** para gerir serviços e valores.
4. **Relatório de Variedade:** Uso de **Sets** para identificar serviços únicos prestados.
5. **Painel Administrativo:** Alteração de preços e configurações em tempo real.
6. **Calculadora Integrada:** Cálculos de totais, descontos e acréscimos.

### 🛠️ Tecnologias e Estruturas Utilizadas
* **Listas (`[]`):** Gestão da fila cronológica.
* **Dicionários (`{}`):** Mapeamento de serviços e preços.
* **Sets (`{}`):** Filtro de serviços únicos para relatórios.
* **Laços de Repetição (`while`):** Menu interativo e persistente.
* **Condicionais (`if/elif/else`):** Lógica de tomada de decisão.

---

## 🏗️ Panorama Geral: O Sistema de Pedidos
Independentemente do tema (Hamburgueria, Açaí ou Salão), o programa segue esta lógica fundamental:
1. **Exibir um Menu:** Mostrar ao cliente o que está disponível.
2. **Receber a Escolha:** O usuário digita o que deseja (`input`).
3. **Processar o Pagamento:** Calcular o total e informar ao usuário.

---

## 👥 Participantes Organizados

### 🌅 Manhã (Segunda e Terça)
* | Anthony Bezerra | Beatriz Borges | C. Adriano | Cauã José | Diego Farias | Gabriel Lima |
* | Gabriele Campos | Henrique Souza | Juan Pablo | Laís Renata | Luan Seiji | Marcos Nobre |
* | Maria Matos | Pedro Henrique | Rafael Araújo | Rychard Rodrigues | Samuel Paiva | Vinicius Batista |

### 🌆 Tarde (Segunda e Terça)
* | Alicya Duarte | Allan Costa | Ana Nascimento | Claudomiro Santos | Davi Lima | Fellipe Lima |
* | Gustavo Jesus | Igor Batista | João Teles | Julio Ilidio | Lana Reis | Larissa Silva |
* | Leandro Xavier | Lorenzo Carmo | Luis Gentil | Luiz Silva | Miguel Alves | Milena Oliveira |
* | Nicolly Gonçalves | Paulo Nascimento | Richard Pimenta | Thalya Alcantara | Thierry Duarte | Yuri Santana |

---

## 📂 Projetos por Tema

* **🍔 Hamburgueria:** Marcos, Samuel, Diego | Gabriel L., Gabriele C., Maria M., Vinicius B. | Gabriela L., Henrique S., Laís R., Rychard R. | Beatriz O., Clara, João, Maria F. | Claudomiro S., Richard P. | Julio I., Miguel A.
* **🍧 Açaí:** Anthony, C. Adriano, Luan S. | Cauã, Juan, Pedro H. | Guilherme, Gustavo, Leonardo, Wilson | Lorenzo, Luis, Maxuel.
* **🥖 Padaria:** Kauã, Miguel M. | Fellipe, Gustavo R., Juliana, Lana.
* **🍽️ Restaurante:** Alicya, Ana, Larissa, Nicolly, Thalya, Thierry.
* **✂️ Barbearia:** Allan, Igor, Milena, Yuri.
* **💄 Salão de Beleza:** Michelle, Rafaela, Stefani.

---

## 💻 Exemplos de Código (Python)

Abaixo, os três níveis de complexidade utilizados no aprendizado:

### 1️⃣ Exemplo Básico: Pedido Único
```python
# Objetivo: Registrar o pedido de um cliente e exibir o valor total.
print("--- Bem-vindo à Nossa Hamburgueria! ---")

hamburguer_simples = 15.00
hamburguer_duplo = 25.00
refrigerante = 7.00

print("Cardápio:")
print(f"1. Hambúrguer Simples - R$ {hamburguer_simples}")
print(f"2. Hambúrguer Duplo - R$ {hamburguer_duplo}")
print(f"3. Refrigerante - R$ {refrigerante}")

escolha = input("\nDigite o número do item que deseja pedir: ")

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
```python
# Objetivo: Simular a recepção de um cliente com F-Strings.
nome_cliente = input("Olá! Qual é o seu nome? ")

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
```python
# Objetivo: Permitir múltiplos pedidos e somar o total.
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
* **Dicionários e Listas:** Como organizar nomes e preços de forma profissional.
* **Variáveis Acumuladoras:** Uso do operador `+=` para somar valores progressivamente.
* **Boas Práticas de UX:** Feedback visual e formatação de moeda (`:.2f`).
