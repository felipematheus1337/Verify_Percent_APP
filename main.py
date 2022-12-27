def main():
    def generate_percentage_choosed(value, prcnt_up, prcnt_dw):
        percent_up_choose = value + (value * prcnt_up / 100)
        percent_down_choose = value - (value * prcnt_dw / 100)

        print(f'Com a porcentagem escolhida para acréscimo: {percent_up_choose}')
        print()
        print(f'Com a porcentagem escolhida para decréscimo: {percent_down_choose}')
        print()
        generate_common_up_percentages(value)
        print()
        generate_common_dw_percentages(value)

    def generate_common_up_percentages(val):
        percents = {
            '75%': str(val + (val * 75 / 100)),
            '85%': str(val + (val * 85 / 100)),
            '65%': str(val + (val * 65 / 100)),
            '55%': str(val + (val * 55 / 100)),
            '45%': str(val + (val * 45 / 100)),
            '35%': str(val + (val * 35 / 100)),
            '30%': str(val + (val * 30 / 100)),
            '20%': str(val + (val * 20 / 100)),
        }
        print()
        print("Valores com acréscimos comuns de porcentagem...")
        for percentage in percents:
            print(f' Com o acréscimo de: {percentage} o valor vai para {percents[percentage]}')


    def generate_common_dw_percentages(val):
        percents = {
            '75%': str(val - (val * 75 / 100)),
            '85%': str(val - (val * 85 / 100)),
            '65%': str(val - (val * 65 / 100)),
            '55%': str(val - (val * 55 / 100)),
            '45%': str(val - (val * 45 / 100)),
            '35%': str(val - (val * 35 / 100)),
            '30%': str(val - (val * 30 / 100)),
            '20%': str(val - (val * 20 / 100)),
        }
        print()
        print("Valores com decréscimos comuns de porcentagem...")
        for percentage in percents:
            print(f' Com o decréscimo de: {percentage} o valor vai para {percents[percentage]}')

    print("Bem-vindo ao Verify Percentage Program, verificaremos a porcentagem baseado no valor a vista")
    produto = input("Digite o nome do produto:  ")
    valor = int(input("Digite o valor ['A vista'] :  "))
    percent_up = int(input("Digite uma porcentagem específica para acréscimo"))
    percent_down = int(input("Digite uma porcentagem específica para decréscimo"))
    generate_percentage_choosed(valor, percent_up, percent_down)


if __name__: '__main__'
main()
