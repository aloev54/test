class Ship:
    def __init__(self, cells):
        self.cells = cells
        self.hits = set()
        self.is_sunk = False

    def mark_hit(self, x, y):
        if (x, y) in self.cells:
            self.hits.add((x, y))
            self.is_sunk = self.hits == set(self.cells)
            return True
        return False
