import serial
import time
import matplotlib.pyplot as plt

# asegúrese de que el 'COM#' esté configurado de acuerdo con el Administrador de dispositivos de Windows
ser = serial.Serial('COM3', 9800, timeout=1)
time.sleep(2)

data = []
for i in range(100):
    line = ser.readline()   # leer una cadena de bytes
    if line:
        string = line.decode()  # convertir la cadena de bytes en una cadena Unicode
        num = int(string) # convertir la cadena Unicode a un int
        print(num)
        data.append(num) # agregar int a la lista de datos
ser.close()

# construir la trama
plt.plot(data)
plt.xlabel('Tiempo')
plt.ylabel('Lectura Potenciometro')
plt.title('Lectura Potenciometro vs Tiempo')
plt.show()