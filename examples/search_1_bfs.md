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


0. Startknoten *Start* auf Queue legen

Queue: in -> [  ] -> out


besucht: []

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_000.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_000.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


0. Startknoten *Start* liegt auf Queue

Queue: in -> [ ->Start ] -> out


besucht: []

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_001.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_001.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start* von Queue nehmen

Queue: in -> [  ] -> out


besucht: []

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_002.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_002.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start* endet nicht im Zielknoten, Knoten Start als besucht markieren

Queue: in -> [  ] -> out


besucht: [Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_003.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_003.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Queue legen.

Queue: in -> [ ->Start->C, ->Start->B ] -> out


besucht: [Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_004.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_004.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->B* von Queue nehmen

Queue: in -> [ ->Start->C ] -> out


besucht: [Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_005.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_005.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start->B* endet nicht im Zielknoten, Knoten B als besucht markieren

Queue: in -> [ ->Start->C ] -> out


besucht: [B, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_006.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_006.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Queue legen.

Queue: in -> [ ->Start->B->F, ->Start->B->D, ->Start->B->C, ->Start->C ] -> out


besucht: [B, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_007.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_007.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->C* von Queue nehmen

Queue: in -> [ ->Start->B->F, ->Start->B->D, ->Start->B->C ] -> out


besucht: [B, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_008.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_008.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start->C* endet nicht im Zielknoten, Knoten C als besucht markieren

Queue: in -> [ ->Start->B->F, ->Start->B->D, ->Start->B->C ] -> out


besucht: [B, C, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_009.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_009.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Queue legen.

Queue: in -> [ ->Start->C->E, ->Start->B->F, ->Start->B->D, ->Start->B->C ] -> out


besucht: [B, C, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_010.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_010.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->B->C* von Queue nehmen

Queue: in -> [ ->Start->C->E, ->Start->B->F, ->Start->B->D ] -> out


besucht: [B, C, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_011.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_011.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Knoten wurde schon besucht

Queue: in -> [ ->Start->C->E, ->Start->B->F, ->Start->B->D ] -> out


besucht: [B, C, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_012.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_012.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->B->D* von Queue nehmen

Queue: in -> [ ->Start->C->E, ->Start->B->F ] -> out


besucht: [B, C, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_013.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_013.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start->B->D* endet nicht im Zielknoten, Knoten D als besucht markieren

Queue: in -> [ ->Start->C->E, ->Start->B->F ] -> out


besucht: [B, C, D, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_014.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_014.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Queue legen.

Queue: in -> [ ->Start->B->D->F, ->Start->B->D->E, ->Start->C->E, ->Start->B->F ] -> out


besucht: [B, C, D, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_015.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_015.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->B->F* von Queue nehmen

Queue: in -> [ ->Start->B->D->F, ->Start->B->D->E, ->Start->C->E ] -> out


besucht: [B, C, D, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_016.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_016.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start->B->F* endet nicht im Zielknoten, Knoten F als besucht markieren

Queue: in -> [ ->Start->B->D->F, ->Start->B->D->E, ->Start->C->E ] -> out


besucht: [B, C, D, F, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_017.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_017.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Queue legen.

Queue: in -> [ ->Start->B->F->Ziel, ->Start->B->D->F, ->Start->B->D->E, ->Start->C->E ] -> out


besucht: [B, C, D, F, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_018.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_018.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->C->E* von Queue nehmen

Queue: in -> [ ->Start->B->F->Ziel, ->Start->B->D->F, ->Start->B->D->E ] -> out


besucht: [B, C, D, F, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_019.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_019.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start->C->E* endet nicht im Zielknoten, Knoten E als besucht markieren

Queue: in -> [ ->Start->B->F->Ziel, ->Start->B->D->F, ->Start->B->D->E ] -> out


besucht: [B, C, D, E, F, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_020.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_020.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Queue legen.

Queue: in -> [ ->Start->B->F->Ziel, ->Start->B->D->F, ->Start->B->D->E ] -> out


besucht: [B, C, D, E, F, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_021.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_021.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->B->D->E* von Queue nehmen

Queue: in -> [ ->Start->B->F->Ziel, ->Start->B->D->F ] -> out


besucht: [B, C, D, E, F, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_022.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_022.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Knoten wurde schon besucht

Queue: in -> [ ->Start->B->F->Ziel, ->Start->B->D->F ] -> out


besucht: [B, C, D, E, F, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_023.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_023.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->B->D->F* von Queue nehmen

Queue: in -> [ ->Start->B->F->Ziel ] -> out


besucht: [B, C, D, E, F, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_024.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_024.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Knoten wurde schon besucht

Queue: in -> [ ->Start->B->F->Ziel ] -> out


besucht: [B, C, D, E, F, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_025.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_025.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->B->F->Ziel* von Queue nehmen. Ziel errreicht -> ENDE

Queue: in -> [  ] -> out


besucht: [B, C, D, E, F, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_bfs_graph_026.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_bfs_tree_026.svg){width=864.0 height=756.0}
   </div>
</div>