from machine import Pin

# Configura o sensor de movimento conectado ao pino 22 como entrada.
motion_sensor = Pin(22, Pin.IN)

def detect_motion():
    """Verifica e retorna True se o sensor de movimento detectar movimento, 
       caso contrário retorna False."""
    # O sensor retorna 1 se houver movimento e 0 se não houver.
    return motion_sensor.value() == 1
