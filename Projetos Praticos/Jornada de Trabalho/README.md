# 🧑‍💻 **Projeto Prático - Jornada de Trabalho**

---

Nos últimos anos, cada vez mais companhias têm adotado o modelo de **trabalho remoto**. Essa tendência se intensificou a partir de 2020 com as adequações necessárias durante a pandemia. Nesse modelo, os funcionários podem trabalhar de suas casas sem a necessidade de estar presencialmente no escritório da empresa onde trabalham. 💻🏠

Embora o trabalho remoto apresente várias vantagens, ele também traz alguns desafios. Um desses desafios é determinar o **tempo dedicado ao trabalho** de cada funcionário. Para lidar com esse problema, você foi escolhido(a) para desenvolver um programa que registre o tempo trabalhado por um funcionário e o valor que ele deve receber de acordo com esse tempo. 💼

## 📋 **Objetivo**

Seu programa deverá processar os **registros de tempo** para uma semana de trabalho. A entrada será composta por:

1. O valor da **hora de trabalho**;
2. O número de **dias trabalhados** (de 0 a 7);
3. Vários registros de **períodos de trabalho** durante os dias trabalhados.

## 📝 **Formato de Entrada**

- A primeira linha: um **inteiro V**, indicando o valor da hora de trabalho.
- A segunda linha: um **inteiro D** entre 0 e 7, indicando quantos dias o funcionário trabalhou na semana.
- Para cada um dos **D dias**, haverá:
  - Uma linha contendo o **número de períodos de trabalho registrados** no dia.
  - Em seguida, para cada período de trabalho, serão dadas **duas linhas**, uma com a **hora de início** e outra com a **hora de fim**.

---

## 📊 **Método de Cálculo do Valor**

1. **Calcule o tempo trabalhado** por dia:
   - Se o funcionário trabalhou **mais de 8 horas** em um dia, as horas excedentes serão consideradas **hora extra**.
   
2. **Horas extras**:
   - Se o funcionário trabalhou mais de **44 horas na semana**, as horas excedentes serão contadas como **hora extra**.

3. **Valor devido**:
   - O valor será calculado multiplicando o número total de **horas trabalhadas** pelo valor da hora de trabalho (`V`).
   - As **horas extras** terão **50% a mais** no valor da hora (acréscimo de `V/2`).

4. **Desconto**:
   - Se houver algum desconto, o valor devido será **sempre R$ 1,00**.

---

### 💰 **Exemplo de Cálculo**

- Se um funcionário trabalhou **55 horas** na semana, sendo que **5 horas** excederam as 8 horas diárias, o cálculo seria:

(V * 55) + (V/2 * 5) + (V/2 * 6) = (V * 55) + (V/2 * 11)


---

## 📤 **Saída Esperada**

O programa deve imprimir os seguintes resultados:

- `"Horas trabalhadas: X"`
- `"Horas extras: X"`
- `"Valor devido: R$ XX.XX"`

**Atenção**: O valor em Real deve ser separado por ponto (não vírgula) e exibido com **duas casas decimais**.

