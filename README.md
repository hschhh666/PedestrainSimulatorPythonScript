这里面就杂七杂八了，可能后续代码会改得飞起，不过不重要，主要是让我知道曾经有这些东西就行了。

简单来说一下这里面主要做的一些工作吧，这里只说最重要的`pedestrainMatrix`是如何生成的，生成方式就是论文里描述的，很简单。至于别的文件看看源码肯定也没啥问题，都是很简单的脚本。


* `createBaseMatrix.py` 随机生成nxn的矩阵，没有任何输入。矩阵所有元素之和为1。具体看里面的注释就好了。
* `createRealMatrix.py` 输入是上面的随机矩阵，里面会生成`PN`和`FD`。输出的是`pedestrainMatrix`。这种方式会保证在校门口生成的人数占比就是`FD`，但是从校门口到校内其他各个点的人数占比则是随机的，同样，出校门的人数占比是`1-FD`，但是人是从校内哪个点生成的则是随机的，这个随机性是由`createBaseMatrix.py`决定的。

`pedestrainMatrix`的生成方式可以改的，现在的方式太简单，后面可以改复杂点。