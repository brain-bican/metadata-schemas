Tooling
This includes any fields required for specific tools (e.g., cellxgene, TDT, CAS, CAP) that are not strictly part of the taxonomy and that do not fit in any of the above categories. This includes things like schema versions and redundent fields from above with different column names. These may not need to match between schemas (or even be encoded into schemas). We may want to merge this category with Analysis 🔥🔥🔥 .
obs
The obs component contains cell level metadata, as above.
cell_label: ID corresponding to each individual cell. See above.
[cellannotation_set]--parent_cell_set_accession: ID corresponding to the parent cell_set. If not needed for annotations, definitely needed for tooling.
uns
The uns component contains taxonomy associated files useful for reproducing analysis or mapping against the taxonomy.
schema_version: cellxgene schema version (e.g., "3.0.0")
[...]_color 🔥🔥🔥 : RGB color vector for metadata [...]; required only for selecting colors in cirrocumulus. This may be the same as the [COLUMN_NAME]_color column above.
cellannotation_schema_version: CAS schema version '[MAJOR].[MINOR].[PATCH]'
cellannotation_timestamp 🔥🔥🔥 : Timestamp when published: %yyyy-%mm-%dd %hh:%mm:%ss; Useful in general, even though currently only required by CAP; also publication_XXXX (unclear how different); This also could be the same as development_date above.
cellannotation_version 🔥🔥🔥 : CAP taxonomy annotation version; required by CAP; also publication_XXXX (unclear how different). I'm also not sure how this differs from the cellannotation_schema_version.
dataset_url: file location, as defined above.
matrix_file_id: file location, as defined above.
author_list: list of taxonomy authors; see above
[additional information] 🔥🔥🔥 : Placeholder for several other (seemingly redundant) fields required by external tools (e.g., CAP, cellxgene) that I want to capture here. It may or may not make sense to spell them all out.
