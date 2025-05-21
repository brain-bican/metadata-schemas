# Assigned Metadata Schema

Document Status: _Under MOWG Review_

Version: 1.0

Owner: @UCDNJJ, @jeremymiller

Reviewers: @patrick-lloyd-ray, @carolth, @djarecka, @memartone

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 10-03-2025

## Overview

The BICAN Taxonomy Assigned Metadata schema specifies the metadata relating to taxonomy metadata that can be taken from a variety of sources in BICAN. These metadata reflect the metadata needed to accurately track taxonomy metadata in BICAN. As such, it is a collaborative schema that reflects the joint efforts of members of BICAN.

There are many metadata schemas that can be used in leiu of those specified in this document. 

* [Developing-Human-Metadata]
* [Developing-NHP-Metadata]
* [Developing-Tissue-Metadata]
* [Donor-Metadata]
* [Macaque-Donor-and-Tissue-Metadata]
* [Marmoset-Metadata]

to name a few. If you are not using one of these metadata schemas, feel free to enter your own metadata in the format specified by this document below.

This document has the following sections:

* [General Requirements](#general-requirements)
* [obs](#obs)
* [uns](#uns)
* [changelog](#changelog)

## General Requirements

This includes cell-level metadata that is assigned at some point in the process between when a cell goes from the donor to a value in the data, and (in theory) can be ENTIRELY captured by values in Allen Institute, BICAN, or related standardized pipelines. It includes things like donor metadata, experimental protocols, dissection information, RNA QC metrics, and sequencing metadata. Ideally a schema for this will be defined through other BICAN groups, and can be adopted here.

### obs

The obs component contains cell level metadata from the experiment.

#### Cell Label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_id</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>34ca0703-429f-4920-8a08-dd4c61b29444</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Identifier corresponding to each individual cell. Included in the data and in every other location to refer to the data (e.g., metadata and annotations). In AnnData files, the ID corresponding to each individual cell is stored in the obs index.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>striing</td>
    </tr>
</tbody></table>
<br>

#### Feature Matrix Label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>feature_matrix_label</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2c860046-83d5-47f9-98d5-29ce81446819</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>ID of the associated feature matrix where the data is stored (if not included in this file). Used in BKP when data is found elsewhere for connecting cell to data file.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Dataset Label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dataset_label</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>519ecc82-e397-4b1e-a846-d27d48610ff3</td>
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

#### Color Vectors

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>[COLUMN_NAME]_color</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0ab06f78-6df2-4555-8990-3eec36b2adbb</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Color vectors for metadata/taxonomy values in format [COLUMN_NAME]_label. Required for molgen-shiny plots (and more generally any situation when we want consistent colors in visualizations). We need to align on a standard for how to store colors in the schema.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### ID Vectors

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>[COLUMN_NAME]_id</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>701b32ca-4d95-47c5-8213-e7ab8c5373eb</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The order of metadata values (e.g., the levels of a factor, or ascending order of a numeric). Likely should use “rank” or “order” rather than “id”, since these are not identifiers.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Assay

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>assay</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a2ced0f5-4fdb-4ede-b524-2d975a70f21a</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Assay type (e.g., RNA-seq, ATAC-seq, etc.). This is a human-readable term that is not standardized. We should align on a standard term for this and it will be provided upstream from BICAN.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Assay Ontology Term ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>assay_ontology_term_id</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>12c1b9a3-57fa-44ea-8254-38eb3fa4ba71</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The ontology ID of the assay term.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Suspension Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>suspension_type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d6d84f18-90c8-4f4f-849a-fd4d0b665b95</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Type of suspension (e.g., cell, nucleus, etc.). This is a human-readable term that is not standardized. We should align on a standard term for this and it will be provided upstream from BICAN.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Batch Condition Columns

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>[batch_condition_columns]</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>5d64eed3-ae83-4b47-864d-cc4b3258e7ce</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Zero or more vectors of metadata associated with batches. These are not required, but called out separately by CELLxGENE for analysis purposes.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Additional Uncontrolled Metadata

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>[additional uncontrolled metadata]</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d417074d-5f7a-4bb8-8a7f-11e20fdcca97</td>
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

#### Brain Region

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain_region</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>71611b58-f98e-4a69-ad88-c0029a377cbe</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>region of interest</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Brain region(s) sampled. Called tissue_ontology_term_id in cellxgene; cell_set structures also defined below; called region_of_interest_label and anatomic_division_label in BKP. Also associated are acronymns, labels, etc.; More generally need to arrive at a way of dealing with brain regions. Note that this slot in the Assigned metadata is meant to deal with cell-level assignments for brain region (e.g., dissection) and NOT cell set summarizations by brain region, which are included below.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Tissue

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>33ccbc85-ae35-44d6-8bc6-c2fb91116cf7</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>tissue type</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Tissue sampled. This is a human-readable term that is not standardized. We should align on a standard term for this and it will be provided upstream from BICAN.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Tissue Ontology Term ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue_ontology_term_id</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7f797e30-8586-48d9-98e8-5d0ae4670a5a</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The ontology ID of the tissue term.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Donor ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>donor_id</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>local donor ID</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Identifier for the unique individual, ideal from the specimen portal (or other upstream source). This is called donor_label in the BKP. Should converge on a standard term. More than one identifier may be needed, but ideally for the analysis only a single one is retained and stored here.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Species

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>species</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d11fb2ce-bfdb-4735-9b17-b6ba606520b1</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Species sampled. This is split into two fields in CAP/cellxgene/BICAN: organism (e.g., homo sapiens) and  organism_ontology_term_id (e.g., 'NCBITaxon:10090'). For consistency, we should change species to organism and could write a function to automatically identify the ontology term (I think GeneOrthology already has one). Called Species name and Species ID in taxonomy Google Sheet.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Age

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>age</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>14eb923a-161d-45e2-889d-81fea7b632b6</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>age at death</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Currently a free text field for defining the age of the donor. In CELLxGENE this is recorded in development_stage_ontology_term_id and is HsapDv if human, MmusDv if mouse. I'm not sure what this means, but more generally, we should align with BICAN on how to deal with this value.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

#### Sex

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>sex</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c819b9d5-2fde-40b2-bf0d-e07b56f96ac9</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>sex at birth</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Placeholder for donor sex. Called sex_ontology_term_id (e.g., PATO:0000384/383 for male/female) in CELLxGENE and called "donor_sex" in BKP. We should align on a single term.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Donor Genotype

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>donor_genotype</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f6e7f720-924f-4098-822d-b79546a33583</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>One (or sometimes more) column related to the genotype of the animal (for transgenic mice, in particular). Not used for humans and most NHP.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Self-reported Ethnicity Ontology Term ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>self_reported_ethnicity_ontology_term_id</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>918370df-49f6-4361-9c52-f46b16412980</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>ethnicity</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Controversial field that is required for CELLxGENE but otherwise not used. HANCESTRO term if human and 'na' if non-human.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Disease

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>disease</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>42695d98-c3b8-447f-9358-364f502a7bda</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>condition type</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A human-readable name for a disease and the associated MONDO ontology term (or PATO:0000461 for 'normal'). Used in CELLxGENE and ideally we can also adopt for SEA-AD and other use cases.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Disease Ontology Term ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>disease_ontology_term_id</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>039354be-2ed5-40e1-a513-02589322d8b7</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The ontology ID of the disease term.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### uns

The uns component contains more general information and fields with formatting incompatible with the above components.

#### Assigned Metadata Metadata

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>assigned_metadata_metadata</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e0cbb726-f108-4514-8243-0799327cb104</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>TBD information about the assigned_metadata itself. This likely is not needed or should be renamed.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Batch Condition

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>batch_condition</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f4abc03e-7f6f-45cb-8a2e-d59a5846f368</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>List of obs fields that define “batches”; Used by CELLxGENE if provided, but otherwise not needed.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

## Changelog