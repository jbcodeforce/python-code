

max_length = 0

def maxLengthPath(park,r,c):
    max_length = 0
    visited=[[]]
    return maxLengthPathR(max_length,park,visited,r,c)

def maxLengthPathR(max_length,park,visited,r,c):
    if r < 0 : 
        return 0
    if c < 0:
        return 0
    if not park[r][c]:
        return 0
    visited[r][c]= True
    if not visited[r][c+1]:
        m1=maxLengthPathR(max_length,park,visited,r,c+1)
    if m1>max_length:
        max_length = m1
    return max_length

print(maxLengthPath([[True,False,False]],0,0))
assert maxLengthPath([[False,False,False]],0,0) == 0
assert maxLengthPath([[True,False,False]],0,0) == 1
assert maxLengthPath([[True,True,False]],0,0) == 2
assert maxLengthPath([[True,True,False]],0,1) == 2
