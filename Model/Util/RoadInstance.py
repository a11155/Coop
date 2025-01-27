from math import hypot, atan, copysign
from .LineInstance import Line
from math import pi

class Road:
    def __init__(self, nodes, start_node, end_node, number_of_lines):
        self.n_lines = number_of_lines
        self.start_node = start_node
        self.end_node = end_node
        dx = nodes[start_node].apos[0] - nodes[end_node].apos[0]
        dy = nodes[start_node].apos[1] - nodes[end_node].apos[1]
        self.length = int(hypot(dx, dy))
        self.angle = atan((dy / dx)) if dx != 0 else copysign(pi / 2, dy)
        self.lines = {start_node: [], end_node: []}

        if number_of_lines == 1:
            self.lines[start_node] = [(Line(start_node, end_node, self))]
        else:
            for i in range(number_of_lines // 2):
                line = Line(start_node, end_node, self)
                self.lines[start_node].append(line)

            for i in range(number_of_lines // 2, number_of_lines):
                line = Line(end_node, start_node, self)
                self.lines[end_node].append(line)

    def __str__(self):
        return "Road: " + str(self.start_node) + ' ' + str(self.end_node)
