| Bemerkung | Queue | Menge besuchter Knoten |
|---------------------------|---------------------------|------------|
| Anfangszustand |  | [] |
| 0. Startknoten *Start* auf Queue legen | ->Start | [] |
| 1. Pfad *->Start* von Queue nehmen |  | [] |
| 2. Pfad *->Start* endet nicht im Zielknoten, Knoten Start als besucht markieren |  | [Start] |
| 3. Neuer Kindknoten: B | ->Start->B | [Start] |
| 3. Neuer Kindknoten: C | ->Start->C, ->Start->B | [Start] |
| 1. Pfad *->Start->B* von Queue nehmen | ->Start->C | [Start] |
| 2. Pfad *->Start->B* endet nicht im Zielknoten, Knoten B als besucht markieren | ->Start->C | [B, Start] |
| 3. Neuer Kindknoten: C | ->Start->B->C, ->Start->C | [B, Start] |
| 3. Neuer Kindknoten: D | ->Start->B->D, ->Start->B->C, ->Start->C | [B, Start] |
| 3. Neuer Kindknoten: F | ->Start->B->F, ->Start->B->D, ->Start->B->C, ->Start->C | [B, Start] |
| 1. Pfad *->Start->C* von Queue nehmen | ->Start->B->F, ->Start->B->D, ->Start->B->C | [B, Start] |
| 2. Pfad *->Start->C* endet nicht im Zielknoten, Knoten C als besucht markieren | ->Start->B->F, ->Start->B->D, ->Start->B->C | [B, C, Start] |
| 3. Neuer Kindknoten: E | ->Start->C->E, ->Start->B->F, ->Start->B->D, ->Start->B->C | [B, C, Start] |
| 1. Pfad *->Start->B->C* von Queue nehmen | ->Start->C->E, ->Start->B->F, ->Start->B->D | [B, C, Start] |
| 1. Pfad *->Start->B->D* von Queue nehmen | ->Start->C->E, ->Start->B->F | [B, C, Start] |
| 2. Pfad *->Start->B->D* endet nicht im Zielknoten, Knoten D als besucht markieren | ->Start->C->E, ->Start->B->F | [B, C, D, Start] |
| 3. Neuer Kindknoten: E | ->Start->B->D->E, ->Start->C->E, ->Start->B->F | [B, C, D, Start] |
| 3. Neuer Kindknoten: F | ->Start->B->D->F, ->Start->B->D->E, ->Start->C->E, ->Start->B->F | [B, C, D, Start] |
| 1. Pfad *->Start->B->F* von Queue nehmen | ->Start->B->D->F, ->Start->B->D->E, ->Start->C->E | [B, C, D, Start] |
| 2. Pfad *->Start->B->F* endet nicht im Zielknoten, Knoten F als besucht markieren | ->Start->B->D->F, ->Start->B->D->E, ->Start->C->E | [B, C, D, F, Start] |
| 3. Neuer Kindknoten: Ziel | ->Start->B->F->Ziel, ->Start->B->D->F, ->Start->B->D->E, ->Start->C->E | [B, C, D, F, Start] |
| 1. Pfad *->Start->C->E* von Queue nehmen | ->Start->B->F->Ziel, ->Start->B->D->F, ->Start->B->D->E | [B, C, D, F, Start] |
| 2. Pfad *->Start->C->E* endet nicht im Zielknoten, Knoten E als besucht markieren | ->Start->B->F->Ziel, ->Start->B->D->F, ->Start->B->D->E | [B, C, D, E, F, Start] |
| 1. Pfad *->Start->B->D->E* von Queue nehmen | ->Start->B->F->Ziel, ->Start->B->D->F | [B, C, D, E, F, Start] |
| 1. Pfad *->Start->B->D->F* von Queue nehmen | ->Start->B->F->Ziel | [B, C, D, E, F, Start] |
| 1. Pfad *->Start->B->F->Ziel* von Queue nehmen. Ziel errreicht -> ENDE |  | [B, C, D, E, F, Start] |
