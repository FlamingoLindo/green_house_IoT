import utime
from machine import Pin

# Mapeamento de pinos do ESP32 para as colunas do teclado
# Cada pino é configurado como entrada com resistor pull-up interno
col_pins = [
    Pin(15, Pin.IN, Pin.PULL_UP),  # GPIO 15
    Pin(2, Pin.IN, Pin.PULL_UP),   # GPIO 2
    Pin(4, Pin.IN, Pin.PULL_UP),   # GPIO 4
    Pin(16, Pin.IN, Pin.PULL_UP)   # GPIO 16
]

# Mapeamento de pinos do ESP32 para as linhas do teclado
# Cada pino é configurado como saída
row_pins = [
    Pin(17, Pin.OUT),  # GPIO 17
    Pin(5, Pin.OUT),   # GPIO 5
    Pin(18, Pin.OUT),  # GPIO 18
    Pin(19, Pin.OUT)   # GPIO 19
]

# Define todas as linhas como HIGH por padrão,
# garantindo que nenhuma linha esteja ativa inicialmente.
for row in row_pins:
    row.value(1)

# Mapeamento das teclas do teclado matricial em uma matriz 4x4
key_map = [
    ["1", "4", "7", "*"],
    ["2", "5", "8", "0"],
    ["3", "6", "9", "#"],
    ["A", "B", "C", "D"]
]

def read_keypad():
    """Lê o teclado matricial e retorna a tecla pressionada."""
    # Percorre cada linha do teclado
    for row_idx, row in enumerate(row_pins):
        # Ativa a linha atual, colocando-a em LOW
        row.value(0)  
        # Verifica cada coluna para detectar se a tecla foi pressionada
        for col_idx, col in enumerate(col_pins):
            # Se o valor do pino da coluna for LOW, a tecla foi pressionada
            if col.value() == 0:
                # Aguarda 20ms para debouncing (evita leituras falsas)
                utime.sleep_ms(20)  
                # Aguarda até que a tecla seja solta (o pino volta a HIGH)
                while col.value() == 0:
                    pass
                # Restaura a linha para HIGH após a leitura
                row.value(1)  
                # Retorna o caractere correspondente à tecla pressionada, de acordo com o key_map
                return key_map[row_idx][col_idx]
        # Restaura a linha para HIGH caso nenhuma tecla tenha sido detectada nesta linha
        row.value(1)
    # Se nenhuma tecla foi pressionada, retorna None
    return None
