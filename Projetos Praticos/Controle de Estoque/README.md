# 🚀 **Projeto Prático - Controle de Estoque**

---

Você foi contratado por uma rede de lojas para criar um **programa de controle de estoque** para um produto de grande procura. 🛒

## 📋 **Objetivo**

O objetivo do programa é **receber uma sequência de pedidos** para um produto durante o dia. Esses pedidos podem ser de **compra de unidades** para reposição ou de **venda para clientes**, e o programa precisa determinar:

- A **quantidade de vendas realizadas**;
- A **quantidade de produtos em estoque** no final do dia.

---

### 🔄 **Regras do Programa**

1. Ao analisar a sequência de pedidos:
   - **Pedido positivo (+X)**: Compra de **X unidades** para reposição do estoque;
   - **Pedido negativo (-Y)**: Venda de **Y unidades** do produto;
   - **Pedido zero (0)**: **Encerramento da sequência** para o dia.

2. O programa **inicia com o estoque zerado** (0 unidades).

3. Durante o processamento, o pedido só será atendido se **houver unidades suficientes no estoque**. Caso contrário, uma mensagem será emitida informando que o produto está em falta.

4. **Mensagem de falta no estoque** (caso não haja unidades suficientes):
   - _"Quantidade indisponível para a venda de Y unidades."_

---

### 📊 **Resultados Esperados**

Ao final da sequência de pedidos, o programa deve exibir as seguintes mensagens:

- **Quantidade de vendas realizadas**;
- **Quantidade em estoque**.

Exemplo de mensagens:

- `"Quantidade de vendas realizadas: Z"`
- `"Quantidade em estoque: X"`