import random

def generate_maze(m, n, room=0, wall=1, cheese='.'):
    """Gera um labirinto utilizando DFS iterativo."""

    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Cada item guarda a sala atual, suas direções e a próxima direção.
    pilha = []

    maze[1][1] = room
    direcoes_iniciais = directions.copy()
    random.shuffle(direcoes_iniciais)
    pilha.append((0, 0, direcoes_iniciais, 0))

    while pilha:
        x, y, direcoes_atuais, indice = pilha[-1]
        if indice == len(direcoes_atuais):
            pilha.pop()
            continue

        # Guarda que esta direção já foi analisada.
        pilha[-1] = (x, y, direcoes_atuais, indice + 1)

        dx, dy = direcoes_atuais[indice]
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            if maze[2 * nx + 1][2 * ny + 1] == wall:
                # Derruba a parede entre as duas salas.
                maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
                maze[2 * nx + 1][2 * ny + 1] = room
                novas_direcoes = directions.copy()
                random.shuffle(novas_direcoes)
                pilha.append((nx, ny, novas_direcoes, 0))

    # O queijo é colocado em uma sala, e não em uma parede.
    while True:
        i = random.randrange(1, 2 * m, 2)
        j = random.randrange(1, 2 * n, 2)
        if maze[i][j] == room:
            maze[i][j] = cheese
            break
    return maze

def print_maze(maze):
    """Imprime o labirinto no terminal."""
    for row in maze:
        print(" ".join(map(str, row)))

def find_cheese(maze, cheese='.'):
    """Retorna as coordenadas do queijo ou None se ele não existir."""
    for i, row in enumerate(maze):
        for j, element in enumerate(row):
            if element == cheese:
                return i, j
    return None

def solve_maze(maze, start=(1, 1), cheese='.'):
    """Encontra um caminho entre start e o queijo utilizando DFS iterativo."""
    goal = find_cheese(maze, cheese)
    if goal is None:
        return None

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pilha = [start]
    visitados = {start}
    pais = {start: None}

    while pilha:
        atual = pilha.pop()
        if atual == goal:
            break
        x, y = atual
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < len(maze) and 0 <= ny < len(maze[nx])):
                continue
            vizinho = (nx, ny)
            # Paredes não podem ser atravessadas.
            if maze[nx][ny] == 1 or vizinho in visitados:
                continue
            visitados.add(vizinho)
            pais[vizinho] = atual
            pilha.append(vizinho)
    if goal not in pais:
        return None

    # Reconstrói o caminho do queijo até o início.
    caminho = []
    atual = goal
    while atual is not None:
        caminho.append(atual)
        atual = pais[atual]
    caminho.reverse()
    return caminho

def print_maze_with_path(maze, path=None, start=(1, 1), cheese='.'):
    """Exibe o labirinto usando blocos coloridos e destaca o caminho."""
    vermelho = '\033[41m'
    branco = '\033[47m'
    verde = '\033[42m'
    amarelo = '\033[43m'
    reset = '\033[0m'

    labirinto_visual = [row.copy() for row in maze]
    posicao_queijo = find_cheese(maze, cheese)
    if path is not None:
        for i, j in path:
            if (i, j) != start and (i, j) != posicao_queijo:
                labirinto_visual[i][j] = '*'
    for i, row in enumerate(labirinto_visual):
        linha = ''
        for j, elemento in enumerate(row):
            if (i, j) == start: linha += verde + '  ' + reset
            elif (i, j) == posicao_queijo: linha += amarelo + 'X ' + reset
            elif elemento == '*': linha += verde + '  ' + reset
            elif elemento == 1: linha += vermelho + '  ' + reset
            else: linha += branco + '  ' + reset
        print(linha)

if __name__ == '__main__':
    m, n = 10, 14
    random.seed(10110)
    maze = generate_maze(m, n)
    print('\nLabirinto gerado com DFS iterativo:\n')
    print_maze_with_path(maze)
    path = solve_maze(maze, start=(1, 1))
    print('\nLabirinto resolvido:\n')
    print_maze_with_path(maze, path, start=(1, 1))
    if path is not None:
        print(f'\nTamanho do caminho: {len(path)}')
    else:
        print('\nNenhum caminho encontrado.')