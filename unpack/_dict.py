def from_dict(dict_to_unpack: dict[str, str]):
    result = tuple([dict_to_unpack[k] for k in dict_to_unpack])
    if len(result) == 1:
        result, = result
    return result