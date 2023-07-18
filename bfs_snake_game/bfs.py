
import collections

# BFS algoritması
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Kuyruktan bir tepe noktasını çıkarıldı
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # Ziyaret edilmediyse, ziyaret edildi olarak işaretleyin
        # enqueue it: kuyruğa alındı
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)