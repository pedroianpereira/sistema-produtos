
# Olá! Estou estudando python na faculdade, na aula de hoje (26 de outubro de 2026) foi apresentado uma maneira de guardar informações dentro dos colchetes...
# Nisso vi um uso perfeito do append e remove dentro das variaveis.
# Então fiz um pequeno e básico sistema de cadastro de produtos, admito que ainda vou estar fazendo um sistema de sorteio, mas preciso alimentar minha curiosidade.
# Aluno de ADS: Pedro Ian.


def bruto():
    import time # importa um temporizador ao código, no etanto, o temporizador vai servir como folga visual, fazendo pequenas pausas para quem estiver vendo.

    nomes = [] # vai receber as informações.

    options = 0 # começo da estrutua de decisão.

    while options != 4: # Enquanto options não for igual a 4, ele estará de pé. Se receber, o processo termina.

        time.sleep(0.5) #aplicação de tempo/pausa.

        # abaixo terá as opções.

        print("\nOlá! Seja bem vindo(a) ao sistema de produtos!")

        print("\n1- Listar produtos") # opção 1
        print("\n2- Cadastrar produtos") # opção 1
        print("\n3- Remover produtos") # opção 2 (Remover Produtos)
        print("\n4- Stop") # opção 4

        time.sleep(0.5)

        options = int(input("\nDigite um número para prosseguir: ")) # função para fazer com que a váriavel receba um número inteiro.
        time.sleep(0.5)
        
        if options == 1: # se options for igual a 1...
            time.sleep(0.5)
            print("\n",*nomes) # vai printar na tela a possível lista. Pode ser usado após um produto ser cadastrado (envolve a opção 2 e 3).
            time.sleep(0.5)
        
        elif options == 2: #se options for igual a 2...
            time.sleep(0.5)
            nome = input("\nAdicione um produto ou produtos: ") # O operador vai cadastrar produtos por meio do input.
            nomes.append(nome) # a váriavel nomes vai guardar a informação recebida pela váriavel nome por meio do input, usando o append.
            time.sleep(0.5)
            print("\nItem adicionado.\n") # em seguida vai mostrar esta mensagem.
            time.sleep(0.5)
        
        elif options == 3: # se options for igual a 3...
            nome = input("\nRemova um produto ou produtos: ") # Praticamente um pequeno reaproveitamento do elif de cima...
            nomes.remove(nome) # o diferencial é que o operador vai remover uma informação gravada na var nomes, ou seja digitar o nome do produto, neste caso é o inverso da opção onde o append está.
            time.sleep(0.5)
            print("\nItem removido.\n") # vai printar que o item foi removido.
            time.sleep(0.5)

        elif options == 4: # se options for igual a 4... vai parar o código.
            time.sleep(0.5)
            print("\nProcesso encerrado.\n") # vai mostrar esta mensagem.
        
        else: # se options for igual a nada do que o código espera receber...
            print("\nOpção inválida! Tente novamente.\n") # vai mostrar esta mensagem.
bruto()
