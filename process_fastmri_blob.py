import argparse
import os
from pathlib import Path
import sys
import tempfile

from azure.storage.blob import ContainerClient
from azure.storage.blob import BlobServiceClient, BlobClient

from fastmri_to_dicom import fastmri_to_dicom

def isempty(iterable):
    try:
        first = next(iterable)
    except StopIteration:
        return True
    return False

def process_container(connection_string: str,
                      container_in: str,
                      container_out: str,
                      prefix: list) -> None:

    con_in = ContainerClient.from_connection_string(connection_string, container_name=container_in)
    con_out = ContainerClient.from_connection_string(connection_string, container_name=container_out)

    for pre in prefix:
        blob_list = con_in.list_blobs(pre)
        for blob in blob_list:
            dicomBlobPath = os.path.splitext(blob.name)[0]
            dcmbloblist = con_out.list_blobs(dicomBlobPath)
            if not isempty(dcmbloblist):
                print('Blob ' + blob.name + ' has been processed')
                continue
            else:
                print('Blob ' + blob.name + ' has NOT been processed')

            d = tempfile.TemporaryDirectory(dir = "./")
            destBlobPath = Path(d.name)/blob.name
            destBlobPath.parent.mkdir(parents=True, exist_ok=True)

            # Download the blob
            if not destBlobPath.exists():
                blobbytes = con_in.get_blob_client(blob).download_blob().readall()
                with open(destBlobPath, 'wb') as outfile:
                    outfile.write(blobbytes)
            
            # Convert to DICOM
            dicomFolder = Path(d.name)/dicomBlobPath
            dicomFolder.mkdir(parents = True, exist_ok = True)
            fastmri_to_dicom(filename = destBlobPath, reconstruction_name = "reconstruction_rss", outfolder = dicomFolder)

            dicomFiles = dicomFolder.glob('*.dcm')
            for dcm in dicomFiles:
                blobclient = con_out.get_blob_client(dicomBlobPath + '/' + dcm.name)
                with open(dcm.absolute(), 'rb') as dcmfile:
                    blobclient.upload_blob(dcmfile)

            d.cleanup()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert fastMRI file to DICOMs')
    parser.add_argument('--connection_string' , type=str, help='Storage account connection string', required=True)
    parser.add_argument('--container_in' , type=str, help='Input container', required=True)
    parser.add_argument('--container_out' , type=str, help='Ouput container', required=True)
    parser.add_argument('--prefix', nargs='+', type=str, help='Prefixes', required = True)
    args = parser.parse_args()

    process_container(connection_string=args.connection_string, container_in=args.container_in, container_out = args.container_out, prefix=args.prefix)
