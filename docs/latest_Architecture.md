# Transformer-Based Tamil Relation Extraction Pipeline for Knowledge Graph Construction

---

# System Overview

This project implements a modular, production-oriented Information Extraction (IE) pipeline for constructing a Neo4j Knowledge Graph from unstructured Tamil documents.

The architecture follows a layered design consisting of two major subsystems:

1. Information Extraction Pipeline
2. Knowledge Graph ETL Pipeline

The Information Extraction Pipeline is responsible for extracting structured triples from unstructured text.

The Knowledge Graph ETL Pipeline refines, normalizes, and stores the extracted triples into Neo4j.

This modular separation enables independent experimentation, benchmarking, and replacement of individual components without affecting the remaining pipeline.

---

# High-Level Architecture

```
Input Documents
        │
        ▼
Sentence Splitting
        │
        ▼
Named Entity Recognition
        │
        ▼
Entity Post Processing
        │
        ▼
Entity Pair Generation
        │
        ▼
Dynamic Relation Schema Selection
        │
        ▼
Entity Marking
        │
        ▼
Transformer-based NLI Relation Classification
        │
        ▼
Triple Construction
        │
──────────────────────────────────────────
        Information Extraction Output
──────────────────────────────────────────
        │
        ▼
Triple Normalization
        │
        ├── Entity Normalization
        ├── Lemmatization
        └── (Future: Canonicalization)
        │
        ▼
Neo4j Graph Loader
        │
        ▼
Knowledge Graph
```

---

# Layer 1 — Input Processing

## Input

Raw Tamil text files

```
data/input/*.txt
```

Responsibilities

- Read input documents
- Preserve original document formatting
- Pass complete document to extraction pipeline

Output

```
Document
```

---

# Layer 2 — Sentence Splitting

Module

```
pipeline/sentence_splitter.py
```

Responsibilities

- Split document into sentences
- Preserve sentence order
- Handle Tamil punctuation

Input

```
Document
```

Output

```
Sentence[]
```

---

# Layer 3 — Named Entity Recognition

Module

```
pipeline/ner_stage.py
```

Model

```
exentai/SriLankan_Tamil_NER
```

Responsibilities

- Detect named entities
- Predict entity type
- Return character offsets

Current Entity Types

- PERSON
- LOCATION
- ORGANIZATION

Output

```
Entity
{
    text
    label
    start
    end
}
```

---

# Layer 4 — Entity Post Processing

Responsibilities

- Recover missing Tamil Pulli characters
- Merge adjacent entity fragments
- Normalize entity labels
- Remove invalid entities

Example

```
யாழ்ப்பாணத்தில

↓

யாழ்ப்பாணத்தில்
```

---

# Layer 5 — Entity Pair Generation

Module

```
pipeline/pair_generator.py
```

Responsibilities

Generate candidate entity pairs.

Current Pair Types

```
PERSON → PERSON

PERSON → LOCATION

PERSON → ORGANIZATION

ORGANIZATION → LOCATION

ORGANIZATION → ORGANIZATION

LOCATION → LOCATION
```

Output

```
EntityPair
```

---

# Layer 6 — Dynamic Relation Schema Selection

Module

```
schemas/
```

Instead of using one global relation inventory, the system dynamically selects candidate relations according to the detected entity type combination.

Example

```
PERSON

↓

LOCATION

↓

[
BORN_IN
LIVED_IN
WORKED_IN
DIED_IN
STUDIED_IN
VISITED
NONE
]
```

Configuration

```
schemas/relation_schemas.json
```

Responsibilities

- Detect entity pair type
- Load appropriate relation family
- Reduce relation search space

---

# Layer 7 — Entity Marker

Module

```
pipeline/entity_marker.py
```

Example

Original

```
சாம்பசிவம் யாழ்ப்பாணத்தில் வாழ்ந்தார்.
```

Marked

```
[E1] சாம்பசிவம் [/E1]

[E2] யாழ்ப்பாணத்தில் [/E2]

வாழ்ந்தார்.
```

