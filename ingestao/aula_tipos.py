# Uma variável é um nome que aponta para um valor.
nome = "Banco Alfa"         # str: texto, sempre entre aspas
reclamacoes = 1240          # int: número inteiro
taxa_mes = 7.85             # float: juro do cheque especial, em % ao mês
e_fintech = False           # bool: verdadeiro ou falso

# type() mostra o tipo de um valor
print(type(nome), type(reclamacoes), type(taxa_mes), type(e_fintech))

# f-string: texto com valores dentro de chaves
print(f"{nome}: {taxa_mes}% ao mês, {reclamacoes} reclamações.")

# Juros compostos: quanto 7,85% ao mês vira em um ano?
taxa_ano = ((1 + taxa_mes / 100) ** 12 - 1) * 100
print(f"Equivale a {taxa_ano:.2f}% ao ano.")

# Conversão de tipos: APIs brasileiras às vezes mandam número como texto com vírgula
taxa_texto = "7,85"
taxa = float(taxa_texto.replace(",", "."))
print(taxa + 1)

print(float("7,85"))