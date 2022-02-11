import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

size = 0
graph = []
while True:
    try:
        graph.append(int(input()))
        size += 1
    except:
        break

def postorder_by_preorder(start, end, graph):
    if start > end:
        return
    
    div = start+1
    while div <= end and graph[start] > graph[div]:
        div += 1
    postorder_by_preorder(start+1, div-1, graph)
    postorder_by_preorder(div, end, graph)
    print(graph[start])
    
postorder_by_preorder(0, size-1, graph)