def calcular_salario_atual(salario_inicial, ano_contratacao, ano_atual):
    # Definir o percentual de aumento em 1996
    percentual_aumento = 1.5 / 100
    
    salario_atual = salario_inicial
    
    for ano in range(ano_contratacao + 1, ano_atual + 1):
        # O aumento de 1996 é fixo em 1,5%
        if ano == 1996:
            salario_atual += salario_inicial * percentual_aumento
        # A partir de 1997, o percentual dobra a cada ano
        else:
            percentual_aumento *= 2
            salario_atual += salario_inicial * percentual_aumento

    return salario_atual


# Solicitar o salário inicial e os anos ao usuário
salario_inicial = float(input("Digite o salário inicial do funcionário: "))
ano_contratacao = 1995
ano_atual = int(input("Digite o ano atual: "))

salario_atual = calcular_salario_atual(salario_inicial, ano_contratacao, ano_atual)
print(f"O salário atual do funcionário em {ano_atual} é: R$ {salario_atual:.2f}")
