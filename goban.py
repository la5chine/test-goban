import enum


class Status(enum.Enum):
    """
    Enum representing the Status of a position on a goban
    """

    WHITE = 1
    BLACK = 2
    EMPTY = 3
    OUT = 4


class Goban(object):
    def __init__(self, goban):
        self.goban = goban

    def get_status(self, x, y):
        """
        Get the status of a given position

        Args:
            x: the x coordinate
            y: the y coordinate

        Returns:
            a Status
        """
        if (
            not self.goban
            or x < 0
            or y < 0
            or y >= len(self.goban)
            or x >= len(self.goban[0])
        ):
            return Status.OUT
        elif self.goban[y][x] == ".":
            return Status.EMPTY
        elif self.goban[y][x] == "o":
            return Status.WHITE
        elif self.goban[y][x] == "#":
            return Status.BLACK

    def is_taken(self, x, y, visited=None) -> bool:
        """
        Get whether a given position is taken or not

        Args:
            x: the x coordinate
            y: the y coordinate
            visited (optional): visited nodes

        Returns:
            a Boolean
        """
        current_status = self.get_status(x, y)
        if visited is None:
            if current_status in [Status.EMPTY, Status.OUT]:
                return False
            visited = set()

        visited |= {(x, y)}
        adjacent_positions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for adjacent_position in adjacent_positions:
            if adjacent_position in visited:
                continue
            adjacent_status = self.get_status(*adjacent_position)
            if adjacent_status == Status.EMPTY:
                return False
            if adjacent_status == Status.OUT:
                continue
            if adjacent_status == current_status:
                return self.is_taken(*adjacent_position, visited=visited)
        return True
