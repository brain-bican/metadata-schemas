# BICAN Library Minimal Metadata Schema

Document Status: _Approved by MOWG_

Version: 1.0

Owners: na.hong@yale.edu; Wenjin.J.Zheng@uth.tmc.edu

Reviewer: @patrick-lloyd-ray

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 09-09-2023

## Background

The Brain Research Through Advancing Innovative Neurotechnologies® (BRAIN) Initiative Cell Atlas Network (BICAN) aims to transform our understanding of brain cell types and the precise tools needed to access them, bringing us one step closer to unraveling the complex workings of the human brain.

Building on findings from the BRAIN Initiative Cell Census Network (BICCN), BICAN takes the next step in mapping brain cells and circuits across multiple species, with an emphasis on humans. The aim of BICAN is to generate a complete reference atlas of cell types in the human brain across the lifespan, which can be shared and used throughout the research community. In addition to developing a “parts list” detailing the vast array of neurons and non-neuronal cells in the human brain, the project also aims to map cell interactions that underlie a wide range of brain disorders.

To this end, BICAN aims to support the publication, sharing, and exploration of datasets generated in the course of the project. Creating a complete reference atlas from multiple datasets requires vast harmonization of metadata. In order to facilitate the harmonization of metadata, we require datasets include a small set of metadata available from data submitters.

This document describes a schema, a type of contract, that BICAN requires of all libraries to enable searching, filtering, and integration of datasets.

Note that the requirements in the schema are just the minimum required information. Datasets often have additional metadata, which is preserved in datasets submitted to the data archives.

## Overview

To harmonize gaps among existing library construction processes, the Library Minimal Metadata (LMM) was developed through the consensus of domain experts, including biomedical researchers, experimenters, data analysts, and informaticians. LMM is a metadata standard that aims to facilitate the interoperation and reuse of essential information and enhance the value of library-related resources.

This document has the following sections:

