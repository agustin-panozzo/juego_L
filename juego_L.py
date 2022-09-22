def imprimir_tablero(tablero: list) -> None:
    """
    Recibe una lista de listas de dimensiones 4x4 y la imprime en forma de tablero.
    """
    print('    A    B    C    D')
    print('   ' + '-----' * 4, end = '')
    for i in range(4):
        print()
        print(f'{i+1} | ', end = '')
        for j in range(4):
            print(tablero[i][j], end = '')
            print('    ', end = '')
    print("")

def trasponer_matriz(tablero: list) -> list:
    tablero_nuevo = []
    for i in range(len(tablero)):
        tablero_nuevo.append([])
        for j in range(len(tablero)):
            tablero_nuevo[i].append(tablero[j][i])
    return tablero_nuevo

def esta_en_tablero(posiciones: list) -> bool:
    """
    Verifica si las coordenadas se encuentran dentro de los márgenes del tablero.
    Recibe una lista de listas y devuelve un booleano.
    """
    en_tablero = True
    for i in range(len(posiciones)):
        for j in range(len(posiciones[i])):
            if posiciones[i][0] < 0 or posiciones[i][0] > 3 or posiciones[i][1] < 0 or posiciones[i][1] > 3:
                en_tablero = False
    return en_tablero

def es_movimiento_valido(tablero: list, jugador: int, posiciones: list) -> bool:
    """
    Verifica si la nueva posición de la ficha es válida. Recibe una lista que representa
    el tablero, el numero de jugador y una lista con las nuevas coordenadas de la ficha. Retorna un booleano.
    """
    es_valido = True
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if [i, j] in posiciones and tablero[i][j] != '*' and tablero[i][j] != jugador:
                es_valido = False
    return es_valido

def obtener_posicion(tablero: list, jugador: int) -> list:
    """
    Recibe una lista que representa el tablero y el numero de jugador. Recorre el tablero y
    devuelve las posiciones en las que se encuentra la ficha.
    """
    posiciones = []
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == jugador:
                posiciones.append([i,j])
    return posiciones

def obtener_extremo_columna(posiciones: list, direccion: str = 'm') -> int:
    """
    Recibe una lista con coordenadas y una cadena (opcional) y devuelve la columna máxima o mínima
    de entre esas coordenadas. Por defecto devuelve el mínimo valor, en caso de querer obtener
    el máximo valor, se debe indicar como parámetro adicional la cadena 'M'.
    """
    valor_columnas = []
    if direccion == 'M':
        for i in range(len(posiciones)):
            valor_columnas.append(posiciones[i][1])
        return max(valor_columnas)
    else:
        for i in range(len(posiciones)):
            valor_columnas.append(posiciones[i][1])
        return min(valor_columnas)

def copiar_matriz(tablero: list) -> list:
    copia = []
    for i in range(len(tablero)):
        copia.append([])
        for j in range(len(tablero[i])):
            copia[i].append(tablero[i][j])
    return copia

def colocar_ficha(tablero: list, jugador: int, posiciones: list) -> list:
    """
    Recibe una lista representando el tablero, el número de jugador(int) y las nuevas coordenadas de la ficha(lista).
    Inserta las coordenadas en el tablero y lo devuelve.
    """
    copia = copiar_matriz(tablero)
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if [i,j] in posiciones:
                copia[i][j] = jugador
            else:
                if tablero[i][j] == jugador:
                    copia[i][j] = '*'
                else:
                    copia[i][j] = tablero[i][j]
    return copia

def intercambiar_pos(posiciones: list) -> list:
    """
    Intercambia filas por columnas y las devuelve.
    """
    if str(posiciones[0]).isdigit(): #Si la posicion es una sola (No es lista de listas)
        pos_nuevas = [posiciones[1], posiciones[0]]
    else:
        pos_nuevas = []
        for i in range(len(posiciones)):
            pos_nuevas.append([posiciones[i][1], posiciones[i][0]])
    return pos_nuevas

def l_esta_horizontal(posiciones: list) -> bool:
    """
    Verifica si la ficha L se encuentra en posición horizontal.
    """
    esta_horizontal = True
    columnas = []
    for i in range(len(posiciones)):
        columnas.append(posiciones[i][1])
    for i in range(len(posiciones)):
        if columnas.count(posiciones[i][1]) == 3:
            esta_horizontal = False
    return esta_horizontal

