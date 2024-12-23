import enum

class SpectrumPacketType(enum.Enum):
    """
    The spectrum packet types. Internally, within raw files, these are defined simply
    as "a short integer packet type" These are then mapped to "constants". It is
    possible that types may be returned by from raw data, or other transmissions,
    which are outside of this range. These types define original compression formats
    from instruments. Note that most data values are returned as "float", when using
    IRawDataPlus regardless of the compressed file format used.
    """
    NoPacketType = -1
    ProfileSpectrum = 0
    LowResolutionSpectrum = 1
    HighResolutionSpectrum = 2
    ProfileIndex = 3
    CompressedAccurateSpectrum = 4
    StandardAccurateSpectrum = 5
    StandardUncalibratedSpectrum = 6
    AccurateMassProfileSpectrum = 7
    PdaUvDiscreteChannel = 8
    PdaUvDiscreteChannelIndex = 9
    PdaUvScannedSpectrum = 10
    PdaUvScannedSpectrumIndex = 11
    UvChannel = 12
    MassSpecAnalog = 13
    ProfileSpectrumType2 = 14
    LowResolutionSpectrumType2 = 15
    ProfileSpectrumType3 = 16
    LowResolutionSpectrumType3 = 17
    LinearTrapCentroid = 18
    LinearTrapProfile = 19,
    FtCentroid = 20
    FtProfile = 21
    HighResolutionCompressedProfile = 22
    LowResolutionCompressedProfile = 23
    LowResolutionSpectrumType4 = 24
    InvalidPacket = 25
