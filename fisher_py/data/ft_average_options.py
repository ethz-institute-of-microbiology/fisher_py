from fisher_py.net_wrapping import NetWrapperBase, ThermoFisher


class FtAverageOptions(NetWrapperBase):
    """
    Options which can be used to control the Ft / Orbitrap averaging
    """

    _wrapped_type = ThermoFisher.CommonCore.Data.Interfaces.FtAverageOptions

    def __init__(self):
        super().__init__()
        self._wrapped_object = self._wrapped_type()

    @property
    def max_charge_determinations(self) -> int:
        """
        Gets or sets the maximum number of ions which are sent to the charge pattern
        calculation (starting from most intense)
        """
        return self._get_wrapped_object_().MaxChargeDeterminations

    @max_charge_determinations.setter
    def max_charge_determinations(self, value: int):
        """
        Gets or sets the maximum number of ions which are sent to the charge pattern
        calculation (starting from most intense)
        """
        assert type(value) is int
        self._get_wrapped_object_().MaxChargeDeterminations = value

    @property
    def merge_in_parallel(self) -> bool:
        """
        Gets or sets a value indicating whether parallel code may be used for resampling
        and merging scans. Tuning option: Permit separate threads to be used for resampling
        profiles.
        """
        return self._get_wrapped_object_().MergeInParallel

    @merge_in_parallel.setter
    def merge_in_parallel(self, value: bool):
        """
        Gets or sets a value indicating whether parallel code may be used for resampling
        and merging scans. Tuning option: Permit separate threads to be used for resampling
        profiles.
        """
        assert type(value) is bool
        self._get_wrapped_object_().MergeInParallel = value

    @property
    def max_scans_merged(self) -> int:
        """
        Gets or sets the maximum number of scans which can be merged at once. This feature
        is currently not yet implemented, and the value is ignored. When MergeInParallel
        is enabled: this restricts the number of scans which are merged in each group.
        Setting this too large may result in more memory allocation for "arrays of results
        to merge" Default: 10
        """
        return self._get_wrapped_object_().MaxScansMerged

    @max_scans_merged.setter
    def max_scans_merged(self, value: int):
        """
        Gets or sets the maximum number of scans which can be merged at once. This feature
        is currently not yet implemented, and the value is ignored. When MergeInParallel
        is enabled: this restricts the number of scans which are merged in each group.
        Setting this too large may result in more memory allocation for "arrays of results
        to merge" Default: 10
        """
        assert type(value) is int
        self._get_wrapped_object_().MaxScansMerged = value

    @property
    def merge_task_batching(self) -> int:
        """
        Gets or sets the minimum number of Re-sample tasks per thread. Tuning parameter
        when MergeInParallel is set. Each scan is analyzed: Determining mass regions
        which contain non-zero data, and re-sampling the intensity data aligned to a
        set of output bins. After all scans have been re-sampled, the re-sampled data
        has to be merged into the final output. Creating re-sampled data for profiles
        is a fairly fast task. It may be inefficient to queue workers to created the
        merged data for each scan in the batch. Setting this >1 will reduce threading
        overheads, when averaging small batches of scans with low intensity peaks. Default:
        2. This feature only affects the re-sampling, as the final merge of the re-sampled
        data is single threaded.
        """
        return self._get_wrapped_object_().MergeTaskBatching

    @merge_task_batching.setter
    def merge_task_batching(self, value: int):
        """
        Gets or sets the minimum number of Re-sample tasks per thread. Tuning parameter
        when MergeInParallel is set. Each scan is analyzed: Determining mass regions
        which contain non-zero data, and re-sampling the intensity data aligned to a
        set of output bins. After all scans have been re-sampled, the re-sampled data
        has to be merged into the final output. Creating re-sampled data for profiles
        is a fairly fast task. It may be inefficient to queue workers to created the
        merged data for each scan in the batch. Setting this >1 will reduce threading
        overheads, when averaging small batches of scans with low intensity peaks. Default:
        2. This feature only affects the re-sampling, as the final merge of the re-sampled
        data is single threaded.
        """
        assert type(value) is int
        self._get_wrapped_object_().MergeTaskBatching = value

    @property
    def use_noise_table_when_available(self) -> bool:
        """
        Gets or sets a value indicating whether to use the noise and baseline table.
        When set: The averaging algorithm calculates average noise based on a noise table
        obtained (separately) from the raw file. The "IRawData" interface doe not have
        methods to obtain this "noise and baseline table" from the raw file. So: The
        scan averaging algorithm (by default) uses noise information saved with centroid
        peaks when calculating the averaged noise. This option is only effective when
        data is read via the IRawDataPlus interface.
        """
        return self._get_wrapped_object_().UseNoiseTableWhenAvailable

    @use_noise_table_when_available.setter
    def use_noise_table_when_available(self, value: bool):
        """
        Gets or sets a value indicating whether to use the noise and baseline table.
        When set: The averaging algorithm calculates average noise based on a noise table
        obtained (separately) from the raw file. The "IRawData" interface doe not have
        methods to obtain this "noise and baseline table" from the raw file. So: The
        scan averaging algorithm (by default) uses noise information saved with centroid
        peaks when calculating the averaged noise. This option is only effective when
        data is read via the IRawDataPlus interface.
        """
        assert type(value) is bool
        self._get_wrapped_object_().UseNoiseTableWhenAvailable = value

