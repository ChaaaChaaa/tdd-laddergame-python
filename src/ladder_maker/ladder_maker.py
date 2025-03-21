from src.ladder_maker import random_line_maker


class LadderMaker:
    def __init__(self, participate, ladder_height):
        self.participate = participate
        self.ladder_participate_count = len(participate)
        self.seperator = "-" * self.ladder_participate_count
        self.ladder_height = ladder_height

    def make_width(self):
        ladder_structure = []
        for _ in range(self.ladder_height):
            segment = [self.seperator if random_line_maker.make_random_line(
                self.ladder_participate_count) == self.ladder_participate_count
                       else " " * self.ladder_participate_count for _ in
                       range(self.ladder_participate_count - 1)]
            ladder_structure.append(segment)
        return ladder_structure
