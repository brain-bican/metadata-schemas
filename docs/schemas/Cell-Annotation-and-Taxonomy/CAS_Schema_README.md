# Cell Annotation Schema

Document Status: _Under MOWG Review_

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
    - [Title](#title)
    - [Description](#description)
    - [Cell Annotation Schema Version](#cell-annotation-schema-version)
    - [Cell Annotation Timestamp](#cell-annotation-timestamp)
    - [Cell Annotation Version](#cell-annotation-version)
    - [Cell Annotation URL](#cell-annotation-url)
    - [Author List](#author-list)
    - [Author Name](#author-name)
    - [Author Contact](#author-contact)
    - [ORCID](#orcid)
    - [Labelsets](#labelsets)
      - [Name](#name)
      - [Description](#description-1)
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
        - [Datestamp](#datestamp)
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
      - [Algorithm Name](#algorithm-name-1)
      - [Comment](#comment)
    - [Cells](#cells)
      - [Cell ID](#cell-id)
      - [Confidence](#confidence)
      - [Author Categories](#author-categories)
    - [Negative Marger Gene Evidence](#negative-marger-gene-evidence)
  - [Appendix](#appendix)
  - [Changelog](#changelog)

## General Requirements

This includes any cell-level or cluster-level metadata that can be calculated explicitly from the Data and Assigned Metadata without the need for human intervention. Some examples include # reads detected/cell, # UMI/cell, fraction of cells per cluster derived from each anatomic dissections, expressed neurotransmitter genes (quantitatively defined), average QUANTITATIVE_VALUE (e.g., doublet score) per cluster. Currently none of these are required for the schema, but they are sometimes used for annotation.

A general, open-standard schema for cell annotations which records connections, types, provenance and evidence.

This is designed not to tie-in to a single project (i.e. no tool-specific fields in core schema),and allows for extensions to support ad hoc user fields, new formal schema extensions, and project/tool specific metadata.

## Properties

### Matrix File ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>matrix_file_id</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>5d625688-96da-4c65-97b9-211cbcad4aea</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A resolvable ID for a cell by gene matrix file in the form namespace:accession, e.g. CellXGene_dataset:8e10f1c4-8e98-41e5-b65f-8cd89a887122.  Please see https://github.com/cellannotation/cell-annotation-schema/registry/registry.json for supported namespaces.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Title

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>title</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>5aab17df-0830-44d4-bcd8-f954695867d0</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The title of the dataset. This MUST be less than or equal to 200 characters. e.g. 'Human retina cell atlas - retinal ganglion cells'.</td>
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
      <td>1b5ff66c-0e00-4a29-8ccf-65dbf59d79da</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The description of the dataset. e.g. 'A total of 15 retinal ganglion cell clusters were identified from over 99K retinal ganglion cell nuclei in the current atlas. Utilizing previous characterized markers from macaque, 5 clusters can be annotated.'.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br> 

### Cell Annotation Schema Version

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cellannotation_schema_version</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>195cbdbf-d486-4d54-9c1d-83edf0a44ec5</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The schema version, the cell annotation open standard. Current version MUST follow 0.1.0This versioning MUST follow the format '[MAJOR].[MINOR].[PATCH]' as defined by Semantic Versioning 2.0.0, https://semver.org/.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Cell Annotation Timestamp

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cellannotation_timestamp</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>37da06ba-9c15-405f-b5d6-f8d2bf5fc3a3</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The timestamp of all cell annotations published (per dataset). This MUST be a string in the format '%yyyy-%mm-%dd %hh:%mm:%ss'.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string, format: date-time</td>
    </tr>
</tbody></table>
<br>

### Cell Annotation Version

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cellannotation_version</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>439f52e8-e2e6-406c-850c-434d448c8b6d</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The version for all cell annotations published (per dataset). This MUST be a string. The recommended versioning format is '[MAJOR].[MINOR].[PATCH]' as defined by Semantic Versioning 2.0.0, https://semver.org/.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Cell Annotation URL

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cellannotation_url</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e47029df-a5cf-49d0-b8de-76302a1e6fbb</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A persistent URL of all cell annotations published (per dataset). This MUST be a string of a valid URL.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string, format: url</td>
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
      <td>15e4be61-b1fb-49a5-9a81-7fed61138256</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>This field stores a list of users who are included in the project as collaborators, regardless of their specific role. An example list; '['John Smith', 'Cody Miller', 'Sarah Jones']'.</td>
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
      <td>0ea83cdb-cd06-4ef8-84c1-6aec29220759</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Primary author's name. This MUST be a string in the format '[FIRST NAME] [LAST NAME]'.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string, required</td>
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
      <td>fa084043-3c8e-47cb-959e-2f3daf2165ec</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Primary author's contact. This MUST be a valid email address of the author.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string, format: email</td>
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
      <td>2c96776b-b158-4e0c-ba67-ea7a63efb1e8</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Primary author's orcid. This MUST be a valid ORCID for the author.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Labelsets

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>labelsets</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e7fa0b7a1-6af7-4f79-8da0-29d7950ea736</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The unique name of the set of cell annotations. Each cell within the AnnData/Seurat file MUST be associated with a 'cell_label' value in order for this to be a valid 'cellannotation_setname'.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>array, required</td>
    </tr>
</tbody></table>
<br>

#### Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>name</td>
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
        <td>Name of annotation key.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string, required</td>
    </tr>
</tbody></table>
<br>

#### Description

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
        <td>Some text describing what types of cell annotation this annotation key is used to record.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>


#### Annotation Method
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>annotation_method</td>
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
        <td>The method used for creating the cell annotations. This MUST be one of the following strings: 'algorithmic', 'manual', or 'both' .</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Automated Annotation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>automated_annotation</td>
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
        <td>This field denotes the algorithm used to create the cell annotations. This MUST be a string of the algorithm's name.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>object</td>
    </tr>
</tbody></table>
<br>

##### Algorithm Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>algorithm_name</td>
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
        <td>The name of the algorithm used. It MUST be a string of the algorithm's name.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string, required</td>
    </tr>
</tbody></table>
<br>

##### Algorithm Version

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>algorithm_version</td>
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
        <td>The version of the algorithm used (if applicable). It MUST be a string of the algorithm's version, which is typically in the format '[MAJOR].[MINOR]', but other versioning systems are permitted (based on the algorithm's versioning).</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string, required</td>
    </tr>
</tbody></table>
<br>

##### Algorithm Repo URL

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>algorithm_repo_url</td>
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
        <td>This field denotes the URL of the version control repository associated with the algorithm used (if applicable). It MUST be a string of a valid URL.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string, required, format: url</td>
    </tr>
</tbody></table>
<br>

##### Reference Location

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>reference_location</td>
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
        <td>This field denotes a valid URL of the annotated dataset that was the source of annotated reference data. This MUST be a string of a valid URL. The concept of a 'reference' specifically refers to 'annotation transfer' algorithms, whereby a 'reference' dataset is used to transfer cell annotations to the 'query' dataset.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string, format: url</td>
    </tr>
</tbody></table>
<br>

#### Rank

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>rank</td>
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
        <td>A number indicating relative granularity with 0 being the most specific.  Use this where a single dataset has multiple keys that are used consistently to record annotations and different levels of granularity.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>integer</td>
    </tr>
</tbody></table>
<br>

### Annotations

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>annotations</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>46e6ec2f-6baf-4df9-bfbd-36463694be93</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A list of annotations.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>array, required</td>
    </tr>
</tbody></table>
<br>

#### Labelset

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>labelset</td>
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
        <td>The unique name of the set of cell annotations. Each cell within the AnnData/Seurat file MUST be associated with a 'cell_label' value in order for this to be a valid 'cellannotation_setname'.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string, required</td>
    </tr>
</tbody></table>
<br>

#### Cell Label

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
        <td>This denotes any free-text term which the author uses to annotate cells, i.e. the preferred cell label name used by the author. Abbreviations are exceptable in this field; refer to 'cell_fullname' for related details. Certain key words have been reserved:- 'doublets' is reserved for encoding cells defined as doublets based on some computational analysis- 'junk' is reserved for encoding cells that failed sequencing for some reason, e.g. few genes detected, high fraction of mitochondrial reads- 'unknown' is explicitly reserved for unknown or 'author does not know'- 'NA' is incomplete, i.e. no cell annotation was provided.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string, required</td>
    </tr>
</tbody></table>
<br>

#### Cell Fullname

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
        <td>This MUST be the full-length name for the biological entity listed in `cell_label` by the author. (If the value in `cell_label` is the full-length term, this field will contain the same value.) NOTE: any reserved word used in the field 'cell_label' MUST match the value of this field.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Cell Ontology Term ID

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
        <td>This MUST be a term from either the Cell Ontology (https://www.ebi.ac.uk/ols/ontologies/cl) or from some ontology that extends it by classifying cell types under terms from the Cell Ontologye.g. the Provisional Cell Ontology (https://www.ebi.ac.uk/ols/ontologies/pcl) or the Drosophila Anatomy Ontology (DAO) (https://www.ebi.ac.uk/ols4/ontologies/fbbt).</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Cell Ontology Term

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
        <td>This MUST be the human-readable name assigned to the value of 'cell_ontology_term_id'.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Cell IDs

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_ids</td>
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
        <td>List of cell barcode sequences/UUIDs used to uniquely identify the cells within the AnnData/Seurat matrix. Any and all cell barcode sequences/UUIDs MUST be included in the AnnData/Seurat matrix.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>list</td>
    </tr>
</tbody></table>
<br>  

#### Rationale

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
        <td>The free-text rationale which users provide as justification/evidence for their cell annotations. Researchers are encouraged to use this field to cite relevant publications in-line using standard academic citations of the form `(Zheng et al., 2020)` This human-readable free-text MUST be encoded as a single string.All references cited SHOULD be listed using DOIs under rationale_dois. There MUST be a 2000-character limit.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>


#### Rationale DOIs

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
        <td>A list of valid publication DOIs cited by the author to support or provide justification/evidence/context for 'cell_label'.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>list</td>
    </tr>
</tbody></table>
<br> 

#### Marker Gene Evidence

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
        <td>List of names of genes whose expression in the cells being annotated is explicitly used as evidence for this cell annotation. Each gene MUST be included in the matrix of the AnnData/Seurat file.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>list</td>
    </tr>
</tbody></table>
<br>  

#### Synonyms

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
        <td>This field denotes any free-text term of a biological entity which the author associates as synonymous with the biological entity listed in the field 'cell_label'.In the case whereby no synonyms exist, the authors MAY leave this as blank, which is encoded as 'NA'. However, this field is NOT OPTIONAL.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>list, required</td>
    </tr>
</tbody></table>
<br>

#### Reviews

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>reviews</td>
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
        <td>A list of reviews.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>list</td>
    </tr>
</tbody></table>
<br>

##### Datestamp

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>datestamp</td>
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
        <td>Date and time review was last edited.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string, format: date-time, required</td>
    </tr>
</tbody></table>
<br>

##### Reviewer

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>reviewer</td>
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
        <td>Review Author.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

##### Review

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>review</td>
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
        <td>Reviewer's verdict on the annotation.  Must be 'Agree' or 'Disagree'.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>enum, Must be one of: `["Agree", "Disagree"]`.</td>
    </tr>
</tbody></table>
<br>

##### Explanation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>explanation</td>
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
        <td>Free-text review of annotation. This is required if the verdict is disagree and should include reasons for disagreement.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Author Annotation Fields
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>author_annotation_fields</td>
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
        <td>A dictionary of author defined key value pairs annotating the cell set. The names and aims of these fields MUST not clash with official annotation fields.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>object</td>
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
        <td>An identifier that can be used to consistently refer to the set of cells being annotated, even if the cell_label changes.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string, required</td>
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
        <td>A list of accessions of cell sets that subsume this cell set. This can be used to compose hierarchies of annotated cell sets, built from a fixed set of clusters.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string, required</td>
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
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A list of annotations that were transferred from a reference dataset.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>list</td>
    </tr>
</tbody></table>
<br>

#### Transferred Cell Label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>transferred_cell_label</td>
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
        <td>The cell label that was transferred from the reference dataset.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string, required</td>
    </tr>
</tbody></table>
<br>

#### Source Taxonomy

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>source_taxonomy</td>
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
        <td>PURL of source taxonomy.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string; URL</td>
    </tr>
</tbody></table>
<br>

#### Source Node Accession

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>source_node_accession</td>
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
        <td>accession of node that label was transferred from.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Algorithm Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>algorithm_name</td>
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
        <td>The name of the algorithm used to transfer the annotation.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Comment

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>comment</td>
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
        <td>Free text comment on annotation transfer.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Cells

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cells</td>
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
        <td>By convention this is only used for annotation transfer labelsets.  It MUST not be combined with the 'cell_ids' field.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>list</td>
    </tr>
</tbody></table>
<br>

#### Cell ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_id</td>
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
        <td>Identifier for a single cell.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string, required</td>
    </tr>
</tbody></table>
<br>

#### Confidence

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>confidence</td>
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
        <td>Normalised confidence score.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>number</td>
    </tr>
</tbody></table>
<br>

#### Author Categories

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>author_categories</td>
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
        <td>A list of author defined categories.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>list</td>
    </tr>
</tbody></table>
<br>

### Negative Marger Gene Evidence

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>negative_marker_gene_evidence</td>
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
        <td>List of names of genes whose expression in the cells being annotated is explicitly used as evidence against this cell annotation. Each gene MUST be included in the matrix of the AnnData/Seurat file.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>list, required</td>
    </tr>
</tbody></table>
<br>

## Appendix

## Changelog

