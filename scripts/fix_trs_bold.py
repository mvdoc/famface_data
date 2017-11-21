#!/usr/bin/env python
import nibabel as nib
import sys

tofix = sys.argv[1]
img = nib.load(tofix)
old_zooms = img.header.get_zooms()
new_zooms = [z for z in old_zooms[:3]] + [2.0]
img.header.set_zooms(new_zooms)
img.to_filename(tofix.replace('.nii.gz', '_trfixed.nii.gz'))
