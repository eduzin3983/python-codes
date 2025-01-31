# 🎬 **Projeto Prático - Ingresso de Cinema**

---

Você foi contratado por uma rede de **cinemas da região** e, como primeira atividade no novo emprego, seu chefe pediu que você desenvolvesse um programa para calcular o valor do ingresso de cinema. 🎥

## 📋 **Objetivo**

O programa deve, a partir das informações fornecidas, calcular o valor do ingresso com base no **dia da semana**, **horário da sessão**, se o cliente é **estudante** e o **método de pagamento**.

### 🧾 **Detalhes Importantes:**

- O **preço do ingresso** varia conforme o **dia da semana** e o **período da sessão** (tarde ou noite). Sessões a partir das **18h30** são consideradas **noturnas**, enquanto as anteriores são **vespertinas**.
- O programa também deve considerar o **desconto no cartão de crédito** e, se o cliente for estudante, ele pagará **meia entrada** (50% do valor do ingresso, sem acumular com descontos de cartão de crédito).

---

## 📊 **Tabelas de Preços e Descontos**

### 💵 **Tabela de Preços**

| Dia da semana   | Preço vespertino | Preço noturno |
|-----------------|------------------|---------------|
| Domingo         | R$ 30,00         | R$ 30,00      |
| Segunda-feira   | R$ 15,00         | R$ 20,00      |
| Terça-feira     | R$ 15,00         | R$ 20,00      |
| Quarta-feira    | R$ 15,00         | R$ 30,00      |
| Quinta-feira    | R$ 20,00         | R$ 30,00      |
| Sexta-feira     | R$ 20,00         | R$ 40,00      |
| Sábado          | R$ 30,00         | R$ 40,00      |

---

### 💳 **Tabela de Descontos com Cartão de Crédito**

| Dia da semana   | Desconto vespertino | Desconto noturno |
|-----------------|---------------------|------------------|
| Domingo         | 30%                 | 30%              |
| Segunda-feira   | 50%                 | 50%              |
| Terça-feira     | 50%                 | 50%              |
| Quarta-feira    | 50%                 | 50%              |
| Quinta-feira    | 50%                 | 50%              |
| Sexta-feira     | 50%                 | 30%              |
| Sábado          | 20%                 | 20%              |

---

### 🎓 **Benefício para Estudantes**

Caso o cliente seja **estudante**, ele terá direito ao **desconto de meia entrada**, ou seja, **50% do valor do ingresso** integral, sem considerar descontos adicionais por pagamento com cartão de crédito.

---

### 📅 **Representação dos Dias da Semana**

- Domingo: **1**
- Segunda-feira: **2**
- Terça-feira: **3**
- Quarta-feira: **4**
- Quinta-feira: **5**
- Sexta-feira: **6**
- Sábado: **7**

---

## 🧑‍💻 **Entrada do Programa**

A entrada do seu programa será composta por **cinco linhas**:

1. Número representando o **dia da semana** (1 a 7).
2. **Hora de início da sessão**.
3. **Minuto de início da sessão**.
4. **Caractere** indicando se o cliente é estudante:
   - `S` para estudante;
   - `N` para não estudante.
5. **Caractere** indicando o método de pagamento:
   - `D` para **dinheiro**;
   - `C` para **cartão de crédito**.

---

## 🧾 **Saída Esperada**

O programa deve imprimir o valor do ingresso. Para facilitar a impressão, utilize a seguinte linha:

```python
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))

Onde a variável ingresso armazenará o valor final do ingresso. Caso deseje, você pode alterar o nome dessa variável.