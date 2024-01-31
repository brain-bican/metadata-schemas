# Projects and Data Collections Metadata Schema

Document Status: _Under MOWG Review_

Version: 1.0

Owner: @pbishwakarma

Reviewers: @patrick-lloyd-ray, @carolth, @mgiglio99, @nsuvarnaiari

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: DD-MM-YYYY

## Overview

The BICAN Projects and Data Collections Metadata schema specifies the minimum metadata required to register a project and data collection with BCDC. These minimum metadata reflect an update to the project inventory schema to support more granular attribution and data management. 

Note that there are additional fields in the project schema which are not explicitly required at time of creation, but will be populated when relevant resources are created/updated (e.g. data collection -> project relations, web resource links, timestamps etc.)

This document has the following sections:

* [General Requirements](#general-requirements)
* [Project Metadata](#project-metadata), which describes metadata for a project.
* [Data Collection Metadata](#data-collection-metadata), which describes metadata for a data collection.
* [Organization Metadata](#organization-metadata), which describes metadata for an organization. This is primarily used in reference to a project creator or funding source/awardee.
* [Person Metadata](#person-metadata), which describes metadata for a person. This is primarily used in reference to a project creator or contributor.
* [Project Registration Controlled Vocabularies](#controlled-vocabularies), which describes the controlled values used to validate the input in the metadata fields.
* [Appendix](#appendix)
## General Requirements

## Data Collection Metadata

The data in Data Collection Metadata is the metadata essential for registering, tracking, and storing data collections. 

The following table describes the Data Collection Metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond ones listed. 
### data collection name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>data collection name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A human-readable, locally unique label that identifies a data collection.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f7b04e21-c12d-4b3d-ba0e-b1de6ac92dca</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### data collection long form title

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>data collection long form title</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A long form title of a data collection.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>62208817-6a7f-4e70-9c4a-d262f43d82cc</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### data collection short form title

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>data collection short form title</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A short form title of a data collection (fewer than 30 characters).</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f5169355-52cf-4720-904f-946c92489faa</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### data collection description

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>data collection description</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A description of a data collection that includes a specification of the license of the data collection.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c5188587-2b4f-4889-ae93-224efdb803d2</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### data collection archive

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>data collection archive</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The location (archive) at which the data in a data collection is to be deposited. </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>39498a35-3cb5-46ce-9e23-dc5e499b85c4</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td>[Archive CV]</td>
    </tr>
</tbody></table>
<br>

### data collection species

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>data collection species</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The common name of the species of the donor from which data were collected for this data collection.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7135fb76-5423-44da-ba52-4c33e8626033</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td>[Species CV](/docs/schemas/project-registration-bican/controlled-vocabularies/species-cv.csv)</td>
    </tr>
</tbody></table>
<br>

### data collection access control

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>data collection access control</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The level of access specified for a data collection.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3880e926-d2fb-4960-bf61-4b5789e6c027</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td>[Access Control CV](/docs/schemas/project-registration-bican/controlled-vocabularies/accessControl-cv.csv)</td>
    </tr>
</tbody></table>
<br>

### data collection access control code

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>data collection access control code</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The code that denotes the access restrictions specified for a data collection.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>1ff82abd-7ada-48f0-b235-6aa1b7c36f6b</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td>[Access Control Code CV]</td>
    </tr>
</tbody></table>
<br>

### data collection access control description

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>data collection access control description</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A free text description of the access restrictions specified for a data collection.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>85b8be40-51e1-4357-af33-fa95fe7d7d68</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### data collection completion state

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>data collection completion state</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A value that specifies whether or not additional data is being generated for a data collection.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>456513f2-0af8-45e1-b8f0-338636ed3f61</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td>[Completion State CV](/docs/schemas/project-registration-bican/controlled-vocabularies/completionState-cv.csv)</td>
    </tr>
</tbody></table>
<br>

### data collection modality

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>data collection modality</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The modality of the data in a data collection.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>480af9eb-0128-4602-9c8f-01416820cee3</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td>[Modality CV](/docs/schemas/project-registration-bican/controlled-vocabularies/modality-cv.csv)</td>
    </tr>
</tbody></table>
<br>

### data collection technique

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>data collection technique</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The technique that was used to acquire the data in a collection.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>bee3bda8-c103-448f-8557-effcaca176bf</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td>[Technique CV](/docs/schemas/project-registration-bican/controlled-vocbularies/technique-cv.csv)</td>
    </tr>
</tbody></table>
<br>

### data collection license

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>data collection license</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A license that is applied to the data in a data collection. </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b184e037-1b45-4ca6-8651-7044b1a74199</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td>[License CV](/docs/schemas/project-registration-bican/controlled-vocabularies/license-cv.csv)</td>
    </tr>
</tbody></table>
<br>

### data collection web resource

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>data collection web resource</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A URL or weblink that provides the location of relevant tools or pages to a data collection.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ebdc27a1-37ca-46ec-8914-6d3fae85a3d9</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### data collection citation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>data collection web citation</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A data citation for a data collection.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>ea4729c6-df21-40db-8141-5af1d44ba75c</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Organization Metadata

The data in Organization Metadata is the metadata essential for registering, tracking, and storing organizational data. 

The following table describes the Organization Metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond ones listed.

### organization name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>organization name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A human-readable, locally unique label that identifies a organization. </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3788d44f-8383-4707-845d-bb8289815b32</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### organization Research Organization Registry ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>organization Research Organization Registry ID</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A Research Organization Registry ID that identifies an organization.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3fd3913c-0e36-4fe0-ac99-073f496c0919</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Person Metadata

The data in Person Metadata is the metadata essential for registering, tracking, and storing data about persons. 

The following table describes the Person Metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond ones listed.
### person name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>person name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A full name of a person in [given name],[family name] format.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>da5203bf-0202-4cd0-b0c2-5cc05806e2e4</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### person given name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>person given name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A given name of a person.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2354176f-40f2-4110-98d9-0c203314bfde</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### person family name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>person family name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A family name of a person.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f5d8f1a3-ce30-45eb-ac26-13a8998c2f5a</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### person ORCID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>person ORCID</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>An ORCID that identifies a person.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e834467e-a05e-4b9f-8348-5c0079bdaac8</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Project Metadata

The data in Person Metadata is the metadata essential for registering, tracking, and storing data about persons. 

The following table describes the Person Metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond ones listed.

### project name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>project name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A human readable, locally unique identifier that denotes a project.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a0d7797f-aaf1-4d3e-8289-51a94237b9c8</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### project title

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>project title</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A long form project title.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>34e55bb4-17db-4b7f-bd7d-7272ffe1c9f2</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### project short title

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>project short title</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A short form project title.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>216cc403-423a-4b43-b935-b9b61dbb8a26</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### project description

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>project description</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A long form project description. </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c51e8c8d-d62b-4b79-843b-a3a6810fe709</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### project subprogram

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>project subprogram</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A subprogram to which a project belongs.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cfd9d928-673a-428a-b5f0-c04e2fdd8ec9</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td>[Subprogram CV](/docs/schemas/project-registration-bican/controlled-vocabularies/subprogram-cv.csv</td>
    </tr>
</tbody></table>
<br>

### project contact

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>project contact</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A primary contact for a project. This is typically a person but can also be an institution.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>62381d66-c414-4fe9-8b07-0a00ee855e71</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### project creator

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>project creator</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A creator of a project. This is either a person or institution.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>34c891d4-d721-4023-bbf9-06b84f6a93cc</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### project contributor

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>project contributor</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A contributor to a project. This is often given as a list.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>8a1a747c-c24d-451a-9168-ed14d274a97c</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### project funding source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>project funding source</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The funding source for a project.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3f85bc4b-2e03-426e-b376-4607fc9515e3</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td>[Grant CV](/docs/schemas/project-registration-bican/controlled-vocabularies/grant-cv.csv)</td>
    </tr>
</tbody></table>
<br>

### project collections

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>project collections</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The data collections that are part of a project.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>66093eb6-fdaf-4782-8dba-23f6575254d8</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td>[Data Collection CV]</td>
    </tr>
</tbody></table>
<br>

### project highlighted web resource

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>project highlighted web resource</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A link to relevant tools/pages of a project.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2bb2472b-73b7-426b-adb2-739924a0751b</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### project protocol

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>project protocol</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A protocol for a project.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3e80809a-de1a-4333-98a9-f19549fda246</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### project publication

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>project publication</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>string</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A publication associated with a project.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>52d1b518-37e0-4b69-b1d8-36d1ff437376</td>
    </tr>    
    <tr>
      <th>Permissible Values</th>
      <td></td>
    </tr>
</tbody></table>
<br>
 
## Controlled Vocabularies

## Appendix