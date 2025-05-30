from machine import Pin, ADC
import time

from rgb_controls import light

# Configura o sensor LDR (fotorresistor) no pino 27
ldr = ADC(Pin(27))
# Configura a atenuação para ampliar a faixa de medição do ADC (0–3.6V)
ldr.atten(ADC.ATTN_11DB)  

# Define dois limiares para implementar histerese
# Isso evita que pequenas variações de luz fiquem ligando/desligando o LED constantemente

# Acende o LED quando o valor do LDR for maior que isso (ambiente claro)
THRESHOLD_ON = 800   
# Apaga o LED quando o valor do LDR for menor que isso (ambiente escuro)
THRESHOLD_OFF = 600  

# Armazena o último estado do LED RGB ('amarelo', 'roxa' ou 'apagado')
last_light_status = None

def get_lux_amount(door_open):
    """
    Lê a luz ambiente e ajusta a cor do LED RGB com base na luminosidade e se a porta está aberta ou fechada.

    Se estiver claro e a porta aberta → LED amarelo  
    Se estiver claro e a porta fechada → LED roxo  
    Se estiver escuro → LED apagado  
    """
    global last_light_status

    # Lê o valor atual do sensor LDR (quanto maior, mais luz)
    light_value = ldr.read()

    # Se o LED já estava aceso (amarelo ou roxo)
    if last_light_status in ['amarelo', 'roxa']:
        if light_value < THRESHOLD_OFF:
            # Se escureceu abaixo do limite, desliga o LED
            new_status = 'apagado'
        else:
            # Continua aceso, mas reavalia a cor com base no estado da porta
            new_status = 'amarelo' if door_open else 'roxa'
    else:
        # Se o LED estava apagado
        if light_value > THRESHOLD_ON:
            # Se clareou acima do limite, liga o LED com a cor baseada na porta
            new_status = 'amarelo' if door_open else 'roxa'
        else:
            # Continua apagado
            new_status = 'apagado'

    # Atualiza o LED somente se o estado mudou
    if new_status != last_light_status:
        print(f"Mudando status da luz: {new_status}")
        # Chama a função para acender o LED com a nova cor
        light(new_status)  
        # Atualiza o status atual
        last_light_status = new_status  
