num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
while True:

    print()
    print('1. A soma deles')
    print()
    print('2. A multiplicação deles ')
    print()
    print('3. A divisão inteira deles')
    print()
    print('4. O maior valor')
    print()
    print('5. A soma deles é par ou impar')
    print()
    print('6. se a multiplicação passar de 40 mostre a divisão inteira deste produto')
    print()
    comando = input('Digite o numero referente ao que deseja: ')

    if comando == '1':
        print('A soma deles é ', num1 + num2)
        continue
    if comando == '2':
        print('A multiplicação deles é', num1 * num2)
        continue
    if comando == '3':
        print('A divisão inteira deles é ', num1 // num2)
        continue
    if comando == '4':
        if num1 > num2:
            print(num1, ' É maior que ', num2)
            continue
        if num2 > num1:
            print(num2, ' É maior que ', num1)
            continue
        if num2 == num1:
            print('Os numeros são iguais')
            continue
    if comando == '5':
        if (num1 + num2) % 2 == 0:
            print('A soma de ', num1, ' + ', num2, 'resulta em um numero par')
            continue
        if (num1 + num2) % 2 != 0:
            print('A soma de ', num1, ' + ', num2,
                  'resulta em um numero impar')
            continue
    if comando == '6':
        if num1 * num2 > 40 and num1 // num2 != 0:
            print((num1 * num2) // (num1 // num2))
            continue
        if num1 * num2 > 40 and num1 // num2 == 0:
            print(
                'A divisão destes numeros interiramente resulta em 0, numeros invalidos')
        if num1 * num2 <= 40:
            print('A multiplicação não é maior que 40')
            continue
