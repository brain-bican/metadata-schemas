# BICAN Marmoset Metadata Schema

Document Status: _Under MOWG Review_

Version: 1.0

Owner: HMBA

Reviewers: @djarecka, @rightbower, @nsuvarnaiari

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 08-07-2024

## Background

The Brain Research Through Advancing Innovative Neurotechnologies® (BRAIN) Initiative Cell Atlas Network (BICAN) aims to transform our understanding of brain cell types and the precise tools needed to access them, bringing us one step closer to unraveling the complex workings of the human brain.

Building on findings from the BRAIN Initiative Cell Census Network (BICCN), BICAN takes the next step in mapping brain cells and circuits across multiple species, with an emphasis on humans. The aim of BICAN is to generate a complete reference atlas of cell types in the human brain across the lifespan, which can be shared and used throughout the research community. In addition to developing a “parts list” detailing the vast array of neurons and non-neuronal cells in the human brain, the project also aims to map cell interactions that underlie a wide range of brain disorders.

To this end, BICAN aims to support the publication, sharing, and exploration of datasets generated in the course of the project. Creating a complete reference atlas from multiple datasets requires vast harmonization of metadata. In order to facilitate the harmonization of metadata, we require datasets include a small set of metadata available from data submitters.

This document describes a schema, a type of contract, that BICAN requires of all donor to alignment datasets to enable searching, filtering, and integration of datasets.

Note that the requirements in the schema are just the minimum required information. Datasets often have additional metadata, which is preserved in datasets submitted to the data archives.

## Overview

The BICAN Marmoset Metadata schema describes metadata associated with and produced from the preparation of marmoset donor and tissue in the HMBA and BICAN. [more detail needed here]

This document has the following sections:

* [General Requirements](#general-requirements)
* [Spatial Omics](#spatial-omics), which describe the metadata required for spatial omics experiements.
* [Population](#population), which describe the metadata required for marmoset population studies.
* [Appendix](#appendix)

## General Requirements

**Organisms**. Data must be from a Metazoan organism and defined in the NCBI organismal classification.

**Redundant Metadata**. It is STRONGLY RECOMMENDED to avoid multiple metadata fields containing identical or similar information.

## Spatial Omics

The data in Spatial Omics is the metadata essential for marmoset spatial omics experiments.

The following tables describe the spatial omics metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

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

### Mating Status

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

### RIN Testing Organization

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

### RINe

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

### RINe Tissue Source

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

### RINe Testing Organization

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

### pH

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

### Brain Tissue Weighed Type

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

### Brain Size Anterior-Posterior

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

### Brain Size Medial-Lateral

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

### Brain Size Dorsal-Ventral

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

### Brain Size Unit

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

### Histological Stains Available

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

### Histological Stains Type

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

### Family History Available

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

### Relative Type

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

### Relative Type Specify

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

### Premortem MRI Available

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

### Premortem MRI Type

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

### Slab type

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

### Slab thickness (mm)

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

### Freezing method

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

The data in population is the metadata essential for marmoset population studies.

The following tables describe the population metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

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

### Mating Status

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

### RINe

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

### pH

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

### Brain Tissue Weighed Type

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

### Brain Size Anterior-Posterior

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

### Brain Size Medial-Lateral

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

### Brain Size Dorsal-Ventral

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

### Brain Size Unit

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

### Histological Stains Available

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

### Histological Stains Type

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

### Antemortem MRI Type

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

### Family History Available

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

### Relative Type

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

### Relative Type Specify

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

### Slab type

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

### Slab thickness (mm)

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

### Freezing method

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