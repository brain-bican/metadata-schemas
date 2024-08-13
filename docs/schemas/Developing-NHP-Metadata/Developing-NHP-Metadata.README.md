# BICAN Developing NHP Metadata Schema

Document Status: _Under MOWG Review_

Version: 1.0

Owner: HMBA

Reviewers: @MariahKenney, @licongcui, @patrick-lloyd-ray

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 08-07-2024

## Background

The Brain Research Through Advancing Innovative Neurotechnologies® (BRAIN) Initiative Cell Atlas Network (BICAN) aims to transform our understanding of brain cell types and the precise tools needed to access them, bringing us one step closer to unraveling the complex workings of the human brain.

Building on findings from the BRAIN Initiative Cell Census Network (BICCN), BICAN takes the next step in mapping brain cells and circuits across multiple species, with an emphasis on humans. The aim of BICAN is to generate a complete reference atlas of cell types in the human brain across the lifespan, which can be shared and used throughout the research community. In addition to developing a “parts list” detailing the vast array of neurons and non-neuronal cells in the human brain, the project also aims to map cell interactions that underlie a wide range of brain disorders.

To this end, BICAN aims to support the publication, sharing, and exploration of datasets generated in the course of the project. Creating a complete reference atlas from multiple datasets requires vast harmonization of metadata. In order to facilitate the harmonization of metadata, we require datasets include a small set of metadata available from data submitters.

This document describes a schema, a type of contract, that BICAN requires of all donor to alignment datasets to enable searching, filtering, and integration of datasets.

Note that the requirements in the schema are just the minimum required information. Datasets often have additional metadata, which is preserved in datasets submitted to the data archives.

## Overview

The BICAN Developing Human and NHP Tissue Metadata schema describes metadata associated with and produced from the preparation of macaque donor and tissue in the HMBA and BICAN. [more detail needed here]

This document has the following sections:

* [General Requirements](#general-requirements)
* [Developing Nonhuman Primate](#developing-nonhuman-primate), which describe the metadata required for macaque population studies.
* [Appendix](#appendix)

## General Requirements

**Organisms**. Data must be from a Metazoan organism and defined in the NCBI organismal classification.

**Redundant Metadata**. It is STRONGLY RECOMMENDED to avoid multiple metadata fields containing identical or similar information.

## Developing Nonhuman Primate

The data in developing nonhuman primate is the metadata essential for developing nonhuman primate experiments.

The following tables describe the developing nonhuman primate metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### local donor ID

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

### donor source

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

### sex at birth

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

### age value (years)

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

### date of death

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

### post mortem interval

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

### left hemisphere preparation

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

### left hemisphere preparation specify

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

### right hemisphere preparation

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

### right hemisphere preparation specify

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

### RIN tissue source

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

### RIN testing organization

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

### RINe tissue source

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

### RINe testing organization

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

### brain weight measurement

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

### brain tissue weighed type

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

### photo 2d available

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

### non-brain tissue available

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

### tissue type

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

### tissue type details

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

### birth weight value (lbs)

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

### birth weight value (oz)

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

### gestational age value (weeks)

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

### gestational age value (days)

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

### body weight

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

### premortem perfusion done

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

### premortem perfusion buffer type

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

### head off time

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

### brain extraction time

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

### brain fixed time

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

### brain frozen time

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

### brain fixation method

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

### brain freeze method

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

### sedation start time

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

### sedation total dose

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

### euthanasia time

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

### euthanasia dose

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

### perfusion time start

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

### perfusion time end

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

### brain size anterior-posterior

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

### brain size medial-lateral

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

### brain size dorsal-ventral

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

### brain size unit

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

### histological stains available

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

### histological stains type

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