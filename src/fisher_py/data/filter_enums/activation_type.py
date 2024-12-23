import enum


class ActivationType(enum.Enum):
    """
    The activation types are used to link a specific precursor mass with an activation
    type. There are 26 possible mode values, including some reserved values.
    """
    CollisionInducedDissociation = 0
    MultiPhotonDissociation = 1
    ElectronCaptureDissociation = 2
    PQD = 3
    ElectronTransferDissociation = 4
    HigherEnergyCollisionalDissociation = 5
    Any = 6
    SAactivation = 7
    ProtonTransferReaction = 8
    NegativeElectronTransferDissociation = 9
    NegativeProtonTransferReaction = 10
    UltraVioletPhotoDissociation = 11
    ModeA = 12
    ModeB = 13
    ModeC = 14
    ModeD = 15
    ModeE = 16
    ModeF = 17
    ModeG = 18
    ModeH = 19
    ModeI = 20
    ModeJ = 21
    ModeK = 22
    ModeL = 23
    ModeM = 24
    ModeN = 25
    ModeO = 26
    ModeP = 27
    ModeQ = 28
    ModeR = 29
    ModeS = 30
    ModeT = 31
    ModeU = 32
    ModeV = 33
    ModeW = 34
    ModeX = 35
    ModeY = 36
    ModeZ = 37
    LastActivation = 38