# Taxonomy Tooling Metadata Schema

Document Status: _Approved BICAN Standard_

Version: 1.0

Owner: @UCDNJJ, @jeremymiller

Reviewers: @patrick-lloyd-ray, @carolth, @djarecka, @memartone

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 10-03-2025

## Overview

The BICAN Taxonomy Tooling Metadata schema specifies the metadata relating to taxonomy tooling that can be taken from a variety of sources in BICAN. These metadata reflect the metadata needed to accurately track taxonomy tooling metadata in BICAN. As such, it is a collaborative schema that reflects the joint efforts of members of BICAN.

This document has the following sections:

- [Taxonomy Tooling Metadata Schema](#taxonomy-tooling-metadata-schema)
  - [Overview](#overview)
  - [General Requirements](#general-requirements)
  - [obs](#obs)
    - [Cell Label](#cell-label)
    - [Parent Cell Set Accession](#parent-cell-set-accession)
  - [uns](#uns)
    - [Dataset URL](#dataset-url)
    - [Matrix File ID](#matrix-file-id)
    - [Author List](#author-list)
    - [Schema Version](#schema-version)
    - [\[...\] Color](#-color)
    - [Cell Annotation Schema Version](#cell-annotation-schema-version)
    - [Cell Annotation Timestamp](#cell-annotation-timestamp)
    - [Cell Annotation Version](#cell-annotation-version)
    - [Additional Information](#additional-information)
  - [Changelog](#changelog)
    - [August 7, 20205 -- Version 1.0.0](#august-7-20205----version-100)
    - [Pre-release Changelog](#pre-release-changelog)

## General Requirements

This includes any fields required for specific tools (e.g., cellxgene, TDT, CAS, CAP) that are not strictly part of the taxonomy and that do not fit in any of the above categories. This includes things like schema versions and redundent fields from above with different column names. These may not need to match between schemas (or even be encoded into schemas).

## obs

The obs component contains cell level metadata, as above.

### Cell Label

|BICAN Field Name | cell_id |
|------------------|-----------------|
| BICAN UUID | 34ca0703-429f-4920-8a08-dd4c61b29444 |
| Aliases | cell_label |
| Definition | Identifier corresponding to each individual cell. Included in the data and in every other location to refer to the data (e.g., metadata and annotations). In AnnData files, the ID corresponding to each individual cell is stored in the obs index. |
| Data Type | string |

### Parent Cell Set Accession

|BICAN Field Name | parent_cell_set_accession |
|------------------|-----------------|
| BICAN UUID | bfa1e2d9-e65d-480d-b54c-9947acaddd93 |
| Aliases | parent_cluster_annotation_term_id |
| Definition | The ID corresponding to the parent cell_set. This corresponds to the parent Cluster Annotation Term ID in knowledgebase. |
| Data Type | string |

## uns

The uns component contains taxonomy associated files useful for reproducing analysis or mapping against the taxonomy.

### Dataset URL

|BICAN Field Name | dataset_url |
|------------------|-----------------|
| BICAN UUID | 029268dc-80e7-4ed5-976b-feecf1eb611f |
| Aliases |  |
| Definition | The PURL of the dataset; this is the URL where the dataset can be found. |
| Data Type | string |

### Matrix File ID

|BICAN Field Name | matrix_file_id |
|------------------|-----------------|
| BICAN UUID | 5d625688-96da-4c65-97b9-211cbcad4aea |
| Aliases |  |
| Definition | The ID of a matrix file. This is like dataset_url; e.g. `CellXGene_dataset:8e10f1c4-8e98-41e5-b65f-8cd89a887122`.  |
| Data Type | string |

### Author List

|BICAN Field Name | author_list |
|------------------|-----------------|
| BICAN UUID | 15e4be61-b1fb-49a5-9a81-7fed61138256 |
| Aliases | taxonomy users |
| Definition | A list of all collaborators, comma separated [First] [Last]. Called `Taxonomy Users` in taxonomy Google Sheet. |
| Data Type | string |

### Schema Version

|BICAN Field Name | schema_version |
|------------------|-----------------|
| BICAN UUID | 34a60ffb-c6ac-4264-9ec3-5846c3745207 |
| Aliases |  |
| Definition | The cellxgene schema version (e.g., "3.0.0"). |
| Data Type | string |

### [...] Color

|BICAN Field Name | [...]_color |
|------------------|-----------------|
| BICAN UUID | b2ee3685-aa64-43d3-b351-9cec1b6214ea |
| Aliases |  |
| Definition |  RGB color vector for metadata [...]; required only for selecting colors in cirrocumulus. This may be the same as the [COLUMN_NAME]_color. |
| Data Type | integer |

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

### Additional Information

|BICAN Field Name | additional_information |
|------------------|-----------------|
| BICAN UUID | 994e6572-2aca-4f0a-89f0-6b7fd893a36b |
| Aliases |  |
| Definition | Placeholder for several other (seemingly redundant) fields required by external tools (e.g., CAP, cellxgene). |
| Data Type | string |

## Changelog

### August 7, 20205 -- Version 1.0.0

- **8-07-2025**: Finalized schema and added document status.
- **8-07-2025**: Approved as BICAN Standard.

### Pre-release Changelog

- **10-03-2025**: Initial version created.
- **10-04-2025**: Added additional fields and clarified definitions.
- **10-05-2025**: Added UUIDs and clarified definitions.
