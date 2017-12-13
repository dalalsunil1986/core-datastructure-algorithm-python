import sys

def find_path_length_and_elevation(x, y, path_lengths, elevations_end):
    if path_lengths[x][y] > 0:
        return path_lengths[x][y], elevations_end[x][y]

    elevations_end[x][y] = matrix[x][y]
    for dx, dy in ((+1, 0), (-1, 0), (0, +1), (0, -1)):
        if 0 <= x + dx < len(matrix) and 0 <= y + dy < len(matrix[x]) and matrix[x + dx][y + dy] < matrix[x][y]:
            length, elevation_end = find_path_length_and_elevation(x + dx, y + dy, path_lengths, elevations_end)
            if length > path_lengths[x][y] or (length == path_lengths[x][y] and elevation_end < elevations_end[x][y]):
                path_lengths[x][y], elevations_end[x][y] = length, elevation_end

    path_lengths[x][y] = path_lengths[x][y] + 1
    return path_lengths[x][y], elevations_end[x][y]

if __name__ == "__main__":
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'test_0.txt', 'r')
    rows, cols = map(int, f.readline().split(' '))
    matrix = [list(map(int, line.split(' '))) for i,line in enumerate(f)]
    path_lengths = [cols*[0] for i in range(rows)]
    elevations_end = [cols*[0] for i in range(rows)]
    path_length_longest = -1
    drop_steepest = -1

    for x, row in enumerate(matrix):
        for y, elevation_start in enumerate(row):
            path_length, elevation_end = find_path_length_and_elevation(x, y, path_lengths, elevations_end)
            drop = elevation_start - elevation_end
            if path_length > path_length_longest or (path_length == path_length_longest and drop > drop_steepest):
                path_length_longest = path_length
                drop_steepest = drop

    print("Longest path: {0}, steepest drop: {1}".format(path_length_longest, drop_steepest))