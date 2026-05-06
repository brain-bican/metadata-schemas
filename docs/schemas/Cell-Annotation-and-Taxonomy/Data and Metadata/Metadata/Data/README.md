# Cell Annotation and Taxonomy Data Schema

Document Status: _Approved BICAN Standard_

Version: 1.0

Owner: @UCDNJJ, @jeremymiller

Reviewers: @patrick-lloyd-ray, @carolth, @djarecka, @memartone

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 10-03-2025

## Overview

The BICAN Cell Annotation and Taxonomy Data Schema specifies the data relating to cell annotations that can be taken from a variety of sources in BICAN. As such, it is a collaborative schema that reflects the joint efforts of members of BICAN.

This document has the following sections:

- [Cell Annotation and Taxonomy Data Schema](#cell-annotation-and-taxonomy-data-schema)
  - [Overview](#overview)
  - [Schema Components](#schema-components)
    - [Cell Label](#cell-label)
    - [Gene](#gene)
    - [ENSEMBL ID](#ensembl-id)
    - [Biotype](#biotype)
    - [Gene Name](#gene-name)
    - [Additional Gene Information](#additional-gene-information)
    - [Dataset Metadata](#dataset-metadata)
  - [Changelog](#changelog)
    - [August 7, 2025 -- Version 1.0.0](#august-7-2025----version-100)
    - [Pre-release Changelog](#pre-release-changelog)

## Schema Components

### Cell Label

| BICAN Field Name | cell_id |
|-----------|-----------|
| BICAN UUID | 34ca0703-429f-4920-8a08-dd4c61b29444 |
| Alises | cell_label |
| Description | Identifier corresponding to each individual cell. Included in the data and in every other location to refer to the data (e.g., metadata and annotations). In AnnData files, the ID corresponding to each individual cell is stored in the obs index. |
| Type | String |

### Gene

| BICAN Field Name | gene |
|-----------|-----------|
| BICAN UUID | 39a71ba6-895b-4e81-8f00-cb7505fc3ae6 |
| Aliases | gene_symbol |
| Description | A vector of gene symbols. This is broadly useful in the community for defining genes. This is called `gene_symbol` in BKP. CELLxGENE uses a very specific version of ensembl_id for the INDEX. |
| Type | string |

### ENSEMBL ID

| BICAN Field Name | ensembl_id |
|-----------|-----------|
| BICAN UUID | 0925b6b6-c117-4f6b-964f-f46368127512 |
| Aliases | gene_identifier |
| Description | A vector of corresponding Ensembl IDs for each gene symbol. This is required for disambiguation of gene symbols; called gene_identifier in BKP. This is optional for AIT. |
| Type | string |

### Biotype

| BICAN Field Name | biotype |
|-----------|-----------|
| BICAN UUID | 3d0fc718-4ca7-4e98-8185-d45212a80415 |
| Aliases |  |
| Description | The biotype from the gtf file (e.g., protein_coding); used in BKP and BICAN for filtering of genes (but optional elsewhere). |
| Type | string |

### Gene Name

| BICAN Field Name | gene_name |
|-----------|-----------|
| BICAN UUID | 612f27c3-12c5-4db4-b0af-894972c42907 |
| Aliases | gene_full_name |
| Description | Longer gene name from the gtf file; used in BKP (optional for now). |
| Type | string |

### Additional Gene Information

| BICAN Field Name | additional_gene_info |
|-----------|-----------|
| BICAN UUID | 0332caff-8232-45b4-b4d1-079f973a8504 |
| Aliases |  |
| Description | Optional uncontrolled gene info; could include gene length, Genecode IDs, NCBI identifiers, etc. |
| Type | string |

### Dataset Metadata

| BICAN Field Name | dataset_metadata |
|-----------|-----------|
| BICAN UUID | 92e98047-7e37-42bb-9ba7-42dfae3698f5 |
| Aliases |  |
| Description | Information about the data set itself. This could include some combination of information recorded for Annotations: description, dataset_url, title, dataset_doi, author_list, author_name, author_contact, orcid, etc. |
| Type | string |

## Changelog

### August 7, 2025 -- Version 1.0.0

- Initial version of the Cell Annotation and Taxonomy Data Schema.
- Includes definitions for cell labels, gene information, and dataset metadata.

### Pre-release Changelog

- Initial draft created.