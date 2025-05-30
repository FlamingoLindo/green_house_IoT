import time
import utime
from keypad import read_keypad          
from servo import move_servo            
from motion import detect_motion        
from buzzer import sound_buzzer         
from temp_hum import read_dht_values    
from rel import temp_control_relay, hum_control_relay  
from light_controls import get_lux_amount

# Senha para destravar a porta
PASSWORD = '6969'
# Lista para armazenar os dígitos digitados pelo usuário
PASS_INPUT = []
# Variável para indicar se a porta está aberta ou fechada
door_open = False
# Guarda o tempo do último controle de temperatura/umidade
last_temp_check = utime.ticks_ms()
# Intervalo para checagem de temperatura/umidade (5000ms = 5 segundos)
TEMP_INTERVAL = 5000

def door_lock(status):
    """Controla a trava da porta. Se o status for 'abrir', 
       destrava a porta; caso contrário, tranca."""
    global door_open
    if status == 'abrir':
        # Move o servo para 180 graus (abrir a porta)
        move_servo(180)     
        door_open = True
        print('Porta destravada')
    else:
        # Move o servo para 0 graus (fechar a porta)
        move_servo(0)       
        door_open = False
        print('Porta fechada')

# Mensagem de inicialização do sistema
print("\033[41m\033[1m\033[4mHorta do Seu João 2000 ativada!\033[0m")
# Inicialmente, a porta está fechada
door_lock(status='fechada')

# Loop principal do programa
while True:
    # Verifica se o intervalo de 5 segundos passou para medir temperatura e umidade
    if utime.ticks_diff(utime.ticks_ms(), last_temp_check) > TEMP_INTERVAL:
        # Lê a temperatura e a umidade do sensor
        t, h = read_dht_values()
        print(f"Temperatura atual: {t}°C")
        print(f"Humidade atual: {h}%")

        # Controla os relés de temperatura e umidade com base nos valores lidos
        temp_control_relay(t)
        hum_control_relay(h)

        # Controla a iluminação (cor do LED) com base na 
        # leitura do sensor de luminosidade e estado da porta
        get_lux_amount(door_open)

        # Atualiza o tempo do último check
        last_temp_check = utime.ticks_ms()

    # Verifica se há movimento e se a porta está fechada
    if detect_motion() and not door_open:
        # Se houver movimento enquanto a porta está fechada, alerta e ativa o buzzer
        print("\033[41m\033[1m\033[4mMOVIMENTO INDESEJADO DETECTADO!\033[0m")
        sound_buzzer(100)

    # Lê a entrada do teclado
    key = read_keypad()
    if key:
        # Se a tecla pressionada for um dígito
        if key.isdigit():
            PASS_INPUT.append(key)
            print(f"Entrada: {''.join(PASS_INPUT)}")

            # Quando 4 dígitos forem inseridos, verifica a senha
            if len(PASS_INPUT) == 4:
                entered_pass = ''.join(PASS_INPUT)
                if entered_pass == PASSWORD:
                    print("Acesso concedido!")

                    # Destrava a porta se a senha estiver correta
                    door_lock(status='abrir')   
                else:
                    print("Senha incorreta! Tente novamente.")

                    # Tranca a porta se a senha estiver errada
                    door_lock(status='fechada') 
                    
                # Limpa a entrada para nova tentativa
                PASS_INPUT.clear()

    # Aguarda 0.2 segundos antes de repetir o loop
    utime.sleep(0.2)
