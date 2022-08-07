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
import time


def Nuevo():

    Menu = input(
        """"
    
        \033[92m[MENU     💫   ]
    
    
        [  👾 sen,cos,tg]  [COMMAND = "ConteudoNovo"   ]
        [  😱 jogo3     ]  [COMMAND = "Jogo3"          ]
        [  😎 tg        ]  [COMMAND = "tg"             ]
        [  😍 Pitagoras ]  [COMMAND = "Pitagora"       ]
        
        
        
        
        
        
        """)
    if Menu == "Jogo3":
        jogo3()
    if Menu == "ConteudoNovo":
        calcular_sct()
    if Menu == "tg":
        tg_30cl()
    if Menu == "Pitagoras":
        MenuPitagoras()



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
    div_str = calculo_str / calculo
    print(div_str)




def tg_30cl():
    #x = int(input("Se o numero conter  √ coloque-o aqui :   "))
    #k_o = math.pow(x, 1 / 2)
    #print(k_o)
    y = int(float(input("Numero se tiver raiz :   ")))

    numero_cima = int(float(input("Valor que fica encima lado esquerdo :    ")))
    numero_baixo = int(float(input("Valor que fica embaixo lado direito :    ")))
    criando_raiz = math.pow(y, 1/2)
    calculando_dnv = numero_cima * numero_baixo
    print(calculando_dnv)
    dividir_ = calculando_dnv / y
    print(dividir_)
    #numero_raiz = int(float(input("Raiz resolvida :    ")))
    div_02 = dividir_ * y
    div_ = dividir_ * criando_raiz
    print(div_)

def MenuPitagoras():
    Menu_ = input("""
    
    
                    \033[92m[MENU PITAGORASSSSSS 😎   ]
                                
                            [Opçoes]
                            
                            
    [Descobrir X com hipotenusa e qualquer lado dos catetos] [ COMMAND = "Op1"  ]
    [Descobrir valor da Hipotenusa com os 2 catetos        ] [ COMMAND = "Op2"  ]
                              
                              
                            [Voltar Menu Principal ] [ COMMAND = "Menu"     ]
                            
                            
                            
                            
                            
                            
                 
    
    
    
    """)

    if Menu_ == "Menu":
            Nuevo()
    if Menu_ == "Op2":
        Pitagoras()
    if Menu_ == "Op1":
        Ope1()



def Pitagoras():
    lado_A = int(input("Digite o valor X ( em todos os casos é 1 )  :    "))
    lado_B = int(input("Digite o valor B :    "))
    lado_C = int(input("Digite o valor C :    "))

    lado_a_elev = lado_A^2
    calculo_padrao = lado_B**2 + lado_C**2
    final = math.pow(calculo_padrao, 1/2)
    print(f"O Valor do X é {final}")

def Ope1():

    valor_hipo = int(float(input("Digite o Valor da hipotenusa :    ")))
    valor_cat = int(float(input("Digite o valor do cateto :     ")))
    calculo = valor_hipo**2
    caculo_02 = valor_cat**2
    resultado = calculo - caculo_02
    raiz_result = math.pow(resultado, 1/2)

    print(f"O Valor do Cateto é {raiz_result}, Obg por utilizar o script :) ")
    time.sleep(10)
    return MenuPitagoras()



Nuevo()