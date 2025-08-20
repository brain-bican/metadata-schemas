# Cell Annotation Schema

Document Status: _Approved BICAN Standard_

Version: 1.0

Owner: @UCDNJJ, @jeremymiller

Reviewers: @patrick-lloyd-ray, @carolth, @djarecka, @memartone

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 10-03-2025

## Overview

The BICAN Cell Annotation schema specifies the metadata relating to cell annotations that can be taken from a variety of sources in BICAN. These metadata reflect the metadata needed to accurately track cell metadata in BICAN. As such, it is a collaborative schema that reflects the joint efforts of members of BICAN.

This document has the following sections:

- [Cell Annotation Schema](#cell-annotation-schema)
  - [Overview](#overview)
  - [General Requirements](#general-requirements)
  - [Properties](#properties)
    - [Matrix File ID](#matrix-file-id)
    - [Dataset Title](#dataset-title)
    - [Dataset Description](#dataset-description)
    - [Cell Annotation Schema Version](#cell-annotation-schema-version)
    - [Cell Annotation Timestamp](#cell-annotation-timestamp)
    - [Cell Annotation Version](#cell-annotation-version)
    - [Cell Annotation URL](#cell-annotation-url)
    - [Author List](#author-list)
    - [Author Name](#author-name)
    - [Author Contact](#author-contact)
    - [ORCID](#orcid)
    - [Labelsets](#labelsets)
      - [Annotation Key Name](#annotation-key-name)
      - [Annotation Key Description](#annotation-key-description)
      - [Annotation Method](#annotation-method)
      - [Automated Annotation](#automated-annotation)
        - [Algorithm Name](#algorithm-name)
        - [Algorithm Version](#algorithm-version)
        - [Algorithm Repo URL](#algorithm-repo-url)
        - [Reference Location](#reference-location)
      - [Rank](#rank)
    - [Annotations](#annotations)
      - [Labelset](#labelset)
      - [Cell Label](#cell-label)
      - [Cell Fullname](#cell-fullname)
      - [Cell Ontology Term ID](#cell-ontology-term-id)
      - [Cell Ontology Term](#cell-ontology-term)
      - [Cell IDs](#cell-ids)
      - [Rationale](#rationale)
      - [Rationale DOIs](#rationale-dois)
      - [Marker Gene Evidence](#marker-gene-evidence)
      - [Synonyms](#synonyms)
      - [Reviews](#reviews)
        - [Review Datestamp](#review-datestamp)
        - [Reviewer](#reviewer)
        - [Review](#review)
        - [Explanation](#explanation)
    - [Author Annotation Fields](#author-annotation-fields)
    - [Cell Set Accession](#cell-set-accession)
    - [Parent Cell Set Accession](#parent-cell-set-accession)
    - [Transferred Annotations](#transferred-annotations)
      - [Transferred Cell Label](#transferred-cell-label)
      - [Source Taxonomy](#source-taxonomy)
      - [Source Node Accession](#source-node-accession)
      - [Annotation Transfer Comment](#annotation-transfer-comment)
    - [Cells](#cells)
      - [Cell ID](#cell-id)
      - [Confidence](#confidence)
      - [Author Categories](#author-categories)
    - [Negative Marger Gene Evidence](#negative-marger-gene-evidence)
  - [Changelog](#changelog)
    - [August 7, 2025 -- Version 1.0.0](#august-7-2025----version-100)

## General Requirements

This includes any cell-level or cluster-level metadata that can be calculated explicitly from the Data and Assigned Metadata without the need for human intervention. Some examples include # reads detected/cell, # UMI/cell, fraction of cells per cluster derived from each anatomic dissections, expressed neurotransmitter genes (quantitatively defined), average QUANTITATIVE_VALUE (e.g., doublet score) per cluster. Currently none of these are required for the schema, but they are sometimes used for annotation.

A general, open-standard schema for cell annotations which records connections, types, provenance and evidence.

This is designed not to tie-in to a single project (i.e. no tool-specific fields in core schema),and allows for extensions to support ad hoc user fields, new formal schema extensions, and project/tool specific metadata.

## Properties

### Matrix File ID

|BICAN Field Name | matrix_file_id |
|------------------|-----------------|
| BICAN UUID | 5d625688-96da-4c65-97b9-211cbcad4aea |
| Aliases |  |
| Definition | The ID of a matrix file. This is like dataset_url; e.g. `CellXGene_dataset:8e10f1c4-8e98-41e5-b65f-8cd89a887122`.  |
| Data Type | string |

### Dataset Title

| BICAN Field Name | dataset_title |
|-------------------|----------------|
| BICAN UUID | 5aab17df-0830-44d4-bcd8-f954695867d0 |
| Aliases |  |
| Definition | The title of the dataset. This MUST be less than or equal to 200 characters. e.g. 'Human retina cell atlas - retinal ganglion cells'. |
| Data Type | string |

### Dataset Description

| BICAN Field Name | dataset_description |
|-------------------|----------------|
| BICAN UUID | 1b5ff66c-0e00-4a29-8ccf-65dbf59d79da |
| Aliases | description |
| Definition | The description of the dataset. e.g. 'A total of 15 retinal ganglion cell clusters were identified from over 99K retinal ganglion cell nuclei in the current atlas. Utilizing previous characterized markers from macaque, 5 clusters can be annotated.'. |
| Data Type | string |

### Cell Annotation Schema Version

|BICAN Field Name | cellannotation_schema_version |
|------------------|-----------------|
| BICAN UUID | 195cbdbf-d486-4d54-9c1d-83edf0a44ec5 |
| Aliases |  |
| Definition | The version of the Cell Annotation Schema (CAS) used, formatted as '[MAJOR].[MINOR].[PATCH]'. This is used to track the version of the schema used for cell annotations. |
| Data Type | string |

### Cell Annotation Timestamp

|BICAN Field Name | cellannotation_timestamp |
|------------------|-----------------|
| BICAN UUID | 37da06ba-9c15-405f-b5d6-f8d2bf5fc3a3 |
| Aliases |  |
| Definition | Timestamp when published: %yyyy-%mm-%dd %hh:%mm:%ss; Useful in general, though currently only required by CAP. This also could be the same as `development_date`. |
| Data Type | datetime |

### Cell Annotation Version

|BICAN Field Name | cellannotation_version |
|------------------|-----------------|
| BICAN UUID | 439f52e8-e2e6-406c-850c-434d448c8b6d |
| Aliases |  |
| Definition | The CAP taxonomy annotation version; required by CAP. |
| Data Type | string |

### Cell Annotation URL

|BICAN Field Name | cellannotation_url |
|------------------|-----------------|
| BICAN UUID | e47029df-a5cf-49d0-b8de-76302a1e6fbb |
| Aliases |  |
| Definition | A persistent URL of all cell annotations published (per dataset). |
| Data Type | string |

### Author List

|BICAN Field Name | author_list |
|------------------|-----------------|
| BICAN UUID | 15e4be61-b1fb-49a5-9a81-7fed61138256 |
| Aliases | taxonomy users |
| Definition | A list of all collaborators, comma separated [First] [Last]. Called `Taxonomy Users` in taxonomy Google Sheet. |
| Data Type | string |

### Author Name

| BICAN Field Name | author_name |
|------------------|----------------|
| BICAN UUID | 0ea83cdb-cd06-4ef8-84c1-6aec29220759 |
| Aliases | taxonomy author, point person name |
| Definition | The primary author [First Name] [Last Name] of the taxonomy. In CCN was called `taxonomy_author`. In CCN it is also seperated by `cell_set` with "cell_set_alias_assignee". This is called `Point person name` in taxonomy Google Sheet. |
| Data Type | string |

### Author Contact

| BICAN Field Name | author_contact |
|------------------|----------------|
| BICAN UUID | fa084043-3c8e-47cb-959e-2f3daf2165ec |
| Aliases | point person email |
| Definition | A valid email address of the primary author of a taxonomy. This is called `Point person email` in taxonomy Google Sheet. |
| Data Type | string |

### ORCID

| BICAN Field Name | orcid |
|------------------|------------|
| BICAN UUID | 2c96776b-b158-4e0c-ba67-ea7a63efb1e8 |
| Aliases | point person orcid |
| Definition | A valid ORCID of the primary author of the taxonomy. This is called `Point person ORCID` in taxonomy Google Sheet. |
| Data Type | string |

### Labelsets

| BICAN Field Name | labelsets |
|------------------|------------|
| BICAN UUID | 87fa0b7a1-6af7-4f79-8da0-29d7950ea736 |
| Aliases | cluster annotation term set |
| Definition | A data frame representation that contains information about each `cellannotation_set` set of columns (e.g., subclass, class, neurotransmitter, etc.). Specifically: `name`, `description`, and `rank` (0 most specific) and some information about provenance needed for each labelset. This is equilalent to `Cluster annotation term set` in BKP.  |
| Data Type | string |

#### Annotation Key Name

| BICAN Field Name | annotation_key_name |
|------------------|-----------------|
| BICAN UUID | f09d7148-9750-4a9c-8eba-da1a11c3b274 |
| Aliases |  |
| Definition | The name of the annotation key. |
| Data Type | string |

#### Annotation Key Description

| BICAN Field Name | annotation_key_description |
|------------------|-----------------|
| BICAN UUID | 63e9a887-cdf9-4248-ae83-41a720ce8f53 |
| Aliases |  |
| Definition | A description of the annotation key, providing context and details about its use. This should include some text describing what types of cell annotation this annotation key is used to record. |
| Data Type | string |

#### Annotation Method

| BICAN Field Name | annotation_method |
|------------------|-----------------|
| BICAN UUID | 2e91e232-dccb-4584-8a0b-0263660d6c08 |
| Aliases |  |
| Definition | The method used for creating the cell annotations. This MUST be one of the following strings: 'algorithmic', 'manual', or 'both' . |
| Data Type | value set |

#### Automated Annotation

| BICAN Field Name | automated_annotation |
|------------------|-----------------|
| BICAN UUID | 9fba68df-a9f0-4cf9-994d-9b15f31fb88d |
| Aliases |  |
| Definition | A boolean indicating whether the annotation was created using an automated method. This is used to distinguish between annotations that were generated by algorithms versus those that were manually curated. |
| Data Type | boolean |

##### Algorithm Name

| BICAN Field Name | algorithm_name |
|------------------|-----------------|
| BICAN UUID | fd9cb36e-5d29-45d7-8002-c4da15c9a3d1 |
| Aliases |  |
| Definition | The name of the algorithm used. It MUST be a string of the algorithm's name. |
| Data Type | string |

##### Algorithm Version

| BICAN Field Name | algorithm_version |
|------------------|-----------------|
| BICAN UUID | 81ed9281-3f29-46e8-8e06-963afe3e27e4 |
| Aliases |  |
| Definition | The version of the algorithm used (if applicable). It MUST be a string of the algorithm's version, which is typically in the format '[MAJOR].[MINOR]', but other versioning systems are permitted (based on the algorithm's versioning). |
| Data Type | string |

##### Algorithm Repo URL

| BICAN Field Name | algorithm_repo_url |
|------------------|-----------------|
| BICAN UUID | ce81ab8b-3892-473d-883c-c8fa266376ec |
| Aliases |  |
| Definition | This field denotes the URL of the version control repository associated with the algorithm used (if applicable). It MUST be a string of a valid URL. |
| Data Type | string |

##### Reference Location

| BICAN Field Name | reference_location |
|------------------|-----------------|
| BICAN UUID | 4d60f911-5c5c-4ebc-a1df-b243a7252730 |
| Aliases |  |
| Definition | This field denotes a valid URL of the annotated dataset that was the source of annotated reference data. This MUST be a string of a valid URL. The concept of a 'reference' specifically refers to 'annotation transfer' algorithms, whereby a 'reference' dataset is used to transfer cell annotations to the 'query' dataset. |
| Data Type | string |

#### Rank

| BICAN Field Name | rank |
|------------------|-----------------|
| BICAN UUID | 25bb3ce6-eda7-47be-8855-317a3b1002ea |
| Aliases |  |
| Definition | A number indicating relative granularity with 0 being the most specific. Use this where a single dataset has multiple keys that are used consistently to record annotations and different levels of granularity. |
| Data Type | integer |

### Annotations

| BICAN Field Name | annotations |
|------------------|-----------------|
| BICAN UUID | 46e6ec2f-6baf-4df9-bfbd-36463694be93 |
| Aliases |  |
| Definition | A list of the annotations. |
| Data Type | string |

#### Labelset

| BICAN Field Name | labelset |
|------------------|-----------------|
| BICAN UUID | 9a521209-c4f3-40df-aab2-17ada8d3abce |
| Aliases |  |
| Definition | The unique name of the set of cell annotations. Each cell within the AnnData/Seurat file MUST be associated with a 'cell_label' value in order for this to be a valid 'cellannotation_setname'. |
| Data Type | string, required |

#### Cell Label

| BICAN Field Name | cell_label |
|------------------|-----------------|
| BICAN UUID | 736fdcaf-06b5-43a9-ae38-022c07d44675 |
| Aliases |  |
| Definition | This denotes any free-text term which the author uses to annotate cells, i.e. the preferred cell label name used by the author. Abbreviations are exceptable in this field; refer to 'cell_fullname' for related details. Certain key words have been reserved:- 'doublets' is reserved for encoding cells defined as doublets based on some computational analysis- 'junk' is reserved for encoding cells that failed sequencing for some reason, e.g. few genes detected, high fraction of mitochondrial reads- 'unknown' is explicitly reserved for unknown or 'author does not know'- 'NA' is incomplete, i.e. no cell annotation was provided. |
| Data Type | string |

#### Cell Fullname

|BICAN Field Name | cell_fullname |
|------------------|-----------------|
| BICAN UUID | b5036e70-9181-45c0-8fdb-66da93be2d87 |
| Aliases | cell_set_preferred_alias |
| Definition | The longer name for a cell type (e.g., "Somatostatin interneuron 1" rather than "SST 1"). This was called the cell_set_preferred_alias in CCN. |
| Data Type | string |

#### Cell Ontology Term ID

|BICAN Field Name | cell_ontology_term_id |
|------------------|-----------------|
| BICAN UUID | fe21fa47-6fd2-4432-82de-2412db9462c6 |
| Aliases | cell_set_ontology_tag |
| Definition | The highest resolution Cell Ontology term ID corresponding to the cell type. This was called `cell_set_ontology_tag` in CCN. |
| Data Type | string |

#### Cell Ontology Term

|BICAN Field Name | cell_ontology_term |
|------------------|-----------------|
| BICAN UUID | 52685f23-9bcc-416a-ae70-e9de43ef4123 |
| Aliases | cell_set_structure |
| Definition | The highest resolution Cell Ontology term (name) corresponding to the cell type. This was called `cell_set_structure` in CCN and was also largely mapping to the `cell_set_aligned_alias`. |
| Data Type | string |

#### Cell IDs

|BICAN Field Name | cell_ids |
|------------------|-----------------|
| BICAN UUID | 64cbaff0-a87b-4cab-9107-4feb97e07e61 |
| Aliases | cell_set_structure |
| Definition | List of cell barcode sequences/UUIDs used to uniquely identify the cells within the AnnData/Seurat matrix. Any and all cell barcode sequences/UUIDs MUST be included in the AnnData/Seurat matrix. |
| Data Type | string |

#### Rationale

|BICAN Field Name | rationale |
|------------------|-----------------|
| BICAN UUID | a76fa81e-ba3f-4813-ac7c-cce1f43683a6 |
| Aliases | |
| Definition | Free text evidence for cell annotations. This human-readable free-text must be encoded as a single string and has a 2000-character limit. |
| Data Type | string |

#### Rationale DOIs

|BICAN Field Name | rationale_dois |
|------------------|-----------------|
| BICAN UUID | cd9ce030-058c-4890-b552-750735c90ba4 |
| Aliases | cell_set_alias_citation |
| Definition | A list of publication DOI's of rationale. In CCN, this is called "cell_set_alias_citation". NOTE: this can use comma-separated, pipe-separated, or /#/-separated. |
| Data Type | string |

#### Marker Gene Evidence

|BICAN Field Name | marker_gene_evidence |
|------------------|-----------------|
| BICAN UUID | e790e621-e7f2-42ba-8f20-bcac2c1f86e4 |
| Aliases |  |
| Definition | A list (comma-separated) of marker genes used as evidence for cell type annotation (e.g., by NS-Forest). Note: This is reserved for ontology markers. |
| Data Type | string |

#### Synonyms

|BICAN Field Name | synonyms |
|------------------|-----------------|
| BICAN UUID | 137f6d7d-d257-4ffb-8a14-24fcb0bab0e9 |
| Aliases | cell_set_additional_alias |
| Definition | A list (comma-separated) of aliases or synonyms (e.g., "neuroglial cell, glial cell, neuroglia"). This was called `cell_set_additional_alias` in CCN. |
| Data Type | string |

#### Reviews

|BICAN Field Name | reviews |
|------------------|-----------------|
| BICAN UUID | 54d10921-012f-4403-bcaa-853a170c29d2 |
| Aliases |  |
| Definition | A list of reviews. |
| Data Type | string |

##### Review Datestamp

|BICAN Field Name | review_datestamp |
|------------------|-----------------|
| BICAN UUID | 5a59ce8d-b35b-4ce7-8515-a93e0ba5818a |
| Aliases |  |
| Definition | Date and time review was last edited. |
| Data Type | datetime |

##### Reviewer

|BICAN Field Name | reviewer |
|------------------|-----------------|
| BICAN UUID | 83675161-f5c0-4fcc-9608-52ee45974788 |
| Aliases |  |
| Definition | Review author. |
| Data Type | string |

##### Review

|BICAN Field Name | review |
|------------------|-----------------|
| BICAN UUID | ca5dd5dd-d60e-420c-a88c-de4a38254e86 |
| Aliases |  |
| Definition | Reviewer's verdict on the annotation. Must be `agree` or `disagree`. |
| Data Type | value set |

##### Explanation

|BICAN Field Name | explanation |
|------------------|-----------------|
| BICAN UUID | 632f2913-a0be-411d-a58f-9566b9aaaa93 |
| Aliases |  |
| Definition | Free-text explanation of annotation review. This is required if the review is `disagree` and should include reasons for disagreement. |
| Data Type | string |

### Author Annotation Fields

|BICAN Field Name | author_annotation_fields |
|------------------|-----------------|
| BICAN UUID | 2acaa8e2-2b31-4f0b-bbea-03a03f6d9ea3 |
| Aliases |  |
| Definition | A dictionary of author defined key value pairs annotating the cell set. The names and aims of these fields MUST not clash with official annotation fields. |
| Data Type | string |

### Cell Set Accession

|BICAN Field Name | cell_set_accession |
|------------------|-----------------|
| BICAN UUID | 55cb81b4-5f6d-4930-aba6-0ef1d1784124 |
| Aliases | cluster annotation term |
| Definition | The ID corresponding to the cell_set; called the "Cluster Annotation Term" in BKP. This is critical for scrattch.taxonomy and scrattch.mapping to work properly. |
| Data Type | string |

### Parent Cell Set Accession

|BICAN Field Name | parent_cell_set_accession |
|------------------|-----------------|
| BICAN UUID | bfa1e2d9-e65d-480d-b54c-9947acaddd93 |
| Aliases | parent_cluster_annotation_term_id |
| Definition | The ID corresponding to the parent cell_set. This corresponds to the parent Cluster Annotation Term ID in knowledgebase. |
| Data Type | string |

### Transferred Annotations

| BICAN Field Name | transferred_annotations |
|------------------|------------|
| BICAN UUID | 1c3f146c-eb76-451d-9925-15f58f47f71a |
| Aliases |  |
| Definition | A dataframe where each column is a string corresponding to the taxonomy of comparison; values are the transferred cell label from that taxonomy. This is used to store annotations that have been transferred from one taxonomy to another, allowing for cross-taxonomy comparisons. |
| Data Type | string |

#### Transferred Cell Label

| BICAN Field Name | tranferred_cell_label |
|------------------|------------|
| BICAN UUID | e2c995b9-2448-4dd8-904a-bf32d6df6233 |
| Aliases |  |
| Definition | The cell label that was transferred from the reference dataset. |
| Data Type | string |

#### Source Taxonomy

| BICAN Field Name | source_taxonomy |
|------------------|------------|
| BICAN UUID | c36dce85-4c4a-4419-8ceb-388236a65b3e |
| Aliases |  |
| Definition | The PURL of the source taxonomy. |
| Data Type | string |

#### Source Node Accession

| BICAN Field Name | source_node_accession |
|------------------|------------|
| BICAN UUID | e119d520-a55b-4b36-9be1-7928f13d3044 |
| Aliases |  |
| Definition | The accession of the node that the label was transferred from.  |
| Data Type | string |

#### Annotation Transfer Comment

| BICAN Field Name | annotation_transfer_comment |
|------------------|-----------------|
| BICAN UUID | 4b846509-4955-4226-b931-5a68041127c8 |
| Aliases |  |
| Definition | Free-text field for comments on the annotation transfer. |
| Data Type | string |

### Cells

| BICAN Field Name | cells |
|------------------|-----------------|
| BICAN UUID | ec4f450b-cf5f-4bfc-9b07-8eac2703c326 |
| Aliases |  |
| Definition | The list of cells that are annotated -- by convention this is only used for annotation transfer labelset. It MUST not be combined with the `cell_ids` field.  |
| Data Type | string |

#### Cell ID

| BICAN Field Name | cell_id |
|------------------|---------|
| BICAN UUID | 34ca0703-429f-4920-8a08-dd4c61b29444 |
| Aliases | cell_label |
| Definition | Identifier corresponding to each individual cell. Included in the data and in every other location to refer to the data (e.g., metadata and annotations). In AnnData files, the ID corresponding to each individual cell is stored in the obs index. |
| Data Type | string |

#### Confidence

| BICAN Field Name | confidence |
|------------------|---------|
| BICAN UUID | e81a70d8-d0db-4ba8-99bd-aef3cb0fd1e5 |
| Aliases | confidence_score |
| Definition | The normalized confidence score. |
| Data Type | float |

#### Author Categories

| BICAN Field Name | author_categories |
|------------------|---------|
| BICAN UUID | 5f3854a0-da07-4cdc-aea1-3ec2efe17cf9 |
| Aliases |  |
| Definition | A list of author defined categories. |
| Data Type | string |

### Negative Marger Gene Evidence

| BICAN Field Name | negative_marker_gene_evidence |
|------------------|---------|
| BICAN UUID | 5720e5f6-18a5-4cb4-b7bf-afef27b8b3d1 |
| Aliases |  |
| Definition | A list of names of genes whose expression in the cells being annotated is explicitly used as evidence against this cell annotation. Each gene MUST be included in the matrix of the AnnData/Seurat file. |
| Data Type | string |

## Changelog

### August 7, 2025 -- Version 1.0.0

- Initial version of the Cell Annotation Schema.
- Added all required fields and definitions.
- Established relationships between fields and their respective data types.
  