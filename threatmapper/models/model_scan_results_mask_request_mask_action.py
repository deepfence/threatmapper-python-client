from enum import Enum


class ModelScanResultsMaskRequestMaskAction(str, Enum):
    MASK_ALL_IMAGE_TAG = "mask_all_image_tag"
    MASK_ENTITY = "mask_entity"
    MASK_GLOBAL = "mask_global"
    MASK_IMAGE_TAG = "mask_image_tag"

    def __str__(self) -> str:
        return str(self.value)
