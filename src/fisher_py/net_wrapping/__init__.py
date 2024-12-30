import pythonnet

# Load dotnet before clr import. See https://pythonnet.github.io/pythonnet/python.html#loading-a-runtime
try:
  pythonnet.load()  # Try default (i.e. 'mono' or PYTHONNET_RUNTIME)
except:
  pythonnet.load('coreclr')  # Fallback on coreclr

import clr
import os
from fisher_py.net_wrapping.net_wrapper_base import NetWrapperBase
from System import Environment

# codecs for implicit enum conversion
import Python.Runtime

Python.Runtime.PyObjectConversions.RegisterEncoder(Python.Runtime.Codecs.EnumPyIntCodec.Instance)
Python.Runtime.PyObjectConversions.RegisterDecoder(Python.Runtime.Codecs.EnumPyIntCodec.Instance)


# access .net standard dlls
dotnet_version = Environment.Version.get_Major()
dll_base_path = os.path.join(os.path.split(__file__)[0], '..', 'dll')

if dotnet_version >= 8:
  dll_path = os.path.join(dll_base_path, 'net8')
elif dotnet_version >= 5:
  dll_path = os.path.join(dll_base_path, 'net5')
else:
  dll_path = os.path.join(dll_base_path, 'net4')

clr.AddReference('System')
clr.AddReference('System.Core')
clr.AddReference('System.Data')
clr.AddReference('System.Configuration')
clr.AddReference('System.Xml')
clr.AddReference('mscorlib')

clr.AddReference(os.path.join(dll_path, 'ThermoFisher.CommonCore.Data.dll'))
clr.AddReference(os.path.join(dll_path, 'ThermoFisher.CommonCore.RawFileReader.dll'))
clr.AddReference(os.path.join(dll_path, 'ThermoFisher.CommonCore.MassPrecisionEstimator.dll'))
clr.AddReference(os.path.join(dll_path, 'ThermoFisher.CommonCore.BackgroundSubtraction.dll'))
try:
    clr.AddReference(os.path.join(dll_path, 'OpenMcdf.dll'))
except Exception as e:
    pass  # avoid duplicate load

# import .net standard libaries
import ThermoFisher.CommonCore.Data as thermo_fisher_data
from ThermoFisher.CommonCore.Data import Extensions
import ThermoFisher.CommonCore.Data.Business as thermo_fisher_data_business
import ThermoFisher.CommonCore.Data.FilterEnums as thermo_fisher_data_filter_enums
import ThermoFisher.CommonCore.Data.Interfaces as thermo_fisher_data_interfaces
import ThermoFisher.CommonCore.MassPrecisionEstimator as thermo_fisher_mass_precision_estimator
import ThermoFisher.CommonCore.RawFileReader as thermo_fisher_raw_file_reader
import ThermoFisher.CommonCore.MassPrecisionEstimator as thermo_fisher_mass_precision_estimator

# expose .net libraries in a friendly manner
class _Data:

    Business = thermo_fisher_data_business
    FilterEnums = thermo_fisher_data_filter_enums
    Interfaces = thermo_fisher_data_interfaces
    Extensions = Extensions


class ThermoFisher:

    class CommonCore:
        Data = _Data()
        MassPrecisionEstimator = thermo_fisher_mass_precision_estimator
        RawFileReader = thermo_fisher_raw_file_reader
        MassPrecisionEstimator = thermo_fisher_mass_precision_estimator
