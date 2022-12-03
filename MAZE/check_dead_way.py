class MazeWayError(Exception):
    pass


class GateMazeError(Exception):
    pass


class DeleteDeadWay:
    final_matrix = []

    def __init__(self, enter: list,
                 matrix: list,
                 gate: str = ".") -> final_matrix:
        self.enter = enter
        self.matrix = matrix
        self.gate = gate
        self.y_line = enter[0]
        self.x_line = enter[1]

    def way_in_the_end(self) -> final_matrix:
        DeleteDeadWay.final_matrix = self.matrix[self.y_line:]
        return DeleteDeadWay.final_matrix

    def way_in_the_start(self) -> final_matrix:
        DeleteDeadWay.final_matrix = self.matrix[: self.y_line + 1]
        return DeleteDeadWay.final_matrix[::-1]

    def check_deadlock(self, matrix: list) -> bool:
        for row in matrix:
            if self.gate not in row[0]:
                return False

        return True

    def we_have_two_ways(self):
        if self.y_line >= len(self.matrix) / 2 \
                and self.y_line != len(self.matrix) - 1:
            if self.check_deadlock(self.matrix[self.y_line:]):
                return self.way_in_the_end()
        if self.y_line == 0:
            return self.way_in_the_end()
        else:
            return self.way_in_the_start()

    def calculating(self):
        if self.matrix[self.y_line][0][self.x_line] != self.gate:
            raise GateMazeError(f"Your start point should be '{self.gate}'")
        if self.gate not in self.matrix[0][0] \
                and self.gate not in self.matrix[-1][0]:
            raise MazeWayError("It`s impossible to find the way ...")

        if self.gate in self.matrix[0][0] \
                and self.gate in self.matrix[-1][0]:
            return self.we_have_two_ways()
        if self.gate not in self.matrix[0][0] \
                and self.y_line != len(self.matrix) - 1:
            return self.way_in_the_end()
        if self.gate not in self.matrix[-1][0] and self.y_line != 0:
            return self.way_in_the_start()
        raise MazeWayError("It`s impossible to find the way ...")
