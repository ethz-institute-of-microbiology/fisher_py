import enum


class FileType(enum.Enum):
    """
    The type of the file.
    """
    NotSupported = 0
    ExperimentMethod = 1
    SampleList = 2
    ProcessingMethod = 4
    TuneMethod = 16
    ResultsFile = 32
    QuanFile = 64
    CalibrationFile = 128
    MethodFile = 256
    XqnFile = 512
    LayoutFile = 4096
    MethodEditorLayout = 4160
    SampleListEditorLayout = 4224
    ProcessingMethodEditLayout = 4352
    QualBrowserLayout = 4608
    TuneLayout = 5120
    ResultsLayout = 6144
