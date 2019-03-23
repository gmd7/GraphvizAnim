| Bemerkung | Priority Queue | Menge besuchter Knoten |
|---------------------------|---------------------------|------------|
| Anfangszustand |  | [] |
| 0. Startknoten *Start* auf Priority Queue legen | ->Start | [] |
| 1. Pfad *->Start* von Priority Queue nehmen |  | [] |
| 2. Pfad *->Start* endet nicht im Zielknoten, Knoten Start als besucht markieren |  | [Start] |
| 3. Neuer Kindknoten: B | ->Start->B (20) | [Start] |
| 3. Neuer Kindknoten: C | ->Start->B (20), ->Start->C (10) | [Start] |
| 1. Pfad *->Start->C (10)* von Priority Queue nehmen | ->Start->B (20) | [Start] |
| 2. Pfad *->Start->C (10)* endet nicht im Zielknoten, Knoten C als besucht markieren | ->Start->B (20) | [C, Start] |
| 3. Neuer Kindknoten: B | ->Start->B (20), ->Start->C->B (19) | [C, Start] |
| 3. Neuer Kindknoten: E | ->Start->C->E (19), ->Start->B (20), ->Start->C->B (19) | [C, Start] |
| 1. Pfad *->Start->C->B (19)* von Priority Queue nehmen | ->Start->B (20), ->Start->C->E (19) | [C, Start] |
| 2. Pfad *->Start->C->B (19)* endet nicht im Zielknoten, Knoten B als besucht markieren | ->Start->B (20), ->Start->C->E (19) | [B, C, Start] |
| 3. Neuer Kindknoten: D | ->Start->C->B->D (31), ->Start->B (20), ->Start->C->E (19) | [B, C, Start] |
| 3. Neuer Kindknoten: F | ->Start->C->B->F (32), ->Start->C->B->D (31), ->Start->B (20), ->Start->C->E (19) | [B, C, Start] |
| 1. Pfad *->Start->C->E (19)* von Priority Queue nehmen | ->Start->C->B->D (31), ->Start->C->B->F (32), ->Start->B (20) | [B, C, Start] |
| 2. Pfad *->Start->C->E (19)* endet nicht im Zielknoten, Knoten E als besucht markieren | ->Start->C->B->D (31), ->Start->C->B->F (32), ->Start->B (20) | [B, C, E, Start] |
| 3. Neuer Kindknoten: D | ->Start->C->B->F (32), ->Start->C->B->D (31), ->Start->C->E->D (30), ->Start->B (20) | [B, C, E, Start] |
| 1. Pfad *->Start->B (20)* von Priority Queue nehmen | ->Start->C->B->D (31), ->Start->C->B->F (32), ->Start->C->E->D (30) | [B, C, E, Start] |
| 1. Pfad *->Start->C->E->D (30)* von Priority Queue nehmen | ->Start->C->B->F (32), ->Start->C->B->D (31) | [B, C, E, Start] |
| 2. Pfad *->Start->C->E->D (30)* endet nicht im Zielknoten, Knoten D als besucht markieren | ->Start->C->B->F (32), ->Start->C->B->D (31) | [B, C, D, E, Start] |
| 3. Neuer Kindknoten: F | ->Start->C->E->D->F (44), ->Start->C->B->F (32), ->Start->C->B->D (31) | [B, C, D, E, Start] |
| 1. Pfad *->Start->C->B->D (31)* von Priority Queue nehmen | ->Start->C->E->D->F (44), ->Start->C->B->F (32) | [B, C, D, E, Start] |
| 1. Pfad *->Start->C->B->F (32)* von Priority Queue nehmen | ->Start->C->E->D->F (44) | [B, C, D, E, Start] |
| 2. Pfad *->Start->C->B->F (32)* endet nicht im Zielknoten, Knoten F als besucht markieren | ->Start->C->E->D->F (44) | [B, C, D, E, F, Start] |
| 3. Neuer Kindknoten: Ziel | ->Start->C->E->D->F (44), ->Start->C->B->F->Ziel (43) | [B, C, D, E, F, Start] |
| 1. Pfad *->Start->C->B->F->Ziel (43)* von Priority Queue nehmen. Ziel errreicht -> ENDE | ->Start->C->E->D->F (44) | [B, C, D, E, F, Start] |
