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

### General Requirements

This includes cell-level metadata that is assigned at some point in the process between when a cell goes from the donor to a value in the data, and (in theory) can be ENTIRELY captured by values in Allen Institute, BICAN, or related standardized pipelines. It includes things like donor metadata, experimental protocols, dissection information, RNA QC metrics, and sequencing metadata. Ideally a schema for this will be defined through other BICAN groups, and can be adopted here.

### obs

The obs component contains cell level metadata from the experiment
cell_label: ID corresponding to each individual cell. (Will likely get renamed.) See above. 
[additional cell ID columns]: Optional additional IDs per cell. They are not used for taxonomy efforts. This could include things like IDs for RNA wells, barcodes, or other tracking IDs used for data processing.
feature_matrix_label: ID of the associated feature matrix where the data is stored (if not included in this file). Used in BKP when data is found elsewhere for connecting cell to data file.
dataset_label 🔥🔥🔥 : Link between each cell and each dataset in BKP. Need clarification on how this differs from feature_matrix_label; for CAS this is a taxonomy-level variable in uns called dataset_url (I think). We should align on this too.
[COLUMN_NAME]_color 🔥🔥🔥 : Color vectors for metadata/taxonomy values in format [COLUMN_NAME]_label. Required for molgen-shiny plots (and more generally any situation when we want consistent colors in visualizations). We need to align on a standard for how to store colors in the schema.
[COLUMN_NAME]_id 🔥🔥🔥 : Same as above, but in this case for the order of metadata values (e.g., the levels of a factor, or ascending order of a numeric). Likely should use “rank” or “order” rather than “id”, since these are not  identifiers.
The obs component also contains experiment metadata per cell
assay and assay_ontology_term_id 🔥🔥🔥 : In CELLxGENE these correspond to a human-readable modality along with the associated EFO ontology term. We often use the term modality in place of assay (e.g., 'Smart-seq2'corresponds to 'EFO:0008931', '10x 3' v3'corresponds to 'EFO:0009922'). This is called "library method" in BKP. Ideally we will agree on a term for this and it will be provided upstream from BICAN. Called Modality in taxonomy Google Sheet.
suspension_type 🔥🔥🔥 : Either "cell", "nucleus", or "na" in CELLxGENE. Called entity in the BKP. We should pick one to use.
[batch_condition_columns]: Zero or more vectors of metadata associated with batches. These are not required, but called out separately by CELLxGENE for analysis purposes.
[additional uncontrolled metadata]: Additional uncontrolled cell metadata. These are not required, but any additional columns are allowed by all h5ad formats.
The obs component also contains brain region metadata per cell, but this is still an active area of development
tissue and tissue_ontology_term_id 🔥🔥🔥 : Fields associated with the dissection corresponding to individual cells. Along with "tissue" field, these correspond to UBERON terms for the 'brain region' fields that we have (e.g., 'brain' = 'UBERON_0000955'). In process: we need to discuss how to integrate Allen reference brain atlases for mouse and human.  I think this corresponds to one or both of the terms: region_of_interest_label and anatomic_division_label in BKP.
brain_region 🔥🔥🔥 : Placehold for the actual brain region(s) sampled for a given cell. This may not be necessary. Called tissue_ontology_term_id in cellxgene; cell_set structures also defined below. Also associated are acronyms, labels, etc.; More generally need to arrive at a way of dealing with brain regions. Note that this slot in the Assigned metadata is meant to deal with cell-level assignments for brain region (e.g., dissection) and NOT cell set summarizations by brain region, which are included below.
The obs component also contains donor level metadata per cell
donor_id 🔥🔥🔥 : Identifier for the unique individual, ideal from the specimen portal (or other upstream source). This is called donor_label in the BKP. Should converge on a standard term. More than one identifier may be needed, but ideally for the analysis only a single one is retained and stored here.
species 🔥🔥🔥 : Species sampled. This is split into two fields in CAP/cellxgene/BICAN: organism (e.g., homo sapiens) and organism_ontology_term_id (e.g., 'NCBITaxon:10090'). For consistency, we should change species to organism and could write a function to automatically identify the ontology term (I think GeneOrthology already has one). Called Species name and Species ID in taxonomy Google Sheet.
age 🔥🔥🔥 : Currently a free text field for defining the age of the donor. In CELLxGENE this is recorded in development_stage_ontology_term_id and is HsapDv if human, MmusDv if mouse. I'm not sure what this means, but more generally, we should align with BICAN on how to deal with this value.
sex 🔥🔥🔥 : Placeholder for donor sex. Called sex_ontology_term_id (e.g., PATO:0000384/383 for male/female) in CELLxGENE and called "donor_sex" in BKP. We should align on a single term.
donor_genotype: One (or sometimes more) column related to the genotype of the animal (for transgenic mice, in particular). Not used for humans and most NHP.
self_reported_ethnicity_ontology_term_id: Controversial field that is required for CELLxGENE but otherwise not used. HANCESTRO term if human and 'na' if non-human.
disease and disease_ontology_term_id: A human-readable name for a disease and the associated MONDO ontology term (or PATO:0000461 for 'normal'). Used in CELLxGENE and ideally we can also adopt for SEA-AD and other use cases.

### uns

The uns component contains more general information and fields with formatting incompatible with the above components.
assigned_metadata_metadata 🔥🔥🔥 : TBD information about the assigned_metadata itself. This likely is not needed or should be renamed.
batch_condition: List of obs fields that define “batches”; Used by CELLxGENE if provided, but otherwise not needed.

## Changelog