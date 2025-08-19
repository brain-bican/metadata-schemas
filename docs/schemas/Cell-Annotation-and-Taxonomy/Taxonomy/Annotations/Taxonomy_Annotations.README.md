# Cell Annotation Schema -- Taxonomy Annotations

Document Status: _Approved BICAN Standard_

Version: 1.0

Owner: @UCDNJJ, @jeremymiller

Reviewers: @patrick-lloyd-ray, @carolth, @djarecka, @memartone

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 10-03-2025

## Overview

The BICAN Cell Annotation Metadata schema specifies the metadata relating to cell annotations that can be taken from a variety of sources in BICAN. These metadata reflect the metadata needed to accurately track cell annotations metadata in BICAN. As such, it is a collaborative schema that reflects the joint efforts of members of BICAN.

This document has the following sections:

- [Cell Annotation Schema -- Taxonomy Annotations](#cell-annotation-schema----taxonomy-annotations)
  - [Overview](#overview)
  - [General Requirements](#general-requirements)
  - [obs](#obs)
    - [Cell ID](#cell-id)
    - [Feature Matrix Label](#feature-matrix-label)
    - [Dataset Label](#dataset-label)
    - [Color Vector](#color-vector)
    - [Vector ID](#vector-id)
    - [Cluster ID](#cluster-id)
    - [Cluster Label](#cluster-label)
    - [Additional Uncontrolled Metadata](#additional-uncontrolled-metadata)
  - [var](#var)
    - [Marker Genes](#marker-genes)
  - [uns](#uns)
  - [uns fields associated with taxonomy metadata (e.g., different label sets)](#uns-fields-associated-with-taxonomy-metadata-eg-different-label-sets)
    - [Taxonomy Title](#taxonomy-title)
    - [Taxonomy ID](#taxonomy-id)
    - [Taxonomy Description](#taxonomy-description)
    - [Taxonomy Citation](#taxonomy-citation)
    - [Marker Gene Metadata](#marker-gene-metadata)
    - [Taxonomy Directory](#taxonomy-directory)
    - [Dataset URL](#dataset-url)
    - [Matrix File ID](#matrix-file-id)
    - [Author List](#author-list)
    - [Author Name](#author-name)
    - [Author Contact](#author-contact)
    - [ORCID](#orcid)
    - [Annotation Source](#annotation-source)
  - [Changelog](#changelog)
    - [August 7, 2025 -- Version 1.0.0](#august-7-2025----version-100)
    - [January 15, 2024](#january-15-2024)
  
## General Requirements

This includes any fields related to the annotation of clusters or groups of clusters (collectively called "cell sets"). This includes things like cluster levels, cluster relationships, canonical marker genes, links to existing ontologies (e.g., CL, UBERON) based on judgement calls, expert annotations, and dendrograms. For the annotation labelsets, please refer to the [BICAN Cell Annotation Labelsets](https://github.com/brain-bican/metadata-schemas/blob/8ddba5750e615e51b13bf1e5a1ef6c5b73e8c071/docs/schemas/Cell-Annotation-and-Taxonomy/Taxonomy/Annotations/Labelsets/Labelsets.md).

## obs

The obs component contains cell level metadata.

The obs component also contains cell set metadata summarized at the cell level. The proposal is to store all of this in the uns in json format and create helper functions to duplicate information as obs columns as needed.  Currently there is a standard way of doing this for CAP, and we will implement a mechanism for this in scrattch.taxonomy as well.

### Cell ID

| BICAN Field Name | cell_id |
|------------------|---------|
| BICAN UUID | 34ca0703-429f-4920-8a08-dd4c61b29444 |
| Aliases | cell_label |
| Definition | Identifier corresponding to each individual cell. Included in the data and in every other location to refer to the data (e.g., metadata and annotations). In AnnData files, the ID corresponding to each individual cell is stored in the obs index. |
| Data Type | string |

### Feature Matrix Label

| BICAN Field Name   | feature_matrix_label |
|--------------------|---------------------|
| BICAN UUID         | 2c860046-83d5-47f9-98d5-29ce81446819 |
| Aliases            |                     |
| Definition         | ID of the associated feature matrix where the data is stored (if not included in this file). This is used in the Brain Knowledge Platform (BKP) when data is found elsewhere for connected cell to data file. |
| Data Type          | string              |

### Dataset Label

| BICAN Field Name | dataset_label |
|------------------|---------------|
| BICAN UUID | 519ecc82-e397-4b1e-a846-d27d48610ff3 |
| Aliases |  |
| Definition | Link between each cell and each dataset in BKP. In CAS, this is a taxonomy-level variable in uns called `dataset_url`. |
| Data Type | string |

### Color Vector

| BICAN Field Name | [COLUMN_NAME]_color |
|------------------|---------------------|
| BICAN UUID | 0ab06f78-6df2-4555-8990-3eec36b2adbb |
| Aliases |  |
| Definition | The color vector for metadata/taxonomy values in format [COLUMN_NAME]_label. This is ONLY used for molgen-shiny plots. Some metadata files come with these and some do not. This field is OPTIONAL. |
| Data Type | string |

### Vector ID

| BICAN Field Name | [COLUMN_NAME]_id |
|------------------|------------|
| BICAN UUID | 701b32ca-4d95-47c5-8213-e7ab8c5373eb |
| Aliases |  |
| Definition | The order of metadata values (e.g., the levels of a factor, or ascending order of a numeric) for metadata/taxonomy values in format [COLUMN_NAME]_id. |
| Data Type | string |

### Cluster ID

| BICAN Field Name | cluster_id |
|------------------|------------|
| BICAN UUID       | 10be876f-7b4b-4420-af9f-d379124a690d |
| Aliases          |  |
| Definition       | A unique integer value corresponding to each cluster in the taxonomy, which also (ideally but not necessarily) encodes the order of clusters in visualizations. Once a taxonomy is minted, this cannot change. This is the CRITICAL column used for cluster annotations. It is the baseline for the majority of cell_annotation columns. Note that “cell_set_accession_ids” and “cluster hash values” can be assigned after these “cluster_ids” are agreed upon. This is a prerequisite for annotations. |
| Data Type       | integer     |

### Cluster Label

| BICAN Field Name | cluster_label |
|------------------|------------|
| BICAN UUID       | 307b18c9-b258-495c-bbe9-96bb4b23ef1d |
| Aliases          | cluster |
| Definition       | A human-readable cluster name used primarily by scientists and other folks. This is the same as “cell_label” for cell sets when the “label_set” is cluster. It's also used for cirrocumulus. This is the CRITICAL column used for cluster annotations. It is the baseline for the majority of cell_annotation columns. Sometimes called cluster_label : ["Annotations"] : There is also an additional cluster_alias column used in mouse whole brain data and for BKP. |
| Data Type       | string     |

### Additional Uncontrolled Metadata

| BICAN Field Name | [additional uncontrolled metadata] |
|------------------|-------------------------------|
| BICAN UUID | d417074d-5f7a-4bb8-8a7f-11e20fdcca97 |
| Aliases |  |
| Definition | Additional uncontrolled cell metadata. These are not required, but any additional columns are allowed by all h5ad formats. |
| Data Type | string |

## var

The var component contains gene level metadata. gene: Same vector included in "data" to link between files.

### Marker Genes

| BICAN Field Name | marker_genes_[...] |
|------------------|----------------|
| BICAN UUID | deddeb0d-0df2-4e53-bf69-21be2c305cd0 |
| Aliases |  |
| Definition | A set of logical vectors (T/F) indicating which genes are markers used to build dendrogram, or for other purposes. The [...] part of the name links to additional metadata in the uns. This needs to be UPDATED in AIT to allow multiple marker gene sets; markers currently stored differently in CAP. |
| Data Type | string |

## uns

The uns component contains more general information and fields with formatting incompatible with the above components. Much of the information about annotations is stored in this field, so we divide it up below.

Proposal: store everything that goes in the TDT taxonomy annotations in a single field called “annotations” and match the TDT structure.  Then write conversions between uns and obs for most h5ad use cases.

## uns fields associated with taxonomy metadata (e.g., different label sets)

### Taxonomy Title

| BICAN Field Name | taxonomy_title |
|------------------|----------------|
| BICAN UUID | 086ee228-c32c-4f3c-b431-108775136775 |
| Aliases | taxonomy_short_name, title |
| Definition | Taxonomy name (e.g., "AIT30"); called `title` in cellxgene. This is called `Taxonomy short name` in taxonomy Google Sheet. |
| Data Type | string |

### Taxonomy ID

| BICAN Field Name | taxonomy_id |
|------------------|----------------|
| BICAN UUID | b9c06d39-4e0e-4345-8883-26e0cf2960ca |
| Aliases |  |
| Definition | The ID of a taxonomy in CCN format (e.g., "CCN030420240"). This MUST be globally unique. It is also used in the PURL system and called `Taxonomy ID` in taxonomy Google Sheet. |
| Data Type | string |

### Taxonomy Description

| BICAN Field Name | description |
|------------------|------------|
| BICAN UUID | 03da4573-6a72-4721-b1d4-f572396a49fb |
| Aliases |  |
| Definition | Free text description of the taxonomy (or of the dataset on CAP). This is called `Description` in taxonomy Google Sheet. |
| Data Type | string |

### Taxonomy Citation

| BICAN Field Name | taxonomy_citation |
|------------------|-------------------|
| BICAN UUID | e23582e7-3be3-4ae9-8682-d904b21daaa3 |
| Aliases | publication |
| Definition | Publication DOI's of the taxonomy (e.g., "doi:10.1038/s41586-018-0654-5"), separated by pipe. This is called `Publication` in taxonomy Google Sheet. |
| Data Type | string |

### Marker Gene Metadata

| BICAN Field Name | marker_gene_metadata |
|------------------|----------------|
| BICAN UUID | b70f1ded-2bd8-426d-94de-bd6e28ae7989 |
| Aliases |  |
| Definition | Metadata about any new marker gene lists added, if any. |
| Data Type | string |

### Taxonomy Directory

| BICAN Field Name | taxonomy_dir |
|------------------|----------------|
| BICAN UUID | d414a71b-aa2b-403b-8a3d-2f201df25d5b |
| Aliases | taxonomyDir, taxonomy_directory, taxonomy_file_location |
| Definition | The location of the h5ad file. This is called `Taxonomy file location` in taxonomy Google Sheet. |
| Data Type | string |

### Dataset URL

| BICAN Field Name | dataset_url |
|------------------|----------------|
| BICAN UUID | 029268dc-80e7-4ed5-976b-feecf1eb611f |
| Aliases |  |
| Definition | The PURL of the dataset; this is the URL where the dataset can be found. |
| Data Type | string |

### Matrix File ID

| BICAN Field Name | matrix_file_id |
|------------------|----------------|
| BICAN UUID | 5d625688-96da-4c65-97b9-211cbcad4aea |
| Aliases |  |
| Definition | The ID of a matrix file. This is like dataset_url; e.g. `CellXGene_dataset:8e10f1c4-8e98-41e5-b65f-8cd89a887122`. |
| Data Type | string |

### Author List

| BICAN Field Name | author_list |
|------------------|----------------|
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

### Annotation Source

| BICAN Field Name | annotation_source |
|------------------|-------------------|
| BICAN UUID | d37cf51c-d38e-4ef3-968f-bfe78dac03a9 |
| Aliases |  |
| Definition | Any additional metadata about the annotation algorithm used. This is similar to `taxonomy algorithm info` stored for CCN |
| Data Type | string |

## Changelog

### August 7, 2025 -- Version 1.0.0

- **8-07-2025**: Finalized schema and added document status.
- **8-07-2025**: Approved as BICAN Standard.

### January 15, 2024

- **1-15-2024**: Added BICAN field names for all fields in the schema.
- **1-15-2024**: Added BICAN UUIDs for all fields in the schema.
- **1-15-2024**: Added aliases for some fields in the schema.
- **1-15-2024**: Added definitions for all fields in the schema.
- **1-15-2024**: Added data types for all fields in the schema.
- **1-15-2024**: Added links to the BICAN schema for each field.
