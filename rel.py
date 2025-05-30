import time
from machine import Pin
from temp_hum import read_dht_values

def temp_control_relay(t):
    # Inicializa o relé de temperatura no pino 12 como saída
    Relay = Pin(12, Pin.OUT)

    # Verifica se a temperatura está fora da faixa ideal (entre 15°C e 21°C)
    if t > 21 or t < 15:
        print("\033[41mALERTA: Temperatura da estufa inadequada...\033[0m")
        Relay.value(1)  # Ativa o relé para amenizar a temperatura
        print('Amenizando temperatura...')

        # Enquanto a temperatura estiver acima de 21°C, atualiza a leitura
        while t > 21:
            # Atualiza a leitura da temperatura (a umidade é ignorada com "_")
            t, _ = read_dht_values()  
            print(f"Temperatura atual: {t:.1f}°C")
            time.sleep(1)

        # Enquanto a temperatura estiver abaixo de 15°C, atualiza a leitura
        while t < 15:
            # Atualiza a leitura da temperatura
            t, _ = read_dht_values()  
            print(f"Temperatura atual: {t:.1f}°C")
            time.sleep(1)

        print("Temperatura estabilizada.")
        # Após normalizar a temperatura, desativa o relé se ele estiver ligado
        if Relay.value() == 1:
            print('Desligando relay de temperatura...')
            Relay.value(0)

def hum_control_relay(h):
    # Inicializa o relé de umidade no pino 14 como saída
    Relay2 = Pin(14, Pin.OUT)

    # Verifica se a umidade está fora da faixa ideal (entre 60% e 70%)
    if h > 70 or h < 60:
        print("\033[41mALERTA: Humidade da estufa inadequada...\033[0m")
        # Ativa o relé para "amenizar" a umidade
        Relay2.value(1)  
        print('Amenizando humidade...')

        # Enquanto a umidade estiver acima de 70%, atualiza a leitura
        while h > 70:
            # Atualiza a leitura da umidade (a temperatura é ignorada com "_")
            _, h = read_dht_values()  
            print(f"Humidade atual: {h:.1f}%")
            time.sleep(1)

        # Enquanto a umidade estiver abaixo de 60%, atualiza a leitura
        while h < 60:
            # Atualiza a leitura da umidade
            _, h = read_dht_values()  
            print(f"Humidade atual: {h:.1f}%")
            time.sleep(1)

        print("Humidade estabilizada.")
        # Após normalizar a umidade, desativa o relé se ele estiver ligado
        if Relay2.value() == 1:
            print('Desligando relay de humidade...')
            Relay2.value(0)
