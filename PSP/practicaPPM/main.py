import os
import sys
from multiprocessing import Process

def main():
    pass

def red(input_path, filename):

    # Leer la imagen PPM
    with open(os.path.join(input_path, filename), 'r') as f:
        header = []
        while len(header) < 3:
            line = f.readline()
            if line.startswith('#'):
                continue
            header.append(line.strip())
        magic, size, maxval = header
        width, height = map(int, size.split())
        pixels = []
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            pixels.extend(map(int, line.strip().split()))

    # Procesar píxeles: solo dejar los rojos, el resto negro
    new_pixels = []
    for i in range(0, len(pixels), 3):
        r, g, b = pixels[i:i+3]
        if r > 0 and g == 0 and b == 0:
            new_pixels.extend([r, g, b])
        else:
            new_pixels.extend([0, 0, 0])
            
    # Guardar la nueva imagen PPM
    output_filename = f'red_{filename}'
    with open(os.path.join(input_path, output_filename), 'w') as f:
        f.write(f'{magic}\n{width} {height}\n{maxval}\n')
        for i in range(0, len(new_pixels), 3):
            f.write(f'{new_pixels[i]} {new_pixels[i+1]} {new_pixels[i+2]}\n')

def blue():
    pass

def green():
    pass

if __name__ == '__main__':
    main()

'''
class Img():
    separators = [" ", "\n", "\r", "\t"]

    def __init__(self, ¿path?):
        pass ¿self.path = path?
if caracter in Img.separators:
    pass
'''