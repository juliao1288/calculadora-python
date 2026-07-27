#Calculadora em Python

def main():

    d = 0

    while d != "5":
        print()
        print()

        print(" -- CALCULADORA -- " +
            "\n 1) SOMA " +
            "\n 2) SUBTRAÇÃO " +
            "\n 3) MULTIPLICAÇÃO " +
            "\n 4) DIVISÃO " +
            "\n 5) SAIR ")

        print()
        d = input(" Insira o valor desejado: ")

        match d:

            case "1":

                while True:
                    try:
                        a = float(input(" Insira um número para realizar a soma: "))
                        b = float(input(" Insira um outro número para realizar a soma: "))
                        break
                    except ValueError:
                        print(" Valores incorretos, tente novamente.\n")

                resultado = soma(a,b)
                print(f" {a} + {b} = {resultado}")

            case "2":
                while True:
                    try:
                        a = float(input(" Insira um número para realizar a subtração: "))
                        b = float(input(" Insira um outro número para realizar a subtração: "))
                        break
                    except ValueError:
                        print(" Valores incorretos, tente novamente.\n")

                resultado = subtração(a,b)
                print(f" {a} - {b} = {resultado}")

            case "3":

                while True:
                    try:
                        a = float(input(" Insira um número para realizar a subtração: "))
                        b = float(input(" Insira um outro número para realizar a subtração: "))
                        break
                    except ValueError:
                        print(" Valores incorretos, tente novamente.\n")

                resultado = multiplicao(a,b)
                print(f" {a} X {b} = {resultado}")

            case "4":
                while True:
                    try:
                        a = float(input(" Insira um número para realizar a divisão: "))
                        b = float(input(" Insira um outro número para realizar a divisão: "))
                        break
                    except ValueError:
                        print(" Valores incorretos, tente novamente.\n")
                
                resultado = divisao(a,b)

                if resultado:
                    print(f" {a} : {b} = {resultado}")

                else:
                    print(" Operação cancelada, divisão por 0.")


            case "5":
                print(" Você escolheu por sair...")
                print()

            case _:
                print(" Valor inválido, tente novamente.")
                print(" Tente novamente...")
                print()

                      
                





def soma(a: float, b: float) -> float:
    """
    Esta função recebe 2 números qualquer e realiza a soma entre eles.
    
    Args:
        a (float) = Número qualquer que o usuário inseriu.
        b (float) = Outro número qualquer que o usuário inseriu.
        
    Returns:
        resultado (float) = Soma entre os 2 números que o usuário inseriu.
    
    """
    resultado = a + b

    return resultado

def subtração(a: float, b: float) -> float:
    """
    Esta função recebe 2 números qualquer e realiza a subtração entre eles.
    
    Args:
        a (float) = Número qualquer que o usuário inseriu.
        b (float) = Outro número qualquer que o usuário inseriu.
        
    Returns:
        resultado (float) = Subtração entre os 2 números que o usuário inseriu.
    
    """
    resultado = a - b

    return resultado

def multiplicao(a: float, b: float) -> float:
    """
    Esta função recebe 2 números quaisquer e realiza a multiplicação entre eles.
    
    Args:
        a (float) = Número qualquer que o usuário inseriu.
        b (float) = Outro número qualquer que o usuário inseriu.
    
    Returns:
        resultado (float) = Multiplicação entre os 2 números que o usuário inseriu.
    
    """
    resultado = a * b

    return resultado

def divisao(a: float, b: float) -> float:
    """ 
    Esta função recebe 2 números quaisquer e realiza a divisão entre eles. 
    Caso b seja igual a 0, cancela a operação e mostra uma mensagem na tela.
        
    Args:
        a (float) = Número qualquer que o usuário inseriu.
        b (float) = Outro número qualquer que o usuário inseriu.
        
    Returns:
        resultado (float) = Multiplicação entre os 2 números que o usuário inseriu.
    
    """

    if (b != 0):
        resultado = a / b
        return resultado
    else:
        return None
   



if __name__ == "__main__":
    main()
