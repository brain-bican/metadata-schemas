# Project registration

The CSVs in `/project-registration-biccn` specify the minimum metadata required to register
a project and data collection with BCDC in BICCN. These are legacy specs, but the new proposed
schema and the legacy schema are highly similar.

- Project-metadata.csv: metadata for a project
- DataCollection-metadata.csv: metadata for a data collection
- Organization-metadata.csv: metadata for an organization
    - Primarily used in reference to a project creator or funding source/awardee
- Person-metadata.csv: metadata for a person
    - Primarily used in reference to a project creator or contributor

The CSVs in `/project-registration-biccn/controlled-vocabularies` contain the controlled 
vocabularies used to validate the input in the metadata fields.