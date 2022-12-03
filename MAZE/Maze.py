from maze_finder import find_closest_gate
from check_dead_way import MazeWayError, DeleteDeadWay
from data_visual import visual_maze


def enter_matrix() -> tuple:
    start_matrix = """  #........#
                        #......###
                        #####.####
                        #.......##
                        #####.####
                        #.......##
                        #......###
                        #..###...#
                        #.....####
                        ####.#####
                        ##....####
                        ##########  """
    start_point = [5, 6]
    gate_symbol = "."
    return start_matrix, start_point, gate_symbol


def main_finder(gate: str = ".") -> str:
    enter = enter_matrix()[1]
    start_matrix = [level.split() for level in enter_matrix()[0].split()]
    clean_matrix = DeleteDeadWay(enter, start_matrix).calculating()
    x_line = [enter[1]]
    result = []
    for number, item in enumerate(clean_matrix, start=enter[0]):
        if gate in item[0]:
            x_line.append(find_closest_gate(item, x_line[-1]))
            result.append([number, x_line[-1]])
        else:
            raise MazeWayError
    if clean_matrix[-1] == start_matrix[0]:
        number = 0
        for elem in result:
            elem[0] = elem[0] - number
            number += 2
    visual_maze(result)
    return f"Your finish is on {result[-1]}"


print(main_finder())
