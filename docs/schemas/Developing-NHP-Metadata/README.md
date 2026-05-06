# BICAN Developing NHP Metadata Schema

Document Status: _Approved by MOWG_

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
      <td>local donor ID</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>subject_id</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### repository

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
      <th>Aliases</th>
      <td>repository</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Repository' trailing modifier (qualifier, 'repository') of 'xref' links of 'Format' concepts. When 'true', the link is pointing to the public source-code repository where the given data format is developed or maintained.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>inclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### donor source

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
      <th>Aliases</th>
      <td>donor_source</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The origin of the donor/subject in this experiment.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>inclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### sex at birth

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
      <th>Aliases</th>
      <td>sex</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>An organismal quality inhering in a bearer by virtue of the bearer's ability to undergo sexual reproduction in order to differentiate the individuals or types involved.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### age value (years)

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
      <th>Aliases</th>
      <td>age_of_death</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A time quality inhering in a bearer by virtue of how long the bearer has existed.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### date of death

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

### hemisphere

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
      <th>Aliases</th>
      <td>hemisphere</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>One of two bilateral, largely symmetrical organ subdivisions within the telencephalon which contain the cerebral cortex and cerebral white matter.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>


### post mortem interval

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
      <th>Aliases</th>
      <td>post_mortem_interval</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The length temporal interval between the time of death of the subject/donor and the time at which the specimen is made.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### left hemisphere preparation

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
      <th>Aliases</th>
      <td>left_hemisphere_preparation</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The type of preparation method used for the left hemisphere.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### left hemisphere preparation specify

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
      <th>Aliases</th>
      <td>left_hemisphere_preparation_specify</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Specific details about the type of preparation method used for the left hemisphere.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### right hemisphere preparation

<<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>right hemisphere preparation</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>477c2600-f979-43c5-9c61-ab61fd771584</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>right_hemisphere_preparation</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The type of preparation method used for the right hemisphere.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### right hemisphere preparation specify

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
      <th>Aliases</th>
      <td>right_hemisphere_preparation_specify</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Specific details about the type of preparation method used for the right hemisphere.</td>
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
      <th>Aliases</th>
      <td>rin</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The RNA integrity number value of a specimen.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### RIN tissue source

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

### RIN testing organization

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
      <th>Aliases</th>
      <td>rine</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A type of RIN (RNA integrity number) value that represents the relative ratio of the signal in the fast zone to the 18S peak signal fpr a specimen.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### RINe tissue source

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

### RINe testing organization

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
      <th>Aliases</th>
      <td>ph</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The value of a measurement of acidity or basicity of a tissue, sample, or specimen.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### brain weight measurement

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
      <th>Aliases</th>
      <td>brain_weight</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The weight of a brain specimen.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### brain tissue weighed type

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
      <th>Aliases</th>
      <td>weighed_type</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The state of a brain specimen when it is weighed (fresh, frozen, fixed).</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### photo 2d available

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
      <th>Aliases</th>
      <td>photo_2d_available</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The status (available, unavailable) of two-dimensional photos of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### non-brain tissue available

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

### tissue type

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

### tissue type details

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
      <td>The details of the non-brain tissue that is available from this organism. </td>
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

### birth weight value (lbs)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>birth weight value (lbs)</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>69d9a60d-32d5-4c3a-a26a-802d8f030c8d</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The weight (at birth) of the subject/donor in pounds.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>birth_weight_lbs</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### birth weight value (oz)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>birth weight value (oz)</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b6f30050-f762-4427-8533-31738e737ea2</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The weight (at birth) of the subject/donor in ounces.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>birth_weight_oz</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### gestational age value (weeks)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>gestational age value (weeks)</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6d8a9b3f-792c-48c2-bd3c-56e52bb51672</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The gestational age of the subject/donor in weeks.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>gestational_age_value_weeks</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### gestational age value (days)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>gestational age value (days)</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4e532e52-6e4c-46cd-9fde-96f97ef3b034</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The gestational age of the subject/donor in days.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>gestational_age_value_days</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### species

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

### body weight

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>body weight</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f2673501-b48f-4703-bb7e-d642b73c2ad4</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The weight of the whole organism/donor/subject.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>body_weight</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### premortem perfusion done

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

### premortem perfusion buffer type

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

### head off time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>head off time</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>00ab5986-a8c4-4a7f-bf2b-6b5f08a97b25</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which the head was removed from the organism/donor/subject.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>head_off_time</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### brain extraction time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain extraction time</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>06be5810-7b9c-452e-b7ca-13eeb15179ca</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which the brain was extracted from the organism/donor/subject.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_extraction_time</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### brain fixed time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain fixed time</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2a09ecb4-0096-4a6c-b4f0-9b68cb231413</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which the brain specimen was fixed.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_fixed_time</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### brain frozen time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain frozen time</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>fb01ce0d-1417-404a-978d-aad708c0404f</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which the brain specimen was frozen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_frozen_time</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### brain fixation method

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain fixation method</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>8e0a01a9-ab7a-49a5-bf44-cc0af47719b1</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The method used for fixing the brain specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>brain_fixation_method</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### brain freeze method

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
      <td></td>
    </tr>
</tbody></table>
<br>

### sedation start time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>sedation start time</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0ad6cca0-d4ce-4cd8-bbce-520bc01db061</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which sedation of the organism/donor/subject began.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>sedation_start_time</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### sedation total dose

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>sedation total dose</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3c895613-4526-4b87-8620-7b42eff94fee</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The total dose of sedation used on the organism/donor/subject.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>sedation_total_dose</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### euthanasia time

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>euthanasia time</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>14c541ab-7db3-4438-9328-c5f3098f5ff7</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which euthanasia of the organism/donor/subject occurred.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>euthanasia_time</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### euthanasia dose

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>euthanasia dose</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d87c6869-c0d1-46b3-bb32-95dc3e3d5ed4</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The dose of compouds used to euthanize the organism/donor/subject.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>euthanasia_dose</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### perfusion time start

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>perfusion time start</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7f94f8ad-82b7-4827-9614-838555a1f046</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which perfusion began.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>perfusion_time_start</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### perfusion time end

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>perfusion time end</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6c873444-8306-4b3f-9e5a-97f6d34c88b3</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The time at which perfusion ended.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>perfusion_time_end</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### matriline

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>matriline</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ae0447a3-0504-43a3-95d5-4248e53d3224</td>
    </tr>
    <tr>
      <th>Definition</th>
      <td>The relavant matriline and patriline information for a subject/donor/sample/specimen.</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>family_history</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### brain size anterior-posterior

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

### brain size medial-lateral

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

### brain size dorsal-ventral

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

### brain size unit

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

### histological stains available

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

### histological stains type

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

## Appendix