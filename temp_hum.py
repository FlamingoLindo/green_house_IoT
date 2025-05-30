from machine import Pin
import time
from dht import DHT22 

# Inicializa o sensor DHT22 conectado ao pino 13
sensor = DHT22(Pin(13))  # Correção aqui, removendo o ponto extra

def read_dht_values():
    """
    Atualiza e retorna os valores de temperatura e umidade.
    
    A função chama sensor.measure() uma vez para atualizar ambas as leituras,
    depois obtém e retorna a temperatura e a umidade.
    """
    # Realiza a medição para atualizar os valores de temperatura e umidade
    sensor.measure()  
    # Obtém a temperatura medida
    t = sensor.temperature()  
    # Obtém a umidade medida
    h = sensor.humidity()   
    # Retorna os valores de temperatura e umidade  
    return t, h               
