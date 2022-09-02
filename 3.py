from typing import Union

def normalize_id(user_id: Union[int, str]) -> str:
    if isinstance(user_id, int):
        return 'user-{}'.format(100000 + user_id)
    else:
        return user_id

print(normalize_id(6))
print(normalize_id('67'))
print(normalize_id(9.56))   