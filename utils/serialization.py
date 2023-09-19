import dataclasses


def enhanced_json_serializer(obj):
    if dataclasses.is_dataclass(obj):
        return dataclasses.asdict(obj)
    raise TypeError(f"Type {type(obj)} not serializable")
