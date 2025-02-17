Annotations
This includes any fields related to the annotation of clusters or groups of clusters (collectively called "cell sets"). This includes things like cluster levels, cluster relationships, canonical marker genes, links to existing ontologies (e.g., CL, UBERON) based on judgement calls, expert annotations, and dendrograms.
obs
The obs component contains cell level metadata, as above.
cell_label: ID corresponding to each individual cell. See above.
cluster_id 🔥🔥🔥 : Unique integer value corresponding to each cluster in the taxonomy, which also (ideally but not necessarily) encodes the order of clusters in visualizations. Once a taxonomy is minted, this cannot change. This is the CRITICAL column used for cluster annotations. It is the baseline for the majority of cell_annotation columns discussed below. Note that “cell_set_accession_ids” and “cluster hash values” can be assigned after these “cluster_ids” are agreed upon. It's also worth noting that this is a prerequisite for annotations, so maybe it better fits in a different category (analysis?).
cluster_label: Human-readable cluster name used primarily by scientists and other folks. This is the same as “cell_label” for cell sets when the “label_set” is cluster. It's also used for cirrocumulus. 
[other cluster columns?]: There is also an additional cluster_alias column used in mouse whole brain data and for BKP that I'm not sure how to wrap in. Are there other columns. 
[additional uncontrolled metadata]: Additional uncontrolled cell metadata. These are not required, but any additional columns are allowed by all h5ad formats.
feature_matrix_label, dataset_label, [COLUMN_NAME]_color, [COLUMN_NAME]_id: See above.
NOTE: The obs component also contains cell set metadata summarized at the cell level. The proposal is to store all of this in the uns in json format and create helper functions to duplicate information as obs columns as needed.  Currently there is a standard way of doing this for CAP, and we will implement a mechanism for this in scrattch.taxonomy as well.
var
The var component contains gene level metadata.
gene: Same vector included in "data" to link between files.
marker_genes_[...] 🔥🔥🔥 : A set of logical vectors (T/F) indicating which genes are markers used to build dendrogram, or for other purposes. The [...] part of the name links to additional metadata in the uns. This needs to be UPDATED in AIT to allow multiple marker gene sets; markers currently stored differently in CAP.
uns
The uns component contains more general information and fields with formatting incompatible with the above components. Much of the information about annotations is stored in this field, so we divide it up below.
Proposal: store everything that goes in the TDT taxonomy annotations in a single field called “annotations” and match the TDT structure.  Then write conversions between uns and obs for most h5ad use cases.

uns fields associated with taxonomy metadata (e.g., different label sets)

