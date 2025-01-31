# 🥞 **Projeto Prático - Torre de Panquecas**

---

Seu restaurante favorito tem sempre vários pratos ambiciosos no cardápio. Um dos pratos mais famosos no **café da manhã** é a **torre de panquecas**. 🥞

Esse prato é composto por uma pilha de panquecas de vários tamanhos, e um grande desafio no preparo é empilhá-las com uma **espátula** de forma a garantir que a torre fique **estável**. 

Como você sabe programar, o restaurante pediu sua ajuda para desenvolver um programa que, dados os **movimentos feitos com a espátula** para empilhar as panquecas, determina se a torre de panquecas final é estável.

---

## 🏰 **Como Funciona a Torre de Panquecas?**

- Uma torre de panquecas será representada por uma **lista de inteiros**, onde cada inteiro indica o **diâmetro** de uma panqueca. As panquecas são representadas de **cima para baixo**.
  - Ou seja, o **primeiro inteiro** representa o diâmetro da panqueca no topo da torre, o **segundo inteiro** representa a panqueca abaixo dela, e assim por diante.

### 🔧 **Movimento de Espátula**

- Um **movimento de espátula**, representado por um número **M**, consiste em virar as **M primeiras panquecas** da torre.
  - Exemplo: 
    - Torre inicial: `[7, 5, 3, 7]`
    - Movimento de espátula 3: `[3, 5, 7, 7]`

---

## 💡 **Condição de Estabilidade**

- Uma torre de panquecas é **considerada estável** se a lista correspondente estiver **ordenada em ordem crescente**. Ou seja, cada panqueca é **menor ou igual** a todas as panquecas abaixo dela.

---

## 📝 **Entrada do Programa**

- O programa deve receber uma linha composta por **vários inteiros**, representando a pilha de panquecas.
- Em seguida, o programa deve receber várias linhas com **inteiros**, representando os **movimentos de espátula**.
- Uma linha com o **inteiro 0** indica o fim da sequência de movimentos.

---

## 🖥️ **Saída Esperada**

- O programa deve imprimir:
  - **"Torre estável"** se a torre de panquecas for estável após a aplicação dos movimentos.
  - **"Torre instável"** caso contrário.
