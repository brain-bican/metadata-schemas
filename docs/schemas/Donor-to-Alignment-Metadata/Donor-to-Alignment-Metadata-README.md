# BICAN Library Metadata Schema

Document Status: _Under MOWG Review_

Version: 1.0

Owner: @lydiang

Reviewer: @patrick-lloyd-ray

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: DD-MM-YYYY

## Background

The Brain Research Through Advancing Innovative Neurotechnologies® (BRAIN) Initiative Cell Atlas Network (BICAN) aims to transform our understanding of brain cell types and the precise tools needed to access them, bringing us one step closer to unraveling the complex workings of the human brain.

Building on findings from the BRAIN Initiative Cell Census Network (BICCN), BICAN takes the next step in mapping brain cells and circuits across multiple species, with an emphasis on humans. The aim of BICAN is to generate a complete reference atlas of cell types in the human brain across the lifespan, which can be shared and used throughout the research community. In addition to developing a “parts list” detailing the vast array of neurons and non-neuronal cells in the human brain, the project also aims to map cell interactions that underlie a wide range of brain disorders.

To this end, BICAN aims to support the publication, sharing, and exploration of datasets generated in the course of the project. Creating a complete reference atlas from multiple datasets requires vast harmonization of metadata. In order to facilitate the harmonization of metadata, we require datasets include a small set of metadata available from data submitters.

This document describes a schema, a type of contract, that BICAN requires of all donor to alignment datasets to enable searching, filtering, and integration of datasets.

Note that the requirements in the schema are just the minimum required information. Datasets often have additional metadata, which is preserved in datasets submitted to the data archives.

## Overview

The BICAN Donor to Alignment Metadata schema describes [@lydiang fill in description here]

This document has the following sections:

