class Game:
    level = None
    step = None
    gain = None
    mise = None

    def __init__(self,level,step,gain,mise):
        self.step = step
        self.gain = gain
        self.mise = mise
        self.level = level