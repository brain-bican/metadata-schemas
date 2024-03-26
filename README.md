# BICAN Metadata Schemas and Documentation
This is the BICAN metadata curation and schemas repository. This repository contains files, documents, and code essential for BICAN metadata curation. 

## Table of Contents
- [Documentation](#documentation)
- [Schemas](#schemas)
- [How to Contribute](#how-to-contribute)
- [Terminology](#terminology)
- [Status Board](#status-board)

## Documentation

Documentation that supports development, implementation, standarization, and description of BICAN metadata can be found in the `docs/` directory. 

## Schemas

Metadata schemas are located in the `schemas/` directory. Each metadata schema is accompanied by a README document that contains descriptive information about that schema. 

Each metadata schema is reviewed and standardized by the BICAN Metadata and Ontologies Integration Working Group (MOWG). Documentation of this process can be found [here](https://docs.google.com/document/d/10lg33rJhbDSwp1VfGlcr_PQ1Fpfb0i-Rkh5g7imMpNY/edit?usp=sharing).

## How to Contribute

The BICAN Metadata and Ontologies Working Group supports community input and collaboration in developing, maintaining, and updating metadata schemas and documents. You (as a member of MOWG or not) are welcome to suggest updates or additions to the BICAN metadata standards by [creating GitHub issues](https://github.com/brain-bican/metadata-schemas/issues/new) or emailing [data.curation@alleninstitute.org](data.curation@alleninstitute.org).

## Terminology

Metadata

**Metadata** is the human and machine-readable descriptive information about a data resource that is necessary for tracking and using the data it describes. In the context of BICAN, metadata is descriptive information that is necessary for understanding the data produced in BICAN. This information is provided in a structure defined by the schema.
 
A **schema** is a human and machine-readable file-based specification for metadata. A specification defines the metadata structure and fields, including field name, description, format, and cardinality.
 
An **owner** of a schema is the person or group of persons that assume responsibility for its creation, documentation, and movement through the metadata approval process.

**Contributors** are any members of the BICAN or scientific community who suggest, contribute, or review updates to the metadata schemas.

**Submitters** are any members of the BICAN or scientific community who submit data or metadata.

**Committers** are any members of the BICAN Metadata and Ontologies WG with commit privileges to the metadata-schemas GitHub repo.

A BICAN metadata schema has the status of **submitted** if and only if it has been uploaded as an attachment to an issue ticket on the brain-bican/metadata issue tracker. 

A BICAN metadata schema has the status of **under MOWG review** if and only if it has the status of submitted and the MOWG (or representative member thereof) has acknowledged its receipt and has assigned MOWG reviewers to the schema.

A BICAN metadata schema has the status of **under revision by owner** if and only if it has the status of under MOWG review and the owner has received recommended changes from MOWG reviewers.

A BICAN metadata schema has the status of **accepted by MOWG** if and only if it has been under MOWG review and MOWG has deemed there are no outstanding necessary changes to the schema.

A BICAN metadata schema has the status of **submitted to BICAN data ecosystem** if and only if it has been accepted by MOWG and the owner of the schema has requested review by the BICAN Data Ecosystem WG.

A BICAN metadata schema has the status of **accepted by BICAN data ecosystem** if and only if it has been submitted to the BICAN data ecosystem and received approval from the BICAN data ecosystem WG.

A BICAN metadata schema has the status of **endorsed BICAN standard** if and only if it has been accepted by BICAN Data Ecosystem, and successfully completed the BICAN data standards process.

## Status Board

Here are the BICAN metadata schemas and their statuses.

| Schema | Version | Release | Status |
|:--|:--|:--|:--|
| [Donor-to-Alignment Metadata] | [v1.0.0] |  [2023-03-31] | Accepted by MOWG |
| [Human Donor Metadata] | [v1.0.0] | [2023-04-01] | Endorsed BICAN Standard |
| [Projects and Data Collections Metadata] | [v1.0.0] | [2023-09-27] | Under MOWG Review |
| [Library Minimal Metadata] | [v1.1.0] | [2024-03-22] | Endorsed BICAN Standard |
| | | | |

[Donor-to-Alignment Metadata]: docs/schemas/Donor-to-Alignment-Metadata
[v1.0.0]: docs/schemas/Donor-to-Alignment-Metadata/Donor-to-Alignment-Metadata-README.md

[Human Donor Metadata]: http://github.com/brain-bican/metadata-schemas/docs/schemas/Human-Donor-Metadata
[v1.0.0]: docs/schemas/Human-Donor-Metadata/BICAN-Human-Donor-Metadata-Schema-README.md

[Projects and Data Collection Metadata]: http://github.com/brain-bican/metadata-schemas/docs/schemas/project-registration-bican
[v1.0.0]: docs/schemas/project-registration-bican/README.md

[Library Minimal Metadata]: docs/schemas/Library-Minimal-Metadata
[v1.1.0]: docs/schemas/Library-Minimal-Metadata/Library-Minimal-Metadata-README.md
