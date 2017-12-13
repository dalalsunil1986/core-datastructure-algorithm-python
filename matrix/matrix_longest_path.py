import sys


def find_path_length_and_elevation(x, y, lengths, elevations):
    if lengths[x][y] > 0:
        return lengths[x][y], elevations[x][y]

    elevations[x][y] = matrix[x][y]
    for dx, dy in ((+1, 0), (-1, 0), (0, +1), (0, -1)):
        if 0 <= x + dx < len(matrix) and 0 <= y + dy < len(matrix[x]) and matrix[x + dx][y + dy] < matrix[x][y]:
            length, elevation_end = find_path_length_and_elevation(x + dx, y + dy, lengths, elevations)
            if length > lengths[x][y] or (length == lengths[x][y] and elevation_end < elevations[x][y]):
                lengths[x][y], elevations[x][y] = length, elevation_end

    lengths[x][y] = lengths[x][y] + 1
    return lengths[x][y], elevations[x][y]

if __name__ == "__main__":
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'test_0.txt', 'r')
    rows, cols = map(int, f.readline().split(' '))
    matrix = [list(map(int, line.split(' '))) for i,line in enumerate(f)]
    lengths = [cols*[0] for i in range(rows)]
    elevations = [cols*[0] for i in range(rows)]
    length_longest = -1
    drop_steepest = -1

    for x, row in enumerate(matrix):
        for y, elevation_start in enumerate(row):
            length, elevation_end = find_path_length_and_elevation(x, y, lengths, elevations)
            drop = elevation_start - elevation_end

            if length > length_longest or (length == length_longest and drop > drop_steepest):
                length_longest = length
                drop_steepest = drop

    print("Longest path: {0}, steepest drop: {1}".format(length_longest, drop_steepest))