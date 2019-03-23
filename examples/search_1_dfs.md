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


besucht: []

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_000.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_000.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


0. Startknoten *Start* liegt auf Stack

Stack: in,out <-> [ ->Start ]


besucht: []

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_001.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_001.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start* von Stack nehmen

Stack: in,out <-> [  ]


besucht: []

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_002.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_002.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start* endet nicht im Zielknoten, Knoten Start als besucht markieren

Stack: in,out <-> [  ]


besucht: [Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_003.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_003.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Stack legen.

Stack: in,out <-> [ ->Start->B, ->Start->C ]


besucht: [Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_004.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_004.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->B* von Stack nehmen

Stack: in,out <-> [ ->Start->C ]


besucht: [Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_005.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_005.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start->B* endet nicht im Zielknoten, Knoten B als besucht markieren

Stack: in,out <-> [ ->Start->C ]


besucht: [B, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_006.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_006.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Stack legen.

Stack: in,out <-> [ ->Start->B->C, ->Start->B->D, ->Start->B->F, ->Start->C ]


besucht: [B, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_007.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_007.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->B->C* von Stack nehmen

Stack: in,out <-> [ ->Start->B->D, ->Start->B->F, ->Start->C ]


besucht: [B, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_008.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_008.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start->B->C* endet nicht im Zielknoten, Knoten C als besucht markieren

Stack: in,out <-> [ ->Start->B->D, ->Start->B->F, ->Start->C ]


besucht: [B, C, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_009.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_009.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Stack legen.

Stack: in,out <-> [ ->Start->B->C->E, ->Start->B->D, ->Start->B->F, ->Start->C ]


besucht: [B, C, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_010.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_010.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->B->C->E* von Stack nehmen

Stack: in,out <-> [ ->Start->B->D, ->Start->B->F, ->Start->C ]


besucht: [B, C, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_011.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_011.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start->B->C->E* endet nicht im Zielknoten, Knoten E als besucht markieren

Stack: in,out <-> [ ->Start->B->D, ->Start->B->F, ->Start->C ]


besucht: [B, C, E, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_012.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_012.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Stack legen.

Stack: in,out <-> [ ->Start->B->C->E->D, ->Start->B->D, ->Start->B->F, ->Start->C ]


besucht: [B, C, E, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_013.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_013.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->B->C->E->D* von Stack nehmen

Stack: in,out <-> [ ->Start->B->D, ->Start->B->F, ->Start->C ]


besucht: [B, C, E, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_014.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_014.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start->B->C->E->D* endet nicht im Zielknoten, Knoten D als besucht markieren

Stack: in,out <-> [ ->Start->B->D, ->Start->B->F, ->Start->C ]


besucht: [B, C, D, E, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_015.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_015.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Stack legen.

Stack: in,out <-> [ ->Start->B->C->E->D->F, ->Start->B->D, ->Start->B->F, ->Start->C ]


besucht: [B, C, D, E, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_016.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_016.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->B->C->E->D->F* von Stack nehmen

Stack: in,out <-> [ ->Start->B->D, ->Start->B->F, ->Start->C ]


besucht: [B, C, D, E, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_017.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_017.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start->B->C->E->D->F* endet nicht im Zielknoten, Knoten F als besucht markieren

Stack: in,out <-> [ ->Start->B->D, ->Start->B->F, ->Start->C ]


besucht: [B, C, D, E, F, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_018.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_018.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Stack legen.

Stack: in,out <-> [ ->Start->B->C->E->D->F->Ziel, ->Start->B->D, ->Start->B->F, ->Start->C ]


besucht: [B, C, D, E, F, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_019.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_019.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->B->C->E->D->F->Ziel* von Stack nehmen. Ziel errreicht -> ENDE

Stack: in,out <-> [ ->Start->B->D, ->Start->B->F, ->Start->C ]


besucht: [B, C, D, E, F, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_dfs_graph_020.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_dfs_tree_020.svg){width=864.0 height=756.0}
   </div>
</div>