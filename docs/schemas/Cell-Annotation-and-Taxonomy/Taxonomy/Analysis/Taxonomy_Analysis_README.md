# Analysis Metadata Schema

Document Status: _Under MOWG Review_

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

## General Requirements

This includes any fields included as the result of or required for specific analysis. Some examples include latent spaces (e.g., UMAP), cluster level gene summaries (e.g., cluster means, proportions), and variable genes. These may not need to match between schemas (or even be encoded into schemas).

## obsm

The obsm component contains all dimensionality reductions of the taxonomy (cell x dim). For all fields listed below, columns are of the format '[FIELD]_#' where # is 1, 2, 3, etc.

### UMAP

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>umap</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>2 (or more)-dimensional representation of cells in AIT. Must be of the form X_[...] for use with CELLxGENE. Only the first two dimensions are used for AIT and CELLxGENE, but 3 dimensions can be used for cirrocumulus.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### PCA

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>pca</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Additional terms for embedding multi-dimensional principal components and latent spaces</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### scVI

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>scvi</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Additional terms for embedding multi-dimensional principal components and latent spaces</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

## var

The var component contains gene level metadata.

### Gene

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>gene</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Same vector included in "data" to link between files.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Highly Variable Genes

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>highly_variable_genes</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Logical vector (T/F) indicating which genes are highly variable. Used for correlation-based mapping in scrattch.mapping.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Marker Genes

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>marker_genes_[...]</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Potentially additional sets of logical vectors for marker genes, as defined above.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

## uns

The uns component contains taxonomy associated files useful for reproducing analysis or mapping against the taxonomy.

### Dendrogram
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dendrogram</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>See above. This may fit better here.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### QC Markers

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>qc_markers</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Marker gene expression in on-target and off-target cell populations, useful for patchseq analysis. Also includes information about KL divergence calculations and associated QC calls. Defined by buildPatchseqTaxonomy.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Filter

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>filter</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Indicator of which cells to use for a given child taxonomy (subset), as defined above.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Mode

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>mode</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Taxonomy mode that determines which filter to use (e.g., that indicates which child taxonomy to map against). Several of the other analysis components of the uns have things saved with mode as the name in the h5ad file. See scrattch.mapping documentation. Mode is the Taxonomy short name in taxonomy Google Sheet for a child taxonomy with the Parent taxonomy listed as the taxonomyName.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Clusters Use

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>clustersUse</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A vector of cluster names to use for taxonomy. We should be able to remove this.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Cluster Info

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>clusterInfo</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A data.frame of cluster information. We should be able to remove this.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Marker Gene Metadata
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>marker_gene_metadata</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Metadata about any new marker gene lists added, if any. See above.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Development Date

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>development_date</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Date of taxonomy development. Required for Google Sheet. Potentially not needed if we want to infer from taxonomy_id.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Public

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>public</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Logical flag indicating whether taxonomy should be public or private. Required for Google Sheet. Potentially not needed if we want to infer from PURL/GitHub somehow.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Annotation Sheet

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>annotation_sheet</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Link to annotation sheet (ideally a TDT GitHub repo link for communal annotation). An optional slot in the Google sheet. I'm not sure if this is listed above somewhere.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Purpose

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>purpose</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Controlled vocabulary (currently "General" and/or "Patch-seq"). Required for Google Sheet at the moment.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

## Appendix

## Changelog