# Project registration

The CSVs in `/project-registration-bican` specify the minimum metadata required to register
a project and data collection with BCDC. These minimum metadata reflect an update to the
project inventory schema to support more granular attribution and data management. Note that there
are additional fields in the project schema which are not explicitly required at time of creation,
but will be populated when relevant resources are created/updated (e.g. data collection -> project
relations, web resource links, timestamps etc.)

- Project-metadata.csv: metadata for a project
- DataCollection-metadata.csv: metadata for a data collection
- Organization-metadata.csv: metadata for an organization
    - Primarily used in reference to a project creator or funding source/awardee
- Person-metadata.csv: metadata for a person
    - Primarily used in reference to a project creator or contributor


The CSVs in `/project-registration-bican/controlled-vocabularies` contain the controlled 
vocabularies used to validate the input in the metadata fields.