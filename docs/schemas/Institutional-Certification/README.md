# BICAN Institutional Certification Metadata Schema

Document Status: _Approved BICAN Standard_

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
    - [IC Form Local Name (donor certification)](#ic-form-local-name-donor-certification)
    - [Cohort Tag](#cohort-tag)
  - [IC Donor Data Use Limitation](#ic-donor-data-use-limitation)
    - [Donor Local Name (data use limitation)](#donor-local-name-data-use-limitation)
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
    - [August 7, 2025 -- Version 1.0.0](#august-7-2025----version-100)
    - [February 2025 (pre-release)](#february-2025-pre-release)

## General Requirements

The BICAN Institutional Certification Metadata is intended to be used by data submitters to provide information about institutional certification forms and data.

The schema is designed to be flexible and extensible, allowing for the addition of new fields as needed. The schema is also designed to be compatible with existing metadata standards.

## Certification

The BICAN Institutional Certification Metadata schema includes fields for certification information, including the institution name, certification date, and certification type. The schema also includes fields for the certification form and data.

### IC Form Local Name

| BICAN Field Name | ic_form_local_name |
|------------------|--------------------|
| BICAN UUID       | f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf |
| Aliases          | donor local name |
| Definition       | An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry. |
| Data Type        | string |

### IC Form Effective Date

| BICAN Field Name | ic_form_effective_date |
|------------------|------------------------|
| BICAN UUID       | 6c0696fc-e6ec-45d2-9440-e61463228936 |
| Aliases          | donor effective date |
| Definition       | The date when the institutional certification form becomes effective. |
| Data Type        | datetime |

### Project Identifier

| BICAN Field Name | project_identifier |
|------------------|--------------------|
| BICAN UUID       | c1d2e3f4-5678-90ab-cdef-1234567890ab |
| Aliases          | project id |
| Definition       | A unique identifier for the project associated with the institutional certification form. |
| Data Type        | string |

## Donor Certification

The BICAN Institutional Certification Metadata schema includes fields for donor certification information, including the donor name, institutional certification name, and cohort tag.

### Donor Local Name

| BICAN Field Name | donor_local_name |
|------------------|------------------|
| BICAN UUID       | f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf |
| Aliases          | donor local name |
| Definition       | An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry. |
| Data Type        | string |

### IC Form Local Name (donor certification)

| BICAN Field Name | ic_form_local_name |
|------------------|--------------------|
| BICAN UUID       | a220b50e-7691-4385-ba35-90ce760be3c3 |
| Aliases          | |
| Definition       | The name of IC form as it is used by a local entity. |
| Data Type        | string |

### Cohort Tag

| BICAN Field Name | cohort_tag |
|------------------|------------|
| BICAN UUID       | 783ec297-f361-4a23-b78d-801bdb1e3fd3 |
| Aliases          | cohort tag |
| Definition       | A data item that indicates a cohort grouping. |
| Data Type        | string |

## IC Donor Data Use Limitation

The BICAN Institutional Certification Metadata schema includes fields for donor data use limitation information, including access level, data use limitation, disease specification and IRB approval fields.

### Donor Local Name (data use limitation)

| BICAN Field Name | donor_local_name |
|------------------|------------------|
| BICAN UUID       | f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf |
| Aliases          | donor local name |
| Definition       | An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry. |
| Data Type        | string |

### Access Level

| BICAN Field Name | access_level |
|------------------|--------------|
| BICAN UUID       | 9f800e73-0d96-45cf-8e92-303e22e80aaf |
| Aliases          | access level |
| Definition       | A data item that is used to indicate the level of access of a dataset (unrestricted or controlled). |
| Data Type        | categorical, enum |

### Data Use Limitation

| BICAN Field Name | data_use_limitation |
|------------------|---------------------|
| BICAN UUID       | 5a122436-5768-47eb-b028-6e2f6b5f1245 |
| Aliases          | data use limitation |
| Definition       | A data item that is used to indicate consent permissions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be removed, stored or used. |
| Data Type        | categorical, enum |

### Disease Specification

| BICAN Field Name | disease_specification |
|------------------|----------------------|
| BICAN UUID       | f76579b7-35b8-415f-ad2b-414f9ad555ac |
| Aliases          | disease specification |
| Definition       | The dataset can be used only for research on a specific disease or related condition. |
| Data Type        | categorical, enum |

### IRB Approval Required

| BICAN Field Name | irb_approval_required |
|------------------|-----------------------|
| BICAN UUID       | c1d2e3f4-5678-90ab-cdef-1234567890ab |
| Aliases          | irb approval required |
| Definition       | A data item that indicates whether IRB approval is required for the use of the dataset. |
| Data Type        | boolean |

### Publication Required

| BICAN Field Name | publication_required |
|------------------|----------------------|
| BICAN UUID       | 432f1e56-7e1f-433d-aca4-5ac20afb4638 |
| Aliases          | publication required |
| Definition       | A data item that is used to indicate whether or not a publication is required -- i.e., whether the requestor must share their results with the larger scientific community. |
| Data Type        | boolean |

### Collaboration Required

| BICAN Field Name | collaboration_required |
|------------------|------------------------|
| BICAN UUID       | 39ab79f3-6c21-423f-9670-4c5a4e9035ed |
| Aliases          | collaboration required |
| Definition       | A data item that is used to indicate whether or not collaboration is required -- i.e., whether the requestor must provide a letter of collaboration with the primary study investigators. |
| Data Type        | boolean |

### Not for Profit Use Only

| BICAN Field Name | not_for_profit_use_only |
|------------------|-------------------------|
| BICAN UUID       | dc4e4bf5-a221-4989-af64-b2f21b0c1dd8 |
| Aliases          | not for profit use only |
| Definition       | A data item that indicates whether or not the dataset can be used for non-profit purposes only. |
| Data Type        | boolean |

### Methods

| BICAN Field Name | methods |
|------------------|---------|
| BICAN UUID       | c5dfba12-4c1c-451e-b516-df95d5c9efd6 |
| Aliases          | methods |
| Definition       | The dataset can be used for methods research and development (e.g., development of statistical software or algorithms). |
| Data Type        | boolean |

### Genetic Study Only

| BICAN Field Name | genetic_study_only |
|------------------|--------------------|
| BICAN UUID       | 0b3acf53-2643-46aa-9f45-f1ad9ecc9564 |
| Aliases          | genetic study only |
| Definition       | A data item that indicates whether or not the dataset can be used for genetic studies only. |
| Data Type        | boolean |

## Changelog

### August 7, 2025 -- Version 1.0.0

- **07-08-2025**: Approved BICAN Standard version 1.0.0

### February 2025 (pre-release)

- **14-02-2025**: Initial version created
- **15-02-2025**: Added additional fields for donor data use limitation
  