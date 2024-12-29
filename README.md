# fisher_py
This Python module allows access to Thermo Orbitrap raw mass spectrometer files. Using this library makes it possible to automate the analysis of mass spectra, without having to export the data first with another tool. This module is a wrapper that builds uppon the RawFileReader project which is a library developed for C#. Structures have been implemented to make processing data more convenient for Python users.

## Installation
fisher_py can be installed via the package repository [PyPi](https://pypi.org/):
```
pip install fisher_py
```

## System Requirements
fishery_py shoud work on any modern desktop operating system (Linux, Windows, Mac OS) with Python 3.6 (or higher) installed.
- Windows: Tested on Windows 10 Pro x64
- Linux: Tested on Ubuntu 20.04 LTS x64
- Mac OS: Not tested

The module relies on the RawFileReader DLLs (Dynamic-Linked-Libraries) to be loaded at runtime (using [pythonnet](https://github.com/pythonnet/pythonnet)). Since Microsoft introduced .NET Standard it is possible to load DLLs compiled with this framework to be loaded on non-Windows systems (such as Mac OS and Linux). However, systems other than Windows may require additional setup steps in order for fisher_py to work.
If you have trouble problems installing fisher_py it is probably because of pythonnet not being able to compile. To resolve this the usualy path is to install the [.Net 8.0 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/8.0).

## Examples
The following example demonstrates how to extract and plot data from a raw-file:
```python
import matplotlib.pyplot as plt
from fisher_py import RawFile
from fisher_py.data.business import TraceType
raw_file = RawFile('my_file.raw')

target_mass = 848.36862
mass_tolerance_ppm = 10
rt, i = raw_file.get_chromatogram(target_mass, mass_tolerance_ppm, TraceType.MassRange)
mz, i2, charges, real_rt = raw_file.get_scan_ms1(1)
print(real_rt)

plt.figure()
plt.plot(rt, i)

plt.figure()
plt.plot(mz, i2)

plt.show()
```

This example may be fine for some use-cases but the RawFile class only provides limited access to all the functionalities and can serve as an example how to use the module wihtin a project.
For an example that uses more of the modules capabilites have a look at [raw_file_reader_examle.py](https://github.com/ethz-institute-of-microbiology/fisher_py/blob/main/examples/raw_file_reader_example.py).

## License and copyright
fisher_py (Copyright 2021 ethz-institute-of-microbiology) is licensed under the  MIT license.

### Third-party licenses and copyright

RawFileReader reading tool. Copyright © 2016 by Thermo Fisher Scientific, Inc. All rights reserved. See [RawFileReaderLicense.md](https://github.com/ethz-institute-of-microbiology/fisher_py/blob/main/RawFileReaderLicense.md) for licensing information. 
Note: anyone recieving RawFileReader as part of a larger software distribution (in the current context, as part of fisher_py) is considered an "end user" under 
section 3.3 of the RawFileReader License, and is not granted rights to redistribute RawFileReader.

Some of the test data used is taken from the [Thermo-Raw-File-Reader](https://github.com/PNNL-Comp-Mass-Spec/Thermo-Raw-File-Reader) repository maintained by [Pacific Northwest National Laboratory](https://github.com/PNNL-Comp-Mass-Spec) and is licensed under the [2-Clause BSD License](https://opensource.org/licenses/BSD-2-Clause).
