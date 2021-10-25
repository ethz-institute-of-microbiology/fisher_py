import enum


class TraceType(enum.Enum):
    """
     Enumeration of trace types, for chromatograms. Note: legacy C++ file reader does
    not support analog trace numbers above "4" or UV above "channel D". Traces are
    organized in blocks of 10 For example: StartAnalogChromatogramTraces=10 (not
    a valid trace type, just a limit) Analog1 to Analog8 = 11 to 18 EndAnalogChromatogramTraces
    =19 (not a valid trace type, just a limit) Next block: StartPDAChromatogramTraces
    = 20 Etc.
    """
    StartMSChromatogramTraces = -1
    MassRange = 0
    TIC = 1
    BasePeak = 2
    Fragment = 3
    EndMSChromatogramTraces = 4
    StartAnalogChromatogramTraces = 10
    Analog1 = 11
    Analog2 = 12
    Analog3 = 13
    Analog4 = 14
    Analog5 = 15
    Analog6 = 16
    Analog7 = 17
    Analog8 = 18
    EndAnalogChromatogramTraces = 19
    StartPDAChromatogramTraces = 20
    WavelengthRange = 21
    TotalAbsorbance = 22
    SpectrumMax = 23
    EndPDAChromatogramTraces = 24
    StartUVChromatogramTraces = 30
    ChannelA = 31
    ChannelB = 32
    ChannelC = 33
    ChannelD = 34
    ChannelE = 35
    ChannelF = 36
    ChannelG = 37
    ChannelH = 38
    EndUVChromatogramTraces = 39
    StartPCA2DChromatogramTraces = 40
    A2DChannel1 = 41
    A2DChannel2 = 42
    A2DChannel3 = 43
    ChromatogramA2DChannel3 = 43
    A2DChannel4 = 44
    ChromatogramA2DChannel4 = 44
    A2DChannel5 = 45
    A2DChannel6 = 46
    A2DChannel7 = 47
    A2DChannel8 = 48
    EndPCA2DChromatogramTraces = 49
    EndAllChromatogramTraces = 50
