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
* [cDNA Amplification](#cdna-amplification),
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

The following table describes the alignment metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

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

The data in the library pool is the metadata that essential for library pool generation and identification. 

The following table describes the library pool metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

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

The data in library aliquot is the metadata that essential for... 

The following table describes the library aliquot metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

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

### library_aliquot_created_by_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_aliquot_created_by_process_id</td>
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
        <td> An identifier for a process that created a library aliquot.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f7471219-1424-4bcc-ae5d-fbc50b2639dd</td>
    </tr>
</tbody></table>
<br>

### library_aliquot_input_quantity_fmol

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_aliquot_input_quantity_fmol</td>
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
        <td> The number of library molecules in an aliquoted portion of a library, as expressed in femtomoles.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>21fa7764-92d5-400c-b73e-5a8caece5a16</td>
    </tr>
</tbody></table>
<br>

### library_aliquot_library_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_aliquot_library_label</td>
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
        <td> A label of the library which a library aliquot is portioned from.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2d073310-911c-4e09-856a-a2ce6c015827</td>
    </tr>
</tbody></table>
<br>

### library_aliquoting_input_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_aliquoting_input_entity_label</td>
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
        <td> A label of the primary input of a library aliquoting process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a5accf6d-98b8-4d0d-af3f-dd967e1ce077</td>
    </tr>
</tbody></table>
<br>

### library_aliquoting_output_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_aliquoting_output_entity_label</td>
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
        <td> A label of the primary output of a library aliquoting process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6163e49b-a523-4adc-a45e-c93fbc6911dd</td>
    </tr>
</tbody></table>
<br>

### library_aliquoting_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_aliquoting_process_id</td>
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
        <td> An identifier for a library aliquoting process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e42425e2-8ceb-4c0a-93f4-6dffbfc57df3</td>
    </tr>
</tbody></table>
<br>

## Library

The data in library is the metadata that essential for... 

The following table describes the library metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:
### library_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_label</td>
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
        <td> A label that refers to a specific library.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f717e254-3630-4342-be7b-4d56376e7afe</td>
    </tr>
</tbody></table>
<br>

### library_created_by_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_created_by_process_id</td>
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
        <td> An identifier for a process that creates a library.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>8255bc41-528a-4559-83f2-c93528c4092e</td>
    </tr>
</tbody></table>
<br>

### library_ag_size_bp

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_ag_size_bp</td>
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
        <td> The average size of a library in terms of base pairs. This is used to calculate the molarity before pooling and sequencing.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f851eba9-56d1-4472-9d0c-d7f8bc33000a</td>
    </tr>
</tbody></table>
<br>

### library_r1_sequence

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_r1_sequence</td>
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
        <td> A sequence of i7 index required by sequencing instrument for demultiplexing (could be sense or antisense).
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ccb0553d-4146-45ee-b731-77563cb805cd</td>
    </tr>
</tbody></table>
<br>

### library_r2_sequence

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_r2_sequence</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A sequence of i5 index required by sequencing instrument for demultiplexing (could be sense or antisense).
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0ee7f272-01d9-453d-94a3-eefd1a86718e</td>
    </tr>
</tbody></table>
<br>

### library_creation_date

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_creation_date</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The date of a library creation.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>9c2f575d-1b64-451d-894f-656861afe07a</td>
    </tr>
</tbody></table>
<br>

### library_input_ng

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_input_ng</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The amount of cDNA going into library construction in nanograms.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3db770eb-078e-4b41-92b9-e2e551660753</td>
    </tr>
</tbody></table>
<br>

### library_prep_pass_fail

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_prep_pass_fail</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A result (pass or fail) of a test for library preparation based on library yield and size.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6817ede2-7ead-402d-9dbc-131aca627c6c</td>
    </tr>
</tbody></table>
<br>

### library_method

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_method</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A technique or method that is used to generate a library (specific to the alignment method required for the library). For example, 10xV3.1 (for RNASeq single assay), 10xMult-RSeq (for RNASeq multiome assay), and 10xMult-ATAC (for ATACSeq multiome assay).
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7b60d59e-fdd7-4b27-a2d4-cae9b69103a6</td>
    </tr>
</tbody></table>
<br>

## Library Quantification

The data in library quantification is the metadata that essential for... 

The following table describes the library quantification metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### library_quantification_ng

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_quantification_ng</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The amount of library generated in nanograms.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>318b2d3a-dae7-4c63-bfbb-93862b92f63e</td>
    </tr>
</tbody></table>
<br>

### library_quantification_nm

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_quantification_nm</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The concentration of library in terms of nM (nMol/L). The number of molecules is needed for accurate pooling of the libraries and for generating the number of target reads/cell in sequencing.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c4771566-82bf-4a0a-8a57-3d1b687e3851</td>
    </tr>
</tbody></table>
<br>

### library_quantification_fmol

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_quantification_fmol</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The amount of library generated in femtomoles
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4c09ada7-c116-48bc-8fb1-0dcf5c4b939a</td>
    </tr>
</tbody></table>
<br>

### library_r1_index

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_r1_index</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The library index used for Read-1 sequence. Indexes allow libraries to be pooled together for sequencing. Sequencing output (fastq) are demultiplexed by using the indexes for each library. The name will be associated with a oligo (string of bases). The required direction of the sequence (sense or antisense) of the index can differ depending on sequencing instruments.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>be6b81ef-c02d-4aaf-bd8d-5891ad919a9e</td>
    </tr>
</tbody></table>
<br>

### library_r2_index

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_r2_index</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The library index used for Read-2 sequence. Indexes allow libraries to be pooled together for sequencing. Sequencing output (fastq) are demultiplexed by using the indexes for each library. The name will be associated with a oligo (string of bases). The required direction of the sequence (sense or antisense) of the index can differ depending on sequencing instruments.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f82e3576-36fb-4399-8485-70cbf4911e8f</td>
    </tr>
</tbody></table>
<br>

## Library Construction

The data in library construction is the metadata that essential for... 

The following table describes the library construction metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### library_construction_input_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_construction_input_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of the primary input of a library construction process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e2d7623d-7313-4d6c-b58d-0795f91a1f45</td>
    </tr>
</tbody></table>
<br>

### library_construction_output_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_construction_output_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of the primary output of a library construction process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>af4dbe52-7ae5-493e-b044-05abbb9fa981</td>
    </tr>
</tbody></table>
<br>

### library_construction_process_date

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_construction_process_date</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The date when a library construction process occurred.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ab4ae9709-3fc4-45e0-a477-80099f102410</td>
    </tr>
</tbody></table>
<br>

### library_construction_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library_construction_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier for a library construction process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d7393dd2-2406-4984-badb-5b85547f4640</td>
    </tr>
</tbody></table>
<br>

## cDNA Amplification

The data in cDNA amplification is the metadata that essential for... 

The following table describes the cDNA amplification metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### amplified_cdna_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified_cdna_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label that refers to a portion of amplified cdna.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e2606a11-114e-472f-9e05-33f9b6fc3089</td>
    </tr>
</tbody></table>
<br>

### amplified_cdna_created_by_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified_cdna_created_by_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier of a process that created a portion of amplified cdna.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d695c983-07ff-450f-bbff-53a8638cd6d8</td>
    </tr>
</tbody></table>
<br>

### amplified_cdna_amplified_quantity_ng

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified_cdna_amplified_quantity_ng</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The amount of cDNA produced from an amplification process in nanograms.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0db79d05-8612-4896-b9d3-eb1558841449</td>
    </tr>
</tbody></table>
<br>

### amplified_cdna_method

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified_cdna_method</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A method used to generate cDNA (eg 10xV3.1, 10xMultiome-Rseq).
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>995369ca-3e05-4f7b-80a8-92427b90e8fa</td>
    </tr>
</tbody></table>
<br>

### amplified_cdna_pcr_cycles

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified_cdna_pcr_cycles</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The number of PCR cycles used during cDNA amplification for a cDNA.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3827634c-3f8f-4760-b358-86ce4b030238</td>
    </tr>
</tbody></table>
<br>

### amplified_cdna_percent_cdna_longer_than_400bp

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified_cdna_percent_cdna_longer_than_400bp</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A QC metric that describes quantifies mRNA degradation of cDNA. Higher % is higher quality starting material.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>8d150467-f69e-461c-b54c-bcfd22f581e5</td>
    </tr>
</tbody></table>
<br>

### amplified_cdna_rna_amplification_pass_fail

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified_cdna_rna_amplification_pass_fail</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A result (pass or fail) based on cDNA yield and size.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>bc62bdb2-7dc8-4404-bb84-ce0bbcae59e5</td>
    </tr>
</tbody></table>
<br>

### cdna_amplification_input_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cdna_amplification_input_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of the primary input of a cDNA amplification process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3e8c5ad4-6a15-478e-ad1c-e68a06b61181</td>
    </tr>
</tbody></table>
<br>

### cdna_amplification_input_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cdna_amplification_input_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of the primary input of a cDNA amplification process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ee5b7407-284a-44d1-813c-746fc934a398</td>
    </tr>
</tbody></table>
<br>

### cdna_amplification_process_date

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cdna_amplification_process_date</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The date when a cDNA amplification process occurred.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6cc333e7-9b98-497f-b7b1-eae904db2400</td>
    </tr>
</tbody></table>
<br>

### cdna_amplification_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cdna_amplification_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier a cDNA amplification process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a4d2b272-64e2-4adb-8886-38ee822488c9</td>
    </tr>
</tbody></table>
<br>

## Cell Barcoding

The data in cell barcoding is the metadata that essential for... 

The following table describes the cell barcoding metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### barcoded_cell_sample_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>barcoded_cell_sample_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label that refers to a barcoded cell sample.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4c0e6380-e53f-4173-a474-d41e836fefe3</td>
    </tr>
</tbody></table>
<br>

### barcoded_cell_sample_created_by_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>barcoded_cell_sample_created_by_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier of a process that created a barcoded cell sample.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1c78b561-d595-4f73-adb0-0de6a2c743e9</td>
    </tr>
</tbody></table>
<br>

### barcoded_cell_sample_port_well

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>barcoded_cell_sample_port_well</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A position of a load port of a 10x chip.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>aca38100-d245-4be4-9be3-ba27192779fe</td>
    </tr>
</tbody></table>
<br>

### barcoded_cell_sample_quantity_count

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>barcoded_cell_sample_quantity_count</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The number of barcoded cells expected after barcoding (usually a calculated fraction of the number of cells going into cell_barcoding).
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>dd6abb3c-b671-48eb-a924-13945484de71</td>
    </tr>
</tbody></table>
<br>

### cell_barcoding_input_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_barcoding_input_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of a primary input of a cell barcoding process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b5d251bd-0944-4c48-9508-74492185376e</td>
    </tr>
</tbody></table>
<br>

### cell_barcoding_output_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_barcoding_output_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of a primary output of a cell barcoding process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>12bc4988-4c21-4eac-93f5-e7c2b17a2b32</td>
    </tr>
</tbody></table>
<br>

### cell_barcoding_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_barcoding_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier for a cell barcoding process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a352af1b-1f33-4c8b-865f-7a6865ae5748</td>
    </tr>
</tbody></table>
<br>

## Cell Dissociation

The data in cell dissociation is the metadata that essential for... 

The following table describes the cell dissociation metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### dissociated_cell_sample_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dissociated_cell_sample_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label that refers to a dissociated cell sample.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>65e2c7da-9eb4-45b2-8ccb-d69ef9785ee2</td>
    </tr>
</tbody></table>
<br>

### dissociated_cell_sample_created_by_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dissociated_cell_sample_created_by_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier of a process that created a dissociated cell sample.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a155d7f4-0126-430c-a7fb-20b8dd35134d</td>
    </tr>
</tbody></table>
<br>

### dissociated_cell_sample_cell_prep_type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dissociated_cell_sample_cell_prep_type</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A type of cell preparation; for example, cells, or nuclei.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>baae4ac3-f959-4594-b943-3a82ec19bd34</td>
    </tr>
</tbody></table>
<br>

### dissociated_cell_sample_facs_population_plan

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dissociated_cell_sample_facs_population_plan</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A fluorescent marker label used to enrich cell dissociation for desired cell types.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a6f16756-4e52-4c37-b9dc-4ee5714f79b5</td>
    </tr>
</tbody></table>
<br>

### dissociated_cell_sample_number_of_cells_collected

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dissociated_cell_sample_number_of_cells_collected</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The total number of dissociated cells or nuclei going into a cell barcoding process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e2922a9e-e549-448a-8983-7e7f4f2338a9</td>
    </tr>
</tbody></table>
<br>

### cell_dissociation_input_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_dissociation_input_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of a primary input of a cell dissociation process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>5ed1a311-e060-4d00-9f24-9615503f9b7b</td>
    </tr>
</tbody></table>
<br>

### cell_dissociation_output_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_dissociation_output_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of a primary output of a cell dissociation process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cd94154e-8062-4156-a503-53bf09e32ba4</td>
    </tr>
</tbody></table>
<br>

### cell_dissociation_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_dissociation_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier of a cell dissociation process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7151ff55-0b40-4caf-b008-818a79e6e9f6</td>
    </tr>
</tbody></table>
<br>

## Tissue Dissectioning

The data in tissue dissectioning is the metadata that essential for... 

The following table describes the tissue dissectioning metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### tissue_sample_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue_sample_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label that refers to a tissue sample.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2e4ca2fc-2d77-4d19-af45-d0fb7bbc2269</td>
    </tr>
</tbody></table>
<br>

### tissue_sample_created_by_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue_sample_created_by_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier of a process that created a tissue sample.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4bb1e57a-3038-4e44-86cf-238eb1874c50</td>
    </tr>
</tbody></table>
<br>

### tissue_sample_roi_plan

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue_sample_roi_plan</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> 
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e7dda557-bda0-4392-ac7f-2651688549b3</td>
    </tr>
</tbody></table>
<br>

### tissue_dissectioning_input_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue_dissectioning_input_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of a primary input of a tissue dissectioning process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>98ad4077-9cb2-4e03-bad7-6358796aa78c</td>
    </tr>
</tbody></table>
<br>

### tissue_dissectioning_output_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue_dissectioning_output_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of a primary output of a tissue dissectioning process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d294e15a-6823-4ecd-aafe-5ce98c2adadf</td>
    </tr>
</tbody></table>
<br>

### tissue_dissectioning_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue_dissectioning_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier of a tissue dissectioning process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>fc5ddba7-d297-410c-942d-e46ecf657dcb</td>
    </tr>
</tbody></table>
<br>

### tissue_dissectioning_input_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue_dissectioning_input_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of a primary input entity of a tissue dissectioning process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d906ee29-f041-4642-8ba2-c1a54af213ea</td>
    </tr>
</tbody></table>
<br>

### tissue_dissectioning_input_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue_dissectioning_input_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier of an associated tissue dissectioning process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>9cfb3a49-ac05-4ce5-8ed9-c9d82d6ff761</td>
    </tr>
</tbody></table>
<br>

## Brain Sections, Segments, Extractions

The data in brain sections, segments, extractions is the metadata that essential for... 

The following table describes the brain specimens metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### brain_section_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain_section_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label that refers to a brain section.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e3bd9517-80e1-4158-981d-bb73baabceca</td>
    </tr>
</tbody></table>
<br>

### brain_section_created_by_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain_section_created_by_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier of a process that created a brain section.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a6e62b20-8c2d-4e40-a03b-41d943ec11cb</td>
    </tr>
</tbody></table>
<br>

### brain_section_ordinal

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain_section_ordinal</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A sequential number of a section used to track the relative positional order of sections from a segment.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d97be176-d39e-413c-8c1f-14e47f23da66</td>
    </tr>
</tbody></table>
<br>

### brain_segment_sectioning_input_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain_segment_sectioning_input_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of a primary input of a brain segment sectioning process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e41e854d-b68a-4c69-b23f-d1d39891dff0</td>
    </tr>
</tbody></table>
<br>

### brain_segment_sectioning_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain_segment_sectioning_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier of a brain segment sectioning process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3d426c44-47b2-4329-a06a-addd323bbf46</td>
    </tr>
</tbody></table>
<br>

### brain_segment_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain_segment_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label that refers to a brain segment.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>befeefc1-4be3-4974-a54e-929fd83cbf28</td>
    </tr>
</tbody></table>
<br>

### brain_segment_created_by_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain_segment_created_by_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier of a process that created a brain segment.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>03856361-d1b5-4983-a0fb-ae5a75d8ec6e</td>
    </tr>
</tbody></table>
<br>

### brain_segment_anatomical_division

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain_segment_anatomical_division</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The anatomical division that describes the brain segment; for example, whole brain, cerebrum, cerebellum, brainstem.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ec2565cc-1a11-4d1d-9c98-7eeeca27fd82</td>
    </tr>
</tbody></table>
<br>

### brain_segment_barcode

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain_segment_barcode</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A physical barcode label for a vessel holding a brain segment.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>516560ed-0715-475a-b717-6ccfa3ec2934</td>
    </tr>
</tbody></table>
<br>

### brain_extraction_input_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain_extraction_input_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of a primary input of a brain extraction process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>29442943-7d3d-4126-8817-9c10e34c8b83</td>
    </tr>
</tbody></table>
<br>

### brain_extraction_output_entity_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain_extraction_output_entity_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label of a primary output of a brain extraction process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>583a312a-43de-4c00-91ad-ec65f6fed2df</td>
    </tr>
</tbody></table>
<br>

### brain_extraction_process_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain_extraction_process_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> An identifier of a brain extraction process.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d1549808-92c8-4cf8-8e88-ad98a123d645</td>
    </tr>
</tbody></table>
<br>

## Donor Metadata

The data in donor metadata is the metadata that essential for... 

The following table describes the donor metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### donor_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>donor_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label that refers to a donor.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cb8ebdda-c8d2-4c29-b6cd-fcb5d0d6e720</td>
    </tr>
</tbody></table>
<br>

### donor_age_at_death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>donor_age_at_death</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The age of a donor at the time of death.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3df398ff-c5ee-4754-aeb8-2dd86027622e</td>
    </tr>
</tbody></table>
<br>

### donor_date_of_birth

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>donor_date_of_birth</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The date of birth of a donor.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4c376dcd-cf1f-4ccb-9d93-28ca73f53019</td>
    </tr>
</tbody></table>
<br>

### donor_date_of_death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>donor_date_of_death</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The date of death of a donor.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4cbe0de6-0d4d-4a7d-b38b-c483deaa0e3a</td>
    </tr>
</tbody></table>
<br>

### donor_full_genotype

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>donor_full_genotype</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The full genotype of a donor.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0a4c3a68-b41f-47e6-8128-257abc2ccaa5</td>
    </tr>
</tbody></table>
<br>

### donor_ncbitaxonomyid

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>donor_ncbitaxonomyid</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The NCBI taxonomy identifier of the organism type of this donor.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6837cb02-6bd7-4fb8-838c-9062ead96ba4</td>
    </tr>
</tbody></table>
<br>

### donor_sex

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>donor_sex</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The sex of a donor organism; for example, M or F.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>632d3d3f-f85b-4efc-a1ab-010fe417ae81</td>
    </tr>
</tbody></table>
<br>

### age_label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>age_label</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> A label that refers to an age.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0630a265-4a63-48f4-8853-66b929002306</td>
    </tr>
</tbody></table>
<br>

### age_reference_point

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>age_reference_point</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The reference point for an age interval; for example, birth or conception.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3bed1f94-9d82-4ed7-afdf-79d896b24dbb</td>
    </tr>
</tbody></table>
<br>

### age_unit

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>age_unit</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The unit used for representing the donor age from the reference point.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b5436e99-f0a7-4c30-825d-56b88ee2ac1d</td>
    </tr>
</tbody></table>
<br>

### age_value

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>age_value</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td> The value representing the donor age from the reference point.
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>57e24d3c-c9c7-4ef3-9809-a35802d563ec</td>
    </tr>
</tbody></table>
<br>

## Appendix
