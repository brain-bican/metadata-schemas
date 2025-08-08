# Assigned Metadata Schema

Document Status: _Approved BICAN Standard_

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

#### Cell ID

| BICAN Field Name | cell_id |
|------------------|---------|
| BICAN UUID | 34ca0703-429f-4920-8a08-dd4c61b29444 |
| Aliases |  |
| Definition | Identifier corresponding to each individual cell. Included in the data and in every other location to refer to the data (e.g., metadata and annotations). In AnnData files, the ID corresponding to each individual cell is stored in the obs index. |
| Data Type | string |

#### Feature Matrix Label

| BICAN Field Name   | feature_matrix_label |
|--------------------|---------------------|
| BICAN UUID         | 2c860046-83d5-47f9-98d5-29ce81446819 |
| Aliases            |                     |
| Definition         | ID of the associated feature matrix where the data is stored (if not included in this file). This is used in the Brain Knowledge Platform (BKP) when data is found elsewhere for connected cell to data file. |
| Data Type          | string              |

#### Dataset Label

| BICAN Field Name | dataset_label |
|------------------|---------------|
| BICAN UUID | 519ecc82-e397-4b1e-a846-d27d48610ff3 |
| Aliases |  |
| Definition | Link between each cell and each dataset in BKP. In CAS, this is a taxonomy-level variable in uns called `dataset_url`. |
| Data Type | string |

#### Color Vector

| BICAN Field Name | [COLUMN_NAME]_color |
|------------------|---------------------|
| BICAN UUID | 0ab06f78-6df2-4555-8990-3eec36b2adbb |
| Aliases |  |
| Definition | The color vector for metadata/taxonomy values in format [COLUMN_NAME]_label. This is ONLY used for molgen-shiny plots. Some metadata files come with these and some do not. This field is OPTIONAL. |
| Data Type | string |

#### [COLUMN_NAME]_id

| BICAN Field Name | [COLUMN_NAME]_id |
|------------------|------------|
| BICAN UUID | 701b32ca-4d95-47c5-8213-e7ab8c5373eb |
| Aliases |  |
| Definition | The order of metadata values (e.g., the levels of a factor, or ascending order of a numeric) for metadata/taxonomy values in format [COLUMN_NAME]_id. |
| Data Type | string |

#### Assay

