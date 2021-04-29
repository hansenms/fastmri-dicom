# Coded version of DICOM file '301.dcm'
# Produced by pydicom codify utility script
import pydicom
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.sequence import Sequence

# File meta info data elements
file_meta = FileMetaDataset()
file_meta.FileMetaInformationGroupLength = 176
file_meta.FileMetaInformationVersion = b'\x00\x01'
file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.4'
file_meta.MediaStorageSOPInstanceUID = '9999.80737131589526800317907414738198661932'
file_meta.TransferSyntaxUID = '1.2.840.10008.1.2.1'
file_meta.ImplementationClassUID = '1.2.40.0.13.1.1.1'
file_meta.ImplementationVersionName = 'dcm4che-1.4.35'

# Main data elements
ds = Dataset()
ds.SpecificCharacterSet = 'ISO_IR 100'
ds.ImageType = ['ORIGINAL', 'PRIMARY', 'OTHER']
ds.InstanceCreationTime = '124810.560'
ds.SOPClassUID = '1.2.840.10008.5.1.4.1.1.4'
ds.SOPInstanceUID = '9999.80737131589526800317907414738198661932'
ds.StudyDate = '20160131'
ds.ContentDate = '20160131'
ds.StudyTime = ''
ds.ContentTime = ''
ds.AccessionNumber = '100099070170'
ds.Modality = 'MR'
ds.ModalitiesInStudy = ['', 'PR', 'MR', '']
ds.Manufacturer = 'Hitachi Medical Corporation'
ds.ReferringPhysicianName = ''
ds.StudyDescription = 'MRI BRAIN WITH AND WITHOUT IV CONTRAST'

# Procedure Code Sequence
procedure_code_sequence = Sequence()
ds.ProcedureCodeSequence = procedure_code_sequence

# Procedure Code Sequence: Procedure Code 1
procedure_code1 = Dataset()
procedure_code1.CodeValue = 'IMG271'
procedure_code1.CodingSchemeDesignator = 'L'
procedure_code1.CodeMeaning = 'MRI BRAIN WITH AND WITHOUT IV CONTRAST'
procedure_code_sequence.append(procedure_code1)

ds.SeriesDescription = 'Axial T1 FSE  POST'
ds.ManufacturerModelName = 'OASIS'

# Related Series Sequence
related_series_sequence = Sequence()
ds.RelatedSeriesSequence = related_series_sequence

# Related Series Sequence: Related Series 1
related_series1 = Dataset()
related_series1.StudyInstanceUID = '1.2.840.114350.2.232.2.798268.2.182582632.1'
related_series1.SeriesInstanceUID = '1.2.392.200036.9123.100.12.12.22235.90170518120923060707062733'

# Purpose of Reference Code Sequence
purpose_of_ref_code_sequence = Sequence()
related_series1.PurposeOfReferenceCodeSequence = purpose_of_ref_code_sequence
related_series_sequence.append(related_series1)

ds.PatientName = '1898817175'
ds.PatientID = '9174164112'
ds.PatientBirthDate = '19860405'
ds.PatientSex = 'F'
ds.PatientAge = '029Y'
ds.PatientIdentityRemoved = 'YES'
ds.ContrastBolusAgent = ''
ds.BodyPartExamined = 'BRAIN'
ds.ScanningSequence = 'SE'
ds.SequenceVariant = 'SK'
ds.ScanOptions = ['SP', 'FC']
ds.MRAcquisitionType = '2D'
ds.SequenceName = 'opFSE'
ds.AngioFlag = 'N'
ds.SliceThickness = "5.0"
ds.RepetitionTime = "602.0"
ds.EchoTime = "10.4"
ds.NumberOfAverages = "2.0"
ds.ImagingFrequency = "49.377199"
ds.ImagedNucleus = '1H'
ds.EchoNumbers = "1"
ds.MagneticFieldStrength = "1.16"
ds.SpacingBetweenSlices = "6.0"
ds.NumberOfPhaseEncodingSteps = "230"
ds.EchoTrainLength = "3"
ds.PercentSampling = "0.0"
ds.PercentPhaseFieldOfView = "90.0"
ds.SecondaryCaptureDeviceID = ''
ds.ContrastBolusVolume = "0.0"
ds.NominalInterval = "0"
ds.BeatRejectionFlag = 'N'
ds.LowRRValue = "90"
ds.HighRRValue = "100"
ds.IntervalsAcquired = "0"
ds.IntervalsRejected = "0"
ds.SkipBeats = "1"
ds.HeartRate = "0"
ds.TriggerWindow = "90"
ds.ReconstructionDiameter = "220.0"
ds.ReceiveCoilName = 'RAPID Head'
ds.AcquisitionMatrix = [0, 288, 230, 0]
ds.InPlanePhaseEncodingDirection = 'ROW'
ds.FlipAngle = "90.0"
ds.VariableFlipAngleFlag = 'N'
ds.SAR = "1.8"
ds.dBdt = "0.44"
ds.PatientPosition = 'HFS'
ds.ContentQualification = 'SERVICE'
ds.SaturationRecovery = 'NO'
ds.GeometryOfKSpaceTraversal = 'RECTILINEAR'
ds.RectilinearPhaseEncodeReordering = 'LINEAR'
ds.NumberOfKSpaceTrajectories = 76
ds.StudyInstanceUID = '9999.201195313229306300504165090941650322040'
ds.SeriesInstanceUID = '9999.77565704772180596049766113144111491928'
ds.StudyID = ''
ds.SeriesNumber = "16"
ds.AcquisitionNumber = "0"
ds.InstanceNumber = "14"
ds.PatientOrientation = ['0.988018', '0.14265']
ds.OverlayNumber = None
ds.CurveNumber = None
ds.LUTNumber = None
ds.ImagePositionPatient = [-96.26828, -112.8608, 38.50235]
ds.ImageOrientationPatient = [0.988018, 0.142657, -0.0589, -0.133943, 0.98216, 0.131983]
ds.FrameOfReferenceUID = '9999.307577518163987444448414094854502648367'
ds.Laterality = ''
ds.ImagesInAcquisition = "26"
ds.PositionReferenceIndicator = '-1757'
ds.SliceLocation = "44.54"
ds.SamplesPerPixel = 1
ds.PhotometricInterpretation = 'MONOCHROME2'
ds.NumberOfFrames = "1"
ds.Rows = 512
ds.Columns = 512
ds.PixelSpacing = [0.4296875, 0.4296875]
ds.PixelAspectRatio = [1, 1]
ds.BitsAllocated = 16
ds.BitsStored = 12
ds.HighBit = 11
ds.PixelRepresentation = 1
ds.SmallestImagePixelValue = -29
ds.LargestImagePixelValue = 1024
ds.BurnedInAnnotation = 'NO'
ds.WindowCenter = "213.0"
ds.WindowWidth = "426.0"
ds.LossyImageCompression = '00'
ds.StudyStatusID = 'COMPLETED'
ds.ResultsID = ''

