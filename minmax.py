import math
def minmax(gdepth, nodevalue, maxTurn, utility, targetDepth):
    if gdepth == targetDepth:
        return utility[nodevalue]

    if maxTurn:
        return max(
            minmax(gdepth + 1, nodevalue * 2, False, utility, targetDepth),
            minmax(gdepth + 1, nodevalue * 2 + 1, False, utility, targetDepth)
        )
    else:
        return min(
            minmax(gdepth + 1, nodevalue * 2, True, utility, targetDepth),
            minmax(gdepth + 1, nodevalue * 2 + 1, True, utility, targetDepth)
        )

utility = [-1, 4, 2, 6, -3, -5, 0, 7]
treeDepth = int(math.log(len(utility), 2))
print("The optimal value is:", minmax(0, 0, True, utility, treeDepth))