# Calculated Metadata Schema

Document Status: _Approved BICAN Standard_

Version: 1.0

Owner: @UCDNJJ, @jeremymiller

Reviewers: @patrick-lloyd-ray, @carolth, @djarecka, @memartone

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 10-03-2025

## Overview

The BICAN Taxonomy Calculated Metadata schema specifies the metadata relating to taxonomy metadata that can be taken from a variety of sources in BICAN. These metadata reflect the metadata needed to accurately track taxonomy metadata in BICAN. As such, it is a collaborative schema that reflects the joint efforts of members of BICAN.

This document has the following sections:

## Table of Contents

- [Overview](#overview)
- [General Requirements](#general-requirements)
    - [obs](#obs)
        - [Cell ID](#cell-id)
        - [Feature Matrix Label](#feature-matrix-label)
        - [Dataset Label](#dataset-label)
        - [Color Vector](#color-vector)
        - [ID Vector](#id-vector)
        - [Additional Uncontrolled Metadata](#additional-uncontrolled-metadata)
        - [Calculated Metadata Metadata](#calculated-metadata-metadata)
        - [Cell Annotation Schema](#cell-annotation-schema)
- [Changelog](#changelog)

## General Requirements

This includes any cell-level or cluster-level metadata that can be calculated explicitly from the Data and Assigned Metadata without the need for human intervention. Some examples include # reads detected/cell, # UMI/cell, fraction of cells per cluster derived from each anatomic dissections, expressed neurotransmitter genes (quantitatively defined), average QUANTITATIVE_VALUE (e.g., doublet score) per cluster. Currently none of these are required for the schema, but they are sometimes used for annotation.

### obs

The obs component contains cell level metadata from the experiment

#### Cell ID

| BICAN Field Name | cell_id |
|------------------|------------|
| BICAN UUID | 34ca0703-429f-4920-8a08-dd4c61b29444 |
| Aliases |  |
| Definition | Identifier corresponding to each individual cell. Included in the data and in every other location to refer to the data (e.g., metadata and annotations). In AnnData files, the ID corresponding to each individual cell is stored in the obs index. |
| Data Type | string |

#### Feature Matrix Label

| BICAN Field Name | feature_matrix_label |
|------------------|----------------------|
| BICAN UUID | 2c860046-83d5-47f9-98d5-29ce81446819 |
| Aliases |  |
| Definition | Identifier corresponding to the feature matrix. Included in the data and in every other location to refer to the data (e.g., metadata and annotations). In AnnData files, the ID corresponding to each individual cell is stored in the obs index. |
| Data Type | string |

#### Dataset Label

| BICAN Field Name | dataset_label |
|------------------|----------------|
| BICAN UUID | 519ecc82-e397-4b1e-a846-d27d48610ff3 |
| Aliases |  |
| Definition | Identifier corresponding to the dataset. Included in the data and in every other location to refer to the data (e.g., metadata and annotations). In AnnData files, the ID corresponding to each individual cell is stored in the obs index. |
| Data Type | string |

#### Color Vector

| BICAN Field Name | [COLUMN_NAME]_color |
|------------------|---------------------|
| BICAN UUID | 0ab06f78-6df2-4555-8990-3eec36b2adbb |
| Aliases |  |
| Definition | Color associated with the cell. Included in the data and in every other location to refer to the data (e.g., metadata and annotations). In AnnData files, the ID corresponding to each individual cell is stored in the obs index. |
| Data Type | string |

#### ID Vector

| BICAN Field Name | [COLUMN_NAME]_id |
|------------------|------------------|
| BICAN UUID | 701b32ca-4d95-47c5-8213-e7ab8c5373eb |
| Aliases |  |
| Definition | The order of metadata values (e.g., the levels of a factor, or ascending order of a numeric). Likely should use “rank” or “order” rather than “id”, since these are not identifiers. Included in the data and in every other location to refer to the data (e.g., metadata and annotations). In AnnData files, the ID corresponding to each individual cell is stored in the obs index. |
| Data Type | string |

#### Additional Uncontrolled Metadata

| BICAN Field Name | [additional uncontrolled metadata] |
|------------------|-------------------------------|
| BICAN UUID | d417074d-5f7a-4bb8-8a7f-11e20fdcca97 |
| Aliases |  |
| Definition | Additional uncontrolled cell metadata. These are not required, but any additional columns are allowed by all h5ad formats. |
| Data Type | string |

#### Calculated Metadata Metadata

| BICAN Field Name | calculated_metadata_metadata |
|------------------|-------------------------------|
| BICAN UUID | daf95e1a-37c5-4edf-889b-3f552b13e09c |
| Aliases |  |
| Definition | Information about the calculated_metadata itself. |
| Data Type | string |

#### Cell Annotation Schema

| BICAN Field Name | cell_annotation_schema |
|------------------|-------------------------|
| BICAN UUID | 6a32b2d5-22d2-457d-b43e-c53cf96729bd |
| Aliases |  |
| Definition | Extended metadata about annotations and labelsets stored in JSON. |
| Data Type | string |

## Changelog

### August 7, 2025 -- Version 1.0.0

* **8-07-2025**: Finalized schema and added document status.
* **8-07-2025**: Approved as BICAN Standard.

### Pre-release Changelog

* **10-03-2025**: Initial version created.
* **10-04-2025**: Added additional fields and clarified definitions.
* **10-05-2025**: Added UUIDs and clarified definitions.