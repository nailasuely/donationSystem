# Versão do PYTHON: 3.10

# /*******************************************************************************
# Autor: Naila
# Componente Curricular: Algoritmos I
# Concluido em: 09/04/2022
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
# ******************************************************************************************/

# Variáveis para contabilizar a quantidade de itens que irão ser adicionados.
sugar = coffee = oil = rice = extract = pasta = crackers = flour = beans = salt = 0
fisica = juridica = name = 0
cesta = 0
extras = 0
sn = "S"
choice = 1

# Variáveis para adicionar os itens e depois subtrair para ficar apenas os itens que sobraram.
remainder_sugar = remainder_rice = remainder_coffee = remainder_extract = remainder_pasta = 0
remainder_crackers = remainder_oil = remainder_flour = remainder_beans = remainder_salt = 0
remainder_extras = 0

total_itens = 0

# Função simples sem parâmetros, apenas para ser utilizada para formatação.
def title():
    print("-" * 45)
    print("-" * 10, "REGISTRATION OF DONORS", "-" * 11)
    print("-" * 45)


def formatting():
    print("-" * 45)


def finish():
    print("-" * 45)
    print("          REGISTERED INFORMATION              ")
    print("-" * 45)

# Função sem parâmetro para formatar o relatório e disponibilizar o relatório parcial e final posteriormente.
def record():
    print("-" * 45)
    print("-" * 14, "ITENS RECEBIDOS", "-" * 14)
    print("-" * 45)
    print(f"Quantidade de KG de açucar: {sugar}")
    print(f"Quantidade de KG arroz:  {rice}")
    print(f"Quantidade de KG café:   {coffee}")
    print(f"Quantidade de unidades de extrato de tomate: {extract}")
    print(f"Quantidade de unidades macarrão: {pasta}")
    print(f"Quantidade de pacotes de bolachas: {crackers}")
    print(f"Quantidade de L de óleo: {oil}")
    print(f"Quantidade de KG de farinha de trigo: {flour}")
    print(f"Quantidade de KG de feijão: {beans}")
    print(f"Quantidade de KG de sal: {salt}")
    print(f"Quantidade de itens extras: {extras}")
    print("-" * 45)
    print("-" * 4, "ITENS RECEBIDOS POR TIPO DE DOADOR", "-" * 5)
    print("-" * 45)
    print(f"A quantidade de itens recebidos por pessoa física: {fisica}")
    print(f"A quantidade de itens recebidos por pessoa juridica: {juridica}")
    print("-" * 45)
    print("-" * 10, "TOTAL DE ITENS RECEBIDOS", "-" * 9)
    print("-" * 45)
    print(f"A quantidade total de itens é: {total_itens}")
    print("-" * 45)
    print("-" * 12, "QUANTIDADE DE CESTAS", "-" * 11)
    print("-" * 45)
    print(f"A quantidade de cestas básicas é: {cesta}")
    if extras != 0 and extras >= cesta:
        print(f"A quantidade de cestas básicas COM itens extras é: {cesta}")
    elif extras != 0 and extras < cesta:
        print(f"A quantidade de cestas básicas COM itens extras é: {extras}")
    elif extras == 0:
        print(f"A quantidade de cestas básicas COM itens extras é: {extras}")
    if extras < cesta and extras > 0:
        print(f"A quantidade de cestas básicas SEM item extra é: {cesta - extras}")
    elif extras == 0:
        print(f"A quantidade de cestas básicas SEM item extra é: {cesta}")
    elif extras >= cesta:
        print(f"A quantidade de cestas básicas SEM item extra é: 0")
    print("-" * 45)
    print("-" * 12, "ITENS QUE SOBRARAM:", "-" * 12)
    print("-" * 45)
    print(f"KG de açucar: {remainder_sugar}")
    print(f"KG arroz:  {remainder_rice}")
    print(f"KG café:   {remainder_coffee}")
    print(f"Unidades de extrato de tomate: {remainder_extract}")
    print(f"Unidades macarrão: {remainder_pasta}")
    print(f"Pacotes de bolachas: {remainder_crackers}")
    print(f"L de óleo: {remainder_oil}")
    print(f"KG de farinha de trigo: {remainder_flour}")
    print(f"KG de feijão: {remainder_beans}")
    print(f"KG de sal: {remainder_salt}")
    if extras > cesta:
        print(f"Itens extras: {extras - cesta}")
    elif extras == cesta:
        print(f"Itens extras: 0")
    elif extras < cesta:
        print(f"Itens extras: 0")
    print("-" * 45)
    print("\n")

