def Soma(n, x):
    y = n + x;
    return y;

def Divisao(n, x):
    y = n / x;
    return y;

def Multiplicacao(n, x):
    y = n * x;
    return y;

def Subtracao(n, x):
    y = n - x;
    return y;

def main():

    n = float(input("Digite um número: "));
    x = float(input("Digite mais um número: "));
    g = int(input("Digite uma operação: \n\t1-soma\n\t2-subtração\n\t3-divisão\n\t4-multiplicação "));

    if g == 1:
        z = Soma(n, x);
        print(z);

    if g == 2:
        z = Subtracao(n, x);
        print(z);

    if g == 3:
        z = Divisao(n, x);
        print(z);

    if g == 4:
        z = Multiplicacao(n, x);
        print(z);

    elif g > 4:
        print("Escolha invalida!");
        
    elif g < 1:
        print("Escolha invalida!");

if __name__== "__main__":
    main();