| BICAN Field Name | assay |
|------------------|-------|
| BICAN UUID | a2ced0f5-4fdb-4ede-b524-2d975a70f21a |
| Aliases |  |
| Definition | The human-readable term that denotes the assay or technique used. In CELLxGENE these correspond to a human-readable modality along with the associated EFO ontology term. We often use the term modality in place of assay (e.g., 'Smart-seq2'corresponds to 'EFO:0008931', '10x 3' v3'corresponds to 'EFO:0009922'). This is called `library method` in BKP. This is called `Modality` in taxonomy Google Sheet. |
| Data Type | string |

#### Assay Ontology Term ID

|BICAN Field Name | assay_ontology_term_id |
|------------------|-------------------------|
| BICAN UUID | 12c1b9a3-57fa-44ea-8254-38eb3fa4ba71 |
| Aliases |  |
| Definition | The ontology ID of the assay term. |
| Data Type | string |

#### Suspension Type

|BICAN Field Name | suspension_type |
|------------------|-----------------|
| BICAN UUID | d6d84f18-90c8-4f4f-849a-fd4d0b665b95 |
| Aliases |  |
| Definition | The type of suspension. This is either "cell", "nucleus", or "na" in CELLxGENE; and called `entity` in the BKP. |
| Data Type | string |

#### Batch Condition Columns

|BICAN Field Name | [batch_condition_columns] |
|------------------|---------------------------|
| BICAN UUID | 5d64eed3-ae83-4b47-864d-cc4b3258e7ce |
| Aliases |  |
| Definition | This is a column for vectors of metadata associated with batches (zero or more). These are not required, but called out separately by cellxgene for analysis purposes. |
| Data Type | string |

#### Additional Uncontrolled Metadata

|BICAN Field Name | [additional uncontrolled metadata] |
|------------------|-----------------------------------|
| BICAN UUID | d417074d-5f7a-4bb8-8a7f-11e20fdcca97 |
| Aliases |  |
| Definition | Additional uncontrolled cell metadata. These are not required, but any additional columns are allowed by all h5ad formats. |
| Data Type | string |

#### Brain Region

|BICAN Field Name | brain_region |
|------------------|---------------|
| BICAN UUID | 71611b58-f98e-4a69-ad88-c0029a377cbe |
| Aliases | region of interest |
| Definition | The brain region(s) sampled. This is called `tissue_ontology_term_id` in cellxgene; cell_set structures also defined below; called `region_of_interest_label` and `anatomic_division_label` in BKP. Also associated are acronymns, labels, etc. Note that this slot in the Assigned metadata is meant to deal with cell-level assignments for brain region (e.g., dissection) and NOT cell set summarizations by brain region, which are included below. |
| Data Type | string |

#### Tissue

|BICAN Field Name | tissue |
|------------------|--------|
| BICAN UUID | 33ccbc85-ae35-44d6-8bc6-c2fb91116cf7 |
| Aliases | tissue type |
| Definition | The human-readable term for the tissue sampled. |
| Data Type | string |

#### Tissue Ontology Term ID

|BICAN Field Name | tissue_ontology_term_id |
|------------------|-------------------------|
| BICAN UUID | 7f797e30-8586-48d9-98e8-5d0ae4670a5a |
| Aliases |  |
| Definition | The ID for the tissue sampled. Along with "tissue" field, these correspond to Allen Atlas or UBERON terms for the 'brain region' fields that we have (e.g., 'brain' = 'UBERON_0000955').  |
| Data Type | string |

#### Donor ID

|BICAN Field Name | donor_id |
|------------------|-----------|
| BICAN UUID | f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf |
| Aliases | local donor ID |
| Definition | Identifier for the unique individual, ideally from the specimen portal (or other upstream source). This is called `donor_label` in the BKP. More than one identifier may be needed, but ideally for the analysis only a single one is retained and stored here.|
| Data Type | string |

#### Species

|BICAN Field Name | species |
|------------------|---------|
| BICAN UUID | d11fb2ce-bfdb-4735-9b17-b6ba606520b1 |
| Aliases |  |
| Definition | This is a term the for the species sampled. This is split into two fields in CAP/cellxgene/BICAN: `organism` (e.g., homo sapiens) and  `organism_ontology_term_id` (e.g., 'NCBITaxon:10090')..This is called `species name` and `species ID` in taxonomy Google Sheet. |
| Data Type | string |

#### Age

| BICAN Field Name | age |
|-------------------|------|
| BICAN UUID | 14eb923a-161d-45e2-889d-81fea7b632b6 |
| Aliases | age at death |
| Definition | A free text field for defining the age of the donor. In CELLxGENE this is recorded in `development_stage_ontology_term_id` and is `HsapDv` if human, `MmusDv` if mouse. |
| Data Type | text |

#### Sex

|BICAN Field Name | sex |
|------------------|-----|
| BICAN UUID | c819b9d5-2fde-40b2-bf0d-e07b56f96ac9 |
| Aliases | |
| Definition | PThis is a label that denotes the biological sex of the donor. This is called `sex_ontology_term_id` (e.g., PATO:0000384/383 for male/female) in CELLxGENE and called `donor_sex` in BKP. |
| Data Type | string |

#### Donor Genotype

|BICAN Field Name | donor_genotype |
|------------------|----------------|
| BICAN UUID | f6e7f720-924f-4098-822d-b79546a33583 |
| Aliases |  |
| Definition | This is the genotype of the donor. This is one (or sometimes more) column describing the genotype of the animal (for transgenic mice, in particular). Not used for humans and most NHP. |
| Data Type | string |

#### Self-reported Ethnicity Ontology Term ID

|BICAN Field Name | self_reported_ethnicity_ontology_term_id |
|------------------|-----------------------------------------|
| BICAN UUID | 918370df-49f6-4361-9c52-f46b16412980 |
| Aliases |  |
| Definition | This denotes the self-reported ethnicity of the donor. This field that is required for CELLxGENE but otherwise not used. The term should be from HANCESTRO if human and 'na' if non-human. |
| Data Type | string |

#### Disease

|BICAN Field Name | disease |
|------------------|---------|
| BICAN UUID | 42695d98-c3b8-447f-9358-364f502a7bda |
| Aliases | condition type |
| Definition | A human-readable name for a disease. |
| Data Type | string |

#### Disease Ontology Term ID

|BICAN Field Name | disease_ontology_term_id |
|------------------|---------------------------|
| BICAN UUID | 039354be-2ed5-40e1-a513-02589322d8b7 |
| Aliases |  |
| Definition | The ID of the disease term. Recommend the associated MONDO ontology term (or PATO:0000461 for 'normal'). Used in CELLxGENE. |
| Data Type | string |

### uns

The uns component contains more general information and fields with formatting incompatible with the above components.

#### Assigned Metadata Metadata

|BICAN Field Name | assigned_metadata_metadata |
|------------------|-----------------------------|
| BICAN UUID | e0cbb726-f108-4514-8243-0799327cb104 |
| Aliases |  |
| Definition | This is information about the assigned_metadata itself. |
| Data Type | string |

#### Batch Condition

|BICAN Field Name | batch_condition |
|------------------|-----------------|
| BICAN UUID | f4abc03e-7f6f-45cb-8a2e-d59a5846f368 |
| Aliases |  |
| Definition | This is the list of obs fields that define “batches”; Used by CELLxGENE if provided, but otherwise not needed. |
| Data Type | string |

## Changelog

### August 7, 2025 -- Version 1.0.0

* **8-07-2025**: Finalized schema and added document status.
* **8-07-2025**: Approved as BICAN Standard.

### Pre-release Changelog

* **10-03-2025**: Initial version created.
* **10-04-2025**: Added additional fields and clarified definitions.
* **10-05-2025**: Added UUIDs and clarified definitions.
