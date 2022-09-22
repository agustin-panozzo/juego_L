from juego_L import *
import random

MOVIMIENTOS = ['W','A','S','D','R','I','*']
TABLERO_INICIAL = [['+', 2, 2, '*'], ['*', 1, 2, '*'], ['*', 1, 2, '*'], ['*', 1, 1, '-']]
#Los (+) y (-) son fichas neutrales, 1 y 2 hacen referencia a los espacios que ocupan las L de cada jugador.
#Los * son espacios en blanco.
def main():
    menu = " "
    ranking = []
    while menu != -1:
        nombre_ganadores = []
        quedan_movimientos = True
        tablero = TABLERO_INICIAL
        posible_tablero = copiar_matriz(tablero) #Para no tener una referencia al original
        menu = int(input('Presione: 1.Iniciar nueva partida \n\
          2.Ver el ranking.\n\
         -1.Para salir.\n '))
        if menu == 1:
            mov = ' '
            jugador_1: str = input('Ingrese nombre del jugador 1: ')
            jugador_2: str = input('Ingrese nombre del jugador 2: ')
            mov_totales = 0 #Si se superan los 20 (10 cada jugador), se activa el modo muerte subita
            jugador = random.randint(1,2)
            if jugador == 1:
                jugador_contrario = 2
                (f'Empieza {jugador_1} (jugador 1)')
            else:
                jugador_contrario = 1
                print(f'Empieza {jugador_2} (jugador 2)')
            imprimir_tablero(tablero)
            while mov not in MOVIMIENTOS:
                mov: str = input(f'Jugador {jugador} ingrese W,A,S,D para mover la ficha, R para rotar, I para invertir y presione * para confirmar: ')
            posiciones = mover_L(posible_tablero, jugador, mov)
            posible_tablero: list = colocar_ficha(tablero, jugador, posiciones)
            
            while quedan_movimientos:
                imprimir_tablero(posible_tablero)
                mov = input(f'Jugador {jugador} ingrese W,A,S,D para mover la ficha, R para rotar, I para invertir y presione * para confirmar: ')
                if mov != '*':
                    if len(obtener_posicion(posible_tablero, jugador)) != 4:
                        posiciones = mover_L(posible_tablero, jugador, mov, posiciones)
                    else:
                        posiciones = mover_L(posible_tablero, jugador, mov, obtener_posicion(posible_tablero, jugador))
                    posible_tablero = colocar_ficha(tablero, jugador, posiciones)
                else:
                    if es_movimiento_valido(tablero, jugador, posiciones) and posible_tablero != tablero and esta_en_tablero(posiciones):
                        posible_tablero = colocar_ficha(tablero, jugador, obtener_posicion(posible_tablero, jugador))
                        tablero = copiar_matriz(posible_tablero)
                        mov_totales += 1
                        mov_extra = 1
                        ficha_neutra = input('Ingrese la pieza neutra que desea mover (+) o (-) o ingrese * para terminar el turno: ')
                        while ficha_neutra != '*':
                            mov = input(f'Jugador {jugador} ingrese W,A,S,D para mover la ficha {ficha_neutra} y presione * para confirmar: ')
                            if mov != '*':
                                posible_tablero = colocar_neutra(tablero, ficha_neutra, mover_neutra(posible_tablero, ficha_neutra, mov))
                            else:
                                if es_movimiento_valido(tablero, ficha_neutra, obtener_neutra(posible_tablero, ficha_neutra)):
                                    posible_tablero = colocar_neutra(tablero, ficha_neutra, obtener_neutra(posible_tablero, ficha_neutra))
                                    tablero = copiar_matriz(posible_tablero)
                                    quedan_movimientos = quedan_mov_validos(tablero, jugador_contrario)
                                    if mov_totales >= 20 and mov_extra == 1:
                                        print('MUERTE SUBITA')
                                        confirmar = input(f'¿Desea mover la otra ficha? (Y/N): ')
                                        if confirmar == 'Y':
                                            if ficha_neutra == '+':
                                                ficha_neutra = '-'
                                            else:
                                                ficha_neutra ='+'
                                            mov_extra -= 1
                                        else:
                                            ficha_neutra = '*'
                                    else:
                                        ficha_neutra = '*' #Para cortar el bucle.
                                else:
                                    print('El movimiento es invalido.')
                                    posible_tablero = copiar_matriz(tablero)
                            imprimir_tablero(posible_tablero)
                        quedan_movimientos = quedan_mov_validos(tablero, jugador_contrario)
                        if jugador == 1:
                            jugador = 2
                            jugador_contrario = 1
                        else:
                            jugador = 1
                            jugador_contrario = 2
                    else:
                        print('El movimiento es invalido.')
                        posible_tablero = copiar_matriz(tablero)
            if jugador == 1:
                jugador = jugador_2 #Intercambio los jugadores porque al finalizar la partida hay un cambio de turnos
            else:
                jugador = jugador_1
            print(f'FELICIDADES !! GANADOR: {jugador}')
            nombre_ganadores = []
            for i in range(len(ranking)):
                nombre_ganadores.append(ranking[i][1])
            if jugador in nombre_ganadores:
                for i in range(len(ranking)):
                    if ranking[i][1] == jugador:
                        ranking[i][0] += 1
            else:
                ranking.append([1, jugador])
            if len(ranking) >= 4:
                ranking.pop(0) #Elimino el ganador mas viejo del ranking.
        if menu == 2:
            if len(ranking) == 0:
                print('No hay ganadores.')
            else:
                ranking_ordenado = sorted(ranking, reverse = True)
                for i in range(len(ranking)):
                    print(f'{ranking_ordenado[i][1]} ganó {ranking_ordenado[i][0]} partida/s.')
main()  