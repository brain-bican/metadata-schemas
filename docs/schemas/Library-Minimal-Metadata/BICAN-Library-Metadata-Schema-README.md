# BICAN Library Metadata Schema

Contact: owner@email.org

Document Status: _Pending Approval_

Version: 0.0.1

## Background

The Brain Research Through Advancing Innovative Neurotechnologies® (BRAIN) Initiative Cell Atlas Network (BICAN) aims to transform our understanding of brain cell types and the precise tools needed to access them, bringing us one step closer to unraveling the complex workings of the human brain.

Building on findings from the BRAIN Initiative Cell Census Network (BICCN), BICAN takes the next step in mapping brain cells and circuits across multiple species, with an emphasis on humans. The aim of BICAN is to generate a complete reference atlas of cell types in the human brain across the lifespan, which can be shared and used throughout the research community. In addition to developing a “parts list” detailing the vast array of neurons and non-neuronal cells in the human brain, the project also aims to map cell interactions that underlie a wide range of brain disorders.

To this end, BICAN aims to suppor the publication, sharing, and exploration of datasets generated in the course of the project. Creating a complete reference atlas from multiple datasets requires vast harmonization of metadata. In order to facilitate the harmonization of metadata, we require datasets include a small set of metadata available from data submitters.

This document describes the schema, a type of contract, that BICAN requires of all datasets to enable searching, filtering, and integration of datasets.

Note that the requirements in the schema are just the minimum required information. Datasets often have additional metadata, which is preserved in datasets submitted to the data archives.

## Overview

The BICAN Library Minimal Metadata Schema defines...

This document has the following sections:

* [General requirements](#general-requirements)
* [(Deliver Library Pool)](#deliver-library-pool), which describe the data required...
* [(Pool Library)](#pool-library), which describe the data required...
* [(Receive Sample)](#receive-sample), which describe the data required...
* [(Shared)](#shared), which describe the data required...

## General Requirements

**Organisms**. Data must be from a Metazoan organism and defined in the NCBI organismal classification.

**Redundant Metadata**. It is STRONGLY RECOMMENDED to avoid multiple metadata fields containing identical or similar information.

## Deliver Library Pool

The data in the Deliver Library Pool is the metadata that essential for the pool... 

The following table describes the Deliver Library Pool metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### Batch Tube Name

<table><tbody>
    <tr>
      <th>Key</th>
      <td>batch_tube_name</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. This is the tube name provided by the sequencing core.
        </td>
    </tr>
</tbody></table>
<br>

### Library Lab Batch Name

<table><tbody>
    <tr>
      <th>Key</th>
      <td>Library_Lab_Batch_name</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. The library lab’s batch name, logged at Seq Core.
        </td>
    </tr>
</tbody></table>
<br>

### Tube Contents nm

<table><tbody>
    <tr>
      <th>Key</th>
      <td>Tube_Contents_nm</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>int</code>. The concentration of the library's pool.
        </td>
    </tr>
</tbody></table>
<br>

### Tube Inputs fmol

<table><tbody>
    <tr>
      <th>Key</th>
      <td>Tube_Inputs_fmol</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>int</code>. fmol library pool.
        </td>
    </tr>
</tbody></table>
<br>

### Tube Average Size bp

<table><tbody>
    <tr>
      <th>Key</th>
      <td>tube_ave_size_bp</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>int</code>. average insert size of library pool.
        </td>
    </tr>
</tbody></table>
<br>

## Pool Library

The data in the Pool Library is the metadata that essential for... 

The following table describes the Pool Library metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:
### Pool Internal Name

<table><tbody>
    <tr>
      <th>Key</th>
      <td>pool_internal_name</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. library pool name, internal.
        </td>
    </tr>
</tbody></table>
<br>

### Library Aliquot Name

<table><tbody>
    <tr>
      <th>Key</th>
      <td>library_aliquot_name</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. One library in the pool, also Start of fastq files
        </td>
    </tr>
</tbody></table>
<br>

## Receive Sample

The data in the Receive Sample is the metadata that essential for... 

The following table describes the Receive Sample metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:
### External Donor Name

<table><tbody>
    <tr>
      <th>Key</th>
      <td>external_donor_name</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. donor name labtracks (mice) or brainbank (human, nhp)
        </td>
    </tr>
</tbody></table>
<br>

### Decoded External Donor Name

<table><tbody>
    <tr>
      <th>Key</th>
      <td>decoded_external_donor_name</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>int</code>. (proposed) decoded BrainBank identifier for external release.
        </td>
    </tr>
</tbody></table>
<br>

### Donor Name

<table><tbody>
    <tr>
      <th>Key</th>
      <td>donor_name</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. donor name (local).
        </td>
    </tr>
</tbody></table>
<br>

### Organism

<table><tbody>
    <tr>
      <th>Key</th>
      <td>organism</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. common name for species.
        </td>
    </tr>
</tbody></table>
<br>

### Age

<table><tbody>
    <tr>
      <th>Key</th>
      <td>age</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. age and unit.
        </td>
    </tr>
</tbody></table>
<br>

### Sex

<table><tbody>
    <tr>
      <th>Key</th>
      <td>sex</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. sex
        </td>
    </tr>
</tbody></table>
<br>

### Medical Conditions

<table><tbody>
    <tr>
      <th>Key</th>
      <td>medical_conditions</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. medical conditions.
        </td>
    </tr>
</tbody></table>
<br>

### Full Genotype

<table><tbody>
    <tr>
      <th>Key</th>
      <td>full_genotype</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. genotype.
        </td>
    </tr>
</tbody></table>
<br>

### Injection Type

<table><tbody>
    <tr>
      <th>Key</th>
      <td>injection_type</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. Injection type.
        </td>
    </tr>
</tbody></table>
<br>

### Injection Method

<table><tbody>
    <tr>
      <th>Key</th>
      <td>injection_method</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. Injection method.
        </td>
    </tr>
</tbody></table>
<br>

### Injection Materials

<table><tbody>
    <tr>
      <th>Key</th>
      <td>injection_materials</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. Injection material (virus used).
        </td>
    </tr>
</tbody></table>
<br>

### Injection ROI

<table><tbody>
    <tr>
      <th>Key</th>
      <td>injection_roi</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. Injection ROI.
        </td>
    </tr>
</tbody></table>
<br>

### ROI Specimen ID

<table><tbody>
    <tr>
      <th>Key</th>
      <td>ROI_specimen_id</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>int</code>. Final intact piece of tissue before cell or nuclei prep.
        </td>
    </tr>
</tbody></table>
<br>

### ROI Specimen Name

<table><tbody>
    <tr>
      <th>Key</th>
      <td>ROI_specimen_name</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. unique tissue prep name, can be used for multiple facs_containers.
        </td>
    </tr>
</tbody></table>
<br>

### Ontology ROI

<table><tbody>
    <tr>
      <th>Key</th>
      <td>Ontology-ROI</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. ROI from controlled vocabulary and ontology-linked list.
        </td>
    </tr>
</tbody></table>
<br>

## Shared

The data in Shared is the metadata that essential for... 

The following table describes the Shared metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### Cell Prep Name

<table><tbody>
    <tr>
      <th>Key</th>
      <td>Cell_prep_name</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. name of cell or nuclei prep from an ROI_specimen_name, can generate multiple FACS_containers.
        </td>
    </tr>
</tbody></table>
<br>


### FACS conditions

<table><tbody>
    <tr>
      <th>Key</th>
      <td>facs_population_plan</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. FACS conditions
        </td>
    </tr>
</tbody></table>
<br>

### Sample Type

<table><tbody>
    <tr>
      <th>Key</th>
      <td>cell_prep_type</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. sample type (cells/nuclei)
        </td>
    </tr>
</tbody></table>
<br>

### Studies

<table><tbody>
    <tr>
      <th>Key</th>
      <td>studies</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. study set
        </td>
    </tr>
</tbody></table>
<br>

### Cell Prep Container

<table><tbody>
    <tr>
      <th>Key</th>
      <td>cell_prep_container</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. container (strip or tube or plate) from a cell_prep_name containing dissociated cells.
        </td>
    </tr>
</tbody></table>
<br>

### Expected Cells Captured

<table><tbody>
    <tr>
      <th>Key</th>
      <td>expc_cell_capture</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>int</code>. Excpected Cell/Nuclei captured.
        </td>
    </tr>
</tbody></table>
<br>

### Sample Name

<table><tbody>
    <tr>
      <th>Key</th>
      <td>sample_name</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. 10x port os SmartSeq well from a cell prep container, generally leading to one library (not used in PatchSeq).
        </td>
    </tr>
</tbody></table>
<br>

### Sample Quantity Count

<table><tbody>
    <tr>
      <th>Key</th>
      <td>sample_quantity_count</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>int</code>. Total Cells/Nuclei loaded
        </td>
    </tr>
</tbody></table>
<br>

### Sample Quantity pg

<table><tbody>
    <tr>
      <th>Key</th>
      <td>sample_quantity_pg</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. sample quant pg
        </td>
    </tr>
</tbody></table>
<br>

### Load Name

<table><tbody>
    <tr>
      <th>Key</th>
      <td>load_name</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. Load name for 10x, can lead to multiple libraries, needed especially for Multiome library unification.
        </td>
    </tr>
</tbody></table>
<br>

### Port Well

<table><tbody>
    <tr>
      <th>Key</th>
      <td>port_well</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. 10x port well
        </td>
    </tr>
</tbody></table>
<br>

### Chemistry

<table><tbody>
    <tr>
      <th>Key</th>
      <td>chemistry</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. Library method/chemistry.
        </td>
    </tr>
</tbody></table>
<br>

### RNA Amplification Set

<table><tbody>
    <tr>
      <th>Key</th>
      <td>rna_amplification_set</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. Amp plate/Amp set.
        </td>
    </tr>
</tbody></table>
<br>

### RNA Amplification

<table><tbody>
    <tr>
      <th>Key</th>
      <td>rna_amplification</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. Amp well.
        </td>
    </tr>
</tbody></table>
<br>

### Amplification Date

<table><tbody>
    <tr>
      <th>Key</th>
      <td>amp_date</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>date</code>. Amp date
        </td>
    </tr>
</tbody></table>
<br>

### PCR Cycles

<table><tbody>
    <tr>
      <th>Key</th>
      <td>pcr_cycles</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>int</code>. number of pcr cycles.
        </td>
    </tr>
</tbody></table>
<br>


### Percent of cDNA Longer than 400bp

<table><tbody>
    <tr>
      <th>Key</th>
      <td>percent_cdna_longer_than_400bp</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>int</code>. % cDNA >400bp
        </td>
    </tr>
</tbody></table>
<br>

### RNA Amplification Pass Fail

<table><tbody>
    <tr>
      <th>Key</th>
      <td>rna_amplification_pass_fail</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. Amp Pass/Fail (lab).
        </td>
    </tr>
</tbody></table>
<br>

### Amplified Quantity ng

<table><tbody>
    <tr>
      <th>Key</th>
      <td>amplified_quantity_ng</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>int</code>. Amp quant ng
        </td>
    </tr>
</tbody></table>
<br>

### Library Date

<table><tbody>
    <tr>
      <th>Key</th>
      <td>lib_date</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>date</code>. library date.
        </td>
    </tr>
</tbody></table>
<br>

### Library Prep Set

<table><tbody>
    <tr>
      <th>Key</th>
      <td>library_prep_set</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. library plate or library set
        </td>
    </tr>
</tbody></table>
<br>

### Library Name

<table><tbody>
    <tr>
      <th>Key</th>
      <td>library_name</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. Library id
        </td>
    </tr>
</tbody></table>
<br>

### Library Input ng

<table><tbody>
    <tr>
      <th>Key</th>
      <td>library_input_ng</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>int</code>. library input.
        </td>
    </tr>
</tbody></table>
<br>

### Library Average Size BP

<table><tbody>
    <tr>
      <th>Key</th>
      <td>avg_size_bp</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>int</code>. library avg size bp
        </td>
    </tr>
</tbody></table>
<br>

### Quantification 2 ng

<table><tbody>
    <tr>
      <th>Key</th>
      <td>quantification2_ng</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>int</code>. library quant ng
        </td>
    </tr>
</tbody></table>
<br>

### Quantification fmol

<table><tbody>
    <tr>
      <th>Key</th>
      <td>quantification_fmol</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. library quant fmol.
        </td>
    </tr>
</tbody></table>
<br>

### Quantification 2 nm

<table><tbody>
    <tr>
      <th>Key</th>
      <td>quantification2_nm</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. library quant nm
        </td>
    </tr>
</tbody></table>
<br>

### Library Prep Pass/Fail

<table><tbody>
    <tr>
      <th>Key</th>
      <td>library_prep_pass_fail</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. library Pass/Fail (lab)
        </td>
    </tr>
</tbody></table>
<br>

### Index Sequence Pair

<table><tbody>
    <tr>
      <th>Key</th>
      <td>index_sequence_pair</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. index sequence for each library_aliquot_name
        </td>
    </tr>
</tbody></table>
<br>

### R1 index

<table><tbody>
    <tr>
      <th>Key</th>
      <td>r1_index</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. index1 for each library_name
        </td>
    </tr>
</tbody></table>
<br>

### R2 index

<table><tbody>
    <tr>
      <th>Key</th>
      <td>r2_index</td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td>Curator</td>
    </tr>
    <tr>
      <th>Value</th>
        <td><code>str</code>. index1 for each library_name
        </td>
    </tr>
</tbody></table>
<br>

## Appendix A. Changelog

schema v0.0.1