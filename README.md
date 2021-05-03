# Generation of DICOM files from FastMRI raw data

Some simple scripting to generate DICOMs from the [FastMRI.org](https://fastmri.org) data.

Convert a single file with:

```bash
python fastmri_to_dicom.py --filename fastmrifile.h5
```

If you have your data in an Azure Blob storage account, you can process from one container to another with:

```bash
CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=<accountName>;AccountKey=<accountKey>;EndpointSuffix=core.windows.net"
python process_fastmri_blob.py --connection_string="${CONNECTION_STRING}" --container_in input_container --container_out output_container --prefix brain/multicoil_val
```

which would process all the multicoil brain validation data. 
