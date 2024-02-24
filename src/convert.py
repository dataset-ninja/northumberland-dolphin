import os
import shutil
from urllib.parse import unquote, urlparse

import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_name,
    get_file_name_with_ext,
)
from supervisely.io.json import load_json_file
from tqdm import tqdm

import src.settings as s


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(
            desc=f"Downloading '{file_name_with_ext}' to buffer...",
            total=fsize,
            unit="B",
            unit_scale=True,
        ) as pbar:
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    ### Function should read local dataset and upload it to Supervisely project, then return project info.###
    dataset_path = "/home/alex/DATASETS/TODO/Dolphin Dataset/NDD20"
    batch_size = 30
    images_ext = ".jpg"
    ds_name = "ds"

    def create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        image_name = get_file_name_with_ext(image_path)
        image_data = im_name_to_data[image_name]

        for curr_im_data in image_data:
            l_tags = []
            poly_data = curr_im_data["shape_attributes"]
            region_data = curr_im_data["region_attributes"]
            id_value = region_data.get("id")
            if id_value is not None:
                id_tag = sly.Tag(id_meta, value=int(id_value))
                l_tags.append(id_tag)

            if region_data.get("species") is not None:
                specie_meta = specie_to_meta.get(region_data["species"])
                species = sly.Tag(specie_meta)
                l_tags.append(species)

            if region_data.get("out of focus") is True:
                focus = sly.Tag(out_of_focus_meta)
                l_tags.append(focus)
            exterior = []
            x_coords = poly_data["all_points_x"]
            y_coords = poly_data["all_points_y"]
            for x, y in zip(x_coords, y_coords):
                exterior.append([int(y), int(x)])
            poligon = sly.Polygon(exterior)
            label_poly = sly.Label(poligon, obj_class, tags=l_tags)
            labels.append(label_poly)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=[tag])

    obj_class = sly.ObjClass("dolphin", sly.Polygon)

    above_meta = sly.TagMeta("above", sly.TagValueType.NONE)
    below_meta = sly.TagMeta("below", sly.TagValueType.NONE)

    id_meta = sly.TagMeta("id", sly.TagValueType.ANY_NUMBER)

    bnd_meta = sly.TagMeta("tursiops truncatus", sly.TagValueType.NONE)
    wbd_meta = sly.TagMeta("lagenorhynchus albirostris", sly.TagValueType.NONE)

    out_of_focus_meta = sly.TagMeta("out of focus", sly.TagValueType.NONE)

    specie_to_meta = {"BND": bnd_meta, "WBD": wbd_meta}

    name_to_meta = {"ABOVE": above_meta, "BELOW": below_meta}

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=[obj_class],
        tag_metas=[above_meta, below_meta, id_meta, bnd_meta, wbd_meta, out_of_focus_meta],
    )
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    for subfolder in os.listdir(dataset_path):
        curr_folder = os.path.join(dataset_path, subfolder)
        if dir_exists(curr_folder):

            images_names = os.listdir(curr_folder)
            tag_meta = name_to_meta[subfolder]
            tag = sly.Tag(tag_meta)

            ann_path = curr_folder + "_LABELS.json"

            im_name_to_data = {}
            ann = load_json_file(ann_path)
            for curr_ann in ann.values():
                im_name_to_data[curr_ann["filename"]] = curr_ann["regions"]

            progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

            for images_names_batch in sly.batched(images_names, batch_size=batch_size):
                img_pathes_batch = [
                    os.path.join(curr_folder, image_name) for image_name in images_names_batch
                ]

                full_im_names = [
                    subfolder.lower() + "_" + im_name for im_name in images_names_batch
                ]

                img_infos = api.image.upload_paths(dataset.id, full_im_names, img_pathes_batch)
                img_ids = [im_info.id for im_info in img_infos]

                anns = [create_ann(image_path) for image_path in img_pathes_batch]
                api.annotation.upload_anns(img_ids, anns)

                progress.iters_done_report(len(images_names_batch))

    return project
