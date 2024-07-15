# BICAN Library Metadata Schema

Document Status: _Under MOWG Review_

Version: 1.0

Owner: HMBA

Reviewers: @mgiglio99, @puja-trivedi, @patrick-lloyd-ray

License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

Date Created: 08-07-2024

## Background

The Brain Research Through Advancing Innovative Neurotechnologies® (BRAIN) Initiative Cell Atlas Network (BICAN) aims to transform our understanding of brain cell types and the precise tools needed to access them, bringing us one step closer to unraveling the complex workings of the human brain.

Building on findings from the BRAIN Initiative Cell Census Network (BICCN), BICAN takes the next step in mapping brain cells and circuits across multiple species, with an emphasis on humans. The aim of BICAN is to generate a complete reference atlas of cell types in the human brain across the lifespan, which can be shared and used throughout the research community. In addition to developing a “parts list” detailing the vast array of neurons and non-neuronal cells in the human brain, the project also aims to map cell interactions that underlie a wide range of brain disorders.

To this end, BICAN aims to support the publication, sharing, and exploration of datasets generated in the course of the project. Creating a complete reference atlas from multiple datasets requires vast harmonization of metadata. In order to facilitate the harmonization of metadata, we require datasets include a small set of metadata available from data submitters.

This document describes a schema, a type of contract, that BICAN requires of all donor to alignment datasets to enable searching, filtering, and integration of datasets.

Note that the requirements in the schema are just the minimum required information. Datasets often have additional metadata, which is preserved in datasets submitted to the data archives.

## Overview

The BICAN Macaque Donor and Tissue Metadata schema describes metadata associated with and produced from the preparation of macaque donor and tissue in the HMBA and BICAN. [more detail needed here]

This document has the following sections:

* [General Requirements](#general-requirements)
* [PatchSeq](#patchseq), which describe the metadata required for macaque patchseq experiments.
* [Population](#population), which describe the metadata required for macaque population studies.
* [Whole Brain Spatial Omics](#whole-brain-spatial-omics), which describe the metadata required for whole brain spatial omics experiements.
* [Appendix](#appendix)

## General Requirements

**Organisms**. Data must be from a Metazoan organism and defined in the NCBI organismal classification.

**Redundant Metadata**. It is STRONGLY RECOMMENDED to avoid multiple metadata fields containing identical or similar information.

## PatchSeq

The data in patchseq is the metadata essential for macaque patchseq experiments.

The following tables describe the patchseq metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### Local Donor ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Repository

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Donor Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Sex at Birth

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Age Value (Years)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Date of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Manner of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Medical Records Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Medical Records Reviewed

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Hemisphere

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Post Mortem Interval

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Left Hemisphere Preparation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Left Hemisphere Preparation Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Right Hemisphere Preparation

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Right Hemisphere Preparation Specify

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Photo 2d Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Antemortem MRI Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Non-Brain Tissue Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Tissue Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Tissue Type Details

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Test Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Result

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Testing Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Species

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Premortem perfusion done

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Premortem perfusion buffer type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Region of interest

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Behavorial Testing

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Behavorial Testing Type

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Non Brain Diagnosis Description

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Population

The data in population is the metadata essential for macaque population studies.

The following tables describe the population metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

subject_id
repository
donor_source
sex
age_of_death
year_of_death
autopsy_report
cause_of_death
cause_of_death_code
manner_of_death
medical_records_reviewed
hemisphere
post_mortem_interval
left_hemisphere_preparation
left_hemisphere_preparation_specify
right_hemisphere_preparation
right_hemisphere_preparation_specify
rin
rin_tissue_source
rin_testing_organization
rine
rine_tissue_source
rine_testing_organization
ph
brain_weight
weighed_type
photo_2d_available
scan_3d_available
antemortem_mri_available
postmortem_mri_available
postmortem_mri_type
non_brain_tissue_available
tissue_type
tissue_type_details
birth_weight_lbs
birth_weight_oz
gestational_age_value_weeks
gestational_age_value_days
species
social_group
body_weight
perfusion
perfusate_type
head_off_time
brain_extraction_time
brain_fixed_time
brain_frozen_time
brain_fixation_method
brain_freeze_method
sedation_start_time
sedation_total_dose
euthanasia_time
euthanasia_dose
perfusion_time_start
perfusion_time_end
trapping_date
trapping_time
matriline
behavioral_scoring_available
behavioral_scoring_type
ordinal_dominance_rank
brain_size_anterior_posterior
brain_size_medial_lateral
brain_size_dorsal_ventral
brain_size_unit_type
histological_stains_available
hiatological_stain_type

## Whole Brain Spatial Omics

The data in whole brain spatial omics is the metadata essential for whole brain spatial omics experiments.

The following tables describe the whole brain spatial omics metadata. If an entry in the table is empty, the schema does not have any other requirements on data in those layers beyond the ones listed above.

Curators must annotate the following columns:

### Local Donor ID

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Repository

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Donor Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Sex at Birth

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Age Value (Years)

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Birth Country Name

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Date of Death

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Hemisphere

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Post Mortem Interval

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RIN

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### RIN Tissue Source

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Brain Weight Measurement

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Photo 2d Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Scan 3d Available

<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

### Antemortem MRI Available
 
<table><tbody>
    <tr>
      <th>BICAN Field Name</th>
      <td></td>
    </tr>
    <tr>
      <th>Annotator</th>
      <td></td>
    </tr>
    <tr>
      <th></th>
        <td><code></code>
        </td>
    </tr>
    <tr>
      <th>Definition</th>
        <td>
        </td>
    </tr>
    <tr>
      <th>BICAN UUID</th>
      <td></td>
    </tr>
</tbody></table>
<br>

## Appendix
