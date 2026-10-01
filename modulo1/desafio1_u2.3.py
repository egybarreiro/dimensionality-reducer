"""Purpose: This module contains a simple script to practice and understand data structure and file operations.
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-23 Modified: 2026-07-23"""

file = open('diario.txt', 'w')
file.write('lunes : Mi diario es muy superficial.')
file.write('martes: Hoy ha sido un dia de muchisimo aprendizaje.')
file.write('miercoles: Se supone que esto sea un diccionario.')
file.close()