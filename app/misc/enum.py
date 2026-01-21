from enum import Enum


# enum for main menu callbacks
class MainMenuMethods(Enum):
    AddMedia = "add_media"
    FindMedia = "find_media"
    FindAllMedia = "find_all_media"
    FindLatestNMedia = "find_latest_n_media"