def obtener_neutra(tablero: int, neutra: str) -> list:
    """
    Busca la posición de la ficha neutra seleccionada.
    """
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == neutra:
                return [i, j]
                
def buscar_extremo(posiciones: list) -> list:
    """
    Busca el extremo inferior de la ficha y devuelve la posicion. (La ficha debe estar vertical)
    """
    columnas = []
    indice = 0
    for i in range(len(posiciones)):
        columnas.append(posiciones[i][1])
    while columnas.count(posiciones[indice][1]) != 1:
        indice += 1
    return posiciones[indice]

def rotar_matriz(tablero: list) -> list:
    """
    Rota la matriz 90 grados, en sentido contrario a las agujas del reloj, y la devuelve.
    """
    copia = []
    for fila in tablero:
        fila = fila[::-1]
        copia.append(fila)
    return trasponer_matriz(copia)

def obtener_centro_L(posiciones: list) -> list:
    """
    Obtiene la coordenada del centro de rotación de la L y la devuelve.
    """
    pos_ant = []
    eje_central = []
    columnas = []
    columna_central = -1
    if l_esta_horizontal(posiciones):
        pos_ant = posiciones
        posiciones = intercambiar_pos(posiciones)
    for i in range(len(posiciones)):
        columnas.append(posiciones[i][1])
    if columnas.count(columnas[0]) == 3: #busco columna principal de L
        columna_central = columnas[0] #Si el primer valor no se repite, entonces el segundo sí.
    else:
        columna_central = columnas[1]
    for i in range(len(posiciones)):
        if posiciones[i][1] == columna_central:
            eje_central.append(posiciones[i])
    if pos_ant:
        if l_esta_horizontal(pos_ant):
            eje_central = intercambiar_pos(eje_central)
    return eje_central[1]

def mover_L(tablero: list, jugador: int, mov: str, posiciones: list = None) -> list:
    """
    Recibe una lista representando el tablero, el numero de jugador(int) y el movimiento(str) que realiza
    la ficha. Según el tipo de movimiento, desplaza las coordenadas de la ficha y las devuelve.
    """
    copia_tablero = copiar_matriz(tablero)
    if mov == 'A':
        if not posiciones:
            posiciones = obtener_posicion(copia_tablero, jugador)
        for i in range(len(posiciones)):
            posiciones[i][1] -= 1

    if mov == 'D':
        if not posiciones:
            posiciones = obtener_posicion(copia_tablero, jugador)
        for i in range(len(posiciones)):
            posiciones[i][1] += 1

    if mov == 'W': #Traspongo la matriz y muevo la ficha hacia la izq.
        if posiciones:
            posiciones = intercambiar_pos(posiciones)
        else:
            posiciones = obtener_posicion(trasponer_matriz(copia_tablero), jugador)
        for i in range(len(posiciones)):
            posiciones[i][1] -= 1
        posiciones = intercambiar_pos(posiciones) #Como la matriz está traspuesta intercambio filas por columnas y viceversa.

    if mov == 'S': #Traspongo la matriz y muevo la ficha hacia la der.
        if posiciones:
            posiciones = intercambiar_pos(posiciones)
        else:
            posiciones = obtener_posicion(trasponer_matriz(copia_tablero), jugador)
        for i in range(len(posiciones)):
            posiciones[i][1] += 1
        posiciones = intercambiar_pos(posiciones) #Si se sale del tablero, devuelvo las posiciones sin modificar.

    if mov == 'R':
        nueva_pos = []
        if not posiciones:
            posiciones = obtener_posicion(tablero, jugador)
        centro = obtener_centro_L(posiciones)
        nueva_pos.append(centro)
        if l_esta_horizontal(posiciones):
            nueva_pos.append([centro[0] + 1, centro[1]])
            nueva_pos.append([centro[0] - 1, centro[1]])
            extremo_inf = buscar_extremo(intercambiar_pos(posiciones))
            extremo_inf = [extremo_inf[1], extremo_inf[0]]
        else:
            extremo_inf = buscar_extremo(posiciones)
            nueva_pos.append([centro[0], centro[1] + 1])
            nueva_pos.append([centro[0], centro[1] - 1])
        if extremo_inf == [centro[0] + 1, centro[1] + 1]:
            nueva_pos.append([centro[0] - 1, centro[1] + 1])
        elif extremo_inf == [centro[0] - 1, centro[1] + 1]:
            nueva_pos.append([centro[0] - 1, centro[1] - 1])
        elif extremo_inf == [centro[0] - 1, centro[1] - 1]:
            nueva_pos.append([centro[0] + 1, centro[1] - 1])
        else:
            nueva_pos.append([centro[0] + 1, centro[1] + 1])
        posiciones = nueva_pos


    if mov == 'I':
        if not posiciones:
            posiciones = obtener_posicion(tablero, jugador)
        if l_esta_horizontal(posiciones): #Si esta horizontal traspongo la matriz para poder intercambiar filas.
            posiciones = intercambiar_pos(posiciones)
            extremo_inf = buscar_extremo(posiciones) 
            if obtener_extremo_columna(posiciones, 'M') == extremo_inf[1]:
                    posiciones[posiciones.index(extremo_inf)][1] -= 2
            else:
                    posiciones[posiciones.index(extremo_inf)][1] += 2
            posiciones = intercambiar_pos(posiciones)

        else:
            if not posiciones:
                posiciones = obtener_posicion(tablero, jugador)
            extremo_inf = buscar_extremo(posiciones)
            if obtener_extremo_columna(posiciones, 'M') == extremo_inf[1]: #Si la L mira hacia la derecha.
                posiciones[posiciones.index(extremo_inf)][1] -= 2
            else:
                posiciones[posiciones.index(extremo_inf)][1] += 2

    return posiciones

