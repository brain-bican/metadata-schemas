# Donor Metadata Schema

Document Status: _Approved by MOWG_

Version: 1.0

Owner: @memartone

Reviewers: @patrick-lloyd-ray, @carolth, @rightbower

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: DD-MM-YYYY

## Overview

The BICAN Donor Metadata schema specifies the metadata relating to donors in BICAN. These metadata reflect the metadata needed to accurately track donors and related entities from the brain banks through the specimen portal. As such, it is a collaborative schema that reflects the joint efforts of members of BICAN. 

Note that there are additional fields in the metadata schema which are not explicitly required at time of creation, but will be populated when relevant resources are created/updated. 

This document has the following sections:

* [General Requirements](#general-requirements)
* [General Subject Fields](#general-subject-fields), which describes...
* [General Specimen Data](#general-specimen-metadata), which describes metadata...
* [Non-Brain Specimen Collected](#non-brain-specimen-collected), which describes metadata...
* [Diagnoses](#diagnoses), which describes metadata...
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



## Non-Brain Specimen Collected

## Diagnoses

## Infant Medical History

## Perinatal Neurologic Events

## Family History

## Infectious Disease Testing

## Toxicology Screening

## Neuropathological Diagnoses



## Appendix

## Changelog