# Estrutura de repetição que contém o primeiro menu.
while choice != 3:
    title()
    print(" \n"
          "    1. Add donor\n"
          "    2. See the registration\n"
          "    3. Exit and see the registration\n"
          "    ")
    formatting()
    # Utilização de Try e except para o tratamento de erros e exceções causados por erros de digitação ou dado inválido.
    try:
        choice = int(input("Enter a  choice: "))
    except ValueError:
        print("ENTER A VALID VALUE!!!")
        continue
    # Utilização de estrutura condicional para verificar o número digitado.
    if choice == 1:
        donor_name = str(input("Enter the name of donor: "))
        # Para não aceitar dígitos digitados no nome do doador.
        while donor_name.isdigit():
            print("ENTER A VALID NAME!!!")
            donor_name = str(input("Enter the name of donor: "))
        donor_type = str(input("Enter donor type: [FIS / JUR] ")).strip().upper()
        while donor_type != "FIS" and donor_type != "JUR":
            print("ENTER A VALID TYPE!!!")
            donor_type = str(input("Enter donor type: [FIS / JUR] ")).strip().upper()
        title()
        sn = "S"
        # Segundo menu com os itens disponíveis para a formação da cesta básica
        while sn in "S":
            print(" \n"
                  "    1. Sugar\n"
                  "    2. Coffee\n"
                  "    3. Oil\n"
                  "    4. Rice\n"
                  "    5. Extract\n"
                  "    6. Pasta\n"
                  "    7. Flour\n"
                  "    8. Beans\n"
                  "    9. Salt\n"
                  "    10. Crackers\n"
                  "    11. Other"
                  "    ")
            formatting()
            try:
                item = int(input("Enter the item: "))
            except ValueError:
                print("\n ENTER A VALID ITEM!!! \n")
                continue
            if item == 1:
                try:
                    quantidade_sugar = int(input("Enter the amount: "))
                    if quantidade_sugar > 0:
                        sugar += quantidade_sugar
                        remainder_sugar += quantidade_sugar
                        total_itens += quantidade_sugar
                        if donor_type == "FIS":
                            fisica += quantidade_sugar
                        elif donor_type == "JUR":
                            juridica += quantidade_sugar
                    while quantidade_sugar < 0:
                        print("ENTER A VALID VALUE!!!")
                        quantidade_sugar = int(input("Enter the amount: "))
                        if quantidade_sugar > 0:
                            sugar += quantidade_sugar
                            remainder_sugar += quantidade_sugar
                            total_itens += quantidade_sugar
                            if donor_type == "FIS":
                                fisica += quantidade_sugar
                            elif donor_type == "JUR":
                                juridica += quantidade_sugar
                except ValueError:
                    print("ENTER A VALID VALUE!!!")
                    continue
            elif item == 2:
                try:
                    quantidade_coffee = int(input("Enter the amount: "))
                    if quantidade_coffee > 0:
                        coffee += quantidade_coffee
                        remainder_coffee += quantidade_coffee
                        total_itens += quantidade_coffee
                        if donor_type == "FIS":
                            fisica += quantidade_coffee
                        elif donor_type == "JUR":
                            juridica += quantidade_coffee
                    while quantidade_coffee < 0:
                        print("ENTER A VALID VALUE!!!")
                        quantidade_coffee = int(input("Enter the amount: "))
                        if quantidade_coffee > 0:
                            coffee += quantidade_coffee
                            remainder_coffee += quantidade_coffee
                            total_itens += quantidade_coffee
                            if donor_type == "FIS":
                                fisica += quantidade_coffee
                            elif donor_type == "JUR":
                                juridica += quantidade_coffee
                except ValueError:
                    print("ENTER A VALID VALUE!!!")
                    continue
            elif item == 3:
                try:
                    quantidade_oil = int(input("Enter the amount: "))
                    if quantidade_oil > 0:
                        oil += quantidade_oil
                        remainder_oil += quantidade_oil
                        total_itens += quantidade_oil
                        if donor_type == "FIS":
                            fisica += quantidade_oil
                        elif donor_type == "JUR":
                            juridica += quantidade_oil
                    while quantidade_oil < 0:
                        print("ENTER A VALID VALUE!!!")
                        quantidade_oil = int(input("Enter the amount: "))
                        if quantidade_oil > 0:
                            oil += quantidade_oil
                            remainder_oil += quantidade_oil
                            total_itens += quantidade_oil
                            if donor_type == "FIS":
                                fisica += quantidade_oil
                            elif donor_type == "JUR":
                                juridica += quantidade_oil
                except ValueError:
                    print("ENTER A VALID VALUE!!!")
                    continue
            elif item == 4:
                try:
                    quantidade_rice = int(input("Enter the amount: "))
                    if quantidade_rice > 0:
                        rice += quantidade_rice
                        remainder_rice += quantidade_rice
                        total_itens += quantidade_rice
                        if donor_type == "FIS":
                            fisica += quantidade_rice
                        elif donor_type == "JUR":
                            juridica += quantidade_rice
                    while quantidade_rice < 0:
                        print("ENTER A VALID VALUE!!!")
                        quantidade_rice = int(input("Enter the amount: "))
                        if quantidade_rice > 0:
                            rice += quantidade_rice
                            remainder_rice += quantidade_rice
                            total_itens += quantidade_rice
                            if donor_type == "FIS":
                                fisica += quantidade_rice
                            elif donor_type == "JUR":
                                juridica += quantidade_rice
                except ValueError:
                    print("ENTER A VALID VALUE!!!")
                    continue
            elif item == 5:
                try:
                    quantidade_extract = int(input("Enter the amount: "))
                    if quantidade_extract > 0:
                        extract += quantidade_extract
                        remainder_extract += quantidade_extract
                        total_itens += quantidade_extract
                        if donor_type == "FIS":
                            fisica += quantidade_extract
                        elif donor_type == "JUR":
                            juridica += quantidade_extract
                    while quantidade_extract < 0:
                        print("ENTER A VALID VALUE!!!")
                        quantidade_extract = int(input("Enter the amount: "))
                        if quantidade_extract > 0:
                            extract += quantidade_extract
                            remainder_extract += quantidade_extract
                            total_itens += quantidade_extract
                            if donor_type == "FIS":
                                fisica += quantidade_extract
                            elif donor_type == "JUR":
                                juridica += quantidade_extract
                except ValueError:
                    print("ENTER A VALID VALUE!!!")
                    continue
            elif item == 6:
                try:
                    quantidade_pasta = int(input("Enter the amount: "))
                    if quantidade_pasta > 0:
                        pasta += quantidade_pasta
                        remainder_pasta += quantidade_pasta
                        total_itens += quantidade_pasta
                        if donor_type == "FIS":
                            fisica += quantidade_pasta
                        elif donor_type == "JUR":
                            juridica += quantidade_pasta
                    while quantidade_pasta < 0:
                        print("ENTER A VALID VALUE!!!")
                        quantidade_pasta = int(input("Enter the amount: "))
                        if quantidade_pasta > 0:
                            pasta += quantidade_pasta
                            remainder_pasta += quantidade_pasta
                            total_itens += quantidade_pasta
                            if donor_type == "FIS":
                                fisica += quantidade_pasta
                            elif donor_type == "JUR":
                                juridica += quantidade_pasta
                except ValueError:
                    print("ENTER A VALID VALUE!!!")
                    continue
            elif item == 7:
                try:
                    quantidade_flour = int(input("Enter the amount: "))
                    if quantidade_flour > 0:
                        flour += quantidade_flour
                        remainder_flour += quantidade_flour
                        total_itens += quantidade_flour
                        if donor_type == "FIS":
                            fisica += quantidade_flour
                        elif donor_type == "JUR":
                            juridica += quantidade_flour
                    while quantidade_flour < 0:
                        print("ENTER A VALID VALUE!!!")
                        quantidade_flour = int(input("Enter the amount: "))
                        if quantidade_flour > 0:
                            flour += quantidade_flour
                            remainder_flour += quantidade_flour
                            total_itens += quantidade_flour
                            if donor_type == "FIS":
                                fisica += quantidade_flour
                            elif donor_type == "JUR":
                                juridica += quantidade_flour
                except ValueError:
                    print("ENTER A VALID VALUE!!!")
                    continue
            elif item == 8:
                try:
                    quantidade_beans = int(input("Enter the amount: "))
                    if quantidade_beans > 0:
                        beans += quantidade_beans
                        remainder_beans += quantidade_beans
                        total_itens += quantidade_beans
                        if donor_type == "FIS":
                            fisica += quantidade_beans
                        elif donor_type == "JUR":
                            juridica += quantidade_beans
                    while quantidade_beans < 0:
                        print("ENTER A VALID VALUE!!!")
                        quantidade_beans = int(input("Enter the amount: "))
                        if quantidade_beans > 0:
                            beans += quantidade_beans
                            remainder_beans += beans
                            total_itens += quantidade_beans
                            if donor_type == "FIS":
                                fisica += quantidade_beans
                            elif donor_type == "JUR":
                                juridica += quantidade_beans
                except ValueError:
                    print("ENTER A VALID VALUE!!!")
                    continue
            elif item == 9:
                try:
                    quantidade_salt = int(input("Enter the amount: "))
                    if quantidade_salt > 0:
                        salt += quantidade_salt
                        remainder_salt += quantidade_salt
                        total_itens += quantidade_salt
                        if donor_type == "FIS":
                            fisica += quantidade_salt
                        elif donor_type == "JUR":
                            juridica += quantidade_salt
                    while quantidade_salt < 0:
                        print("ENTER A VALID VALUE!!!")
                        quantidade_salt = int(input("Enter the amount: "))
                        if quantidade_salt > 0:
                            salt += quantidade_salt
                            remainder_salt += quantidade_salt
                            total_itens += quantidade_salt
                            if donor_type == "FIS":
                                fisica += quantidade_salt
                            elif donor_type == "JUR":
                                juridica += quantidade_salt
                except ValueError:
                    print("ENTER A VALID VALUE!!!")
                    continue
            elif item == 10:
                try:
                    quantidade_crackers = int(input("Enter the amount: "))
                    if quantidade_crackers > 0:
                        crackers += quantidade_crackers
                        remainder_crackers += quantidade_crackers
                        total_itens += quantidade_crackers
                        if donor_type == "FIS":
                            fisica += quantidade_crackers
                        elif donor_type == "JUR":
                            juridica += quantidade_crackers
                    while quantidade_crackers < 0:
                        print("ENTER A VALID VALUE!!!")
                        quantidade_crackers = int(input("Enter the amount: "))
                        if quantidade_crackers > 0:
                            crackers += quantidade_crackers
                            remainder_crackers += quantidade_crackers
                            total_itens += quantidade_crackers
                            if donor_type == "FIS":
                                fisica += quantidade_crackers
                            elif donor_type == "JUR":
                                juridica += quantidade_crackers
                except ValueError:
                    print("ENTER A VALID VALUE!!!")
                    continue
            elif item == 11:
                try:
                    other = str(input("What is the other? "))
                    quantidade_extras = int(input("Enter the amount: "))
                    if quantidade_extras > 0:
                        extras += quantidade_extras
                        remainder_extras += quantidade_extras
                        total_itens += quantidade_extras
                        if donor_type == "FIS":
                            fisica += quantidade_extras
                        elif donor_type == "JUR":
                            juridica += quantidade_extras
                    while quantidade_extras < 0:
                        print("ENTER A VALID VALUE!!!")
                        quantidade_extras = int(input("Enter the amount: "))
                        if quantidade_extras > 0:
                            extras += quantidade_extras
                            remainder_extras += quantidade_extras
                            total_itens += quantidade_extras
                            if donor_type == "FIS":
                                fisica += quantidade_extras
                            elif donor_type == "JUR":
                                juridica += quantidade_extras
                except ValueError:
                    print("ENTER A VALID VALUE!!!")
                    continue
            else:
                print("\n ENTER A ITEM VALID!!!\n")
            finish()
            try:
                sn = str(input("Do you want to continue donating?")).strip().upper()[0]
                # Enquanto o usuario não digitar uma entrada correta, a pergunta irá repetir.
                while sn not in "SN":
                    print("\n ENTER JUST [S] or [N]!!!\n")
                    sn = str(input("Do you want to continue donating?")).strip().upper()[0]
            except IndexError:
                print("\nENTER A VALID OPTION!!!\n")
                continue

            # Verifica se tem a quantidade suficiente de itens para formar a cesta.
            while remainder_sugar >= 1 and remainder_rice >= 4 and remainder_coffee >= 2 and remainder_extract >= 2 and remainder_pasta >= 3 and remainder_crackers >= 1 and remainder_oil >= 1 and remainder_flour >= 1 and remainder_beans >= 4 and remainder_salt >= 1:
                cesta += 1
                remainder_sugar -= 1
                remainder_rice -= 4
                remainder_coffee -= 2
                remainder_extract -= 2
                remainder_pasta -= 3
                remainder_crackers -= 1
                remainder_oil -= 1
                remainder_flour -= 1
                remainder_beans -= 4
                remainder_salt -= 1
                if remainder_extras > 0:
                    remainder_extras -= 1
    # Possibilita a visão de um relatório parcial.
    elif choice == 2:
        record()
    else:
        print("\n ENTER A VALID CHOICE!!! \n")
# Relatório final e fim do código.
record()