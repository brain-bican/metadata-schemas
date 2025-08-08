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
| BICAN UUID | 45ee1d3a-abb6-4dc5-a1e8-1e16c82c2496 |
| Aliases |  |
| Definition | A 2 (or more)-dimensional representation of cells in AIT. Must be of the form X_[...] for use with CELLxGENE. Only the first two dimensions are used for AIT and CELLxGENE, but 3 dimensions can be used for cirrocumulus. |
| Data Type | string |

### PCA

| BICAN Field Name | pca |
|------------------|------------|
| BICAN UUID | 87697783-97ce-4c43-a5d8-f59553e59aff |
| Aliases |  |
| Definition | Additional terms for embedding multi-dimensional principal components and latent spaces. |
| Data Type | string |

### scVI

| BICAN Field Name | scvi |
|------------------|------------|
| BICAN UUID | 2ca30bc8-776f-4e74-95f2-923c3d5d6002 |
| Aliases |  |
| Definition | Additional terms for embedding multi-dimensional principal components and latent spaces. |
| Data Type | string |

## var

The var component contains gene level metadata.

### Gene

| BICAN Field Name | gene |
|------------------|------------|
| BICAN UUID | 5348b721-8bdf-4f0d-8bf4-68810f2f4da4 |
| Aliases | gene_symbol |
| Definition | A vector of gene symbols. This is broadly useful in the community for defining genes but occasionally problematic; called `gene_symbol` in BKP. CELLxGENE uses a very specific version of ensembl_id for the INDEX. |
| Data Type | string |

### Highly Variable Genes

| BICAN Field Name | highly_variable_genes |
|------------------|----------------------|
| BICAN UUID | c058ee9b-2ae8-44b1-abae-57f736309726 |
| Aliases |  |
| Definition | A logical vector (T/F) indicating which genes are highly variable. Used for correlation-based mapping in scrattch.mapping. |
| Data Type | string |

### Marker Genes

| BICAN Field Name | marker_genes |
|------------------|----------------|
| BICAN UUID | c813e546-e4c2-4215-8225-1ce734a7f534 |
| Aliases |  |
| Definition | A set of logical vectors (T/F) indicating which genes are markers used to build dendrogram, or for other purposes. The [...] part of the name links to additional metadata in the uns. This needs to be UPDATED in AIT to allow multiple marker gene sets; markers currently stored differently in CAP. |
| Data Type | string |

## uns

The uns component contains taxonomy associated files useful for reproducing analysis or mapping against the taxonomy.

### Dendrogram

| BICAN Field Name | dendrogram |
|------------------|------------|
| BICAN UUID | 7eee350d-1bd8-4d5d-84f0-85ad1213f703 |
| Aliases | dend |
| Definition | A JSON formatted dendrogram used for tree mapping. Created by scrattch.taxonomy if not provided. Sometimes used for taxonomy annotation. |
| Data Type | string |

### QC Markers

| BICAN Field Name | QC_markers |
|------------------|------------|
| BICAN UUID | 46d9459e-c936-4e7f-8703-6ab7097adec9 |
| Aliases |  |
| Definition | The marker gene expression in on-target and off-target cell populations, useful for patchseq analysis. Also includes information about KL divergence calculations and associated QC calls and is defined by `buildPatchseqTaxonomy`. |
| Data Type | string |

### Filter

| BICAN Field Name | filter |
|------------------|------------|
| BICAN UUID | ac4bdbee-c31f-46f9-afc9-6021e7feccbe |
| Aliases |  |
| Definition | The indicator of which cells to use for a given child taxonomy (subset). |
| Data Type | string |

### Mode

| BICAN Field Name | mode |
|------------------|------------|
| BICAN UUID | 7c340d6f-909b-4e39-b4f1-83ec8fd8ff3d |
| Aliases |  |
| Definition | A taxonomy mode determines which filter to use (e.g., that indicates which child taxonomy to map against). Several of the other analysis components of the uns have things saved with mode as the name in the h5ad file. See also the scrattch.mapping documentation. Mode is the Taxonomy short name in taxonomy Google Sheet for a child taxonomy with the Parent taxonomy listed as the `taxonomyName`. |
| Data Type | string |

### Clusters Use

| BICAN Field Name | clustersUse |
|------------------|------------|
| BICAN UUID | 68e6df92-aeab-4f5a-849c-db1bf7259b96 |
| Aliases |  |
| Definition | A vector of cluster names to use for taxonomy. |
| Data Type | string |

### Cluster Info

| BICAN Field Name | clusterInfo |
|------------------|------------|
| BICAN UUID | e0581d89-7550-40ee-9c5f-d985123718a6 |
| Aliases |  |
| Definition | A data.frame of cluster information. |
| Data Type | string |

### Marker Gene Metadata

| BICAN Field Name | marker_gene_metadata |
|------------------|---------------------|
| BICAN UUID | abcc6c5c-9b8b-407b-a20f-6f3301c9c200 |
| Aliases |  |
| Definition | Metadata about any new marker gene lists added, if any. |
| Data Type | string |

### Development Date

| BICAN Field Name | development_date |
|------------------|-----------------|
| BICAN UUID | 32a8fc5d-e429-4550-b020-2a9ff84cffae |
| Aliases |  |
| Definition | Date of taxonomy development. Required for Google Sheet. |
| Data Type | string |

### Public

| BICAN Field Name | public |
|------------------|------------|
| BICAN UUID | e69de720-559c-441b-bab0-d765a433d2b8 |
| Aliases |  |
| Definition | A logical flag indicating whether taxonomy should be public or private. Required for Google Sheet. |
| Data Type | string |

### Annotation Sheet

| BICAN Field Name | annotation_sheet |
|------------------|-----------------|
| BICAN UUID | daef45bb-ec6e-45da-827e-0e4c20b9b7c9 |
| Aliases |  |
| Definition | A link to annotation sheet. An optional slot in the Google sheet. |
| Data Type | string |

### Purpose

| BICAN Field Name | purpose |
|------------------|---------|
| BICAN UUID | efc20587-b6d2-475e-b682-3076a54921ab |
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
