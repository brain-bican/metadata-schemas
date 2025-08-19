# Taxonomy and Cell Annotation Schema -- Labelsets

Document Status: _Approved BICAN Standard_

Version: 1.0

Owner: @UCDNJJ, @jeremymiller

Reviewers: @patrick-lloyd-ray, @carolth, @djarecka, @memartone

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 10-03-2025

## Overview

The BICAN Cell Annotation Metadata schema specifies the metadata relating to cell annotations that can be taken from a variety of sources in BICAN. These metadata reflect the metadata needed to accurately track cell annotations metadata in BICAN. As such, it is a collaborative schema that reflects the joint efforts of members of BICAN.

This document has the following sections:

- [Taxonomy and Cell Annotation Schema -- Labelsets](#taxonomy-and-cell-annotation-schema----labelsets)
  - [Overview](#overview)
  - [uns fields associated with individual cell set annotations (e.g., different label sets)](#uns-fields-associated-with-individual-cell-set-annotations-eg-different-label-sets)
    - [labelsets](#labelsets)
    - [labelsets fields](#labelsets-fields)
  - [Fields relating to a specific labelset in uns](#fields-relating-to-a-specific-labelset-in-uns)
    - [Neurotransmitters](#neurotransmitters)
    - [Cell Set Accession](#cell-set-accession)
    - [Cell Set Label](#cell-set-label)
    - [Cell Fullname](#cell-fullname)
    - [Cell Ontology Exists](#cell-ontology-exists)
    - [Cell Ontology Term ID](#cell-ontology-term-id)
    - [Cell Ontology Term](#cell-ontology-term)
    - [Rationale](#rationale)
    - [Rationale DOIs](#rationale-dois)
    - [Marker Gene Evidence](#marker-gene-evidence)
    - [Synonyms](#synonyms)
    - [Parent Cell Set Name](#parent-cell-set-name)
    - [Parent Cell Set Accession](#parent-cell-set-accession)
  - [uns fields associated with complex cell set relationships and metadata (e.g., dendrograms, child taxonomies, gradients, level relationships, annotation transfer)](#uns-fields-associated-with-complex-cell-set-relationships-and-metadata-eg-dendrograms-child-taxonomies-gradients-level-relationships-annotation-transfer)
    - [dend](#dend)
    - [Cell Set Relationships](#cell-set-relationships)
    - [Filter](#filter)
    - [Transferred Annotations](#transferred-annotations)
    - [Transferred Annotations Metadata](#transferred-annotations-metadata)
  - [Annotation Key Metadata](#annotation-key-metadata)
    - [Annotation Key Name](#annotation-key-name)
    - [Annotation Key Description](#annotation-key-description)
    - [Annotation Method](#annotation-method)
    - [Automated Annotation](#automated-annotation)
    - [Algorithm Name](#algorithm-name)
    - [Algorithm Version](#algorithm-version)
    - [Algorithm Repo URL](#algorithm-repo-url)
    - [Reference Location](#reference-location)
    - [Rank](#rank)
  - [Changelog](#changelog)
    - [August 7, 2025 -- Version 1.0.0](#august-7-2025----version-100)
    - [Pre-release Changelog](#pre-release-changelog)

## uns fields associated with individual cell set annotations (e.g., different label sets)

### labelsets

| BICAN Field Name | labelsets |
|------------------|------------|
| BICAN UUID | 87fa0b7a1-6af7-4f79-8da0-29d7950ea736 |
| Aliases | cluster annotation term set |
| Definition | A data frame representation that contains information about each `cellannotation_set` set of columns (e.g., subclass, class, neurotransmitter, etc.). Specifically: `name`, `description`, and `rank` (0 most specific) and some information about provenance needed for each labelset. This is equilalent to `Cluster annotation term set` in BKP.  |
| Data Type | string |

### labelsets fields

| BICAN Field Name | labelsets fields |
|------------------|-----------------|
| BICAN UUID | 3b7de4bc-d2e2-431f-a029-fcccae7b1ccf |
| Aliases | cluster annotation term sets, label_sets |
| Definition | This is a list of fields that are used in the labelsets data frame. The column name is a string (e.g., "subclass") and the values are cell_labels (e.g., "SST"). The equivalent in BKP are Cluster Annotation Term Sets and in CAP is label_sets. This also encapsulates the concept of cell_ids from CAP/CAS, since in the h5ad file each row corresponds to a cell and therefore you get the cell_label --> cell_ids mapping for free. This is stored as separate files in both BKP and TDT. This is critical for scrattch.taxonomy and scrattch.mapping to work properly, but none of the [cellannotation_set]--XXXX fields below are needed for AIT. |
| Data Type | string |

## Fields relating to a specific labelset in uns

### Neurotransmitters

|BICAN Field Name | neurotransmitters |
|------------------|-----------------|
| BICAN UUID | c0bd3c28-e523-4e9c-af73-4d01ce82390b |
| Aliases | neurotransmitter |
| Definition | The neurotransmitter(s) that are associated with the cell set. This is a string that can be a single neurotransmitter or a comma-separated list of neurotransmitters (e.g., "GABA, Glutamate"). |
| Data Type | string |

### Cell Set Accession

|BICAN Field Name | cell_set_accession |
|------------------|-----------------|
| BICAN UUID | 55cb81b4-5f6d-4930-aba6-0ef1d1784124 |
| Aliases | cluster annotation term |
| Definition | The ID corresponding to the cell_set; called the "Cluster Annotation Term" in BKP. This is critical for scrattch.taxonomy and scrattch.mapping to work properly. |
| Data Type | string |

### Cell Set Label

|BICAN Field Name | cell_set_label |
|------------------|-----------------|
| BICAN UUID | 69dc12e7-e825-400f-bf51-5f3f54a1204b |
| Aliases | |
| Definition | A label for a particular cell set. In CCN this is used as a tag for each cluster or (for cell sets with >1 cluster) included a list of underlying cluster labels. It was important for proper databasing without a database. |
| Data Type | string |

### Cell Fullname

|BICAN Field Name | cell_fullname |
|------------------|-----------------|
| BICAN UUID | b5036e70-9181-45c0-8fdb-66da93be2d87 |
| Aliases | cell_set_preferred_alias |
| Definition | The longer name for a cell type (e.g., "Somatostatin interneuron 1" rather than "SST 1"). This was called the cell_set_preferred_alias in CCN. |
| Data Type | string |

### Cell Ontology Exists

|BICAN Field Name | cell_ontology_exists |
|------------------|-----------------|
| BICAN UUID | 9d840e2f-af93-45b5-9528-a7e9a74bf237 |
| Aliases | |
| Definition | A true/false field about whether a cell ontology term exists that corresponds to the cell type. |
| Data Type | boolean |

### Cell Ontology Term ID

|BICAN Field Name | cell_ontology_term_id |
|------------------|-----------------|
| BICAN UUID | fe21fa47-6fd2-4432-82de-2412db9462c6 |
| Aliases | cell_set_ontology_tag |
| Definition | The highest resolution Cell Ontology term ID corresponding to the cell type. This was called `cell_set_ontology_tag` in CCN. |
| Data Type | string |

### Cell Ontology Term

|BICAN Field Name | cell_ontology_term |
|------------------|-----------------|
| BICAN UUID | 52685f23-9bcc-416a-ae70-e9de43ef4123 |
| Aliases | cell_set_structure |
| Definition | The highest resolution Cell Ontology term (name) corresponding to the cell type. This was called `cell_set_structure` in CCN and was also largely mapping to the `cell_set_aligned_alias`. |
| Data Type | string |

### Rationale

|BICAN Field Name | rationale |
|------------------|-----------------|
| BICAN UUID | a76fa81e-ba3f-4813-ac7c-cce1f43683a6 |
| Aliases | |
| Definition | Free text evidence for cell annotations. |
| Data Type | string |

### Rationale DOIs

|BICAN Field Name | rationale_dois |
|------------------|-----------------|
| BICAN UUID | cd9ce030-058c-4890-b552-750735c90ba4 |
| Aliases | cell_set_alias_citation |
| Definition | A list of publication DOI's of rationale. In CCN, this is called "cell_set_alias_citation". NOTE: this can use comma-separated, pipe-separated, or /#/-separated. |
| Data Type | string |

### Marker Gene Evidence

|BICAN Field Name | marker_gene_evidence |
|------------------|-----------------|
| BICAN UUID | e790e621-e7f2-42ba-8f20-bcac2c1f86e4 |
| Aliases |  |
| Definition | A list (comma-separated) of marker genes used as evidence for cell type annotation (e.g., by NS-Forest). Note: This is reserved for ontology markers. |
| Data Type | string |

### Synonyms

|BICAN Field Name | synonyms |
|------------------|-----------------|
| BICAN UUID | 137f6d7d-d257-4ffb-8a14-24fcb0bab0e9 |
| Aliases | cell_set_additional_alias |
| Definition | A list (comma-separated) of aliases or synonyms (e.g., "neuroglial cell, glial cell, neuroglia"). This was called `cell_set_additional_alias` in CCN. |
| Data Type | string |

### Parent Cell Set Name

|BICAN Field Name | parent_cell_set_name |
|------------------|-----------------|
| BICAN UUID | 27bf9e17-13e9-4a52-8d15-24c55146aec4 |
| Aliases | parent_cell_set_label |
| Definition | The `cell_label` corresponding to the parent cell_set. |
| Data Type | string |

### Parent Cell Set Accession

|BICAN Field Name | parent_cell_set_accession |
|------------------|-----------------|
| BICAN UUID | bfa1e2d9-e65d-480d-b54c-9947acaddd93 |
| Aliases | parent_cluster_annotation_term_id |
| Definition | The ID corresponding to the parent cell_set. This corresponds to the parent Cluster Annotation Term ID in knowledgebase. |
| Data Type | string |

## uns fields associated with complex cell set relationships and metadata (e.g., dendrograms, child taxonomies, gradients, level relationships, annotation transfer)

### dend

| BICAN Field Name | dend |
|------------------|------------|
| BICAN UUID | 27bdd1f9-aebe-4868-ba22-91710fc371fe |
| Aliases | |
| Definition | A JSON formatted dendrogram used for tree mapping. This is created by scrattch.taxonomy if not provided. |
| Data Type | string |

### Cell Set Relationships

| BICAN Field Name | cell_set_relationships |
|------------------|------------|
| BICAN UUID | 554af932-8f56-490d-a5bd-f75a7aecc28f |
| Aliases | cell_set_relations |
| Definition | This is a dataframe of all sibling relationships (things like gradients, trajectories, constellation diagrams, etc.). This has five columns: cells_set_accession1, cell_set_accession2, relation_label, value, direction. Potentially, this could alternatively be stored as a JSON representation that unpacks into a dataframe. |
| Data Type | string |

### Filter

| BICAN Field Name | filter |
|------------------|------------|
| BICAN UUID | 2b5c18ef-5436-44dc-ab60-13965f052efb |
| Aliases | |
| Definition | An indicator of which cells to use for a given child taxonomy (subset), saved as a list of vectors. Each entry in this list is named for the relevant "mode" and has TRUE/FALSE calls indicating whether a cell is filtered out (e.g., the "standard" taxonomy is all FALSE). This is critical for how child taxonomies are defined and implemented in scrattch.taxonomy but differs from how taxonomies are stored in all other schemas. |
| Data Type | string |

### Transferred Annotations

| BICAN Field Name | transferred_annotations |
|------------------|------------|
| BICAN UUID | 1c3f146c-eb76-451d-9925-15f58f47f71a |
| Aliases |  |
| Definition | A dataframe where each column is a string corresponding to the taxonomy of comparison; values are the transferred cell label from that taxonomy. This is used to store annotations that have been transferred from one taxonomy to another, allowing for cross-taxonomy comparisons. |
| Data Type | string |

### Transferred Annotations Metadata

| BICAN Field Name | transferred_annotations_metadata |
|------------------|------------|
| BICAN UUID | 80e26439-2e51-4faa-87ef-576937b89c71 |
| Aliases |  |
| Definition | A data frame of information about each transferred annotation column: `source_taxonomy`, `algorithm_name`, `comment`. This is for taxonomy-level metadata and linked to data in var. This is important for tracking the provenance of transferred annotations and ensuring that the source of each annotation is clear. |
| Data Type | string |

## Annotation Key Metadata

The annotation keys are used to identify the specific annotations within the labelsets. These keys are essential for linking the annotations to their respective metadata and ensuring that the correct information is associated with each cell set.

### Annotation Key Name

| BICAN Field Name | annotation_key_name |
|------------------|-----------------|
| BICAN UUID | f09d7148-9750-4a9c-8eba-da1a11c3b274 |
| Aliases |  |
| Definition | The name of the annotation key. |
| Data Type | string |

### Annotation Key Description

| BICAN Field Name | annotation_key_description |
|------------------|-----------------|
| BICAN UUID | 63e9a887-cdf9-4248-ae83-41a720ce8f53 |
| Aliases |  |
| Definition | A description of the annotation key, providing context and details about its use. This should include some text describing what types of cell annotation this annotation key is used to record. |
| Data Type | string |

### Annotation Method

| BICAN Field Name | annotation_method |
|------------------|-----------------|
| BICAN UUID | 2e91e232-dccb-4584-8a0b-0263660d6c08 |
| Aliases |  |
| Definition | The method used for creating the cell annotations. This MUST be one of the following strings: 'algorithmic', 'manual', or 'both' . |
| Data Type | value set |

### Automated Annotation

| BICAN Field Name | automated_annotation |
|------------------|-----------------|
| BICAN UUID | 9fba68df-a9f0-4cf9-994d-9b15f31fb88d |
| Aliases |  |
| Definition | A boolean indicating whether the annotation was created using an automated method. This is used to distinguish between annotations that were generated by algorithms versus those that were manually curated. |
| Data Type | boolean |

### Algorithm Name

| BICAN Field Name | algorithm_name |
|------------------|-----------------|
| BICAN UUID | fd9cb36e-5d29-45d7-8002-c4da15c9a3d1 |
| Aliases |  |
| Definition | The name of the algorithm used. It MUST be a string of the algorithm's name. |
| Data Type | string |

### Algorithm Version

| BICAN Field Name | algorithm_version |
|------------------|-----------------|
| BICAN UUID | 81ed9281-3f29-46e8-8e06-963afe3e27e4 |
| Aliases |  |
| Definition | The version of the algorithm used (if applicable). It MUST be a string of the algorithm's version, which is typically in the format '[MAJOR].[MINOR]', but other versioning systems are permitted (based on the algorithm's versioning). |
| Data Type | string |

### Algorithm Repo URL

| BICAN Field Name | algorithm_repo_url |
|------------------|-----------------|
| BICAN UUID | ce81ab8b-3892-473d-883c-c8fa266376ec |
| Aliases |  |
| Definition | This field denotes the URL of the version control repository associated with the algorithm used (if applicable). It MUST be a string of a valid URL. |
| Data Type | string |

### Reference Location

| BICAN Field Name | reference_location |
|------------------|-----------------|
| BICAN UUID | 4d60f911-5c5c-4ebc-a1df-b243a7252730 |
| Aliases |  |
| Definition | This field denotes a valid URL of the annotated dataset that was the source of annotated reference data. This MUST be a string of a valid URL. The concept of a 'reference' specifically refers to 'annotation transfer' algorithms, whereby a 'reference' dataset is used to transfer cell annotations to the 'query' dataset. |
| Data Type | string |

### Rank

| BICAN Field Name | rank |
|------------------|-----------------|
| BICAN UUID | 25bb3ce6-eda7-47be-8855-317a3b1002ea |
| Aliases |  |
| Definition | A number indicating relative granularity with 0 being the most specific. Use this where a single dataset has multiple keys that are used consistently to record annotations and different levels of granularity. |
| Data Type | integer |

## Changelog

### August 7, 2025 -- Version 1.0.0

- **8-07-2025**: Finalized schema and added document status.
- **8-07-2025**: Approved as BICAN Standard.

### Pre-release Changelog

- **10-03-2024**: Initial version created.
