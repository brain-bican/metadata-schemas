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
      <td>An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry.</td>
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

### Year of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>year of death</td>
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

### Mating Status

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>mating status</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>dd2ea811-b424-4b85-a572-16707a6612f3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The mating status of the subject/donor.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>mating_status</td>
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

### RIN

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RIN</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cd472c0d-0b64-45c9-a38e-e54d15cea953</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The RNA integrity number value of a specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rin</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### RIN Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RIN tissue source</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d547ee51-9ec3-489c-8e49-7d8cd94080a8</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The tissue sample location or identifier that is used for calculating the RNA integrity number.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rin_tissue_source</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### RIN Testing Organization

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RIN testing organization</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cfed831e-9a62-4a32-bf92-532873420eb3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The organization that determines the RNA integrity number of a sample/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rin_testing_organization</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### RINe

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RINe</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1210148d-d8fb-45aa-b51a-4b19b6d09bec</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>A type of RIN (RNA integrity number) value that represents the relative ratio of the signal in the fast zone to the 18S peak signal fpr a specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rine</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### RINe Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RINe tissue source</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7d5fd9af-82a1-4bdb-a3c6-9225d1717c53</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The tissue sample location or identifier that is used for calculating the RINe number.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rine_tissue_source</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### RINe Testing Organization

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RINe testing organization</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>15a6d162-a3ca-4852-b626-a911c37c04c9</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The organization that determines the RINe number.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rine_testing_organization</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### pH

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>pH</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>9e67af02-c081-43e1-a42c-bf9603cae616</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The value of a measurement of acidity or basicity of a tissue, sample, or specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>ph</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Weight

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain weight measurement</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>546fc32d-f8a2-4c00-924a-8c4730f11f51</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The weight of a brain specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_weight</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Tissue Weighed Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain tissue weighed type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a7463e3f-0c61-4718-a7d0-60fd2116908a</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The state of a brain specimen when it is weighed (fresh, frozen, fixed).</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>weighed_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Brain Size Anterior-Posterior

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain size anterior-posterior</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0830564a-26ba-41eb-888a-33d0c39ead8f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The size of the brain specimen in the anterior-posterior axis.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_size_anterior_posterior</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Size Medial-Lateral

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain size medial-lateral</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4722f739-71f6-4001-9784-afef8f9f2d0e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The size of the brain specimen in the medial-lateral axis.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_size_medial_lateral</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Size Dorsal-Ventral

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain size dorsal-ventral</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e683f5ee-696f-4baf-a9bf-2f12226ceb4a</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The size of the brain specimen in the dorsal-ventral axis.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_size_dorsal_ventral</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Size Unit Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain size unit</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4d0c44c6-e620-455d-989e-126c3c81ec91</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The unit that the brain size measurements are recorded.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_size_unit_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Histological Stains Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>histological stains available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4b868ba6-dba8-45e3-a43e-88e421625cab</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of histological stainings of a specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>histological_stains_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Histological Stain Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>histological stains type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6723e756-e4c1-42c7-bf2d-ee2e300b88ff</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of histological stains available for a specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>histological_stain_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
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

### Family History Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>family history available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c88bf4dc-5a7c-4f70-a773-e6bbb5a12ec9</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of the family history of the subject/donor.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>family_history_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Relative Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>relative type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1adef34c-bb96-4dd0-bc87-51868f2ddc3f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The familial relation to the subject/donor.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>relative_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Relative Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>relative type specify</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>094064a1-362c-4b75-8556-6b874c843fdb</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The specifici familial relation to the subject/donor.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>relative_type_specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### Postmortem MRI Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>postmortem MRI available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0badd072-0c25-48c6-9357-44d5b5bc0818</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of postmortem MRI images of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>postmortem_mri_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Postmortem MRI Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>postmortem MRI type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>64a607a9-21e6-4c73-8f2e-2d67b0dc51c8</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of postmortem MRI that is available (cadeveric, fresh ex vivo, fixed ex vivo).</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>postmortem_mri_type</td>
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

