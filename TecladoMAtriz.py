# -*- coding: utf-8 -*-

from machine import Pin
import utime

matrix_keys = [['1', '2', '3', 'A'],
               ['4', '5', '6', 'B'],
               ['7', '8', '9', 'C'],
               ['*', '0', '#', 'D']]

keypad_rows = [2,3,4,5]
keypad_columns = [6,7,8,9]

col_pins = []
row_pins = []

def asignacion():   
    for dato in range(len(keypad_rows)):
        row_pins.append(Pin(keypad_rows[dato], Pin.OUT))
        col_pins.append(Pin(keypad_columns[dato], Pin.IN, Pin.PULL_DOWN))

def main():
    asignacion()
    while True:
        for row in range(len(row_pins)):
            for col in range(len(col_pins)):
                row_pins[row].on()
                
                if col_pins[col].value() == 1:
                    print("Presionaste", matrix_keys[row][col])
                    utime.sleep(0.5)
                        
            row_pins[row].off()

if __name__ == '__main__':
    print("Ingrese el valor del teclado")
    main()