# BICAN Library Minimal Metadata Schema

Document Status: _Under MOWG Review_

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
