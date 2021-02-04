# coding=utf-8
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Consulta import consulta
from CRUD import crud
import socket

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        consulta()
        crud()
    except socket.error:
        print("Error en la conexión. ¿Está basex levantado (basexserver)?")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
