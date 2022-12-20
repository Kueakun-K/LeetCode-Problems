def canVisitAllRooms(rooms) -> bool:
    key = []
    def getKey(n):
        if rooms[n] != []:
            for k in rooms[n]:
                if k not in key:
                    key.append(k)
                    getKey(k)
        else:
            return
    getKey(0)
    try:
        key.remove(0)
        return True if len(key) == len(rooms) - 1 else False
    except:
        return True if len(key) == len(rooms) - 1 else False
        
rooms = [[1,3],[3,0,1],[2],[0]]
print(canVisitAllRooms(rooms))