def mover_neutra(tablero: list, neutra: str, mov: str) -> list:
    """
    Devuelve la nueva posición de la ficha neutra.
    """
    posicion = obtener_neutra(tablero, neutra)
    if mov == 'A':
        if posicion[1] > 0:
            posicion[1] -= 1
    if mov == 'D':
        if posicion[1] < 3:
            posicion[1] += 1
    if mov == 'W':
        if posicion[0] > 0:
            posicion[0] -= 1 
    if mov == 'S':
        if posicion[0] < 3:
            posicion[0] += 1
    return posicion

def colocar_neutra(tablero: list, neutra: str, posicion: list) -> list:
    """
    Devuelve un nuevo tablero con la nueva posicion de la ficha neutra.
    """
    copia = copiar_matriz(tablero)
    pos_ant = obtener_neutra(tablero, neutra)
    copia[pos_ant[0]][pos_ant[1]] = '*'
    copia[posicion[0]][posicion[1]] = neutra
    return copia

def quedan_mov_validos(tablero: list, jugador: int) -> bool:
    """
    Recibe el tablero(list) y verifica que los espacios vacios sean consecutivos entre sí.
    """
    lista = []
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == '*' or tablero[i][j] == jugador:
                lista.append([i, j])
    hay_consecutivos = False
    continuos = []
    recorridos = 0
    while recorridos != 2:
        recorridos += 1
        copia_lista = copiar_matriz(lista)
        while len(continuos) != 3 and len(copia_lista) != 0:
            if recorridos == 2:
                tablero = trasponer_matriz(tablero)
                copia_lista = intercambiar_pos(copia_lista)
            continuos.append(copia_lista[0])
            ant = continuos[0]
            for i in range(len(copia_lista) - 1):
                if ant[1] + 1 == copia_lista[i+1][1] and ant[0] == copia_lista[i+1][0]:
                    continuos.append(copia_lista[i+1])
                    ant = copia_lista[i+1]
                    if len(continuos) == 3:
                        #Verifico los extremos
                        if existe_extremo_inf(tablero, continuos):
                            hay_consecutivos = True
            continuos = []
            copia_lista.pop(0)

    return hay_consecutivos

def existe_extremo_inf(tablero: list, coordenadas: list) -> bool:
    """
    Dada tres coordenadas consecutivas entre sí (horizontalmente), verifica si existen casilleros vacios en los extremos.
    Es decir, si existe un casillero vacio consecutivo a esas coordenadas tal que conformen una L.
    """
    extremo_inf = False
    posibles_extremos = [[coordenadas[0][0] + 1, coordenadas[0][1]], [coordenadas[0][0] - 1, coordenadas[0][1]],\
                        [coordenadas[2][0] + 1, coordenadas[2][1]], [coordenadas[2][0] - 1, coordenadas[2][1]]]
    for i in range(len(posibles_extremos)):
        if posibles_extremos[i][0] >= 0 and posibles_extremos[i][0] <= 3 and posibles_extremos[i][1] >= 0\
        and posibles_extremos[i][1] <= 3:
            if tablero[posibles_extremos[i][0]][posibles_extremos[i][1]] == '*':
                extremo_inf = True
    return extremo_inf