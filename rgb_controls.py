from machine import Pin
import utime

# Configura os pinos do LED RGB como saída:
yellow = Pin(26, Pin.OUT)
purple = Pin(25, Pin.OUT)

# Variável para armazenar o estado atual do LED para evitar atualizações desnecessárias
current_status = None

def light(status):
    global current_status

    yellow.value(0)
    purple.value(0)

    current_status = status

    if status == 'amarelo':
        purple.value(0)
        yellow.value(1)
        print('Ligando luz amarela...')
    elif status == 'roxa':
        yellow.value(0)
        purple.value(1)
        print('Ligando luz roxa...')
    elif status == 'apagado':
        print('Desligando luz...')

