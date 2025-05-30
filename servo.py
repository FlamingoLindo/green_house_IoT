from machine import Pin, PWM

# Inicializa o PWM do servo no pino 21 com frequência de 50Hz
# e inicialmente com duty cycle 0 (servo parado)
pwm = PWM(Pin(21), freq=50, duty=0)

def move_servo(angle):
    """Move o servo para um ângulo específico.
    
    O cálculo do duty cycle é feito convertendo o ângulo (0 a 180°)
    para um valor proporcional que o PWM espera, levando em conta:
      - Um ângulo de 0° corresponde aproximadamente a 0.5ms de pulso
      - Um ângulo de 180° corresponde aproximadamente a 2.5ms de pulso
      - A janela total do pulso é de 20ms (frequência de 50Hz)
      - O valor máximo de duty é 1023 para o PWM configurado
    """
    # Calcula o duty cycle baseado no ângulo fornecido
    duty_cycle = int(((angle) / 180 * 2 + 0.5) / 20 * 1023)
    # Define o duty cycle no PWM para mover o servo para o ângulo desejado
    pwm.duty(duty_cycle)
