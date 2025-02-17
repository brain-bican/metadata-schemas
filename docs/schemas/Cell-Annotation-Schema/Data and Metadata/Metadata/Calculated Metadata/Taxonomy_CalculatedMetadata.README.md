Calculated metadata
This includes any cell-level or cluster-level metadata that can be calculated explicitly from the Data and Assigned Metadata without the need for human intervention. Some examples include # reads detected/cell, # UMI/cell, fraction of cells per cluster derived from each anatomic dissections, expressed neurotransmitter genes (quantitatively defined), average QUANTITATIVE_VALUE (e.g., doublet score) per cluster. Currently none of these are required for the schema, but they are sometimes used for annotation.
obs
The obs component contains cell level metadata from the experiment
cell_label: ID corresponding to each individual cell. (will likely be renamed) See above.
[additional uncontrolled metadata]: Additional uncontrolled cell metadata. These are not required, but any additional columns are allowed by all h5ad formats.
feature_matrix_label, dataset_label, [COLUMN_NAME]_color, [COLUMN_NAME]_id: See above.
uns
The uns component contains more general information and fields with formatting incompatible with the above components.
calculated_metadata_metadata 🔥🔥🔥 : TBD information about the calculated_metadata itself. This likely is not needed or should be renamed.
