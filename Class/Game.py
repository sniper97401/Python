class Game:
    pseudo = None
    level = None
    step = None
    gain = None
    mise = None

    def __init__(self,pseudo,level,step,gain,mise):
        self.step = step
        self.gain = gain
        self.mise = mise
        self.level = level
        self.pseudo = pseudo