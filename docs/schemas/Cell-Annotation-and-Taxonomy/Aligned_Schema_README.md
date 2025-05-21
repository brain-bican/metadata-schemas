# AIT / CAS / BKP schema integration

*(Note: An evolving version of this standard is available **[as a Google Doc](https://docs.google.com/document/d/1nj6LHUPoo3JnNwZ7PTdniT9pBPsoJr1B/edit?usp=sharing&ouid=113573359044104089630&rtpof=true&sd=true)**).*

Several competing schema have been created for packaging of taxonomies, data sets, and associated metadata and annotations.  This document aims to align three such schema and propose a way of integrating them into the Allen Institute Taxonomies (AIT) .h5ad file format presented as part of this GitHub repository. The three standards are:

1. **AIT** (described herein)
2. **[Cell Annotation Schema](https://github.com/cellannotation/cell-annotation-schema/) (CAS)**: this schema is becoming more widely-used in the cell typing field as a whole because it is largely compatible with [the CZ CELLxGENE schema](https://github.com/chanzuckerberg/single-cell-curation/blob/main/schema/3.0.0/schema.md). It is also compabible with [Cell Annotation Platform](https://celltype.info/) (CAP) and with [Taxonomy Development Tools](https://brain-bican.github.io/taxonomy-development-tools/) (TDT). CAS has both a general schema and a BICAN-associated schema, both of which are considered herein.  CAS can be embedded in the header (`uns`) of an AIT/Scraatch.taxonomy file, where it functions as a store of extended information about an annotation, including ontology term mappings, evidence for annotation (from annotation transfer and marker expression).
3. **Brain Knowledge Platform (BKP)**: this schema isn't publicly laid out anywhere that I can find, but this is the data model used for [Jupyter Notebooks](https://alleninstitute.github.io/abc_atlas_access/intro.html) associated with the [Allen Brain Cell (ABC) Atlas](https://portal.brain-map.org/atlases-and-data/bkp/abc-atlas).  More generally, any data sets to be included in ABC Atlas, [MapMyCells](https://portal.brain-map.org/atlases-and-data/bkp/mapmycells), or other related BKP resources will eventually need to conform to this format.

It's worth noting that all of these schema are still under development, and we hope they will approach a common schema.

[Taxonomy_field_mappings](https://docs.google.com/spreadsheets/d/1PhsOipO0yCrtTGrkWXLU2Tj2m4qFPgdKID0SqetYN0Y/edit#gid=0) in table form.

## Cell type taxonomy organization

One major challenge in creating a cell type taxonomy schema is in definition of terms such as "taxonomy," "dataset," "annotation," "metadata," and "data."  Our current working model of a taxonomy is shown below; however, it is becoming increasingly important to (at minimum) separate out the data from the other components, and (ideally) separately out all components to avoid the need to download, open, or upload huge and unweildy files and to integrate with under-development databases.

![Taxonomy_overview](https://github.com/AllenInstitute/scrattch.taxonomy/assets/25486679/9d36e6bc-db14-4d73-8011-23026756ec08)

That said, it is still important for many use cases to have an option of including all of the information listed above in a single h5ad file for use with CELLxGENE, [scrattch.mapping](https://github.com/AllenInstitute/scrattch.mapping), and other analysis tools, and for ease of sharing in a single file format. To this end, we divide the schema components in this document by the following broad category terms (described below), and for each term indicate which component of the schematic in which it can be found.  In cases where the same information is saved in multiple ways in different schema, we group these fields together as well.

**EXAMPLE**:fire::fire::fire:

We highlight areas of the schema that are not currently in sync and that need continued effort using fire emojis, as shown here.  

### Broad category terms

Here are the current categories that all fields are placed in as a starting point for discussion.  Cases where the location of a field is unclear or ambiguous are called out :fire: .

* **[Data]**: This includes anything critical for understanding the cell by gene matrix and to link it with other components.  This includes data (raw and processed), gene information, and cell identifiers.  *Note that for the purposes of this schema, we are excluding raw data (fastq, bam files, etc.) from consideration and are starting from the count matrix.*
* **[Assigned metadata](https://github.com/AllenInstitute/scrattch.taxonomy/blob/KL_div/schema/aligned_schema.md#assigned-metadata)**: This includes cell-level metadata that is assigned at some point in the process between when a cell goes from the donor to a value in the data, and (in theory) can be ENTIRELY captured by values in Allen Institute, BICAN, or related standardized pipelines.  It includes things like donor metadata, experimental protocols, dissection information, RNA QC metrics, and sequencing metadata.
* **[Calculated metadata](https://github.com/AllenInstitute/scrattch.taxonomy/blob/KL_div/schema/aligned_schema.md#calculated-metadata)**: This includes any cell-level or cluster-level metadata that can be calculated explicitly from the **Data** and **Assigned Metadata** without the need for human intervention.  Some examples include # reads detected/cell, # UMI/cell, fraction of cells per cluster derived from each anatomic dissections, expressed neurotransmitter genes (quantitatively defined), average QUANTITATIVE_VALUE (e.g., doublet score) per cluster.
* **[Annotations](https://github.com/AllenInstitute/scrattch.taxonomy/blob/KL_div/schema/aligned_schema.md#annotations)**: This includes any fields related to the annotation of clusters or groups of clusters (collectively called "cell sets").  This includes things like cluster levels, cluster relationships, canonical marker genes, links to existing ontologies (e.g., CL, UBERON) based on judgement calls, expert annotations, and dendrograms.
* **[Analysis](https://github.com/AllenInstitute/scrattch.taxonomy/blob/KL_div/schema/aligned_schema.md#analysis)**: This includes any fields included as the result of or required for specific analysis.  Some examples include latent spaces (e.g., UMAP), cluster level gene summaries (e.g., cluster means, proportions), and variable genes.
* **[Tooling](https://github.com/AllenInstitute/scrattch.taxonomy/blob/KL_div/schema/aligned_schema.md#tooling)**: This includes any fields required for specific tools (e.g., cellxgene, TDT, CAS, CAP) that are not strictly part of the taxonomy and that do not fit in any of the above categories.  This includes things like schema versions and redundent fields from above with different column names.

We expect some of these categories to change but feel this is a good starting point.

Here is a graphical representation of these terms in the context of data, metadata, and taxonomies:
![image](https://github.com/AllenInstitute/scrattch.taxonomy/assets/25486679/eaf6b3d3-0b5f-49fc-9a49-2b7168605964)

### Anndata schematic

Within each broad categorical term, fields are ordered by their location in the anndata object: X, layers, obsm, obs, var, uns.

![Schematic](https://github.com/AllenInstitute/AllenInstituteTaxonomy/blob/main/assets/AIT_anndata_schema.png)

And now let's go on to the schema!

## Proposed integrated schema

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED" "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14, RFC2119, and RFC8174 when, and only when, they appear in all capitals, as shown here.  :fire::fire::fire: :fire::fire::fire: :fire::fire::fire:
