# Taxonomy Tooling Metadata Schema

Document Status: _Under MOWG Review_

Version: 1.0

Owner: @UCDNJJ, @jeremymiller

Reviewers: @patrick-lloyd-ray, @carolth, @djarecka, @memartone

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 10-03-2025

## Overview

The BICAN Taxonomy Tooling Metadata schema specifies the metadata relating to taxonomy tooling that can be taken from a variety of sources in BICAN. These metadata reflect the metadata needed to accurately track taxonomy tooling metadata in BICAN. As such, it is a collaborative schema that reflects the joint efforts of members of BICAN.

This document has the following sections:

- [Taxonomy Tooling Metadata Schema](#taxonomy-tooling-metadata-schema)
  - [Overview](#overview)
  - [General Requirements](#general-requirements)
  - [obs](#obs)
    - [Cell Label](#cell-label)
    - [Parent Cell Set Accession](#parent-cell-set-accession)
  - [uns](#uns)
    - [Schema Version](#schema-version)
    - [\[...\] Color](#-color)
    - [Cell Annotation Schema Version](#cell-annotation-schema-version)
    - [Cell Annotation Timestamp](#cell-annotation-timestamp)
    - [Cell Annotation Version](#cell-annotation-version)
    - [Dataset URL](#dataset-url)
    - [Matrix File ID](#matrix-file-id)
    - [Author List](#author-list)
    - [Additional Information](#additional-information)
  - [Changelog](#changelog)

## General Requirements

This includes any fields required for specific tools (e.g., cellxgene, TDT, CAS, CAP) that are not strictly part of the taxonomy and that do not fit in any of the above categories. This includes things like schema versions and redundent fields from above with different column names. These may not need to match between schemas (or even be encoded into schemas).

## obs

The obs component contains cell level metadata, as above.

### Cell Label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_label</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Identifier corresponding to each individual cell.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Parent Cell Set Accession

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cellannotation_set</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Identifier corresponding to the parent cell_set. If not needed for annotations, definitely needed for tooling.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

## uns

The uns component contains taxonomy associated files useful for reproducing analysis or mapping against the taxonomy.

### Schema Version
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>schema_version</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Cellxgene schema version (e.g., "3.0.0")</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### [...] Color

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>[...]_color</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>RGB color vector for metadata [...]; required only for selecting colors in cirrocumulus. This may be the same as the [COLUMN_NAME]_color column above.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>array of integers</td>
    </tr>
</tbody></table>
<br>

### Cell Annotation Schema Version

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cellannotation_schema_version</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>CAS schema version '[MAJOR].[MINOR].[PATCH]'</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Cell Annotation Timestamp

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cellannotation_timestamp</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Timestamp when published: %yyyy-%mm-%dd %hh:%mm:%ss; Useful in general, even though currently only required by CAP; also publication_XXXX (unclear how different); This also could be the same as development_date above.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Cell Annotation Version

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cellannotation_version</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>CAP taxonomy annotation version; required by CAP; also publication_XXXX (unclear how different). I'm also not sure how this differs from the cellannotation_schema_version.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Dataset URL

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dataset_url</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>File location, as defined above.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Matrix File ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>matrix_file_id</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>File location, as defined above.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

### Author List

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>author_list</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>List of taxonomy authors; see above.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>array of strings</td>
    </tr>
</tbody></table>
<br>

### Additional Information

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>[additional information]</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Placeholder for several other (seemingly redundant) fields required by external tools (e.g., CAP, cellxgene) that I want to capture here. It may or may not make sense to spell them all out.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

## Changelog
- **10-03-2025**: Initial version created.
- **10-04-2025**: Added additional fields and clarified definitions.
- **10-05-2025**: Added UUIDs and clarified definitions.
