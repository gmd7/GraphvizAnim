---
presentation:
  theme: serif.css
  width: 1920
  height: 1080
  transition: 'none'
  transitionSpeed: 'fast'
  backgroundTransition: 'none'
  overview: true
  progress: true
  slideNumber: true
---

<!-- slide -->


0. Startknoten *Start* auf Stack legen

Stack: in,out <-> [  ]


closed set: []

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_000.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_000.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


0. Startknoten *Start* liegt auf Stack

Stack: in,out <-> [ Start ]


closed set: []

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_001.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_001.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


1. Knoten *Start* von Stack nehmen

Stack: in,out <-> [  ]


closed set: []

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_002.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_002.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


2. Knoten *Start* ist kein Zielknoten

Stack: in,out <-> [  ]


closed set: ['Start']

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_003.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_003.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


3. Kindknoten von *Start* auf Stack legen.

Stack: in,out <-> [ F D B ]


closed set: ['Start']

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_004.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_004.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


1. Knoten *F* von Stack nehmen

Stack: in,out <-> [ D B ]


closed set: ['Start']

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_005.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_005.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


2. Knoten *F* ist kein Zielknoten

Stack: in,out <-> [ D B ]


closed set: ['F', 'Start']

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_006.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_006.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


3. Kindknoten von *F* auf Stack legen.

Stack: in,out <-> [ D D B ]


closed set: ['F', 'Start']

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_007.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_007.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


1. Knoten *D* von Stack nehmen

Stack: in,out <-> [ D B ]


closed set: ['F', 'Start']

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_008.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_008.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


2. Knoten *D* ist kein Zielknoten

Stack: in,out <-> [ D B ]


closed set: ['D', 'F', 'Start']

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_009.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_009.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


3. Kindknoten von *D* auf Stack legen.

Stack: in,out <-> [ E C D B ]


closed set: ['D', 'F', 'Start']

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_010.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_010.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


1. Knoten *E* von Stack nehmen

Stack: in,out <-> [ C D B ]


closed set: ['D', 'F', 'Start']

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_011.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_011.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


2. Knoten *E* ist kein Zielknoten

Stack: in,out <-> [ C D B ]


closed set: ['D', 'E', 'F', 'Start']

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_012.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_012.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


3. Kindknoten von *E* auf Stack legen.

Stack: in,out <-> [ C C D B ]


closed set: ['D', 'E', 'F', 'Start']

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_013.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_013.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


1. Knoten *C* von Stack nehmen

Stack: in,out <-> [ C D B ]


closed set: ['D', 'E', 'F', 'Start']

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_014.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_014.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


2. Knoten *C* ist kein Zielknoten

Stack: in,out <-> [ C D B ]


closed set: ['C', 'D', 'E', 'F', 'Start']

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_015.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_015.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


3. Kindknoten von *C* auf Stack legen.

Stack: in,out <-> [ Ziel C D B ]


closed set: ['C', 'D', 'E', 'F', 'Start']

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_016.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_016.svg){width=864 height=756}
   </div>
</div>
<!-- slide -->


1. Knoten *Ziel* von Stack nehmen. Zielknoten -> ENDE

Stack: in,out <-> [ C D B ]


closed set: ['C', 'D', 'E', 'F', 'Start']

<div class="columns">
   <div class="column" width="50%">
![](search_dfs_1_graph_017.svg){width=864 height=756}
   </div>
   <div class="column" width="50%">
![](search_dfs_1_tree_017.svg){width=864 height=756}
   </div>
</div>