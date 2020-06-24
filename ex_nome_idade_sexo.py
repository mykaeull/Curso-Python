#ERRO NA CONDIÇÃO DA VARIÁVEL IDADE_MAIS_VELHA
cont = 3
soma_idade = 0
m_menores_20 = 0
for c in range(1, cont+1):
    nome = str(input("NOME DA {}ª PESSOA: ".format(c)))
    idade = int(input("IDADE DA {}ª PESSOA: ".format(c)))
    sexo = str(input("SEXO DA {}ª PESSOA[M/F]: ".format(c)))
    soma_idade = soma_idade + idade
    if c ==1:
        idade_mais_velha = idade
    else:
        if idade > idade_mais_velha and sexo == "M":
            idade_mais_velha = idade
            h_mais_velho = nome
        if sexo == "F" and idade < 20:
            m_menores_20 = m_menores_20 + 1
media_idade = soma_idade / 3
print("A MÉDIA DE IDADE DO GRUPO É:{}".format(media_idade))
print("HOMEM MAIS VELHO SE CHAMA {} E TEM {} ANOS.".format(h_mais_velho, idade_mais_velha))
print("{} MULHERES TEM MENOS DE 20 ANOS.".format(m_menores_20))
