# Patch-seq metadata table

`Patchseq_Metadata.csv` lists the fields of the Patch-seq model, one row per field. It uses the
format of the BICAN
[Library Minimal Metadata](https://github.com/brain-bican/metadata-schemas/blob/refactoring/docs/schemas/Library-Minimal-Metadata/Library_Minimal_Metadata.csv)
table.

## Classes

**Donor and specimens** (from NIMP)
- **Donor**: the animal the brain tissue comes from.
- **PatchedCell**: a single neuron recorded by patch clamp in a brain slice. Its electrophysiology
  is recorded, it is filled with biocytin for morphology, and its nucleus is extracted for
  sequencing. A kind of DissociatedCellSample.
- **BarcodedCellSample** and **LibraryAliquot**: the patched cell's nucleus and its sequencing
  library, as in the library generation model.

**Files**
- **DigitalAsset**: the FASTQ files of a library aliquot, on NeMO.
- **PatchClampEphysRecording**: the patch-clamp recording of one patched cell, one NWB file on DANDI.
- **ImageStack**: a brightfield z-stack (TIFF) of one biocytin-filled cell, on BIL.
- **NeuronReconstruction**: the 3D reconstruction of one neuron (SWC file, on BIL), traced from its
  image stack.

**Stimuli**
- **StimulusSet**: a kind of stimulus used in the recording: long square, short square, ramp or chirp.
- **StimulusProtocol**: one MIES protocol (stimulus code) of a stimulus set, e.g. X3LP_Rheo.

**Feature sets**
- **FeatureSet**: the features computed in one feature extraction run for one cell, with the
  software and version used.
- **EphysFeatureSet**: the electrophysiology features from the responses to one stimulus set, one
  class per stimulus set: **LongSquareFeatureSet**, **ShortSquareFeatureSet**,
  **RampFeatureSet** and **ChirpFeatureSet**.
- **MorphologyFeatureSet**: the morphology features of one neuron, computed from its reconstruction.

**Cell type mapping**
- **CellTypeMapping**: the result of mapping one patched cell's transcriptome to a cell type
  taxonomy with MapMyCells: the cluster it was mapped to, with the confidence values.
