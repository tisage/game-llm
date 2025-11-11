# Prompt Structure - 5 Section Framework

```mermaid
flowchart TB
    Start([📋 Game Design Prompt])
    Start --> Section1

    subgraph Section1["1️⃣ OBJECTIVE"]
        direction TB
        Obj[What game to build?<br/>One sentence goal]
    end

    Section1 --> Section2

    subgraph Section2["2️⃣ CORE GAMEPLAY MECHANICS"]
        direction TB
        GP1[Game World]
        GP2[Player Character]
        GP3[Items/Enemies]
        GP4[Scoring]
        GP5[Win/Loss Rules]
    end

    Section2 --> Section3

    subgraph Section3["3️⃣ GUI DESIGN"]
        direction TB
        UI1[Art Style]
        UI2[UI Elements]
        UI3[Sound/Music]
    end

    Section3 --> Section4

    subgraph Section4["4️⃣ IMPLEMENTATION PLAN"]
        direction TB
        Impl1[Language & Library]
        Impl2[Code Structure]
        Impl3[Best Practices]
    end

    Section4 --> Section5

    subgraph Section5["5️⃣ DELIVERABLE"]
        direction TB
        Del[Single Python file]
    end

    Section5 --> End([✅ Complete Prompt])

    style Start fill:#e3f2fd,stroke:#1976d2,stroke-width:3px
    style End fill:#c8e6c9,stroke:#388e3c,stroke-width:3px
    style Section1 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style Section2 fill:#f3e5f5,stroke:#8e24aa,stroke-width:2px
    style Section3 fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    style Section4 fill:#fce4ec,stroke:#c2185b,stroke-width:2px
    style Section5 fill:#fff9c4,stroke:#f9a825,stroke-width:2px
```
