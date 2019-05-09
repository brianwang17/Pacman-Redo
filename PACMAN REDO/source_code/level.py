from .levelbase import Level

class CurrentLevel(Level):
    """Level 1 of the PyMan Game"""

    def __init__(self,ai_settings,level_cho):
        self.BLOCK = 1
        self.PACMAN = 2
        self.PELLET = 0
        self.POWER_PELLET = 3
        self.REDGHOST = 4
        self.BLUEGHOST = 5
        self.ORANGEGHOST = 6
        self.PINKGHOST = 7
        self.SCAREDGHOST = 8
        self.ai_settings = ai_settings
        self.level_cho = level_cho

    def getLayout(self):
        name = "/levels/" + self.level_cho
        file = open(name,"r")
        rows = file.readlines()
        file.close()

        layout = [[0]*24]*24
        row_num = 0

        for row in rows:
            for index in range(len(row)):
                layout[row_num][index] = row[index]
            row_num+=1
        return layout

    def getSprites(self):
        block, rect = self.ai_settings.blue_block_image
        pellet, rect = self.ai_settings.pellet_image
        pacman, rect = self.ai_settings.pacman_right_image
        power_pellet, rect = self.ai_settings.power_pellet_image
        power_pellet, rect = self.ai_settings.power_pellet_image
        red_ghost, rect = self.ai_settings.red_ghost_image
        blue_ghost, rect = self.ai_settings.blue_ghost_image
        orange_ghost, rect = self.ai_settings.orange_ghost_image
        pink_ghost, rect = self.ai_settings.pink_ghost_image
        scared_ghost, rect = self.ai_settings.scared_ghost_image
        return [pellet,block,pacman,power_pellet,red_ghost,blue_ghost,orange_ghost,pink_ghost,scared_ghost]
