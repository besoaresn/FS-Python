LITROS = 12

def entrada():
    tempo = int(input())
    vel = int(input())
    return tempo, vel

def calculo(tempo, vel):
    km = ( tempo * vel )
    litros = ( km / LITROS )
    return litros

def main():
    tempo, vel = entrada()
    resultado = calculo(tempo, vel)
    print(f'{resultado:.3f}')

main()