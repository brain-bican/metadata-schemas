Analysis
This includes any fields included as the result of or required for specific analysis. Some examples include latent spaces (e.g., UMAP), cluster level gene summaries (e.g., cluster means, proportions), and variable genes. These may not need to match between schemas (or even be encoded into schemas).
obsm
The obsm component contains all dimensionality reductions of the taxonomy (cell x dim). For all fields listed below, columns are of the format '[FIELD]_#' where # is 1, 2, 3, etc..
umap 🔥🔥🔥 : 2 (or more)-dimensional representation of cells in AIT. Must be of the form X_[...] for use with CELLxGENE. Only the first two dimensions are used for AIT and CELLxGENE, but 3 dimensions can be used for cirrocumulus.
pca: Additional terms for embedding multi-dimensional principal components and latent spaces
scVI: Additional terms for embedding multi-dimensional principal components and latent spaces
var
The var component contains gene level metadata.
gene: Same vector included in "data" to link between files.
highly_variable_genes: A logical vector (T/F) indicating which genes are highly variable. Used for correlation-based mapping in scrattch.mapping.
marker_genes_[...]: Potentially additional sets of logical vectors for marker genes, as defined above.
uns
The uns component contains taxonomy associated files useful for reproducing analysis or mapping against the taxonomy.
dend: See above. This may fit better here.
QC_markers: Marker gene expression in on-target and off-target cell populations, useful for patchseq analysis. Also includes information about KL divergence calculations and associated QC calls. Defined by buildPatchseqTaxonomy.
filter: Indicator of which cells to use for a given child taxonomy (subset), as defined above.
mode: Taxonomy mode that determines which filter to use (e.g., that indicates which child taxonomy to map against). Several of the other analysis components of the uns have things saved with mode as the name in the h5ad file. See scrattch.mapping documentation. Mode is the Taxonomy short name in taxonomy Google Sheet for a child taxonomy with the Parent taxonomy listed as the taxonomyName.
clustersUse 🔥🔥🔥 : A vector of cluster names to use for taxonomy. We should be able to remove this
clusterInfo 🔥🔥🔥 : A data.frame of cluster information. We should be able to remove this
marker_gene_metadata: Metadata about any new marker gene lists added, if any. See above.
development_date: Data of taxonomy development. Required for Google Sheet. Potentially not needed if we want to infer from taxonomy_id.
public: logical flag indicating whether taxonomy should be public or private. Required for Google Sheet. Potentially not needed if we want to infer from PURL/GitHub somehow.
annotation_sheet: Link to annotation sheet (ideally a TDT GitHub repo link for communal annotation). An optional slot in the Google sheet. I'm not sure if this is listed above somewhere.
purpose: Controlled vocabulary (currently "General" and/or "Patch-seq"). Required for Google Sheet at the moment.
