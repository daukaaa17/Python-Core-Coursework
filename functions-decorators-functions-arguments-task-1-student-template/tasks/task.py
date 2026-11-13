from typing import Dict, Any, Callable, Iterable
DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]
def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    for filter_func in filters:
        data = filter_func(data)
    return selector(data)
def select(*columns: str) -> ModifierFunc:
    def selector(data: DataType) -> DataType:
        return [{col: item[col] for col in columns if col in item} for item in data]
    return selector
def field_filter(column: str, *values: Any) -> ModifierFunc:
    def filter_func(data: DataType) -> DataType:
        return [item for item in data if item.get(column) in values]
    return filter_func
def test_query():
    friends = [{'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()