* [General Requirements](#general-requirements)
* [Alignment](#alignment), which describe the data required for alignment processes.
* [Library Pool](#library-pool), which describe the data required for library pooling and pools.
* [Library Aliquot](#library-aliquot), which describe the data required for library aliquots and aliquoting processes.
* [Library](#library), which describe the data required...
* [Library Quantification](#library-quantification),
* [Library Construction](#library-construction), 
* [cDNA Amplification](#cDNA-amplification),
* [Cell Barcoding](#cell-barcoding),
* [Cell Dissociation](#cell-dissociation),
* [Tissue Dissectioning](#tissue-dissectioning),
* [Brain Sections, Segments, Extractions](#brain-sections-segments-extractions), 
* [Donor Metadata](#donor-metadata), 
* [Appendix](#appendix)

## General Requirements

**Organisms**. Data must be from a Metazoan organism and defined in the NCBI organismal classification.

**Redundant Metadata**. It is STRONGLY RECOMMENDED to avoid multiple metadata fields containing identical or similar information.

## Alignment

The data in Alignment is the metadata that essential for the alignment processes and entities.

The following table describes the Deliver Library Pool metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### Alignment output label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>alignment_output_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A string that serves as a label (name) for an alignment output.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1ca34909-2923-4219-848e-c7c250ec92cd</td>
    </tr>
</tbody></table>
<br>

### Alignment output created by process ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>alignment_output_created_by_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier of the process that created an alignment output.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>66caedfa-add6-4e8a-bb45-03cc9d90c149</td>
    </tr>
</tbody></table>
<br>

### Alignment output path

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>alignment_output_path</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A path to the alignment output for a specific alignment process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6015464d-6820-4baf-bc7a-a601c0507085</td>
    </tr>
</tbody></table>
<br>

### Alignment output barcoded cell sample label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>alignment_output_barcoded_cell_sample_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of the barcoded cell sample associated with an alignment output.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>754281ea-94c6-47d8-aab4-7443b6132004</td>
    </tr>
</tbody></table>
<br>

### Alignment output entity label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>alignment_output_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of the primary output entity (alignment output) of an alignment process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0d27affc-bb94-405e-81df-ffdbbc735e5d</td>
    </tr>
</tbody></table>
<br>

### Alignment process id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>alignment_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier used to refer to an alignment process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ae61d258-5f16-42a2-90cc-1279d87384a6</td>
    </tr>
</tbody></table>
<br>

### Alignment input entity label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>alignment_input_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of the primary input entity (library_aliquot) of an alignment process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ec7344d5-e6f9-46ed-8f0c-d6d0591b3656</td>
    </tr>
</tbody></table>
<br>

### Alignment input process id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>alignment_input_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier of the alignment input process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>671b4be4-a12b-4d34-856d-300fa28a3c69</td>
    </tr>
</tbody></table>
<br>

### Alignment input library pool sequencing process id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>alignment_input_library_pool_sequencing_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier of the library pool sequencing process for alignment input.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d8fa34ad-ab7c-418b-b0ce-a48ced53dff6</td>
    </tr>
</tbody></table>
<br>

### Alignment input barcoded cell sample id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>alignment_input_barcoded_cell_sample_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of the barcoded cell sample associated with the input library aliquot.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2f2b32db-0a86-499a-b4e4-08fbef3eab96</td>
    </tr>
</tbody></table>
<br>

## Library Pool

The data in the Library Pool is the metadata that essential for library pool generation and identification. 

The following table describes the Library Pool metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### Library pool sequencing output created by process id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_pool_sequencing_output_created_by_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier of the process that created a library pool sequencing output.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>61d2cdf1-3ea0-4695-a8b0-debe6bc79fd0</td>
    </tr>
</tbody></table>
<br>

### Library pool sequencing output fastq file path

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_pool_sequencing_output_fastq_file_path</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A path to a the fastq file for a specific library aliquot.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>54dfb80a-c86b-4c85-a05e-37a8eb136c41</td>
    </tr>
</tbody></table>
<br>

### Library pool sequencing output fastq file type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_pool_sequencing_output_fastq_file_type</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A Fastq file type that is an output from a library pool sequencing process. For example, R1, R2, R3, I1 and I2.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>69381fb6-39a2-41d9-b69a-743398016e15</td>
    </tr>
</tbody></table>
<br>

### Library pool sequencing output library aliquot label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_pool_sequencing_output_library_aliquot_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifer of a library aliquot associated with a fastq file.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7325a944-f9d6-4314-8e96-323496242736</td>
    </tr>
</tbody></table>
<br>

### library_pool_sequencing_input_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_pool_sequencing_input_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of the primary input of a library pool sequencing process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a6ee19dc-8e46-4993-9da9-81aeb0f63462</td>
    </tr>
</tbody></table>
<br>

### library_pool_sequencing_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_pool_sequencing_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier of a library pool sequencing process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f5f0d55e-006e-4b0e-a502-f4a7f5673e8c</td>
    </tr>
</tbody></table>
<br>

### library_pool_sequencing_vendor_read_count

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_pool_sequencing_vendor_read_count</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The number of pass filter reads assigned to an indexed library aliquot.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c3f96263-7f6b-4031-b715-f17ee1ccaf7a</td>
    </tr>
</tbody></table>
<br>

### library_pool_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_pool_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A string that refers to a library pool.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>29e0578b-6427-4c93-b29b-bde27fbadeec</td>
    </tr>
</tbody></table>
<br>

### library_pool_created_by_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_pool_created_by_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier for a process that created a library pool.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>871fe632-54f2-433c-8734-6045d5f9203f</td>
    </tr>
</tbody></table>
<br>

### library_pool_tube_avg_size_bp

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_pool_tube_avg_size_bp</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The average size of the pooled libraries given in terms of base pairs.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cf1b7c96-cdc1-4eed-8e76-ac44fbd151f7</td>
    </tr>
</tbody></table>
<br>

### library_pool_tube_contents_nm

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_pool_tube_contents_nm</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The concentration of the library pool in terms of nM (nMol/L).
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>32f2d02b-7300-4554-aa93-6de6e456eda7</td>
    </tr>
</tbody></table>
<br>

### library_pool_tube_internal_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_pool_tube_internal_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An internal label for a library pool tube container.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f1fdea98-7849-4def-a62f-a04cbbf98922</td>
    </tr>
</tbody></table>
<br>

### library_pool_construction_output_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_pool_construction_output_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of a primary output entity (library pool ) of a library pool construction process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0129624c-3cec-46e6-aa8c-49df75937c56</td>
    </tr>
</tbody></table>
<br>

### library_pool_construction_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_pool_construction_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier for a library pool construction process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b26ed5a7-ad3e-4457-9fdd-cf9895980a34</td>
    </tr>
</tbody></table>
<br>

### library_pool_construction_input_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_pool_construction_input_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of an input entity (library aliquot) of a library pool construction process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>296c8571-b1b2-4f06-a0f2-60bbdd050797</td>
    </tr>
</tbody></table>
<br>

### library_pool_construction_input_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_pool_construction_input_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier for a library pool construction process input.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d25187b3-bc2d-4f99-953f-10cae0b56122</td>
    </tr>
</tbody></table>
<br>

## Library Aliquot

The data in the Receive Sample is the metadata that essential for... 

The following table describes the Receive Sample metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:
### library_aliquot_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_aliquot_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>str</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of a library aliquot.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>34191bad-d167-4335-8224-ade897d3728e</td>
    </tr>
</tbody></table>
<br>

## Library

The data in Shared is the metadata that essential for... 

The following table describes the Shared metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:


## Library Quantification

## Library Construction

## cDNA Amplification

## Cell Barcoding

## Cell Dissociation

## Tissue Dissectioning

## Brain Sections, Segments, Extractions

## Donor Metadata
## Appendix
