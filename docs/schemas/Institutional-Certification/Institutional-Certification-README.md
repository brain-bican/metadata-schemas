# BICAN Institutional Certification Metadata Schema

Document Status: _Under Review by MOWG_

Version: 1.0

Owner: @lydiang

Reviewers: @patrick-lloyd-ray, @rightbower, @carolth

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 14-02-2025

## Background

The Brain Research Through Advancing Innovative Neurotechnologies® (BRAIN) Initiative Cell Atlas Network (BICAN) aims to transform our understanding of brain cell types and the precise tools needed to access them, bringing us one step closer to unraveling the complex workings of the human brain.

Building on findings from the BRAIN Initiative Cell Census Network (BICCN), BICAN takes the next step in mapping brain cells and circuits across multiple species, with an emphasis on humans. The aim of BICAN is to generate a complete reference atlas of cell types in the human brain across the lifespan, which can be shared and used throughout the research community. In addition to developing a “parts list” detailing the vast array of neurons and non-neuronal cells in the human brain, the project also aims to map cell interactions that underlie a wide range of brain disorders.

To this end, BICAN aims to support the publication, sharing, and exploration of datasets generated in the course of the project. Creating a complete reference atlas from multiple datasets requires vast harmonization of metadata. In order to facilitate the harmonization of metadata, we require datasets include a small set of metadata available from data submitters.

This document describes a schema, a type of contract, that BICAN requires of all donor to alignment datasets to enable searching, filtering, and integration of datasets.

Note that the requirements in the schema are just the minimum required information. Datasets often have additional metadata, which is preserved in datasets submitted to the data archives.

## Overview

The BICAN Institutional Certification Metadata schema describes metadata associated with and produced from institutional certification forms and data in BICAN.

This document has the following sections:

- [BICAN Institutional Certification Metadata Schema](#bican-institutional-certification-metadata-schema)
  - [Background](#background)
  - [Overview](#overview)
  - [General Requirements](#general-requirements)
  - [Certification](#certification)
    - [IC Form Local Name](#ic-form-local-name)
    - [IC Form Effective Date](#ic-form-effective-date)
    - [Project Identifier](#project-identifier)
  - [Donor Certification](#donor-certification)
    - [Donor Local Name](#donor-local-name)
    - [IC Form Local Name](#ic-form-local-name-1)
    - [Cohort Tag](#cohort-tag)
  - [IC Donor Data Use Limitation](#ic-donor-data-use-limitation)
    - [Donor Local Name](#donor-local-name-1)
    - [Access Level](#access-level)
    - [Data Use Limitation](#data-use-limitation)
    - [Disease Specification](#disease-specification)
    - [IRB Approval Required](#irb-approval-required)
    - [Publication Required](#publication-required)
    - [Collaboration Required](#collaboration-required)
    - [Not for Profit Use Only](#not-for-profit-use-only)
    - [Methods](#methods)
    - [Genetic Study Only](#genetic-study-only)
  - [Changelog](#changelog)

## General Requirements

The BICAN Institutional Certification Metadata is intended to be used by data submitters to provide information about institutional certification forms and data.

The schema is designed to be flexible and extensible, allowing for the addition of new fields as needed. The schema is also designed to be compatible with existing metadata standards.

## Certification

The BICAN Institutional Certification Metadata schema includes fields for certification information, including the institution name, certification date, and certification type. The schema also includes fields for the certification form and data.

### IC Form Local Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>ic_form_local_name</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>donor local name</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### IC Form Effective Date

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>ic_form_effective_date</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6c0696fc-e6ec-45d2-9440-e61463228936</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>donor effective date</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The date when the institutional certification form becomes effective.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>datetime</td>
    </tr>
</tbody></table>
<br>

### Project Identifier

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>project_identifier</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c1d2e3f4-5678-90ab-cdef-1234567890ab</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>project id</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>abd4e1df-9c8e-4560-9077-ace8358b26de</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

## Donor Certification

The BICAN Institutional Certification Metadata schema includes fields for donor certification information, including the donor name, institutional certification name, and cohort tag.

### Donor Local Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>donor_local_name</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>donor local name</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### IC Form Local Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>ic_form_local_name</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a220b50e-7691-4385-ba35-90ce760be3c3</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The name of IC form as it is used by a local entity.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Cohort Tag

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cohort_tag</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>783ec297-f361-4a23-b78d-801bdb1e3fd3</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>cohort tag</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A data item that indicates a cohort grouping.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

## IC Donor Data Use Limitation

The BICAN Institutional Certification Metadata schema includes fields for donor data use limitation information, including access level, data use limitation, disease specification and IRB approval fields.

### Donor Local Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>donor_local_name</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>donor local name</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Access Level

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>access_level</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>9f800e73-0d96-45cf-8e92-303e22e80aaf</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>access level</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A data item that is used to indicate the level of access of a dataset (unrestricted or controlled).</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>categorical, enum</td>
    </tr>
</tbody></table>
<br>

### Data Use Limitation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>data_use_limitation</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>5a122436-5768-47eb-b028-6e2f6b5f1245</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>data use limitation</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A data item that is used to indicate consent permissions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be removed, stored or used.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>categorical, enum</td>
    </tr>
</tbody></table>
<br>

### Disease Specification

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>disease_specification</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f76579b7-35b8-415f-ad2b-414f9ad555ac</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>disease specification</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The dataset can be used only for research on a specific disease or related condition.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>categorical, enum</td>
    </tr>
</tbody></table>
<br>

### IRB Approval Required

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>irb_approval_required</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c1d2e3f4-5678-90ab-cdef-1234567890ab</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>irb approval required</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A data item that indicates whether IRB approval is required for the use of the dataset.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>boolean</td>
    </tr>
</tbody></table>
<br>

### Publication Required

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>publication_required</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>432f1e56-7e1f-433d-aca4-5ac20afb4638</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>publication required</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A data item that is used to indicate whether or not a publication is required -- i.e., whether the requestor must share their results with the larger scientific community.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>boolean</td>
    </tr>
</tbody></table>
<br>

### Collaboration Required

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>collaboration_required</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>39ab79f3-6c21-423f-9670-4c5a4e9035ed</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>collaboration required</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A data item that is used to indicate whether or not collaboration is required -- i.e., whether the requestor must privide a letter of collaboration with the primary study investigators.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>boolean</td>
    </tr>
</tbody></table>
<br>

### Not for Profit Use Only

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>not_for_profit_use_only</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>dc4e4bf5-a221-4989-af64-b2f21b0c1dd8</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>not for profit use only</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A data item that indicates whether or not the dataset can be used for non-profit purposes only.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>boolean</td>
    </tr>
</tbody></table>
<br>

### Methods

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>methods</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c5dfba12-4c1c-451e-b516-df95d5c9efd6</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>methods</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The dataset can be used for methods research and development (e.g., development of statistical software or algorithms).</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>boolean</td>
    </tr>
</tbody></table>
<br>

### Genetic Study Only

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>genetic_study_only</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0b3acf53-2643-46aa-9f45-f1ad9ecc9564</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td>genetic study only</td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>A data item that indicates whether or not the dataset can be used for genetic studies only.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>boolean</td>
    </tr>
</tbody></table>
<br>

## Changelog
- **14-02-2025**: Initial version created
- **15-02-2025**: Added additional fields for donor data use limitation