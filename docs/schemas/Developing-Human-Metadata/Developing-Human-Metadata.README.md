# BICAN Developing Human Metadata Schema

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
* [Developing Human](#developing-human), which describe the metadata required for macaque patchseq experiments.
* [Appendix](#appendix)

## General Requirements

**Organisms**. Data must be from a Metazoan organism and defined in the NCBI organismal classification.

**Redundant Metadata**. It is STRONGLY RECOMMENDED to avoid multiple metadata fields containing identical or similar information.

## Developing Human

The data in developing human is the metadata essential for developing human experiments.

The following tables describe the developing human metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

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

### ethnicity

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>ethnicity</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>918370df-49f6-4361-9c52-f46b16412980</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>ethnicity</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Population category defined in terms of cultural, religious, tribal or other social similarities.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### race

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>race</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e515c009-550e-4f9c-b1b6-fc876a6fb2a8</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>race</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>An arbitrary classification of a taxonomic group that is a division of a species. It usually arises as a consequence of geographical isolation within a species and is characterized by shared heredity, physical attributes and behavior, and in the case of humans, by common history, nationality, or geographic distribution.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
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

### gender

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>gender</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1c71e775-65aa-442b-a392-1cf9a44e326e</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>gender</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Identification as male/masculine, female/feminine or something else, and association with a (social) role or set of behavioral and cultural traits, clothing, etc; a category to which a person belongs on this basis. Gender is the result of a complex combination of gender role, gender expression, gender identity, and gender modality. Do not use this term for non-human animals.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### sex orientation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>sex orientation</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e47e8a2f-72fb-4036-b288-f4580dc2aa4e</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>sex_orientation</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The pattern of a person's emotional, romantic, and/or sexual attractions.</td>
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

### birth country name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>birth country name</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>9c27fd29-b512-492f-a32f-b615c7585ff7</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>birth_country_name</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The name of the country where a subject was born.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### primary language

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>primary language</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>abe9edc7-96ca-4c6a-a1ed-c008548cc373</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>primary_language</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The alphanumeric code from the ISO 639 standard which denotes the primary lanugage of a subject. The ISO 639 standard includes a two letter representation and a three letter representation.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### secondary language

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>secondary language</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>37b7495f-b010-4d1c-ae32-9cb19c680950</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>secondary_language</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The alphanumeric code from the ISO 639 standard which denotes the secondary lanugage of a subject. The ISO 639 standard includes a two letter representation and a three letter representation.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### autopsy report

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>autopsy report</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3f787b64-0985-4d0f-9523-54475164b7ad</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>autopsy_report</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A document assembled by an author for the purpose of providing information regarding the cause of death of a subject for the audience.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### cause of death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cause of death</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>fa970a03-41ea-473b-a8ce-427fec92cdff</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>cause_of_death</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The circumstance or condition that results in the death of a living being.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### cause of death code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cause of death code</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>61374624-2d3c-477e-95b3-9bd30974b52a</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>cause_of_death_code</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The ISO code that denotes the circumstance or condition that results in the death of a living being.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>text</td>
    </tr>
</tbody></table>
<br>

### manner of death

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
      <th>Aliases</th>
      <td>manner_of_death</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The manner of death is the determination of how the injury or disease leads to death.  There are five manners of death (natural, accident, suicide, homicide, and undetermined).</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### informant questionnaire completed

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>informant questionnaire completed</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e8b9666f-a112-456f-aa5a-69a101c3866f</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>informant_questionnaire_completed</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The status (completed, not completed) of the document about the subject completed by an informant.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### informant interview performed

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>informant interview performed</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>274b838b-74c6-46ec-808a-0c080ddeedd9</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>informant_interview_performed</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The status (performed, not performed) of the interview event between a clinician and an informant.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### informant relationship

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>informant relationship</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>836c19fe-b735-4bf7-bee5-3213122b571e</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>informant_relationship</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The relationship that a informant bears to a subject/donor.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### handedness

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>handedness</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>82a4087c-d0e3-48ca-8bea-a81eefc683a0</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>handedness</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A behavioral quality inhering ina bearer by virtue of the bearer's unequal distribution of fine motor skill between its left and right hands or feet. [PATO]</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### medical records available

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
      <th>Aliases</th>
      <td>medical_records_available</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The status (available, unavailable) of the medical records of the subject/donor.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### medical records reviewed

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
      <th>Aliases</th>
      <td>medical_records_reviewed</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The status (reviewed, not reviewed) of the medical records of the subject/donor.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
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

### left hemisphere tissue inventory

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>left hemisphere tissue inventory</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>05e2821e-e7dc-4e33-94dc-7b55c372e5a0</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>left_hemisphere_tissue_inventory</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The inventory (list) of the tissue samples for a specific left hemisphere specimen.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### left hemisphere tissue sampling history

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>left hemisphere tissue sampling history</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b02f7dd7-4535-4b41-b8df-73786b8983bc</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>left_hemisphere_tissue_sampling_history</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The history of the tissue sampling for a specific left hemisphere specimen.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
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

### right hemisphere tissue inventory

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>right hemisphere tissue inventory</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>8b6b910f-beb7-4e2b-881a-7f862ef5d588</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>right_hemisphere_tissue_inventory</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The inventory (list) of the tissue samples for a specific right hemisphere specimen.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### right hemisphere tissue sampling history

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>right hemisphere tissue sampling history</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>60d2efe0-bf7f-48f7-96fc-71cdf03226dd</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>right_hemisphere_tissue_sampling_history</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The history of the tissue sampling for a specific right hemisphere specimen.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
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

### scan 3d available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>scan 3d available</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>658e8a80-e232-438f-8c1e-d5f38724dc55</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>scan_3d_available</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The status (available, unavailable) of three-dimensional scans of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### antemortem MRI available

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
      <th>Aliases</th>
      <td>antemortem_mri_available</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The status (available, unavailable) of antemortem MRI images of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### postmortem MRI available

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
      <th>Aliases</th>
      <td>postmortem_mri_available</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The status (available, unavailable) of postmortem MRI images of a subject/donor/specimen.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### postmortem MRI type

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
      <th>Aliases</th>
      <td>postmortem_mri_type</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The type of postmortem MRI that is available (cadeveric, fresh ex vivo, fixed ex vivo).</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>exclusive_categorical</td>
    </tr>
</tbody></table>
<br>

### anatomical atlas registration

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>anatomical atlas registration</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b6835813-2bab-42f3-ae63-4c372ed0aad9</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>anatomical_atlas_registration</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The anatomical atlas structure to which a specimen/tissue is registered.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td></td>
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
      <th>Aliases</th>
      <td>gestational_age_value_weeks</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The gestational age of the subject/donor in weeks.</td>
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
      <th>Aliases</th>
      <td>gestational_age_value_days</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The gestational age of the subject/donor in days.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

### gestational age value (months)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>gestational age value (months)</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c110d0c9-8acd-4889-b62d-3efe9b07657a</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>gestational_age_months</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The gestational age of the subject/donor in months.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>numeric</td>
    </tr>
</tbody></table>
<br>

## Appendix