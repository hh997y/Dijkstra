def dijkstra(graph):
    l = len(graph)
    visit = [i for i in range(6)]
    current = visit[0]
    path = {}
    res = {}
    # 0到各个点的初始值
    for i in range(l):
        res[i] = graph[0][i]
        path[i] = '0->{}'.format(i)
    while visit:
        dtmp = []
        for i in range(l):
            if current != i:
                # 松弛操作
                if (res[current] + graph[current][i]) < res[i]:
                    res[i] = res[current] + graph[current][i]
                    path[i] = path[current] + '->{}'.format(i)
                # 记录当前点到周围点的距离，并排序
                if not dtmp:
                    dtmp.append([i, graph[current][i]])
                else:
                    f = 0
                    for j in range(len(dtmp)):
                        if graph[current][i] < dtmp[j][1]:
                            dtmp.insert(j, [i, graph[current][i]])
                            f = 1
                            break
                    if f == 0:
                        dtmp.append([i, graph[current][i]])
        for i in dtmp:
            if i[0] not in visit:
                dtmp = dtmp[1:]
            else:
                visit.remove(i[0])
                current = i[0]
                break
        # print(dtmp)
        # print(current,res)
    return res, path


if __name__ == '__main__':
    graph = [[0, 2, 1, 4, 5, 1],
             [1, 0, 4, 2, 3, 4],
             [2, 1, 0, 1, 2, 4],
             [3, 5, 2, 0, 3, 3],
             [2, 4, 3, 4, 0, 1],
             [3, 4, 7, 3, 1, 0]]

    res, path = dijkstra(graph)
    print(res)
    print(path)