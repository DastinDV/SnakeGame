from pygame.rect import Rect
import enum

class Direction(enum.Enum):
    Left = [-1, 0]
    Right = [1, 0]
    Down = [0, 1]
    Up = [0, -1]

class Snake():
    __step = 32

    def __init__(self, posX, posY):
        self.__bodyList = []
        self.__head = Rect(posX, posY, self.__step, self.__step)
        self.__bodyList.append(self.__head)
        self.__bodyList.append(Rect(posX-32, posY, self.__step, self.__step))
        self.__bodyList.append(Rect(posX-64, posY, self.__step, self.__step))
        self.__bodyList.append(Rect(posX-96, posY, self.__step, self.__step))
        self.__posX = posX
        self.__posY = posY

    def move(self, direction):
        prevPosX = self.__posX
        prevPosY = self.__posY
        self.__posX = self.__posX + (self.__step * direction[0])
        self.__posY = self.__posY + (self.__step * direction[1])
        self.__head.x = self.__posX
        self.__head.y = self.__posY

        for i, node in enumerate(self.__bodyList):
            print(i)
            if i == 0:
                continue
            
            bufPrevPosX = node.x
            bufPrevPosY = node.y

            node.x = prevPosX
            node.y = prevPosY

            prevPosX = bufPrevPosX
            prevPosY = bufPrevPosY

    def getBody(self):
        return self.__bodyList
        

