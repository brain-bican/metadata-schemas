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
      <td>local donor ID</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>subject_id</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Repository

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>repository</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>408682ed-0e27-41e2-b9fa-f05674366d6e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>'Repository' trailing modifier (qualifier, 'repository') of 'xref' links of 'Format' concepts. When 'true', the link is pointing to the public source-code repository where the given data format is developed or maintained.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>repository</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>inclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Donor Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>donor source</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0d0cf732-0f76-409d-9a73-7a96d829d3d3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The origin of the donor/subject in this experiment.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>donor_source</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>inclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Sex at Birth

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>sex at birth</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c819b9d5-2fde-40b2-bf0d-e07b56f96ac9</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>An organismal quality inhering in a bearer by virtue of the bearer's ability to undergo sexual reproduction in order to differentiate the individuals or types involved.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>sex</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Age Value (Years)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>age value (years)</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>14eb923a-161d-45e2-889d-81fea7b632b6</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>A time quality inhering in a bearer by virtue of how long the bearer has existed.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>age_of_death</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Date of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>date of death</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>60445046-d9d8-4f00-959e-9a4c42613e5e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The year wherein the subject or donor has ceased to exist.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>year_of_death</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>date</td>
    </tr>
</tbody></table>
<br>

### Manner of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>manner of death</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>36eeb35b-5020-4a9e-a74b-6e1104415e0e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The manner of death is the determination of how the injury or disease leads to death.  There are five manners of death (natural, accident, suicide, homicide, and undetermined).</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>manner_of_death</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Medical Records Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>medical records available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ee2c9223-f7d1-4c64-a1da-cd7408309955</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of the medical records of the subject/donor.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>medical_records_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Medical Records Reviewed

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>medical records reviewed</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6139b159-c36c-4501-9176-fe2741e3d448</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (reviewed, not reviewed) of the medical records of the subject/donor.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>medical_records_reviewed</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Hemisphere

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>hemisphere</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>68b7a28b-d695-4ec9-800b-6a27ca206081</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>One of two bilateral, largely symmetrical organ subdivisions within the telencephalon which contain the cerebral cortex and cerebral white matter.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>hemisphere</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Post Mortem Interval

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>post mortem interval</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6fd5c5ac-b128-4a4a-ae98-09eaeba22f92</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The length of the temporal interval between the time of death of the subject/donor and the time at which the specimen is made.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>post_mortem_interval</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Left Hemisphere Preparation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>left hemisphere preparation</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>57d5378f-a451-4bf5-a472-cc88d0d29586</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of preparation method used for the left hemisphere.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>left_hemisphere_preparation</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Left Hemisphere Preparation Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>left hemisphere preparation specify</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>002e915e-01c3-4570-a1f3-76680dcb2c33</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>Specific details about the type of preparation method used for the left hemisphere.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>left_hemisphere_preparation_specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Right Hemisphere Preparation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>right hemisphere preparation</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>477c2600-f979-43c5-9c61-ab61fd771584</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of preparation method used for the right hemisphere.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>right_hemisphere_preparation</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Right Hemisphere Preparation Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>right hemisphere preparation specify</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>efd50be4-f7cf-4146-a08e-28f25680728c</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>Specific details about the type of preparation method used for the right hemisphere.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>right_hemisphere_preparation_specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Photo 2D Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>photo 2d available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>611beda8-1ac6-4183-a284-04a30bb474f3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of two-dimensional photos of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>photo_2d_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Antemortem MRI Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>antemortem MRI available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>43a04caa-4f28-47ac-8a9d-74c40f10776f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of antemortem MRI images of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>antemortem_mri_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Non-Brain Tissue Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>non-brain tissue available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3a064c96-a956-4cf3-8b77-056b8e392f99</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (yes, no) of whether non-brain tissue from this organism is available.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>non_brain_tissue_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Tissue Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>33ccbc85-ae35-44d6-8bc6-c2fb91116cf7</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of tissue (non-brain) that is available from this organism. </td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>tissue_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Tissue Type Details

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue type details</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f551cf87-2c6e-4b92-888d-6310e6a500d8</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The details of the non-brain tissue that is available from this organism.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>tissue_type_details</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Test Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>test name</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b6865e15-7538-4890-be99-a6f9e9920af3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The name of the test that has been performed.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>test_name</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Result

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>test result</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c14ea006-662c-4666-bfd1-6ff580c403ed</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The result(s) of the test that has been performed.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>test_result</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Testing Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>testing tissue source</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>42f8e11b-d9a3-48fe-ac1e-cd6f4469de46</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The tissue sample location or identifier that is the subject of a test. </td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>tissue_source</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Species

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
      <th>Definition</th>
      <td>The species of a subject/donor/sample/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>species</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Premortem perfusion done

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>premortem perfusion done</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1fc487d8-2403-4d7c-952f-7e502d5f8359</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status of premortem perfusion (done, not done).</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>perfusion</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Premortem perfusion buffer type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>premortem perfusion buffer type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>78d62e29-4323-4927-aec8-6fc8dc59a889</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of premortem perfusion buffer that was used for premortem perfusion. </td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>perfusate_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Region of interest

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>region of interest</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>71611b58-f98e-4a69-ad88-c0029a377cbe</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The brain region, structure, or area from which a brain tissue source derives.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>ROI</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Behavorial Testing

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>behavioral scoring available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ea33881a-9813-4111-979b-135355e8141e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of the behavioral scoring results for a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>behavioral_scoring_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Behavorial Testing Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>behavioral scoring type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0a7a1eeb-8682-4261-8221-82d587dde0fa</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of behavioral scoring that is available for a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>behavioral_scoring_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Non Brain Diagnosis Description

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>non brain diagnosis description</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4ba7c8cc-563c-4f0b-ab57-ae9c9762943f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The description (text) of a non-brain diagnosis for a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>non_brain_diagnosis_description</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
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
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Data Type</th>
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
