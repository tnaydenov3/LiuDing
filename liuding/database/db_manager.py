import pymain

class DatabaseManager(Singleton):

    @staticmethod
    def _settings_dir() -> pymain.Path:
        raise NotImplementedError

    def __init__(self) -> None:
        self._dl_manager = DownloaderManager(self._settings_dir())

    @property
    def dl_manager(self) -> DownloaderManager:
        return self._dl_manager