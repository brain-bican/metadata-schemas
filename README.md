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

## How to Contribute

The BICAN Metadata and Ontologies Working Group supports community input and collaboration in developing, maintaining, and updating metadata schemas and documents. You (as a member of MOWG or not) are welcome to suggest updates or additions to the BICAN metadata standards by [creating GitHub issues](https://github.com/brain-bican/metadata-schemas/issues/new) or emailing [data.curation@alleninstitute.org](data.curation@alleninstitute.org).

## Terminology

**Metadata** is the human and machine-readable descriptive information about a data resource that is necessary for tracking and using the data it describes. In the context of BICAN, metadata is descriptive information that is necessary for understanding the data produced in BICAN. This information is provided in a structure defined by the schema.

**Schemas** are a human and machine-readable file-based specification for metadata. A specification defines the metadata structure and fields, including field name, description, format, and cardinality.

**Owner** of a schema is the person or group of persons that assume responsibility for its creation, documentation, and movement through the metadata approval process.

**Contributors** are any members of the BICAN or scientific community who suggest, contribute, or review updates to the metadata schemas.

**Submitters** are any members of the BICAN or scientific community who submit data or metadata.

**Committers** are any members of the BICAN Metadata and Ontologies WG with commit privileges to the metadata-schemas GitHub repo.

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
