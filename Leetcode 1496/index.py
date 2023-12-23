class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y=0,0
        points = [(0,0)]
        for dir in path:
            if dir == 'N':
                y+=1
            elif dir == 'S':
                y-=1
            elif dir == 'E':
                x+=1
            else :
                x-=1
            if (x,y) in points:
                return True
            else:
                points.append((x,y))

        return False
