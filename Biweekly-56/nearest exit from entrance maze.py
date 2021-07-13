
def nearestExit(maze, entrance):
    # Creating a queue for BFS
    queue = []
    queue.append(entrance)
    
    moves = 1
    rows = len(maze)
    columns = len(maze[0])
    # All Available movements
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # Setting the entrace as visited
    maze[entrance[0]][entrance[1]] = '+'
    # As long as queue is not empty
    while(queue):
        l = len(queue)
        # Now exploring every element in the queue
        for k in range(0, l):
            [i, j] = queue.pop(0)
            # Trying all possible directions
            for t in range(0, 4):
                x = i + directions[t][0]
                y = j + directions[t][1]
                # Invalid position
                if(x < 0 or y < 0 or x >= rows or y >= columns or maze[x][y] == '+'):
                    continue
                # Exit Reached
                elif(x == 0 or y == 0 or x == rows -1 or y == columns -1 ):
                    return moves
                # Mark as Visited
                maze[x][y] = '+'
                queue.append([x, y])
        moves += 1
    return -1