* [General Requirements](#general-requirements)
* [Recieve Sample](#recieve-sample), which describe...
* [Generate Library](#generate-library), which describe...
* [Pool Library](#pool-library), which describe...
* [Delivery Library Pool](#deliver-library-pool), which describe...
* [Appendix](#appendix)
* [Changelog](#changelog)

## General Requirements



## Recieve Sample

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>tissue sample label</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Identifier name for final intact piece of tissue before cell or nuclei prep.  This piece of tissue will be used in dissociation and has an ROI associated with it.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>2e4ca2fc-2d77-4d19-af45-d0fb7bbc2269</td>
    </tr>    
</tbody></table>
<br>

## Generate Library

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified cDNA label</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of a collection of cDNA molecules derived and amplified from an input barcoded_cell_sample.  These cDNA molecules represent the gene expression of each cell, with all cDNA molecules from a given cell retaining that cell's unique barcode from the cell barcoding step.  This is a necessary step for GEX methods but is not used for ATAC methods.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e2606a11-114e-472f-9e05-33f9b6fc3089</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified cDNA amplified quantity ng</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Amount of cDNA produced after cDNA amplification measured in nanograms.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0db79d05-8612-4896-b9d3-eb1558841449</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified cDNA PCR cycles</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Number of PCR cycles used during cDNA amplification for this cDNA.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>3827634c-3f8f-4760-b358-86ce4b030238</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cDNA amplification process date</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>date</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Date of cDNA amplification.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6cc333e7-9b98-497f-b7b1-eae904db2400</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified cDNA RNA amplification pass-fail</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Pass or Fail result based on qualitative assessment of cDNA yield and size.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>bc62bdb2-7dc8-4404-bb84-ce0bbcae59e5</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>amplified cDNA percent cDNA longer than 400bp</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>QC metric to measure mRNA degradation of cDNA.  Higher % is higher quality starting material.  Over 400bp is used as a universal cutoff for intact (full length) vs degraded cDNA and is a common output from Bioanalyzer and Fragment Analyzer elecropheragrams.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>8d150467-f69e-461c-b54c-bcfd22f581e5</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>cDNA amplification set</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>cDNA amplification set, containing multiple amplified_cDNA_names that were processed at the same time.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>42e98a88-50b3-4ea2-871b-2142f6a0dfdd</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>barcoded cell sample port well</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Specific position of the loaded port of the 10x chip.  An Enriched or Dissociated Cell Sample is loaded into a port on a chip (creating a Barcoded Cell Sample).  Can be left null for non-10x methods.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>aca38100-d245-4be4-9be3-ba27192779fe</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>barcoded cell input quantity count</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Number of enriched or dissociated cells/nuclei going into the barcoding process.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>aa534269-7c9b-4b63-b990-eea8cda56d0e</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>barcoded cell sample label</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of a collection of barcoded cells.  Input will be either dissociated_cell_sample or enriched_cell_sample.  Cell barcodes are only guaranteed to be unique within this one collection. One dissociated_cell_sample or enriched_cell_sample can lead to multiple barcoded_cell_samples.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4c0e6380-e53f-4173-a474-d41e836fefe3</td>
    </tr>    
</tbody></table>
<br>
	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Expected cell capture</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Expected number of cells/nuclei of a barcoded_cell_sample that will be barcoded and available for sequencing.  This is a derived number from 'Barcoded cell input quantity count' that is dependent on the "capture rate" of the barcoding method.  It is usually a calculated fraction of the 'Barcoded cell input quantity count' going into the barcoding method.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f10e928d-5a2b-4943-af18-d8fe5d05528d</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>study sets</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Intended cohort or dataset that the Barcoded Cell Sample initially belongs to.  This Study helps to group together samples that are meant to be analyzed together.  Multiple Studies can be assigned to a Barcoded Cell Sample.  These studies are more granular than the grant or PI and can be used to group together samples from related ROIs.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>8877f8f0-3939-4062-84c9-414bdcdd04ca</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>1st round barcodes</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Specific element for Paired-tag.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>24bc6d6b-fd91-4c7f-9357-22664b3e0632</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>2nd&3rd round barcode</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Specific element for Paired-tag.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>95c7fe57-2eae-42ce-b4a2-6445574e8e92</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Antibody information</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Vendor, Catalog# and Lot#</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a7af711c-f30b-469b-a3ca-b78b1b2fb99a</td>
    </tr>    
</tbody></table>
<br>
	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dissociated cell sample cell prep type</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>The type of cell preparation. For example: Cells, Nuclei. This is a property of dissociated_cell_sample.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>baae4ac3-f959-4594-b943-3a82ec19bd34</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>dissociated cell sample label</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of a collection of dissociated cells or nuclei derived from dissociation of a tissue sample.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>65e2c7da-9eb4-45b2-8ccb-d69ef9785ee2</td>
    </tr>    
</tbody></table>
<br>
	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Dissociated cell oligo tag name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of oligo used in cell plexing.  The oligo will tag allow separate dissociated cell samples to be combined downstream in the barcoded cell sample.  The oligo name is associated with a sequence in a lookup table.  This sequence will be needed to during analysis, after alignment, to associate reads with parent dissociated cell sample.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>184abbaf-baff-4b5f-b51e-dd38de6006af</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Enriched cell sample container name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of container (strip or tube or plate) of the enriched_cell_prep.  This container could contain 1 or more enriched_cell_samples.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>5ace37aa-85d6-4493-909e-8fc221ec2609</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Enriched cell sample name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of collection of enriched cells or nuclei after enrichment process (usually via FACS using the Enrichment Plan) applied to dissociated_cell_sample.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>bb3fc701-23a7-45c1-890d-7471730e0ec1</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Enrichment population</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Actual percentage of cells as a result of using set of fluorescent marker label(s) to enrich dissociated_cell_sample with desired mix of cell populations.  This plan can also be used to describe 'No FACS' where no enrichment was performed.  This is a property of enriched_cell_prep_container. </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>875f1c70-f5aa-45e3-94b9-5e482f6c4830</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library avg size bp</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Average size of the library in terms of base pairs.  This is used to calculate the molarity before pooling and sequencing.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f851eba9-56d1-4472-9d0c-d7f8bc33000a</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library method</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Standardized nomenclature to describe the library method used.  This specifies the alignment method required for the library.  For example, 10xV3.1 (for RNASeq single assay), 10xMult-GEX (for RNASeq multiome assay), and 10xMult-ATAC (for ATACSeq multiome assay).</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>7b60d59e-fdd7-4b27-a2d4-cae9b69103a6</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Library concentration nm</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Concentration of library in terms of nM (nMol/L).  Number of molecules is needed for accurate pooling of the libraries and for generating the number of target reads/cell in sequencing.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>90805b3f-f380-4f23-b159-e7eaa0c8f052</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library creation date</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>date</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Date of library construction.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>9c2f575d-1b64-451d-894f-656861afe07a</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library input ng</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Amount of cDNA going into library construction in nanograms.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e4d31d97-722d-4771-a0e4-e6062190f2c1</td>
    </tr>    
</tbody></table>
<br>
	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library label</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of a library, which is a collection of fragmented and barcode-indexed DNA molecules for sequencing.  An index or barcode is typically introduced to enable identification of library origin to allow libraries to be pooled together for sequencing.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f717e254-3630-4342-be7b-4d56376e7afe</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library prep pass-fail</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>enum</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Pass or Fail result based on qualitative assessment of library yield and size.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>6817ede2-7ead-402d-9dbc-131aca627c6c</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library prep set</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Library set, containing multiple library_names that were processed at the same time.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b124ffa9-9134-4a61-a30d-bb191b2fc7fa</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library quantification fmol</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Amount of library generated in terms of femtomoles.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>4c09ada7-c116-48bc-8fb1-0dcf5c4b939a</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library quantification ng</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Amount of library generated in terms of nanograms.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>318b2d3a-dae7-4c63-bfbb-93862b92f63e</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>R1/R2 index name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of the pair of library indexes used for sequencing.  Indexes allow libraries to be pooled together for sequencing.  Sequencing output (fastq) are demultiplexed by using the indexes for each library.  The name will be associated with the sequences of i7, i5, and i5as, which are needed by SeqCores for demultiplexing.  The required direction of the sequence (sense or antisense) of the index can differ depending on sequencing instruments.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>c94b5d8a-e92d-47af-8c0e-ea3b58be4d06</td>
    </tr>    
</tbody></table>
<br>
	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Read 2 sequencing index name</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Name of the library index used for Read-2 sequence.  Indexes allow libraries to be pooled together for sequencing.  Sequencing output (fastq) are demultiplexed by using the indexes for each library.  The name will be associated with a oligo (string of bases).  The required direction of the sequence (sense or antisense) of the index can differ depending on sequencing instruments.  The lookup table will associate each R1/R2 index name with the required sequences needed by the SeqCores.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>9f76b379-5551-487e-8d47-fa5167ae4c32</td>
    </tr>    
</tbody></table>
<br>

## Pool Library

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library aliquot label</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>One library in the library pool.  Each Library_aliquot_name in a library pool will have a unique R1/R2 index to allow for sequencing together then separating the sequencing output by originating library aliquot through the process of demultiplexing.  The resulting demultiplexed fastq files will include the library_aliquot_name.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>34191bad-d167-4335-8224-ade897d3728e</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library pool tube internal label</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Library Pool Tube local name.  Label of the tube containing the library pool, which is made up of multiple library_aliquots.  This is a Library Lab local tube name, before the pool is aliquoted to the Seq Core provided tube 'Library Pool Tube Name'.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f1fdea98-7849-4def-a62f-a04cbbf98922</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>embargo date</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>date</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>date until which data much be embargoed.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>e7bc38d8-7315-40be-b8b7-923bf770ff38</td>
    </tr>    
</tbody></table>
<br>

## Delivery Library Pool

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>SeqCore library pool tube barcode</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Library Pool tube name as provided by the SeqCore (often a barcode).  This tube is provided from the SeqCore and is part of the SeqCore tracking system.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>da02a0ee-9abf-45ef-abb1-981f1aaba6b2</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library pool label</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>text</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Library lab's library pool name.  For some labs this may be the same as "Libray pool tube local name".   Other labs distinguish between the local tube label of the library pool and the library pool name provided to SeqCore for tracking.  Local Pool Name is used to communicate sequencing status between SeqCore and Library Labs.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>29e0578b-6427-4c93-b29b-bde27fbadeec</td>
    </tr>    
</tbody></table>
<br>
	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library pool tube avg size bp</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Average insert size of library pool, measured in base pairs.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>cf1b7c96-cdc1-4eed-8e76-ac44fbd151f7</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library pool fmol</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Amount of library pool in the tube as measured in femtamoles (fmol).</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>af1a6f3f-aca9-4452-b86e-f3c70c3600b6</td>
    </tr>    
</tbody></table>
<br>
	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>loading concentration pM</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>float</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Sequencer Loading Concentration as measured in pM (pmol/L).  This is a value used by the SeqCore.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a1a1b046-549d-4e94-9b3c-5fac2a31fdd6</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Length of Read 2 (for Paired End Runs)</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Separate field to replace the combined field "Sequencing cycle". Sequencing Cycle is needed for sequencing the library pool.  The sequencing cycle needed is specific to the Library Chemistry Method and is required instruction to the SeqCores.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0b9a9cbc-b8dd-42a2-a567-aafd9370db30</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Length of Index 1 (i7 Primer)</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Separate field to replace the combined field "Sequencing cycle". Sequencing Cycle is needed for sequencing the library pool.  The sequencing cycle needed is specific to the Library Chemistry Method and is required instruction to the SeqCores.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>0b94df0d-d96e-4d49-a498-b3eb83afc5f8</td>
    </tr>    
</tbody></table>
<br>
 	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Length of Index 2 (i5 Primer)</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Separate field to replace the combined field "Sequencing cycle". Sequencing Cycle is needed for sequencing the library pool.  The sequencing cycle needed is specific to the Library Chemistry Method and is required instruction to the SeqCores.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>a61c1d55-b880-499c-ba4a-30311fdca62f</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>Length of Read 1</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Separate field to replace the combined field "Sequencing cycle". Sequencing Cycle is needed for sequencing the library pool.  The sequencing cycle needed is specific to the Library Chemistry Method and is required instruction to the SeqCores.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>f22ac08a-bb81-4524-91f0-0e1e1a032335</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library pool tube contents nM</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>float</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Library pool concentration as measured in nanomolarity (nMol/L).</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>32f2d02b-7300-4554-aa93-6de6e456eda7</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>library pool tube volume ul</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Library pool volume as measured in ul.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b1b923ac-c218-4db4-a3b1-45a219612567</td>
    </tr>    
</tbody></table>
<br>
	
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>PhiX spike in percent</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>integer</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>PhiX spike-in percent desired to be added to the library pool for sequencing.  PhiX is used to increase complexity of the sample being sequenced, to reduce sequencing artifacts maintain sequencing quality on the instruments.  This is an optional instruction to the SeqCore.</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>b5ab26ad-d523-406e-a85b-e77f2f4b06b5</td>
    </tr>    
</tbody></table>
<br>

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td>custom primers</td>
    </tr>
    <tr>
      <th>Data Type</th>
        <td><code>boolean</code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>Custom sequencing primers if needed, indicate with reads require them (R1/R2/i7/i5).</td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td>76c905d5-ef4a-421a-bd59-b541c5c1d45d</td>
    </tr>    
</tbody></table>
<br>

## Appendix

## Changelog
