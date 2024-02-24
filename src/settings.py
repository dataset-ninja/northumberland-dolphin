from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Northumberland Dolphin"
PROJECT_NAME_FULL: str = "NDD20: The Northumberland Dolphin Dataset 2020"
HIDE_DATASET = True  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_SA_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [
    Research.Environmental(),
    Industry.Robotics(),
]
CATEGORY: Category = Category.Environmental(extra=[Category.Robotics(), Category.Biology()])

CV_TASKS: List[CVTask] = [CVTask.SemanticSegmentation(), CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.SemanticSegmentation()]

RELEASE_DATE: Optional[str] = "2020-05-27"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = (
    "https://data.ncl.ac.uk/collections/The_Northumberland_Dolphin_Dataset_2020/4982342/1"
)
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 14255358
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/northumberland-dolphin"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = (
    "https://data.ncl.ac.uk/articles/dataset/NDD20_zip/12357383?backTo=/collections/The_Northumberland_Dolphin_Dataset_2020/4982342"
)
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = "https://arxiv.org/pdf/2005.13359"
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = None

CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = [
    "Cameron Trotter",
    "Georgia Atkinson",
    "Matt Sharpe",
    "Kirsten Richardson",
    "Stephen McGough",
    "Nick Wright",
    "Ben Burville",
    "Per Berggren",
]
AUTHORS_CONTACTS: Optional[List[str]] = [
    "c.trotter2@ncl.ac.uk",
    "g.atkinson@ncl.ac.uk",
    "m.j.sharpe@ncl.ac.uk",
    "k.crane2@ncl.ac.uk",
    "stephen.mcgough@ncl.ac.uk",
    "nick.wright@ncl.ac.uk",
    "ben.burville@ncl.ac.uk",
    "per.berggren@ncl.ac.uk",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "Newcastle University, UK"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://www.ncl.ac.uk/"

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "positions": ["above", "below"],
    "dolphins species": ["tursiops truncatus", "lagenorhynchus albirostris"],
    "__POSTTEXT__": "Additionally, some labels marked with dolphin ***id*** and ***out of focus*** tags",
}
TAGS: Optional[List[str]] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
