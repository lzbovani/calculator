def calculator():
    print("Calculadora Simples")
    print("Operações disponíveis:")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    
    while True:
        try:
            # Obtém a operação desejada
            operacao = input("\nEscolha a operação (1-4) ou 'sair' para encerrar: ")
            
            if operacao.lower() == 'sair':
                print("Obrigado por usar a calculadora!")
                break
                
            if operacao not in ['1', '2', '3', '4']:
                print("Operação inválida! Por favor, escolha uma operação válida.")
                continue
            
            # Obtém os números
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            # Realiza a operação
            if operacao == '1':
                resultado = num1 + num2
                print(f"\n{num1} + {num2} = {resultado}")
            elif operacao == '2':
                resultado = num1 - num2
                print(f"\n{num1} - {num2} = {resultado}")
            elif operacao == '3':
                resultado = num1 * num2
                print(f"\n{num1} * {num2} = {resultado}")
            elif operacao == '4':
                if num2 == 0:
                    print("\nErro: Divisão por zero não é permitida!")
                    continue
                resultado = num1 / num2
                print(f"\n{num1} / {num2} = {resultado}")
                
        except ValueError:
            print("\nErro: Por favor, digite números válidos!")
        except Exception as e:
            print(f"\nOcorreu um erro: {e}")

if __name__ == "__main__":
    calculator()