# BICAN Macaque Donor and Tissue Metadata Schema

Document Status: _Under MOWG Review_

Version: 1.0

Owner: HMBA

Reviewers: @mgiglio99, @puja-trivedi, @patrick-lloyd-ray

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 08-07-2024

## Background

The Brain Research Through Advancing Innovative Neurotechnologies® (BRAIN) Initiative Cell Atlas Network (BICAN) aims to transform our understanding of brain cell types and the precise tools needed to access them, bringing us one step closer to unraveling the complex workings of the human brain.

Building on findings from the BRAIN Initiative Cell Census Network (BICCN), BICAN takes the next step in mapping brain cells and circuits across multiple species, with an emphasis on humans. The aim of BICAN is to generate a complete reference atlas of cell types in the human brain across the lifespan, which can be shared and used throughout the research community. In addition to developing a “parts list” detailing the vast array of neurons and non-neuronal cells in the human brain, the project also aims to map cell interactions that underlie a wide range of brain disorders.

To this end, BICAN aims to support the publication, sharing, and exploration of datasets generated in the course of the project. Creating a complete reference atlas from multiple datasets requires vast harmonization of metadata. In order to facilitate the harmonization of metadata, we require datasets include a small set of metadata available from data submitters.

This document describes a schema, a type of contract, that BICAN requires of all donor to alignment datasets to enable searching, filtering, and integration of datasets.

Note that the requirements in the schema are just the minimum required information. Datasets often have additional metadata, which is preserved in datasets submitted to the data archives.

## Overview

The BICAN Macaque Donor and Tissue Metadata schema describes metadata associated with and produced from the preparation of macaque donor and tissue in the HMBA and BICAN. [more detail needed here]

This document has the following sections:

* [General Requirements](#general-requirements)
* [PatchSeq](#patchseq), which describe the metadata required for macaque patchseq experiments.
* [Population](#population), which describe the metadata required for macaque population studies.
* [Whole Brain Spatial Omics](#whole-brain-spatial-omics), which describe the metadata required for whole brain spatial omics experiements.
* [Appendix](#appendix)

## General Requirements

**Organisms**. Data must be from a Metazoan organism and defined in the NCBI organismal classification.

**Redundant Metadata**. It is STRONGLY RECOMMENDED to avoid multiple metadata fields containing identical or similar information.

## PatchSeq

The data in patchseq is the metadata essential for macaque patchseq experiments.

The following tables describe the patchseq metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### Local Donor ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Repository

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Donor Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Sex at Birth

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Age Value (Years)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Date of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Manner of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Medical Records Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Medical Records Reviewed

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Hemisphere

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Post Mortem Interval

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Left Hemisphere Preparation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Left Hemisphere Preparation Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Right Hemisphere Preparation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Right Hemisphere Preparation Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Photo 2d Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Antemortem MRI Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Non-Brain Tissue Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Tissue Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Tissue Type Details

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Test Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Result

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Testing Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Species

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Premortem perfusion done

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Premortem perfusion buffer type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Region of interest

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Behavorial Testing

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Behavorial Testing Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Non Brain Diagnosis Description

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Population

The data in population is the metadata essential for macaque population studies.

The following tables describe the population metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### subject_id

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### repository

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### donor_source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### sex

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### age_of_death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### year_of_death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### autopsy_report

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### cause_of_death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### cause_of_death_code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### manner_of_death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### medical_records_reviewed

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### hemisphere

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### post_mortem_interval

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### left_hemisphere_preparation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### left_hemisphere_preparation_specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### right_hemisphere_preparation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### right_hemisphere_preparation_specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### rin

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### rin_tissue_source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### rin_testing_organization

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### rine

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### rine_tissue_source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### rine_testing_organization

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### ph

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### brain_weight

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### weighed_type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### photo_2d_available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### scan_3d_available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### antemortem_mri_available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### postmortem_mri_available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### postmortem_mri_type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### non_brain_tissue_available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### tissue_type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### tissue_type_details

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### birth_weight_lbs

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### birth_weight_oz

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### gestational_age_value_weeks

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### gestational_age_value_days

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### species

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### social_group

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### body_weight

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### perfusion

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### perfusate_type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### head_off_time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### brain_extraction_time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### brain_fixed_time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### brain_frozen_time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### brain_fixation_method

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### brain_freeze_method

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### sedation_start_time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### sedation_total_dose

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### euthanasia_time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### euthanasia_dose

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### perfusion_time_start

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### perfusion_time_end

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### trapping_date

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### trapping_time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### matriline

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### behavioral_scoring_available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### behavioral_scoring_type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### ordinal_dominance_rank

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### brain_size_anterior_posterior

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### brain_size_medial_lateral

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### brain_size_dorsal_ventral

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### brain_size_unit_type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### histological_stains_available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### histological_stain_type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Whole Brain Spatial Omics

The data in whole brain spatial omics is the metadata essential for whole brain spatial omics experiments.

The following tables describe the whole brain spatial omics metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### Local Donor ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Repository

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Donor Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Sex at Birth

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Age Value (Years)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Birth Country Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Date of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Hemisphere

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Post Mortem Interval

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RIN

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RIN Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Brain Weight Measurement

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Photo 2d Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Scan 3d Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Antemortem MRI Available
 
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Appendix
