from threatmapper.paths.deepfence_users_id.get import ApiForget
from threatmapper.paths.deepfence_users_id.put import ApiForput
from threatmapper.paths.deepfence_users_id.delete import ApiFordelete


class DeepfenceUsersId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