### Slab type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>slab type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>95d12973-310b-4631-87ea-94d698ef8030</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of brain slab specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>slab_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Slab thickness (mm)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>slab thickness (mm)</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ba931b4b-ba49-4789-bf8d-d1b37aca5702</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The thickness (in mm) of the brain slab specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>slab_thickness_mm</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Freeze Method

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain freeze method</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>71237def-9b50-481f-a01d-65dc99e3493f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The method used for freezing the brain specimen. </td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_freeze_method</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
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
      <td>local donor ID</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry.</td>
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

### Year of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>year of death</td>
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

### Mating Status

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>mating status</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>dd2ea811-b424-4b85-a572-16707a6612f3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The mating status of the subject/donor.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>mating_status</td>
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

### RIN

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RIN</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cd472c0d-0b64-45c9-a38e-e54d15cea953</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The RNA integrity number value of a specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rin</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### RINe

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>RINe</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1210148d-d8fb-45aa-b51a-4b19b6d09bec</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>A type of RIN (RNA integrity number) value that represents the relative ratio of the signal in the fast zone to the 18S peak signal fpr a specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>rine</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### pH

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>pH</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>9e67af02-c081-43e1-a42c-bf9603cae616</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The value of a measurement of acidity or basicity of a tissue, sample, or specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>ph</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Weight Measurement

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain weight measurement</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>546fc32d-f8a2-4c00-924a-8c4730f11f51</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The weight of a brain specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_weight</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Tissue Weighed Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain tissue weighed type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a7463e3f-0c61-4718-a7d0-60fd2116908a</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The state of a brain specimen when it is weighed (fresh, frozen, fixed).</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>weighed_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Brain Size Anterior-Posterior

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain size anterior-posterior</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0830564a-26ba-41eb-888a-33d0c39ead8f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The size of the brain specimen in the anterior-posterior axis.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_size_anterior_posterior</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Size Medial-Lateral

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain size medial-lateral</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4722f739-71f6-4001-9784-afef8f9f2d0e</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The size of the brain specimen in the medial-lateral axis.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_size_medial_lateral</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Size Dorsal-Ventral

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain size dorsal-ventral</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e683f5ee-696f-4baf-a9bf-2f12226ceb4a</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The size of the brain specimen in the dorsal-ventral axis.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_size_dorsal_ventral</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Size Unit

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain size unit</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4d0c44c6-e620-455d-989e-126c3c81ec91</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The unit that the brain size measurements are recorded.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_size_unit_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Histological Stains Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>histological stains available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4b868ba6-dba8-45e3-a43e-88e421625cab</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of histological stainings of a specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>histological_stains_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Histological Stain Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>histological stains type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6723e756-e4c1-42c7-bf2d-ee2e300b88ff</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of histological stains available for a specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>histological_stain_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
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

### Antemortem MRI Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>antemortem MRI type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>05ce0a33-16e7-4580-96b2-701c0ed4fbd2</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The specific type of antemortem MRI that is available.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>antemortem_MRI_type</td>
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

### Family History Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>family history available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c88bf4dc-5a7c-4f70-a773-e6bbb5a12ec9</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The status (available, unavailable) of the family history of the subject/donor.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>family_history_available</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Relative Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>relative type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1adef34c-bb96-4dd0-bc87-51868f2ddc3f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The familial relation to the subject/donor.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>relative_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Relative Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>relative type specify</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>094064a1-362c-4b75-8556-6b874c843fdb</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The specifici familial relation to the subject/donor.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>relative_type_specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
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

### Slab type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>slab type</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>95d12973-310b-4631-87ea-94d698ef8030</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The type of brain slab specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>slab_type</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### Slab thickness (mm)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>slab thickness (mm)</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ba931b4b-ba49-4789-bf8d-d1b37aca5702</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The thickness (in mm) of the brain slab specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>slab_thickness_mm</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### Brain Freeze Method

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain freeze method</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>71237def-9b50-481f-a01d-65dc99e3493f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The method used for freezing the brain specimen. </td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_freeze_method</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

## Appendix