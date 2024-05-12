## Table of Contents + Main Results
### Lab 0: Recursion Examples
### Lab 1: Searching Algorithms

|                                                                                                     Depth First Search                                                                                                      |                                                                                                    Breadth First Search                                                                                                     |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![COMPUTATIONAL_BIOLOGY/lab1-Searching-Heuristics/gifs/dfs.gif at main · MaximoRdz/COMPUTATIONAL_BIOLOGY (github.com)](https://github.com/MaximoRdz/COMPUTATIONAL_BIOLOGY/blob/main/lab1-Searching-Heuristics/gifs/dfs.gif) | ![COMPUTATIONAL_BIOLOGY/lab1-Searching-Heuristics/gifs/bfs.gif at main · MaximoRdz/COMPUTATIONAL_BIOLOGY (github.com)](https://github.com/MaximoRdz/COMPUTATIONAL_BIOLOGY/blob/main/lab1-Searching-Heuristics/gifs/bfs.gif) |

|                                                                                                                  Hill Climbing                                                                                                                  |                                                                                                                 Beam Search                                                                                                                 |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![COMPUTATIONAL_BIOLOGY/lab1-Searching-Heuristics/gifs/hill_climbing.gif at main · MaximoRdz/COMPUTATIONAL_BIOLOGY (github.com)](https://github.com/MaximoRdz/COMPUTATIONAL_BIOLOGY/blob/main/lab1-Searching-Heuristics/gifs/hill_climbing.gif) | ![COMPUTATIONAL_BIOLOGY/lab1-Searching-Heuristics/gifs/beam_search.gif at main · MaximoRdz/COMPUTATIONAL_BIOLOGY (github.com)](https://github.com/MaximoRdz/COMPUTATIONAL_BIOLOGY/blob/main/lab1-Searching-Heuristics/gifs/beam_search.gif) |

|                                                                                                       Branch and Bound (Best First Search)                                                                                                        |                                                                                                               A $^{*}$                                                                                                               |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![COMPUTATIONAL_BIOLOGY/lab1-Searching-Heuristics/gifs/branch_n_bound.gif at main · MaximoRdz/COMPUTATIONAL_BIOLOGY (github.com)](https://github.com/MaximoRdz/COMPUTATIONAL_BIOLOGY/blob/main/lab1-Searching-Heuristics/gifs/branch_n_bound.gif) | ![COMPUTATIONAL_BIOLOGY/lab1-Searching-Heuristics/gifs/a_star.gif at main · MaximoRdz/COMPUTATIONAL_BIOLOGY (github.com)](https://github.com/MaximoRdz/COMPUTATIONAL_BIOLOGY/blob/main/lab1-Searching-Heuristics/gifs/a_star.gif) |

$$A^{*} = \text{branch and bound} + \text{extended set} + \text{admissible heuristic}$$
### Lab 2: Games search
Minimax + alpha-beta + progressive deepening implementation on a simple game
#### TODO
- [ ] Connect four game
- [ ] Game visualization
### Lab 3: Constraints and Domain reduction
Applicable to resource optimization problems (i.e. flights scheduling)
Graph coloring example, no two connected nodes can share the same color. The algorithm will only converge if there are enough resources (3 vs 4 colors available).

| 3 colors                                                                                                                                                                                                                                                                            | 4 colors                                                                                                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![COMPUTATIONAL_BIOLOGY/lab3-Constraints-Domain-Reduction/gifs/graph_coloring_3_colors.gif at main · MaximoRdz/COMPUTATIONAL_BIOLOGY (github.com)](https://github.com/MaximoRdz/COMPUTATIONAL_BIOLOGY/blob/main/lab3-Constraints-Domain-Reduction/gifs/graph_coloring_3_colors.gif) | ![COMPUTATIONAL_BIOLOGY/lab3-Constraints-Domain-Reduction/gifs/graph_coloring_4_colors.gif at main · MaximoRdz/COMPUTATIONAL_BIOLOGY (github.com)](https://github.com/MaximoRdz/COMPUTATIONAL_BIOLOGY/blob/main/lab3-Constraints-Domain-Reduction/gifs/graph_coloring_4_colors.gif) |

### Lab 4: Correlation and convolution
### Lab 5: K Nearest Neighbors and Decision trees
* Principal component analysis
* Classification trees, one hot encoding, cost complexity pruning, cross validation, ...

| CV Alpha Pruning                                                                                                                                                                                                                  | CV Results                                                                                                                                                                                                                  | Final Tree                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![COMPUTATIONAL_BIOLOGY/lab5-Learning/images/ccp_alpha_search.png at main · MaximoRdz/COMPUTATIONAL_BIOLOGY (github.com)](https://github.com/MaximoRdz/COMPUTATIONAL_BIOLOGY/blob/main/lab5-Learning/images/ccp_alpha_search.png) | ![COMPUTATIONAL_BIOLOGY/lab5-Learning/images/cv_final_tree.png at main · MaximoRdz/COMPUTATIONAL_BIOLOGY (github.com)](https://github.com/MaximoRdz/COMPUTATIONAL_BIOLOGY/blob/main/lab5-Learning/images/cv_final_tree.png) | ![COMPUTATIONAL_BIOLOGY/lab5-Learning/images/ccp_alpha_final_tree.png at main · MaximoRdz/COMPUTATIONAL_BIOLOGY (github.com)](https://github.com/MaximoRdz/COMPUTATIONAL_BIOLOGY/blob/main/lab5-Learning/images/ccp_alpha_final_tree.png) |
### Lab7: Genetic Algorithms

| Maxima Search                                                                                                                                                                                                                                       | PyGAD |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| ![COMPUTATIONAL_BIOLOGY/lab7-Genetic-Algorithms/gifs/genetic_algorithm.gif at main · MaximoRdz/COMPUTATIONAL_BIOLOGY (github.com)](https://github.com/MaximoRdz/COMPUTATIONAL_BIOLOGY/blob/main/lab7-Genetic-Algorithms/gifs/genetic_algorithm.gif) |       |

## References
- [Universidad Carlos III de Madrid Course](https://ocw.uc3m.es/mod/page/view.php?id=1431)
- [MIT Course](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/video_galleries/lecture-videos/)
    - [Lab Solutions](https://github.com/yenicelik/mit_ocw_6034_ai_patrick_winston/tree/master)
* [Customizing Matplotlib with style sheets and rcParams — Matplotlib 3.8.4 documentation](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-dynamic-rc-settings)
## Bibliography
- Python's Networkx Package: [examples](https://networkx.org/documentation/latest/auto_examples/index.html)
- [MIT AI BOOK TOC](https://people.csail.mit.edu/phw/Books/AITABLE.HTML)
    - [Contents](https://courses.csail.mit.edu/6.034f/ai3/)
