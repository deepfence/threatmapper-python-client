# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from threatmapper.paths.deepfence_search_count_hosts import Api

from threatmapper.paths import PathValues

path = PathValues.DEEPFENCE_SEARCH_COUNT_HOSTS