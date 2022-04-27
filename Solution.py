import time
from queue import Queue

def Maze_Input(input_file):
    lines = []
    with open(input_file) as file:
        lines = [line.strip() for line in file]

    if '' in lines:
        lines.remove('')

    maze_size = 0
    maze = []
    temp = []
    for i in range(0, len(lines)):
        if i == 0:
            maze_size = int(lines[i])
        else:
            temp.append(int(lines[i]))
            if i % maze_size == 0:
                maze.append(temp)
                temp = []
    return maze, maze_size

def NumberOfMoves(maze, sx, sy, dx, dy):
    visited = [[False for i in range(len(maze))] for j in range(len(maze))]
    q = Queue()
    visited[sx][sy] = True
    node = {'x': sx, 'y': sy, 'val': maze[sx][sy], 'min_dist': 0}
    q.put(node)
    minmove = float("inf")
    while not q.empty():
        node = q.get()
        cx = node['x']
        cy = node['y']
        dist = node['min_dist']
        if cx == dx and cy == dy:
            minmove = dist
            break
        current_value = maze[cx][cy]
        if current_value >= 0:
            nx = cx
            ny = cy - current_value
            if is_valid_move(maze, visited, nx, ny):
                visited[nx][ny] = True
                node = {
                    'x': nx,
                     'y': ny,
                    'val': maze[nx][ny], 
                    'min_dist': dist + 1
                    }
                q.put(node)
            nx = cx
            ny = cy + current_value
            if is_valid_move(maze, visited, nx, ny):
                visited[nx][ny] = True
                node = {
                    'x': nx, 
                    'y': ny,
                    'val': maze[nx][ny],
                    'min_dist': dist + 1
                    }
                q.put(node)
            nx = cx - current_value
            ny = cy
            if is_valid_move(maze, visited, nx, ny):
                visited[nx][ny] = True
                node = {
                    'x': nx, 
                    'y': ny,
                    'val': maze[nx][ny],
                    'min_dist': dist + 1}
                q.put(node)
            nx = cx + current_value
            ny = cy
            if is_valid_move(maze, visited, nx, ny):
                visited[nx][ny] = True
                node = {
                    'x': nx, 
                    'y': ny,
                    'val': maze[nx][ny],
                    'min_dist': dist + 1}
                 q.put(node)
    return minmove

def is_valid_move(maze, visited, rno, cno):
    if 0 <= rno < len(maze) \
            and 0 <= cno < len(maze)\
            and not visited[rno][cno]:
        return True
    return False
if __name__ == '__main__':
    input_file = input("Enter path to input file: ")
    start_time = time.time()
    maze, maze_size = Maze_Input(input_file)
    minmove = NumberOfMoves(maze, 0, 0, maze_size - 1, maze_size - 1)
    if minmove != float("inf"):
        print("Minimum number of moves: " + str(minmove))
    else:
        print("Destination can't be reached from given source")
    end_time = time.time()
    elapsed_time = float((end_time - start_time) * 1000)
    print("Total time taken (milliseconds) : " + str(elapsed_time))


