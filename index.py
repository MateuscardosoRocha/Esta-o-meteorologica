import machine
import dht
import time
import network
import urequests
from wifi import conexao


#Declarando portas
sensor = dht.DHT11(machine.Pin(4))
rele = machine.Pin(2, machine.Pin.OUT)
rele.value(0)


print("Aluno:Mateus Cardoso Rocha\n\n")

print("-------------Estação meteorológica para internet das coisas-------------\n")

while True:
    sensor.measure()
    temperature = sensor.temperature()
    humidity = sensor.humidity()
    print("Condições climaticas atuais:\n")
    print("A temperatura é: {}°C.".format(temperature))
    print("A umidade relativa do ar é: {}%.\n\n".format(humidity))
    time.sleep(3)
    
    #Condições 
    if temperature > 31:
        print("Temperatura acima de 31°C, o relé está sendo energizado!\n")
        rele.value(1)
    
    elif humidity > 70:
        print("Umidade do ar acima de 70%, o relé está sendo energizado!\n")
        rele.value(1)
        
    else:
        rele.value(0)
        
    
    print("--------------------------------------------NETWORK--------------------------------------------")
        
    print("Logando a uma rede de internet...\n")
    time.sleep(1)
    print("Conectado a rede!\n")
    station = conexao("NomeRede", "SenhaRede")
    
    
    if not station.isconnected():
        print("Erro na conexão com a rede de internet, tente novamente!\n")
        
    else:
        print("Entrando no ThingSpeak....\n")
        time.sleep(2)
        print("Acesso no ThingSpeak confirmada!\n")
        print("Enviando os dados de temperatura e umidade para o ThingSpeak...\n")
        response = urequests.get("https://api.thingspeak.com/update?api_key=NNLGZES0ZS0IJJF8&field1={}&field2={}".format(temperature,humidity))
        time.sleep(2)
        print("Dados enviados com sucesso!\n\n")
        response.text
        station.disconnect()
        time.sleep(2)