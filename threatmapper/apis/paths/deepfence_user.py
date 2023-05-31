from threatmapper.paths.deepfence_user.get import ApiForget
from threatmapper.paths.deepfence_user.put import ApiForput
from threatmapper.paths.deepfence_user.delete import ApiFordelete


class DeepfenceUser(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
