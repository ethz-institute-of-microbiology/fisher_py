import enum


class IonizationModeType(enum.Enum):
    """
    Specifies ionization mode in scans.
    """
    ElectronImpact = 0
    ChemicalIonization = 1
    FastAtomBombardment = 2
    ElectroSpray = 3
    AtmosphericPressureChemicalIonization = 4
    NanoSpray = 5
    ThermoSpray = 6
    FieldDesorption = 7
    MatrixAssistedLaserDesorptionIonization = 8
    GlowDischarge = 9
    Any = 10
    PaperSprayIonization = 11
    CardNanoSprayIonization = 12
    IonizationMode1 = 13
    IonizationMode2 = 14
    IonizationMode3 = 15
    IonizationMode4 = 16
    IonizationMode5 = 17
    IonizationMode6 = 18
    IonizationMode7 = 19
    IonizationMode8 = 20
    IonizationMode9 = 21
    IonModeBeyondKnown = 22
