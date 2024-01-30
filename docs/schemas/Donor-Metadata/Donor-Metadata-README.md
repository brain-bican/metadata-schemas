# Donor Metadata Schema

Document Status: _Endorsed BICAN Standard_

Version: 1.0

Owner: @memartone

Reviewers: @patrick-lloyd-ray, @carolth, @rightbower

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 23-09-2023

## Overview

The BICAN Donor Metadata schema specifies the metadata relating to donors in BICAN. These metadata reflect the metadata needed to accurately track donors and related entities from the brain banks through the specimen portal. As such, it is a collaborative schema that reflects the joint efforts of members of BICAN. 

Note that there are additional fields in the metadata schema which are not explicitly required at time of creation, but will be populated when relevant resources are created/updated. 

This document has the following sections:

* [General Requirements](#general-requirements)
* [General Subject Fields](#general-subject-fields)
* [General Specimen Data](#general-specimen-metadata)
* [Non-Brain Specimen Collected](#non-brain-specimen-collected)
* [Diagnoses](#diagnoses)
* [Infant Medical History](#infant-medical-history)
* [Perinatal Neurologic Events](#perinatal-neurologic-events)
* [Family History](#family-history)
* [Infectious Disease Testing](#infectious-disease-testing)
* [Toxicology Screening](#toxicology-screening)
* [Neuropathological Diagnoses](#neuropathological-diagnoses)
* [Appendix](#appendix)
* [Changelog](#changelog)

## General Requirements

[brief description of general requirements]

## General Subject Fields

### Local Donor ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Local Donor ID</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</td>
    </tr>    
</tbody></table>
<br>

### Repository

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Repository</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>inclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>408682ed-0e27-41e2-b9fa-f05674366d6e</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>inclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0d0cf732-0f76-409d-9a73-7a96d829d3d3</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Ethnicity

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>ethnicity</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>918370df-49f6-4361-9c52-f46b16412980</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Race

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>race</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e515c009-550e-4f9c-b1b6-fc876a6fb2a8</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c819b9d5-2fde-40b2-bf0d-e07b56f96ac9</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Gender at Time of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>gender at time of death</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1c71e775-65aa-442b-a392-1cf9a44e326e</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Sexual Orientation at Time of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>sexual orientation at time of death</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e47e8a2f-72fb-4036-b288-f4580dc2aa4e</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Age Value (Years)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>age at death</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>14eb923a-161d-45e2-889d-81fea7b632b6</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Birth Country Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>birth country name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>9c27fd29-b512-492f-a32f-b615c7585ff7</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Primary Language Code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>primary language code</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A human-readable, locally unique label that identifies a data collection.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>abe9edc7-96ca-4c6a-a1ed-c008548cc373</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Secondary Language Code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>secondary language code</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>37b7495f-b010-4d1c-ae32-9cb19c680950</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>date</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>60445046-d9d8-4f00-959e-9a4c42613e5e</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Autopsy Report

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>autopsy report</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3f787b64-0985-4d0f-9523-54475164b7ad</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Cause of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cause of death</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>inclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>fa970a03-41ea-473b-a8ce-427fec92cdff</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Cause of Death Code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cause of death code</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>inclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>61374624-2d3c-477e-95b3-9bd30974b52a</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>36eeb35b-5020-4a9e-a74b-6e1104415e0e</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Marital or Partner Status ATOD

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>marital or partner status at time of death</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4f0e41c9-dd15-4a37-ae6b-11b7131d7cba</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Education Years Number

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>education years number</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>add3f7fe-ae60-4cc1-bb2e-72bbbe9a1a7d</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Family Income Range

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>family income range</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6cd785e2-7333-43fe-8c8c-c19532e96ea6</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Informant Questionnaire Completed

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>informant questionnaire completed</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e8b9666f-a112-456f-aa5a-69a101c3866f</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Informant Interview Performed

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>informant interview performed</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>274b838b-74c6-46ec-808a-0c080ddeedd9</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Informant Relationship

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>informant relationship</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>836c19fe-b735-4bf7-bee5-3213122b571e</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Informant Relationship Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>informant relationship specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>289bcbb8-5177-4c65-b0af-159fd65b69aa</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Handedness

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>handedness</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>82a4087c-d0e3-48ca-8bea-a81eefc683a0</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ee2c9223-f7d1-4c64-a1da-cd7408309955</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6139b159-c36c-4501-9176-fe2741e3d448</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## General Specimen Data

### Hemisphere

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>hemisphere</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>68b7a28b-d695-4ec9-800b-6a27ca206081</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Post-Mortem Interval

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>post mortem interval</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6fd5c5ac-b128-4a4a-ae98-09eaeba22f92</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>57d5378f-a451-4bf5-a472-cc88d0d29586</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>002e915e-01c3-4570-a1f3-76680dcb2c33</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>477c2600-f979-43c5-9c61-ab61fd771584</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>efd50be4-f7cf-4146-a08e-28f25680728c</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RIN

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>rin</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cd472c0d-0b64-45c9-a38e-e54d15cea953</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RIN Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>rin tissue source</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d547ee51-9ec3-489c-8e49-7d8cd94080a8</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RIN Testing Organization

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>rin testing organization</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cfed831e-9a62-4a32-bf92-532873420eb3</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RINe

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>rine</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1210148d-d8fb-45aa-b51a-4b19b6d09bec</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RINe Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>rine tissue source</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7d5fd9af-82a1-4bdb-a3c6-9225d1717c53</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RINe Testing Organization

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>rine testing organization</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>15a6d162-a3ca-4852-b626-a911c37c04c9</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>9e67af02-c081-43e1-a42c-bf9603cae616</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Brain Weight

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>brain weight</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>546fc32d-f8a2-4c00-924a-8c4730f11f51</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a7463e3f-0c61-4718-a7d0-60fd2116908a</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Photo 2D Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>photo 2D available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>611beda8-1ac6-4183-a284-04a30bb474f3</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Scan 3D Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>scan 3D available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>658e8a80-e232-438f-8c1e-d5f38724dc55</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>43a04caa-4f28-47ac-8a9d-74c40f10776f</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0badd072-0c25-48c6-9357-44d5b5bc0818</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Postmortum MRI Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>postmortem MRI type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>64a607a9-21e6-4c73-8f2e-2d67b0dc51c8</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Antatomical Atlas Registration

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>anatomical atlas registration</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b6835813-2bab-42f3-ae63-4c372ed0aad9</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>










## Non-Brain Specimen Collected

### Non-Brain Tissue Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>non-brain tissue available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3a064c96-a956-4cf3-8b77-056b8e392f99</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>33ccbc85-ae35-44d6-8bc6-c2fb91116cf7</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f551cf87-2c6e-4b92-888d-6310e6a500d8</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Subject ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>subject ID</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b2bb8225-aa6e-423a-a32d-98feaf84984f</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue source</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ee83ecf8-4fca-4353-a9ed-4cdd82eb167e</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Date of Collection

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>date of collection</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>date</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>9b94949c-a7c9-4d81-a1c9-a70c96c16ca3</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Age at Date of Collection

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>age at date of collection</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6c53ac16-fe2d-48d7-b3d4-b8946b5d2547</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Diagnoses

### Clinical Brain Diagnosis Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>clinical brain diagnosis available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b49f026b-4f6c-48c8-b170-bf6d24c672ef</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Clinical Brain Diagnosis Code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>clinical brain diagnosis code</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b7a34c73-ae08-43d3-80d2-d5ef8436e449</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Clinical Brain Diagnosis Confidence Level

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>clinical brain diagnosis confidence level</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2e72b4b9-d5fb-4f0d-897c-1f977ed4fabd</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Genetic Diagnosis Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>genetic diagnosis available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f67d3837-159d-4868-9749-aa6c83ded7eb</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Genetic Diagnosis Code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>genetic diagnosis code</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7a7916e0-ff79-4426-b49f-58e2f2a8a367</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Genetic Diagnosis Confidence Level

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>genetic diagnosis confidence level</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cb2b0108-8c07-40e8-92a3-b693b6dc64b4</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Non-Brain Diagnosis Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>non-brain diagnosis available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>009ec58e-32e4-4712-930c-056e72c8d8fa</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Non-Brain Diagnosis Code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>non-brain diagnosis code</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>65e8824e-01d2-44cf-9f47-9962461a65c9</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Non-Brain Diagnosis Confidence Level

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>non-brain diagnosis confidence level</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2a7ff937-287b-40a3-a1f6-ebf598683774</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Infant Medical History

### Birth Weight lbs

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>birth weight lbs</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>69d9a60d-32d5-4c3a-a26a-802d8f030c8d</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Birth Weight ozs

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>birth weight ozs</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b6f30050-f762-4427-8533-31738e737ea2</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Gestational Age Value Weeks

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>gestational age value weeks</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6d8a9b3f-792c-48c2-bd3c-56e52bb51672</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Gestational Age Value Days

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>gestational age value days</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4e532e52-6e4c-46cd-9fde-96f97ef3b034</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### APGAR 5 Minute Score Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>APGAR 5 minute score available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e67d93ac-3753-4835-a250-e2ca207b2675</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### APGAR 5 Minute Score

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>APGAR 5 minute score</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3a10dabf-39b0-4eb7-8399-85fd325c5646</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### APGAR 10 Minute Score Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>APGAR 10 minute score available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3d085ff9-7034-487d-a2b2-b9ae80d55333</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### APGAR 10 Minute Score

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>APGAR 10 minute score</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>numeric</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>09d512b6-7c20-4693-8894-77824ad7f04d</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Perinatal Neurologic Events

### Perinatal Neurologic Event Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>perinatal neurologic event type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cb4c7e3b-73fc-400e-a4c3-b149a5544363</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Perinatal Neurologic Event Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>perinatal neurologic event type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1bf1f9c5-79a6-4203-910f-cad79fe9cac9</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Family History

### Family History Availalble

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>family history available</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c88bf4dc-5a7c-4f70-a773-e6bbb5a12ec9</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1adef34c-bb96-4dd0-bc87-51868f2ddc3f</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
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
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>094064a1-362c-4b75-8556-6b874c843fdb</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Condition Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>condition type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>030c8275-04c0-4e4f-9f68-48fd0f559250</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Condition Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>condition type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a1ed23dc-3cd5-41c8-87f6-58604fc66a70</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Infectious Disease Testing

### Test Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>test name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b6865e15-7538-4890-be99-a6f9e9920af3</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Test Result

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>test result</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c14ea006-662c-4666-bfd1-6ff580c403ed</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>testing tissue source</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>42f8e11b-d9a3-48fe-ac1e-cd6f4469de46</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Toxicology Screening

### Drugs Found

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>drugs found</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e35b53f1-0daa-4b5b-9246-cfba52f61bfb</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Drugs Found Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>drugs found specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ec3f7c47-9062-4b66-ba80-a9355a388bc0</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Toxicology Result

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>toxicology result</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2cf1a1af-1ece-4ef7-b513-e4d1949f237c</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Toxicology Report Level

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>toxicology report level</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>594179b0-c744-40a4-958d-fc81461b4b74</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Toxicology Units

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>toxicology units</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6f124149-50de-489d-b9e2-f198b2b9857d</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Neuropathological Diagnoses

### Artifacts

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>artifacts</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b344b605-21dd-4e06-9104-21005179026f</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Artifacts Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>artifacts type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>dc217b9b-ed6b-48e2-93b4-4f648dc395f7</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Artifacts Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>artifacts type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ae11485d-dfc6-45fe-9d22-1d0bf7244d7c</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Developmental

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>developmental</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c259cdc2-7c68-48de-ab57-57328f3bddfa</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Developmental Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>developmental type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>bee7d477-2dec-4bf5-878e-a105a0054366</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Inflammatory

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>inflammatory</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>05e83583-078d-4a1e-892d-e6f611e5a0b8</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Inflammatory Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>inflammatory type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>616ba8d8-ced3-4f3e-b1ca-7103eb7a2c94</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Infectious

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>infectious</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>266f5fb8-716b-4472-be30-4a94b62f2245</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Infectious Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>infectious type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c73cea5e-44d1-4dd9-b55e-3c6ef5dd2ef2</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Traumatic

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>traumatic</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a00497c0-376f-4b2e-b60e-d6add2af41dc</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Traumatic Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>traumatic type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>01d2f488-f30b-40e0-913f-c9adc6b39b97</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Traumatic Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>traumatic type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>aa574a9a-a3d0-4a07-bf8b-9db4a1110a88</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Vascular

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>vascular</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b02d8386-d059-42a8-94cb-751d56b15b3a</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Vascular Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>vascular type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>5beafa90-ffdb-4cce-a78c-a3b3175210b6</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Vascular Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>vascular type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>543acbbb-9da4-4e24-a9d7-c0642aa33f32</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Neoplastic

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>neoplastic</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3f52a0e9-6469-46d3-8ed5-3cdb8afdc259</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Neoplastic Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>neoplastic type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a58be8f4-2756-4a66-9d05-1fbf44b4e810</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Neoplastic Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>neoplastic type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b9e8aead-fdf3-453e-a46b-fcb01d661f8f</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Aging

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>aging</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>40e3caa7-657b-4137-9879-07e6b29bae14</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Aging Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>aging type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>5e31b66f-131e-4d5e-8760-ddd85f5634d5</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Aging Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>aging type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>8667d972-175c-430a-ac5e-656563e75736</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Neurodegenerative

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>neurodegenerative</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>764d80ce-7a83-4e68-92df-34a416475e1b</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Neurodegenerative Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>neurodegenerative type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>exclusive categorical</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b150b62c-a968-4f5d-9aa3-d1ab5207ff83</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Neurodegenerative Type Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>neurodegenerative type specify</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td></td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d422d827-539f-4d10-b09d-0f4be00d7c91</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Appendix

## Changelog