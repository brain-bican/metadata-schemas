# Analysis Metadata Schema

Document Status: _Approved BICAN Standard_

Version: 1.0

Owner: @UCDNJJ, @jeremymiller

Reviewers: @patrick-lloyd-ray, @carolth, @djarecka, @memartone

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 10-03-2025

## Overview

The BICAN Analysis Metadata schema specifies the metadata relating to analysis that can be taken from a variety of sources in BICAN. These metadata reflect the metadata needed to accurately track analysis metadata in BICAN. As such, it is a collaborative schema that reflects the joint efforts of members of BICAN.

This document has the following sections:

- [Analysis Metadata Schema](#analysis-metadata-schema)
  - [Overview](#overview)
  - [General Requirements](#general-requirements)
  - [obsm](#obsm)
    - [UMAP](#umap)
    - [PCA](#pca)
    - [scVI](#scvi)
  - [var](#var)
    - [Gene](#gene)
    - [Highly Variable Genes](#highly-variable-genes)
    - [Marker Genes](#marker-genes)
  - [uns](#uns)
    - [Dendrogram](#dendrogram)
    - [QC Markers](#qc-markers)
    - [Filter](#filter)
    - [Mode](#mode)
    - [Clusters Use](#clusters-use)
    - [Cluster Info](#cluster-info)
    - [Marker Gene Metadata](#marker-gene-metadata)
    - [Development Date](#development-date)
    - [Public](#public)
    - [Annotation Sheet](#annotation-sheet)
    - [Purpose](#purpose)
  - [Appendix](#appendix)
  - [Changelog](#changelog)
    - [August 7, 2025 -- Version 1.0.0](#august-7-2025----version-100)
  - [Pre-release Changelog](#pre-release-changelog)

## General Requirements

This includes any fields included as the result of or required for specific analysis. Some examples include latent spaces (e.g., UMAP), cluster level gene summaries (e.g., cluster means, proportions), and variable genes. These may not need to match between schemas (or even be encoded into schemas).

## obsm

The obsm component contains all dimensionality reductions of the taxonomy (cell x dim). For all fields listed below, columns are of the format '[FIELD]_#' where # is 1, 2, 3, etc.

### UMAP

| BICAN Field Name | umap |
|------------------|------------|
| BICAN UUID | 15e38e64-76d8-4150-af4e-ea76f5abfd6f |
| Aliases |  |
| Definition | A 2 (or more)-dimensional representation of cells in AIT. Must be of the form X_[...] for use with CELLxGENE. Only the first two dimensions are used for AIT and CELLxGENE, but 3 dimensions can be used for cirrocumulus. |
| Data Type | string |

### PCA

| BICAN Field Name | pca |
|------------------|------------|
| BICAN UUID | ef83b392-763b-4ae4-b77d-01759bc514d4 |
| Aliases |  |
| Definition | Additional terms for embedding multi-dimensional principal components and latent spaces. |
| Data Type | string |

### scVI

| BICAN Field Name | scvi |
|------------------|------------|
| BICAN UUID | 7accffad-bd7d-4f13-bedc-557e1b813481 |
| Aliases |  |
| Definition | Additional terms for embedding multi-dimensional principal components and latent spaces. |
| Data Type | string |

## var

The var component contains gene level metadata.

### Gene

| BICAN Field Name | gene |
|------------------|------------|
| BICAN UUID | 39a71ba6-895b-4e81-8f00-cb7505fc3ae6 |
| Aliases | gene_symbol |
| Definition | A vector of gene symbols. This is broadly useful in the community for defining genes but occasionally problematic; called `gene_symbol` in BKP. CELLxGENE uses a very specific version of ensembl_id for the INDEX. |
| Data Type | string |

### Highly Variable Genes

| BICAN Field Name | highly_variable_genes |
|------------------|----------------------|
| BICAN UUID | 9d00952f-284b-4575-9a94-2e0572cb4abc |
| Aliases |  |
| Definition | A logical vector (T/F) indicating which genes are highly variable. Used for correlation-based mapping in scrattch.mapping. |
| Data Type | string |

### Marker Genes

| BICAN Field Name | marker_genes |
|------------------|----------------|
| BICAN UUID | deddeb0d-0df2-4e53-bf69-21be2c305cd0 |
| Aliases |  |
| Definition | A set of logical vectors (T/F) indicating which genes are markers used to build dendrogram, or for other purposes. The [...] part of the name links to additional metadata in the uns. This needs to be UPDATED in AIT to allow multiple marker gene sets; markers currently stored differently in CAP. |
| Data Type | string |

## uns

The uns component contains taxonomy associated files useful for reproducing analysis or mapping against the taxonomy.

### Dendrogram

| BICAN Field Name | dendrogram |
|------------------|------------|
| BICAN UUID | 27bdd1f9-aebe-4868-ba22-91710fc371fe |
| Aliases | dend |
| Definition | A JSON formatted dendrogram used for tree mapping. Created by scrattch.taxonomy if not provided. Sometimes used for taxonomy annotation. |
| Data Type | string |

### QC Markers

| BICAN Field Name | QC_markers |
|------------------|------------|
| BICAN UUID | 6d10fcce-7895-4a33-b004-370db3a6698f |
| Aliases |  |
| Definition | The marker gene expression in on-target and off-target cell populations, useful for patchseq analysis. Also includes information about KL divergence calculations and associated QC calls and is defined by `buildPatchseqTaxonomy`. |
| Data Type | string |

### Filter

| BICAN Field Name | filter |
|------------------|------------|
| BICAN UUID | 2b5c18ef-5436-44dc-ab60-13965f052efb |
| Aliases |  |
| Definition | The indicator of which cells to use for a given child taxonomy (subset). |
| Data Type | string |

### Mode

| BICAN Field Name | mode |
|------------------|------------|
| BICAN UUID | c6cdf84a-6128-4c92-92aa-e33739ae1715 |
| Aliases |  |
| Definition | A taxonomy mode determines which filter to use (e.g., that indicates which child taxonomy to map against). Several of the other analysis components of the uns have things saved with mode as the name in the h5ad file. See also the scrattch.mapping documentation. Mode is the Taxonomy short name in taxonomy Google Sheet for a child taxonomy with the Parent taxonomy listed as the `taxonomyName`. |
| Data Type | string |

### Clusters Use

| BICAN Field Name | clustersUse |
|------------------|------------|
| BICAN UUID | 4375b86a-eefe-4e41-9ba9-3aacd224572e |
| Aliases |  |
| Definition | A vector of cluster names to use for taxonomy. |
| Data Type | string |

### Cluster Info

| BICAN Field Name | clusterInfo |
|------------------|------------|
| BICAN UUID | 6e49e5f4-05f7-42a9-b5eb-400f51419065 |
| Aliases |  |
| Definition | A data.frame of cluster information. |
| Data Type | string |

### Marker Gene Metadata

| BICAN Field Name | marker_gene_metadata |
|------------------|---------------------|
| BICAN UUID | b70f1ded-2bd8-426d-94de-bd6e28ae7989 |
| Aliases |  |
| Definition | Metadata about any new marker gene lists added, if any. |
| Data Type | string |

### Development Date

| BICAN Field Name | development_date |
|------------------|-----------------|
| BICAN UUID | 08e5466c-afce-481c-b6b4-a260150f88b7 |
| Aliases |  |
| Definition | Date of taxonomy development. Required for Google Sheet. |
| Data Type | string |

### Public

| BICAN Field Name | public |
|------------------|------------|
| BICAN UUID | c0c82901-3045-419b-9826-d973c3e8a801 |
| Aliases |  |
| Definition | A logical flag indicating whether taxonomy should be public or private. Required for Google Sheet. |
| Data Type | string |

### Annotation Sheet

| BICAN Field Name | annotation_sheet |
|------------------|-----------------|
| BICAN UUID | 17295ee7-a1b5-4174-ba1f-86adfa5273f7 |
| Aliases |  |
| Definition | A link to annotation sheet. An optional slot in the Google sheet. |
| Data Type | string |

### Purpose

| BICAN Field Name | purpose |
|------------------|---------|
| BICAN UUID | c26bec4c-0d5c-456f-9dc7-8f405551a030 |
| Aliases |  |
| Definition | The overarching purpose of the taxonomy. This is a controlled vocabulary (currently "General" and/or "Patch-seq"). Required for Google Sheet at the moment. |
| Data Type | string |

## Appendix

## Changelog

### August 7, 2025 -- Version 1.0.0

* **8-07-2025**: Finalized schema and added document status.
* **8-07-2025**: Approved as BICAN Standard.

## Pre-release Changelog

* **10-03-2025**: Initial version created.
* **10-04-2025**: Added additional fields and clarified definitions.
* **10-05-2025**: Added UUIDs and clarified definitions.
