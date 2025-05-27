# Cell Annotation Schema

Document Status: _Under MOWG Review_

Version: 1.0

Owner: @UCDNJJ, @jeremymiller

Reviewers: @patrick-lloyd-ray, @carolth, @djarecka, @memartone

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 10-03-2025

## Overview

The BICAN Cell Annotation Metadata schema specifies the metadata relating to cell annotations that can be taken from a variety of sources in BICAN. These metadata reflect the metadata needed to accurately track cell annotations metadata in BICAN. As such, it is a collaborative schema that reflects the joint efforts of members of BICAN.

This document has the following sections:

- [Cell Annotation Schema](#cell-annotation-schema)
  - [Overview](#overview)
  - [General Requirements](#general-requirements)
  - [obs](#obs)
    - [Cell Label](#cell-label)
    - [Cluster ID](#cluster-id)
    - [Cluster Label](#cluster-label)
    - [Other Cluster Columns](#other-cluster-columns)
    - [Additional Uncontrolled Metadata](#additional-uncontrolled-metadata)
    - [Feature Matrix Label](#feature-matrix-label)
    - [Dataset Label](#dataset-label)
    - [\[COLUMN\_NAME\]\_color](#column_name_color)
    - [\[COLUMN\_NAME\]\_id](#column_name_id)
  - [var](#var)
    - [marker\_genes\_\[...\]](#marker_genes_)
  - [uns](#uns)
  - [uns fields associated with taxonomy metadata (e.g., different label sets)](#uns-fields-associated-with-taxonomy-metadata-eg-different-label-sets)
    - [Taxonomy Name](#taxonomy-name)
    - [Taxonomy ID](#taxonomy-id)
    - [Description](#description)
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
  - [uns fields associated with individual cell set annotations (e.g., different label sets)](#uns-fields-associated-with-individual-cell-set-annotations-eg-different-label-sets)
    - [labelsets](#labelsets)
    - [labelsets fields](#labelsets-fields)
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
    - [Canonical Marker Genes](#canonical-marker-genes)
    - [Synonyms](#synonyms)
    - [Category XXXX](#category-xxxx)
    - [Parent Cell Set Name](#parent-cell-set-name)
    - [Parent Cell Set Accession](#parent-cell-set-accession)
  - [uns fields associated with complex cell set relationships and metadata (e.g., dendrograms, child taxonomies, gradients, level relationships, annotation transfer)](#uns-fields-associated-with-complex-cell-set-relationships-and-metadata-eg-dendrograms-child-taxonomies-gradients-level-relationships-annotation-transfer)
    - [dend](#dend)
    - [Cell Set Relationships](#cell-set-relationships)
    - [Filter](#filter)
    - [Transferred Annotations](#transferred-annotations)
    - [Transferred Annotations Metadata](#transferred-annotations-metadata)
  - [Changelog](#changelog)
    - [2024-01-15](#2024-01-15)

## General Requirements

This includes any fields related to the annotation of clusters or groups of clusters (collectively called "cell sets"). This includes things like cluster levels, cluster relationships, canonical marker genes, links to existing ontologies (e.g., CL, UBERON) based on judgement calls, expert annotations, and dendrograms.

## obs

The obs component contains cell level metadata. 

The obs component also contains cell set metadata summarized at the cell level. The proposal is to store all of this in the uns in json format and create helper functions to duplicate information as obs columns as needed.  Currently there is a standard way of doing this for CAP, and we will implement a mechanism for this in scrattch.taxonomy as well.

### Cell Label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_label</td>
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
        <td>ID corresponding to each individual cell.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Cluster ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cluster_id</td>
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
        <td>Unique integer value corresponding to each cluster in the taxonomy, which also (ideally but not necessarily) encodes the order of clusters in visualizations. Once a taxonomy is minted, this cannot change. This is the CRITICAL column used for cluster annotations. It is the baseline for the majority of cell_annotation columns discussed below. Note that “cell_set_accession_ids” and “cluster hash values” can be assigned after these “cluster_ids” are agreed upon. It's also worth noting that this is a prerequisite for annotations, so maybe it better fits in a different category (analysis?).</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>integer</td>
    </tr>
</tbody></table>
<br>

### Cluster Label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cluster_label</td>
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
        <td>Human-readable cluster name used primarily by scientists and other folks. This is the same as “cell_label” for cell sets when the “label_set” is cluster. It's also used for cirrocumulus.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Other Cluster Columns

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>[other cluster columns?]</td>
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
        <td>There is also an additional cluster_alias column used in mouse whole brain data and for BKP that I'm not sure how to wrap in. Are there other columns?</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Additional Uncontrolled Metadata

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>[additional uncontrolled metadata]</td>
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
        <td>Additional uncontrolled cell metadata. These are not required, but any additional columns are allowed by all h5ad formats.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Feature Matrix Label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>feature_matrix_label</td>
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
        <td>ID of the associated feature matrix where the data is stored (if not included in this file). Used in BKP when data is found elsewhere for connected cell to data file.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Dataset Label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dataset_label</td>
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
        <td>Link between each cell and each dataset in BKP. Need clarification on how this differs from feature_matrix_label; for CAS this is a taxonomy-level variable in uns called dataset_url.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### [COLUMN_NAME]_color

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>[COLUMN_NAME]_color</td>
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
        <td>Color vector for metadata/taxonomy values in format [COLUMN_NAME]_label. This is ONLY used for molgen-shiny plots, but because of this, some metadata files come with these and some don't and that could cause challenges. Should revisit how to store colors and how to deal with metadata in both formats. Should also agree on a standard for which way is preferred.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### [COLUMN_NAME]_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>[COLUMN_NAME]_id</td>
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
        <td>Same as above, but in this case for the order of metadata values (e.g., the levels of a factor, or ascending order of a numeric)</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

## var

The var component contains gene level metadata. gene: Same vector included in "data" to link between files.

### marker_genes_[...]

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>marker_genes_[…]</td>
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
        <td>A set of logical vectors (T/F) indicating which genes are markers used to build dendrogram, or for other purposes. The [...] part of the name links to additional metadata in the uns. This needs to be UPDATED in AIT to allow multiple marker gene sets; markers currently stored differently in CAP.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

## uns

The uns component contains more general information and fields with formatting incompatible with the above components. Much of the information about annotations is stored in this field, so we divide it up below.

Proposal: store everything that goes in the TDT taxonomy annotations in a single field called “annotations” and match the TDT structure.  Then write conversions between uns and obs for most h5ad use cases.

## uns fields associated with taxonomy metadata (e.g., different label sets)

### Taxonomy Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>taxonomy_name</td>
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
        <td>Taxonomy name (e.g., "AIT30"); called title in cellxgene, not sure about other schema. Called Taxonomy short name in taxonomy Google Sheet.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>


### Taxonomy ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>taxonomy_id</td>
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
        <td>Taxonomy ID in CCN format (e.g., "CCN030420240"); TBD how this is generated, but MUST be globally unique. Also used as part of PURL (I think). Called Taxonomy ID in taxonomy Google Sheet.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Description

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>description</td>
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
        <td>Free text description of the taxonomy (or of the dataset on CAP). This is also something we are adding as a requirement for the BKP, and I think should be required for all taxonomies. Called Description in taxonomy Google Sheet.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Taxonomy Citation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>taxonomy_citation</td>
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
        <td>"|"-separated publication DOI's of the taxonomy (e.g., "doi:10.1038/s41586-018-0654-5"). Called Publication in taxonomy Google Sheet.</td>
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
        <td>Data frame of Marker genes x dims that includes metadata for marker gene sets in var above; NEW and required if marker_genes_[…] is provided. At minimum a name (matching above) and description are needed, but potentially other things (e.g., what is it for, with controlled vocabulary).</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>dataframe</td>
    </tr>
</tbody></table>
<br>

### Taxonomy Directory

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>taxonomyDir</td>
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
        <td>Location of the h5ad file; we might be able to remove this, since it is redundant with dataset_url and/or matrix_file_id. Called Taxonomy file location in taxonomy Google Sheet.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Dataset URL

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dataset_url</td>
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
        <td>PURL of taxonomy; Possibly a redundant field, but critical; also publication_url and cellannotation_url (unclear how different)</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Matrix File ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>matrix_file_id</td>
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
        <td>Like dataset_url; e.g. CellXGene_dataset:8e10f1c4-8e98-41e5-b65f-8cd89a887122; Note: needs to be extended to allow for more than one file and connected to feature_matrix_label in obs. We need this field!</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Author List

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>author_list</td>
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
        <td>List of all collaborators, comma separated [First] [Last]; Useful in general, even though currently only required by CAP. Called Taxonomy Users in taxonomy Google Sheet.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Author Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>author_name</td>
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
        <td>The primary author [First Name] [Last Name]; in CCN was called "taxonomy_author"; In CCN also separated by cell_set with "cell_set_alias_assignee"; Called Point person name in taxonomy Google Sheet.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Author Contact

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>author_contact</td>
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
        <td>Valid email address; Called Point person email in taxonomy Google Sheet.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### ORCID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>orcid</td>
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
        <td>Valid ORCID; Called Point person ORCID in taxonomy Google Sheet.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Annotation Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>annotation_source</td>
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
        <td>Additional metadata about annotation algorithm; Similar to taxonomy algorithm info stored for CCN.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

## uns fields associated with individual cell set annotations (e.g., different label sets)

### labelsets
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>labelsets</td>
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
        <td>CRITICAL extra component; Equivalent to Cluster annotation term set in BKP. This is saved as a data frame representation (or is a list of data frames needed?), with some information about each [cellannotation_set] set of columns (e.g., subclass, class, neurotransmitter, etc.). Specifically: "name", "description", and "rank" (0 most specific) and some information about provenance are needed for each labelset.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>dataframe</td>
    </tr>
</tbody></table>
<br>

### labelsets fields

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>labelsets fields</td>
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
        <td>This is where taxonomy levels are stored in AIT)CCN)CAS. The column name is a string (e.g., "subclass") and the values are cell_labels (e.g., "SST"). The equivalent in BKP are Cluster Annotation Term Sets and in CAP is label_sets. This also encapsulates the concept of cell_ids from CAP/CAS, since in the h5ad file each row corresponds to a cell and therefore you get the cell_label --> cell_ids mapping for free. This is stored as separate files in both BKP and TDT and so we should confirm appropriate translations and agree on terms for this. Finally, this concept is critical for scrattch.taxonomy and scrattch.mapping to work properly, but none of the [cellannotation_set]--XXXX fields below are needed for AIT (although keeping this is best practice!).</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>


*** NOTE: the fields below each relate to a specific labelset.  We need to flesh out a bit better how to structure this in a json in the uns, but for now I’m just showing them as individual columns

### Neurotransmitters
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>[neurotransmitters]</td>
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
        <td>Placeholder in case this isn’t included already in labelsets; if it is, we can remove this.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Cell Set Accession

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_set_accession</td>
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
        <td>ID corresponding to the cell_set; called the "Cluster Annotation Term" in BKP. Some work still needed on deciding what to name this (CCNXXXXX?, a hash code?, something else?) and HOW to name this (automatically? if so, but what authority).</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Cell Set Label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_set_label</td>
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
        <td>This can probably be dropped. For CCN this was used as a tag for each cluster or (for cell sets with >1 cluster) included a list of underlying cluster labels. It was important for proper databasing without a database.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Cell Fullname
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_fullname</td>
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
        <td>The longer name for a cell type (e.g., "Somatostatin interneuron 1" rather than "SST 1"). This was called the cell_set_preferred_alias in CCN.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Cell Ontology Exists

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_ontology_exists</td>
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
        <td>True/false call about whether a cell ontology term exists (This seems redundant to me with next two rows). I vote we remove it and derive as needed.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>boolean</td>
    </tr>
</tbody></table>
<br>

### Cell Ontology Term ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_ontology_term_id</td>
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
        <td>Highest resolution Cell Ontology term (ID); was called cell_set_ontology_tag in CCN.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Cell Ontology Term

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_ontology_term</td>
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
        <td>Highest resolution Cell Ontology term (name); was called cell_set_structure in CCN and was also largely mapping to the cell_set_aligned_alias. Note that we currently don't have a field in the schema for dealing with cross-species homologies (like the cell_set_aligned_alias) as far as I can tell.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Rationale

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>rationale</td>
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
        <td>Free text evidence for cell annotations.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Rationale DOIs

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>rationale_dois</td>
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
        <td>Comma-separated publication DOI's of rationale CCN: "cell_set_alias_citation". NOTE: We sometimes use comma-separated and sometimes "|"-separated (and BICAN uses something else: "/#/").</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Marker Gene Evidence

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>marker_gene_evidence</td>
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
        <td>Comma-separated marker genes used as evidence for cell type annotation (e.g., by NS-Forest). Note: This is reserved for ontology markers. See var above for how to store general marker genes.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Canonical Marker Genes

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>canonical_marker_genes</td>
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
        <td>Comma separated list of canonical marker genes. I don't understand how this differs from marker_gene_evidence. I vote we omit this.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Synonyms

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>synonyms</td>
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
        <td>Comma-separated aliases (e.g., "neuroglial cell, glial cell, neuroglia"); was called cell_set_additional_alias in CCN.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Category XXXX

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>category_XXXX</td>
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
        <td>I'm not entirely sure what these columns represent. They appear to be the same as cell_XXXX above for several fields (e.g., fullname, cell_ontology_term, etc.). Can we please omit or clarify?</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Parent Cell Set Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>parent_cell_set_name</td>
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
        <td>‘cell_label’ corresponding to the parent cell_set.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Parent Cell Set Accession

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>parent_cell_set_accession</td>
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
        <td>ID corresponding to the parent cell_set. I think this would correspond to the parent Cluster Annotation Term ID in knowlegebase?</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

## uns fields associated with complex cell set relationships and metadata (e.g., dendrograms, child taxonomies, gradients, level relationships, annotation transfer)

### dend

<table><tbody>
      <tr>
        <th>BICAN Field Name</th>
        <td>dend</td>
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
          <td>A json formatted dendrogram used for tree mapping. Created by scrattch.taxonomy if not provided. Sometimes used for taxonomy annotation, but we are moving away from it with larger taxonomies and so this may now make more sense in the "analysis" category.</td>
      </tr>
      <tr>
        <th>Data Type</th>
        <td>json</td>
      </tr>
</tbody></table>
<br>

### Cell Set Relationships

<table><tbody>
      <tr>
        <th>BICAN Field Name</th>
        <td>cell_set_relationships</td>
      </tr>
      <tr>
        <th>BICAN UUID</th>
        <td></td>
      </tr>
      <tr>
        <th>Aliases</th>
        <td>cell_set_relations</td>
      </tr>
      <tr>
        <th>Definition</th>
          <td>🔥🔥🔥 NEW proposed mechanism for dealing with sibling relationships for things like gradients, trajectories, constellation diagrams, etc.. This is stored as a data frame (table) of all relations with five columns: cells_set_accession1, cell_set_accession2, relation_label, value, direction. Could alternatively be stored as a JSON representation that unpacks into a dataframe.</td>
      </tr>
      <tr>
        <th>Data Type</th>
        <td>dataframe</td>
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
          <td>Indicator of which cells to use for a given child taxonomy (subset), saved as a list of vectors. Each entry in this list is named for the relevant "mode" and has TRUE/FALSE calls indicating whether a cell is filtered out (e.g., the "standard" taxonomy is all FALSE). This is critical for how child taxonomies are defined and implemented in scrattch.taxonomy but differs from how taxonomies are stored in all other schemas--some discussion may be needed.</td>
      </tr>
      <tr>
        <th>Data Type</th>
        <td>list of vectors</td>
      </tr>
</tbody></table>
<br>

### Transferred Annotations

<table><tbody>
      <tr>
        <th>BICAN Field Name</th>
        <td>transferred_annotations</td>
      </tr>
      <tr>
        <th>BICAN UUID</th>
        <td></td>
      </tr>
      <tr>
        <th>Aliases</th>
        <td>[transferred_annotations]</td>
      </tr>
      <tr>
        <th>Definition</th>
          <td>Column name is a string corresponding to the taxonomy of comparison; values are the transferred cell label from that taxonomy. I think there is still some work on the best way to code this, but it is important. This is also already encoded in TDT--how? It is linked to some information in the uns below. Potentially more columns needed for annotation-level metadata (e.g., source_node_accesssion, comments).</td>
        </tr>
        <tr>
        <th>Data Type</th>
        <td>dataframe</td>
        </tr>
</tbody></table>
<br>

### Transferred Annotations Metadata
<table><tbody>
      <tr>
        <th>BICAN Field Name</th>
        <td>transferred_annotations_metadata</td>
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
          <td>Data frame of info about each transferred annotation column: source_taxonomy, algorithm_name, comment; Still some work on the best way to code this, but it is important. Linked to data in var above. This is for taxonomy-level metadata. This is also already encoded in TDT--how?</td>
      </tr>
      <tr>
        <th>Data Type</th>
        <td>dataframe</td>
      </tr>
</tbody></table>
<br>

## Changelog
This section is for tracking changes to the schema and the BICAN field names. It is not part of the schema itself, but it is useful to keep track of changes.
### 2024-01-15
- Added BICAN field names for all fields in the schema.
- Added BICAN UUIDs for all fields in the schema.
- Added aliases for some fields in the schema.
- Added definitions for all fields in the schema.
- Added data types for all fields in the schema.
- Added links to the BICAN schema for each field.