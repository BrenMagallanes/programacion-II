import numpy as np

rssi = np.array([-68.2, -67.9, -67.5, -67.8, -68.0, -68.9,
-70.4, -72.8, -74.1, -75.6, -76.3, -75.9,
-74.8, -75.2, -76.8, -77.1, -75.4, -73.9,
-72.2, -70.8, -69.9, -69.1, -68.7, -68.4])

prom_directo = np.mean(rssi)

p_mw = 10 ** (rssi / 10)
prom_potencia = 10 * np.log10(np.mean(p_mw))

def main():
    print(prom_directo)
    print(prom_potencia)