Purpose

Provide explicit entity boundaries for Transformer inference.

---

# Layer 8 — Transformer-based Relation Classification

Module

```
pipeline/relation_stage.py
```

Model

Transformer-based Multilingual NLI Model

Current Architecture

```
Sentence

+

Entity Pair

+

Dynamic Relation Schema

↓

Transformer

↓

Best Relation
```

Output

```
RelationPrediction

{

relation

confidence

}
```

---

# Layer 9 — Triple Construction

Module

```
pipeline/triple_builder.py
```

Responsibilities

Convert relation prediction into RDF-style triple.

Output

```
Triple

{

subject

predicate

object

}
```

---

# Information Extraction Output

Output

```
Raw Triples
```

Example

```
(சாம்பசிவம்,

LIVED_IN,

யாழ்ப்பாணத்தில்)
```

---

# Knowledge Graph ETL Pipeline

The second stage of the architecture prepares extracted triples before graph insertion.

---

# Triple Normalization

Module

```
normalization/triple_normalizer.py
```

Responsibilities

Normalize only graph entities.

Current Workflow

```
Triple

↓

Subject Normalization

↓

Object Normalization

↓

Return Triple
```

Predicate remains unchanged.

---

# Entity Normalization

Module

```
entity_normalizer.py
```

Responsibilities

- Text cleanup
- Unicode normalization
- Basic preprocessing

---

# Entity Lemmatization

Module

```
entity_lemmatizer.py
```

Current Backend

```
Stanza
```

Responsibilities

Convert inflected entities into canonical lemmas.

Example

```
யாழ்ப்பாணத்தில்

↓

யாழ்ப்பாணம்
```

Purpose

Prevent duplicate graph nodes.

---

# Neo4j Graph Loader

Module

```
knowledge_graph/
```

Responsibilities

- Create nodes
- Create relationships
- Merge duplicates
- Insert into Neo4j

Output

```
Neo4j Knowledge Graph
```

---

# Current Folder Structure

```
pipeline/

sentence_splitter.py

ner_stage.py

pair_generator.py

entity_marker.py

relation_stage.py

triple_builder.py

extraction_pipeline.py

kg_extraction_pipeline.py


models/

ner/

relation/


schemas/

relation_schema_loader.py

relation_schemas.json


normalization/

entity_normalizer.py

entity_lemmatizer.py

normalization_pipeline.py

triple_normalizer.py


knowledge_graph/

neo4j_client.py

graph_loader.py

graph_builder.py

graph_schema.py


domain/

entity.py

entity_pair.py

relation_prediction.py

triple.py


tests/

tests_manual/


data/

input/
```

---

# Current Features

✅ Sentence Splitting

✅ Tamil Named Entity Recognition

✅ Entity Post Processing

✅ Entity Pair Generation

✅ Dynamic Relation Schema Selection

✅ Transformer-based Relation Extraction

✅ Triple Construction

✅ Triple Normalization

✅ Lemmatization

✅ Neo4j Knowledge Graph Integration

---

# Planned Enhancements

## Information Extraction

- Better Tamil NER Model
- Transformer Model Benchmarking
- Confidence Calibration
- Expanded Entity Types

## Knowledge Graph

- Entity Canonicalization
- Duplicate Entity Resolution
- Graph Validation
- Confidence-based Triple Filtering

## Context Modeling

- Cross-Sentence Entity Pair Generation
- Sliding Context Window
- Document-Level Relation Extraction

## Future

- Coreference Resolution
- Ontology Alignment
- Entity Linking
- Graph Embeddings
- GraphRAG Integration

---

# Architectural Principles

- Modular pipeline architecture
- Loose coupling between components
- Dynamic ontology selection
- Separation of IE and KG construction
- Configurable relation schemas
- Independent model benchmarking
- Production-ready component isolation
- Extensible normalization layer
- Knowledge Graph ETL design