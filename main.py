import math



#def verificador_triangulos():
    #valor_a = input("Digite o valor A :   ")
    #valor_b = input("Digite o valor B :   ")
    #valor_c = input("Digite o valor C :   ")

    #calculo_test = (valor_a * valor_b)
   # print(calculo_test)


#def tg_30cl():
    #x = int(input("Valor lado X :   "))
    #y = int(input("Valor lado Y :   "))
    #numero_cima = int(input("Valor que fica encima lado esquerdo :    "))
    #numero_baixo = int(input("Valor que fica embaixo lado direito :    "))

    #calculando_dnv = numero_cima * numero_baixo
    #print(calculando_dnv)
    #dividir_ = calculando_dnv / y
    #print(dividir_)

def Nuevo():

    Menu = input(
        """"
    
        \033[92m[MENU     💫   ]
    
    
        [  👾 sen,cos,tg]  [COMMAND = "ConteudoNovo"   ]
        [  😱 jogo3     ]  [COMMAND = "Jogo3"          ]""")
    if Menu == "Jogo3":
        jogo3()



def calcular_sct():





    a = int(input("Angulo :   "))
    b = math.radians(a)
    seno = math.sin(b)
    cos = math.cos(b)
    tg = math.tan(b)
    print(seno, cos, tg)
    print("Obs : Pegue somente os 3 numeros dps do .")



    #x = int(input("Se o numero conter  √ coloque-o aqui :   "))
    #k_o = math.pow(x, 1/2)
    #print(k_o)
    #y = int(input("Valor do numero da raiz :   "))

    #numero_cima = int(input("Valor que fica encima lado esquerdo :    "))
    #numero_baixo = int(input("Valor que fica embaixo lado direito :    "))





    #calculo = tg/1
    #x_div = x/1
    #tudo = x/tg
    #print(calculo)
    #print(tudo)


def jogo3():
    print("\033[91mSe houver qualquer str na conta, utiliza o numero 1 para o calculo ")
    valor_a = int(float(input("\033[92mDigite o valor A ( valor str aqui)   :   ")))
    valor_a2 = int(float(input("\033[92mDigite o valor embaixo do A :   ")))
    valor_b = int(float(input("\033[92mDigite o valor B :   ")))
    valor_b2 = int(float(input("\033[92mDigite o valor embaixo B :  ")))

    #Magica :)

    calculo = valor_a2 * valor_b
    calculo_str = valor_a * valor_b2
    div_str = calculo / calculo_str
    print(div_str)




def tg_30cl():
    #x = int(input("Se o numero conter  √ coloque-o aqui :   "))
    #k_o = math.pow(x, 1 / 2)
    #print(k_o)
    y = int(float(input("Valor do numero da raiz :   ")))

    numero_cima = int(float(input("Valor que fica encima lado esquerdo :    ")))
    numero_baixo = int(float(input("Valor que fica embaixo lado direito :    ")))


    calculando_dnv = numero_cima * numero_baixo
    print(calculando_dnv)
    dividir_ = calculando_dnv / y
    print(dividir_)
    numero_raiz = int(float(input("Raiz resolvida :    ")))
    div_ = dividir_ * numero_raiz
    print(div_)

Nuevo()
