# BICAN Library Metadata Schema

Contact: data-curation@alleninstitute.org

Document Status: _Pending Approval_

Version: 0.0.1

## Background

The Brain Research Through Advancing Innovative Neurotechnologies® (BRAIN) Initiative Cell Atlas Network (BICAN) aims to transform our understanding of brain cell types and the precise tools needed to access them, bringing us one step closer to unraveling the complex workings of the human brain.

Building on findings from the BRAIN Initiative Cell Census Network (BICCN), BICAN takes the next step in mapping brain cells and circuits across multiple species, with an emphasis on humans. The aim of BICAN is to generate a complete reference atlas of cell types in the human brain across the lifespan, which can be shared and used throughout the research community. In addition to developing a “parts list” detailing the vast array of neurons and non-neuronal cells in the human brain, the project also aims to map cell interactions that underlie a wide range of brain disorders.

To this end, BICAN aims to suppor the publication, sharing, and exploration of datasets generated in the course of the project. Creating a complete reference atlas from multiple datasets requires vast harmonization of metadata. In order to facilitate the harmonization of metadata, we require datasets include a small set of metadata available from data submitters.

This document describes the schema, a type of contract, that BICAN requires of all datasets to enable searching, filtering, and integration of datasets.

Note that the requirements in the schema are just the minimum required information. Datasets often have additional metadata, which is preserved in datasets submitted to the data archives.

## Overview

This schema supports multiple assay types. Each assay takes the form of one or more two-dimensional matrices whose values are quantitative measures of the phenotypes of cells.

The schema additionally describes how the dataset, genes, and cells are annotated to describe the biological and technical characteristics of the data.

This document has the following sections:

* [General requirements](#general-requirements)
* [(Deliver Library Pool)](#Deliver-Library-Pool), which describe the data required...

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
