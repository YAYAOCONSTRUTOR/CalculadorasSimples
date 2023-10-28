#Calculadora de velocidade Valor, tempo e quantidade de litros gastos 
'''
Calculadora simples e básica sobre o uso de python em situações cotidianas 
Utilize  compilador online ou programas para compilar 
Yago Barbosa, Pix para doação: 
Agradecimento: https://www.online-python.com/
'''
#Dados
km = 270 # Distancia de uma cidade a outra
kmh = 80 #Velocidade média que você irá percorrer 
kmL = 30 #Consumo por litro de seu veiculo
preco = 6.50 #preço do combustível

#Contas
tempo = km / kmh
litros = km / kmL
valor = preco * litros * 2  #2 pois está contabilizando ida e volta

#imprimir
print(f'Tempo seria de :{tempo}horas, sendo que gastaria: {litros:.2f}litros custando R${valor} no custo de ida de volta')
