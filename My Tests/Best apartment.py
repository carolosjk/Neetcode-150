from typing import List

def bestApartment(blocks: List[dict], preferences: List[str]) -> int:

    distances = [{} for _ in range(len(blocks))]

    for i,block in enumerate(blocks):
        for p in preferences:
            if i == 0:
                distances[i][p] = 0 if block[p] == True else float("inf")
            else:
                distances[i][p] = 0 if block[p] == True else distances[i-1][p] + 1
        
        print(distances[i])

    print("--------SECOND RUN--------")

    blockWithMinDistance = None
    minDistance = float("inf")

    for i in range(len(blocks)-1,0,-1):
        block = blocks[i]

        if i == len(blocks)-1:
            blockWithMinDistance = 0
            minDistance = max(distances[i].values())
        else:
            for p in preferences:
                distances[i][p] = min(distances[i][p],distances[i+1][p]+1)
            
            if minDistance > max(distances[i].values()):
                minDistance = max(distances[i].values())
                blockWithMinDistance = i
    
        
        print(distances[i],blockWithMinDistance,minDistance)
    return blockWithMinDistance

        

    return 0


if __name__ == "__main__":

    print(bestApartment(
        [
            {"gym": True, "store": False, "office": False},
            {"gym": False, "store": True, "office": False},
            {"gym": False, "store": False, "office": False},
            {"gym": False, "store": False, "office": True},
            {"gym": True, "store": False, "office": True},
            {"gym": False, "store": False, "office": True},
            {"gym": True, "store": False, "office": False},
        ], 
        ["gym", "office","store"]
    ))