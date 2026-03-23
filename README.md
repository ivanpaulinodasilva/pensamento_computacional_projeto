# 🍧 Sistema de Pedidos de Açaí (CRUD em Python)

Este projeto é um sistema simples de linha de comando desenvolvido em **Python**, que simula um aplicativo de pedidos de açaí.
O sistema permite criar, visualizar, atualizar e cancelar pedidos (CRUD), utilizando estruturas básicas da linguagem.

---

## 🚀 Funcionalidades

O sistema possui um menu interativo com as seguintes opções:

### 🟢 1. Fazer Pedido (CREATE)

* Cadastro de cliente
* Escolha do tamanho do açaí:

  * 300ml
  * 500ml
  * 1 Litro
* Adição de complemento
* Escolha da forma de pagamento
* Registro do endereço de entrega

---

### 📋 2. Listar Pedidos (READ)

* Exibe todos os pedidos realizados
* Mostra índice, nome, tamanho, complemento, pagamento e endereço

---

### 🔄 3. Mudar Pedido (UPDATE)

* Permite alterar informações de um pedido existente
* Atualização feita através do índice do pedido

---

### ❌ 4. Cancelar Pedido (DELETE)

* Remove um pedido da lista
* Cancelamento baseado no número do pedido

---

## 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido utilizando apenas Python puro:

* **Listas (`list`)** → Armazenamento dos pedidos
* **Dicionários (`dict`)** → Estrutura dos dados de cada pedido
* **Laços de repetição (`while`)** → Menu contínuo
* **Condicionais (`if/elif/else`)** → Controle de fluxo

---

## 📂 Estrutura do Pedido

Cada pedido é armazenado no seguinte formato:

```python
{
    "nome": "Cliente",
    "tamanho": "500ml",
    "complemento": "Nutella",
    "pagamento": "Pix",
    "endereco": "Rua Exemplo, 123"
}
```

---

## ▶️ Como Executar

### Pré-requisitos

* Python 3.x instalado

### Passos

1. Baixe o arquivo do projeto:

   ```
   projeto_acai.py
   ```

2. Abra o terminal na pasta do arquivo

3. Execute o comando:

```bash
python projeto_acai.py
```

---

## 💡 Exemplo de Uso

```
=== SITE AÇAI ===
1. Fazer Pedido
2. Listar Pedidos
3. Mudar Pedido
4. Cancelar Pedido
0. Sair
```

---

## 🔥 Melhorias Futuras

Este projeto pode ser expandido com:

* 💰 Cálculo automático do valor total
* 📊 Relatório de vendas
* 💾 Salvamento em arquivo (JSON)
* 🧾 Geração de recibos
* 🎨 Interface gráfica (Tkinter)
* 🌐 Versão web (estilo iFood)

---

## 👨‍💻 Autor

Projeto desenvolvido para fins de estudo de lógica de programação e estruturas de dados em Python.

---

## 📄 Licença

Este projeto é livre para uso e modificação para fins educacionais.