taxonomyName 🔥🔥🔥 : Taxonomy name (e.g., "AIT30"); called title in cellxgene, not sure about other schema. Called Taxonomy short name in taxonomy Google Sheet.
taxonomy_id 🔥🔥🔥 : Taxonomy ID in CCN format (e.g., "CCN030420240"); TBD how this is generated, but MUST be globally unique. Also used as part of PURL (I think). Called Taxonomy ID in taxonomy Google Sheet too.
description 🔥🔥🔥 : Free text description of the taxonomy (or of the dataset on CAP). This is also something we are adding as a requirement for the BKP, and I think should be required for all taxonomies. Called Description in taxonomy Google Sheet.
taxonomy_citation: "|"-separated publication DOI's of the taxonomy (e.g., "doi:10.1038/s41586-018-0654-5"). Called Publication in taxonomy Google Sheet.
marker_gene_metadata 🔥🔥🔥 : Data frame of Marker genes x dims that includes metadata for marker gene sets in var above; NEW and required if marker_genes_[…] is provided. At minimum a name (matching above) and description are needed, but potentially other things (e.g., what is it for, with controlled vocabulary).
taxonomyDir 🔥🔥🔥 : Location of the h5ad file; we might be able to remove this, since it is redundant with dataset_url and/or matrix_file_id. Called Taxonomy file location in taxonomy Google Sheet.
dataset_url 🔥🔥🔥 : PURL of taxonomy; Possibly a redundant field, but critical; also publication_url and cellannotation_url (unclear how different)
matrix_file_id 🔥🔥🔥 : Like dataset_url; e.g. CellXGene_dataset:8e10f1c4-8e98-41e5-b65f-8cd89a887122; Note: needs to be extended to allow for more than one file and connected to feature_matrix_label in obs. We need this field!
author_list: List of all collaborators, comma separated [First] [Last]; Useful in general, even though currently only required by CAP. Called Taxonomy Users in taxonomy Google Sheet.
author_name: The primary author [First Name] [Last Name]; in CCN was called "taxonomy_author"; In CCN also seperated by cell_set with "cell_set_alias_assignee"; Called Point person name in taxonomy Google Sheet.
author_contact: Valid email address; Called Point person email in taxonomy Google Sheet.
orcid: Valid ORCID; Called Point person ORCID in taxonomy Google Sheet.
annotation_source : Additional metadata about annotation algorithm; Similar to taxonomy algorithm info stored for CCN
uns fields associated with individual cell set annotations (e.g., different label sets)
labelsets 🔥🔥🔥 : CRITICAL extra component; Equivalent to Cluster annotation term set in BKP. This is saved as a data frame representation (or is a list of data frames needed?), with some information about each [cellannotation_set] set of columns (e.g., subclass, class, neurotransmitter, etc.). Specifically: "name", "description", and "rank" (0 most specific) and some information about provenance are needed for each labelset.
labelsets 🔥🔥🔥 : This is where taxonomy levels are stored in AIT)CCN)CAS. The column name is a string (e.g., "subclass") and the values are cell_labels (e.g., "SST"). The equivalent in BKP are Cluster Annotation Term Sets and in CAP is label_sets. This also encapsulates the concept of cell_ids from CAP/CAS, since in the h5ad file each row corresponds to a cell and therefore you get the cell_label --> cell_ids mapping for free. This is stored as separate files in both BKP and TDT and so we should confirm appropriate translations and agree on terms for this. Finally, this concept is critical for scrattch.taxonomy and scrattch.mapping to work properly, but none of the [cellannotation_set]--XXXX fields below are needed for AIT (although keeping this is best practice!).
NOTE: the fields below each relate to a specific labelset.  We need to flesh out a bit better how to structure this in a json in the uns, but for now I’m just showing them as individual columns
[neurotransmitters] 🔥🔥🔥 : Placeholder in case this isn’t included already in labelsets
cell_set_accession 🔥🔥🔥 : ID corresponding to the cell_set; called the "Cluster Annotation Term" in BKP. Some work still needed on deciding what to name this (CCNXXXXX?, a hash code?, something else?) and HOW to name this (automatically? if so, but what authority).
cell_set_label 🔥🔥🔥 : This can probably be dropped. For CCN this was used as a tag for each cluster or (for cell sets with >1 cluster) included a list of underlying cluster labels. It was important for proper databasing without a database.
cell_fullname: The longer name for a cell type (e.g., "Somatostatin interneuron 1" rather than "SST 1"). This was called the cell_set_preferred_alias in CCN.
cell_ontology_exists 🔥🔥🔥 : True/false call about whether a cell ontology term exists (This seems redundant to me with next two rows). I vote we remove it and derive as needed.
cell_ontology_term_id: Highest resolution Cell Ontology term (ID); was called cell_set_ontology_tag in CCN
cell_ontology_term 🔥🔥🔥 : Highest resolution Cell Ontology term (name); was called cell_set_structure in CCN and was also largely mapping to the cell_set_aligned_alias. Note that we currently don't have a field in the schema for dealing with cross-species homologies (like the cell_set_aligned_alias) as far as I can tell.
rationale: Free text evidence for cell annotations.
rationale_dois 🔥🔥🔥 : Comma-separated publication DOI's of rationale CCN: "cell_set_alias_citation". NOTE: We sometimes use comma-separated and sometimes "|"-separated (and BICAN uses something else: "/#/").
marker_gene_evidence: Comma-separated marker genes used as evidence for cell type annotation (e.g., by NS-Forest). Note: This is reserved for ontology markers. See var below for how to store general marker genes.
canonical_marker_genes 🔥🔥🔥 : Comma separated list of canonical marker genes. I don't understand how this differs from marker_gene_evidence. I vote we omit this.
synonyms: Comma-separated aliases (e.g., "neuroglial cell, glial cell, neuroglia"); was called cell_set_additional_alias in CCN.
category_XXXX 🔥🔥🔥 : I'm not entirely sure what these columns represent. They appear to be the same as cell_XXXX above for several fields (e.g., fullname, cell_ontology_term, etc.). Can we please omit or clarify?
parent_cell_set_name 🔥🔥🔥 : ‘cell_label’ corresponding to the parent cell_set.
parent_cell_set_accession 🔥🔥🔥 : ID corresponding to the parent cell_set. I think this would correspond to the parent Cluster Annotation Term ID in knowlegebase?
uns fields associated with complex cell set relationships and metadata (e.g., dendrograms, child taxonomies, gradients, level relationships, annotation transfer)

dend 🔥🔥🔥 : A json formatted dendrogram used for tree mapping. Created by scrattch.taxonomy if not provided. Sometimes used for taxonomy annotation, but we are moving away from it with larger taxonomies and so this may now make more sense in the "analysis" category.
cell_set_relationships 🔥🔥🔥 : NEW proposed mechanism for dealing with sibling relationships for things like gradients, trajectories, constellation diagrams, etc.. This is stored as a data frame (table) of all relations with five columns: cells_set_accession1, cell_set_accession2, relation_label, value, direction. Could alternatively be stored as a JSON representation that unpacks into a dataframe.
filter 🔥🔥🔥 : Indicator of which cells to use for a given child taxonomy (subset), saved as a list of vectors. Each entree in this list is named for the relevant "mode" and has TRUE/FALSE calls indicating whether a cell is filtered out (e.g., the "standard" taxonony is all FALSE). This is critical for how child taxonomies are defined and implemented in scrattch.taxonomy but differs from how taxonomies are stored in all other schemas--some discussion may be needed.
[transferred_annotations] 🔥🔥🔥 : Column name is a string corresponding to the taxonomy of comparison; values are the transferred cell label from that taxonomy. I think there is still some work on the best way to code this, but it is important. This is also already encoded in TDT--how? It is linked to some information in the uns below. Potentially more columns needed for annotation-level metadata (e.g., source_node_accesssion, comments).
transferred_annotations_metadata 🔥🔥🔥 : Data frame of info about each transferred annotation column: source_taxonomy, algorithm_name, comment; Still some work on the best way to code this, but it is important. Linked to data in var above. This is for taxonomy-level metadata. This is also already encoded in TDT--how?
