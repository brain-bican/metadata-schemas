# Calculated Metadata Schema

Document Status: _Under MOWG Review_

Version: 1.0

Owner: @UCDNJJ, @jeremymiller

Reviewers: @patrick-lloyd-ray, @carolth, @djarecka, @memartone

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 10-03-2025

## Overview

The BICAN Taxonomy Calculated Metadata schema specifies the metadata relating to taxonomy metadata that can be taken from a variety of sources in BICAN. These metadata reflect the metadata needed to accurately track taxonomy metadata in BICAN. As such, it is a collaborative schema that reflects the joint efforts of members of BICAN.

This document has the following sections:

* [General Requirements](#general-requirements)
* [obs](#obs)
* [uns](#uns)
* [changelog](#changelog)

## General Requirements

This includes any cell-level or cluster-level metadata that can be calculated explicitly from the Data and Assigned Metadata without the need for human intervention. Some examples include # reads detected/cell, # UMI/cell, fraction of cells per cluster derived from each anatomic dissections, expressed neurotransmitter genes (quantitatively defined), average QUANTITATIVE_VALUE (e.g., doublet score) per cluster. Currently none of these are required for the schema, but they are sometimes used for annotation.

### obs

The obs component contains cell level metadata from the experiment

#### Cell Label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_id</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>34ca0703-429f-4920-8a08-dd4c61b29444</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Identifier corresponding to each individual cell. Included in the data and in every other location to refer to the data (e.g., metadata and annotations). In AnnData files, the ID corresponding to each individual cell is stored in the obs index.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Feature Matrix Label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>feature_matrix_label</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2c860046-83d5-47f9-98d5-29ce81446819</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Identifier corresponding to the feature matrix. Included in the data and in every other location to refer to the data (e.g., metadata and annotations). In AnnData files, the ID corresponding to each individual cell is stored in the obs index.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Dataset Label

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dataset_label</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>519ecc82-e397-4b1e-a846-d27d48610ff3</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Identifier corresponding to the dataset. Included in the data and in every other location to refer to the data (e.g., metadata and annotations). In AnnData files, the ID corresponding to each individual cell is stored in the obs index.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Color Vector

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>[COLUMN_NAME]_color</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0ab06f78-6df2-4555-8990-3eec36b2adbb</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Color associated with the cell. Included in the data and in every other location to refer to the data (e.g., metadata and annotations). In AnnData files, the ID corresponding to each individual cell is stored in the obs index.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### ID Vector

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>[COLUMN_NAME]_id</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>701b32ca-4d95-47c5-8213-e7ab8c5373eb</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The order of metadata values (e.g., the levels of a factor, or ascending order of a numeric). Likely should use “rank” or “order” rather than “id”, since these are not identifiers..</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Additional Uncontrolled Metadata

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>[additional uncontrolled metadata]</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>d417074d-5f7a-4bb8-8a7f-11e20fdcca97</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Additional uncontrolled cell metadata. These are not required, but any additional columns are allowed by all h5ad formats.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Calculated Metadata Metadata

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>calculated_metadata_metadata</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>daf95e1a-37c5-4edf-889b-3f552b13e09c</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>TBD information about the calculated_metadata itself. This likely is not needed or should be renamed.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

#### Cell Annotation Schema

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cell_annotation_schema</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6a32b2d5-22d2-457d-b43e-c53cf96729bd</td>
    </tr>
    <tr>
      <th>Aliases</th>
      <td></td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>extended metadata about annotations and labelsets stores in JSON.</td>
    </tr>
    <tr>
      <th>Data Type</th>
      <td>string</td>
    </tr>
</tbody></table>
<br>

## Changelog
| Date       | Version | Description                                                                 |
|------------|---------|-----------------------------------------------------------------------------|