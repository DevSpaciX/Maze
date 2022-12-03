from Maze import main_finder
from check_dead_way import MazeWayError, GateMazeError
import pytest
from unittest import mock


class TestMazeWay:
    @pytest.mark.parametrize(
        "matrix, enter, result",
        [
            (
                """  #........#
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
                     ##########  """,
                [5, 6],
                [0, 5],
            ),
            (
                """  #........#
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
                     ######.###  """,
                [0, 6],
                [11, 6],
            ),
            (
                """  #........#
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
                     ######.###  """,
                [11, 6],
                [0, 5],
            ),
            (
                """  #........#
                     #......###
                     #####.####
                     #.......##
                     #####.####
                     #.......##
                     #......###
                     #..###...#
                     #.....####
                     ####.#####
                     ##########
                     ######.###  """,
                [9, 4],
                [0, 5],
            ),
            (
                """  #........#
                     #......###
                     #####.####
                     #.......##
                     #####.####
                     #.......##
                     #......###
                     #..###...#
                     #.....####
                     ####.#####
                     ##.#######
                     ######.###  """,
                [0, 4],
                [11, 6],
            ),
            (
                """  #........#
                     #......###
                     #####.####
                     #.......##
                     #####.####
                     #.......##
                     #......###
                     #..###...#
                     #.....####
                     ##########
                     ##.#######
                     ######.###  
                     ########## """,
                [6, 4],
                [0, 5],
            ),
        ],
    )
    @mock.patch("Maze.enter_matrix")
    def test_check_if_maze_ok(self,
                              enter_matrix_mock: tuple,
                              matrix: str, enter: list,
                              result: list) -> None:
        enter_matrix_mock.return_value = (matrix, enter)
        assert main_finder() == f"Your finish is on {result}"


class TestMazeWayError:
    @pytest.mark.parametrize(
        "matrix, enter, error",
        [
            (
                """  ##########
                     #......###
                     #####.####
                     #.......##
                     #####.####
                     #.......##
                     #......###
                     #..###...#
                     #.....####
                     ##########
                     ##.#######
                     ######.###  
                     ########## """,
                [6, 4],
                MazeWayError,
            ),
            (
                """  ##########
                     #......###
                     #####.####
                     #.......##
                     #####.####
                     #.......##
                     #......###
                     #..###...#
                     #.....####
                     ##########
                     ##.#######
                     ######.###  
                     ########## """,
                [4, 1],
                GateMazeError,
            ),
        ],
    )
    @mock.patch("Maze.enter_matrix")
    def test_check_if_maze_is_raise_error(
        self,
            enter_matrix_mock: tuple,
            matrix: str,
            enter: list,
            error: Exception
    ) -> None:
        enter_matrix_mock.return_value = (matrix, enter)
        with pytest.raises(error):
            main_finder()