# Per-frame Functional Groups Sequence
per_frame_functional_groups_sequence = Sequence()
ds.PerFrameFunctionalGroupsSequence = per_frame_functional_groups_sequence

# Per-frame Functional Groups Sequence: Per-frame Functional Groups 1
per_frame_functional_groups1 = Dataset()

# MR Receive Coil Sequence
mr_receive_coil_sequence = Sequence()
per_frame_functional_groups1.MRReceiveCoilSequence = mr_receive_coil_sequence

# MR Receive Coil Sequence: MR Receive Coil 1
mr_receive_coil1 = Dataset()

# Multi-Coil Definition Sequence
multi_coil_definition_sequence = Sequence()
mr_receive_coil1.MultiCoilDefinitionSequence = multi_coil_definition_sequence

# Multi-Coil Definition Sequence: Multi-Coil Definition 1
multi_coil_definition1 = Dataset()
multi_coil_definition1.MultiCoilElementName = 'RAPID Head'
multi_coil_definition1.MultiCoilElementUsed = 'YES'
multi_coil_definition_sequence.append(multi_coil_definition1)
mr_receive_coil_sequence.append(mr_receive_coil1)


# MR Spatial Saturation Sequence
mr_spatial_saturation_sequence = Sequence()
per_frame_functional_groups1.MRSpatialSaturationSequence = mr_spatial_saturation_sequence

# MR Spatial Saturation Sequence: MR Spatial Saturation 1
mr_spatial_saturation1 = Dataset()
mr_spatial_saturation1.SlabThickness = 50.0
mr_spatial_saturation1.SlabOrientation = [0.07667737, -0.1225113, 0.9894996]
mr_spatial_saturation1.MidSlabPosition = [-11.17622, 25.01912, -67.74574]
mr_spatial_saturation_sequence.append(mr_spatial_saturation1)


# MR Modifier Sequence
mr_modifier_sequence = Sequence()
per_frame_functional_groups1.MRModifierSequence = mr_modifier_sequence

# MR Modifier Sequence: MR Modifier 1
mr_modifier1 = Dataset()
mr_modifier1.T2Preparation = 'NO'
mr_modifier1.SpectrallySelectedExcitation = 'NONE'
mr_modifier1.ParallelReductionFactorInPlane = 1.0
mr_modifier1.ParallelAcquisition = 'NO'
mr_modifier1.ParallelReductionFactorOutOfPlane = 1.0
mr_modifier_sequence.append(mr_modifier1)


# MR Diffusion Sequence
mr_diffusion_sequence = Sequence()
per_frame_functional_groups1.MRDiffusionSequence = mr_diffusion_sequence
per_frame_functional_groups_sequence.append(per_frame_functional_groups1)

ds.PixelData = # XXX Array of 524288 bytes excluded

ds.file_meta = file_meta
ds.is_implicit_VR = False
ds.is_little_endian = True
ds.save_as(r'301_from_codify.dcm', write_like_original=False)