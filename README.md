# Dijkstra
Dijkstra by python

参考：https://blog.csdn.net/lbperfect123/article/details/84281300

思路：

1. 首先遍历一边图上各点，找出起点到其它可达点之间的距离，并储存下来。

2. 然后开始算法主体：遍历整个图，计算每一个点到其它点的距离。若当前点a到其它某点b的距离加上起点s到点a的距离，小于起点s直接到点b的距离，那么就对起点a到b的距离做松弛操作，更新其最短距离，并且更新最短路径。

3. 在未遍历过的点中，选择与当前点距离最近的一个点，作为下一次的遍历点，继续开始步骤2的遍历。

4. 当所有点遍历完成，即得到最后的答案。
