from machine import Pin
import time

# Configura o buzzer no pino 23 como saída.
buzzer = Pin(23, Pin.OUT)

def sound_buzzer(duration_ms=100):
    """Ativa o buzzer por um curto período.
    
    Parâmetros:
      duration_ms: duração em milissegundos que o buzzer ficará ativo.
    """
    # Ativa o buzzer
    buzzer.value(1)
    # Aguarda pelo tempo especificado        
    time.sleep_ms(duration_ms)
    # Desativa o buzzer  
    buzzer.value(0)           
