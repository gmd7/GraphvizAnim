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


0. Startknoten *Start* auf Priority Queue legen

Priority Queue: in -> [  ] -> out


besucht: []

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_000.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_000.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


0. Startknoten *Start* liegt auf Priority Queue

Priority Queue: in -> [ ->Start ] -> out


besucht: []

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_001.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_001.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start* von Priority Queue nehmen

Priority Queue: in -> [  ] -> out


besucht: []

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_002.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_002.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start* endet nicht im Zielknoten, Knoten Start als besucht markieren

Priority Queue: in -> [  ] -> out


besucht: [Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_003.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_003.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Priority Queue legen.

Priority Queue: in -> [ ->Start->B (20), ->Start->C (10) ] -> out


besucht: [Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_004.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_004.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->C (10)* von Priority Queue nehmen

Priority Queue: in -> [ ->Start->B (20) ] -> out


besucht: [Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_005.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_005.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start->C (10)* endet nicht im Zielknoten, Knoten C als besucht markieren

Priority Queue: in -> [ ->Start->B (20) ] -> out


besucht: [C, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_006.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_006.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Priority Queue legen.

Priority Queue: in -> [ ->Start->C->E (19), ->Start->B (20), ->Start->C->B (19) ] -> out


besucht: [C, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_007.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_007.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->C->B (19)* von Priority Queue nehmen

Priority Queue: in -> [ ->Start->B (20), ->Start->C->E (19) ] -> out


besucht: [C, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_008.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_008.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start->C->B (19)* endet nicht im Zielknoten, Knoten B als besucht markieren

Priority Queue: in -> [ ->Start->B (20), ->Start->C->E (19) ] -> out


besucht: [B, C, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_009.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_009.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Priority Queue legen.

Priority Queue: in -> [ ->Start->C->B->F (32), ->Start->C->B->D (31), ->Start->B (20), ->Start->C->E (19) ] -> out


besucht: [B, C, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_010.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_010.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->C->E (19)* von Priority Queue nehmen

Priority Queue: in -> [ ->Start->C->B->D (31), ->Start->C->B->F (32), ->Start->B (20) ] -> out


besucht: [B, C, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_011.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_011.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start->C->E (19)* endet nicht im Zielknoten, Knoten E als besucht markieren

Priority Queue: in -> [ ->Start->C->B->D (31), ->Start->C->B->F (32), ->Start->B (20) ] -> out


besucht: [B, C, E, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_012.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_012.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Priority Queue legen.

Priority Queue: in -> [ ->Start->C->B->F (32), ->Start->C->B->D (31), ->Start->C->E->D (30), ->Start->B (20) ] -> out


besucht: [B, C, E, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_013.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_013.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->B (20)* von Priority Queue nehmen

Priority Queue: in -> [ ->Start->C->B->D (31), ->Start->C->B->F (32), ->Start->C->E->D (30) ] -> out


besucht: [B, C, E, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_014.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_014.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Knoten wurde schon besucht

Priority Queue: in -> [ ->Start->C->B->D (31), ->Start->C->B->F (32), ->Start->C->E->D (30) ] -> out


besucht: [B, C, E, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_015.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_015.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->C->E->D (30)* von Priority Queue nehmen

Priority Queue: in -> [ ->Start->C->B->F (32), ->Start->C->B->D (31) ] -> out


besucht: [B, C, E, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_016.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_016.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start->C->E->D (30)* endet nicht im Zielknoten, Knoten D als besucht markieren

Priority Queue: in -> [ ->Start->C->B->F (32), ->Start->C->B->D (31) ] -> out


besucht: [B, C, D, E, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_017.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_017.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Priority Queue legen.

Priority Queue: in -> [ ->Start->C->E->D->F (44), ->Start->C->B->F (32), ->Start->C->B->D (31) ] -> out


besucht: [B, C, D, E, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_018.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_018.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->C->B->D (31)* von Priority Queue nehmen

Priority Queue: in -> [ ->Start->C->E->D->F (44), ->Start->C->B->F (32) ] -> out


besucht: [B, C, D, E, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_019.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_019.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Knoten wurde schon besucht

Priority Queue: in -> [ ->Start->C->E->D->F (44), ->Start->C->B->F (32) ] -> out


besucht: [B, C, D, E, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_020.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_020.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->C->B->F (32)* von Priority Queue nehmen

Priority Queue: in -> [ ->Start->C->E->D->F (44) ] -> out


besucht: [B, C, D, E, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_021.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_021.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


2. Pfad *->Start->C->B->F (32)* endet nicht im Zielknoten, Knoten F als besucht markieren

Priority Queue: in -> [ ->Start->C->E->D->F (44) ] -> out


besucht: [B, C, D, E, F, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_022.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_022.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


3. Pfade mit den neuen unbesuchten Kindknoten auf Priority Queue legen.

Priority Queue: in -> [ ->Start->C->E->D->F (44), ->Start->C->B->F->Ziel (43) ] -> out


besucht: [B, C, D, E, F, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_023.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_023.svg){width=864.0 height=756.0}
   </div>
</div>
<!-- slide -->


1. Pfad *->Start->C->B->F->Ziel (43)* von Priority Queue nehmen. Ziel errreicht -> ENDE

Priority Queue: in -> [ ->Start->C->E->D->F (44) ] -> out


besucht: [B, C, D, E, F, Start]

<div class="columns">
   <div class="column" width="50%">
![](search_1_ucs_graph_024.svg){width=864.0 height=756.0}
   </div>
   <div class="column" width="50%">
![](search_1_ucs_tree_024.svg){width=864.0 height=756.0}
   </div>
</div>