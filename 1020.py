""" 1020 - Idade em dias | Bernardo Soares  | Fabrica de Software """

ANO = 365
MES = 30

def entrada():
    idade = int(input())
    return idade

def calculo(idade):
    ano = (idade / ANO)
    mes = ((idade % ANO) / MES)
    dias = ((idade % ANO) % MES)
    return ano, mes, dias

def main():
    idade = entrada()
    ano, mes, dias= calculo(idade)
    print(f'{int(ano)} ano(s)')
    print(f'{int(mes)} mes(es)')
    print(f'{int(dias)} dia(s)')

main()