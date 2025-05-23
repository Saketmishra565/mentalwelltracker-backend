def validate_username(username: str):
    if " " in username:
        raise ValueError("Username must not contain spaces.")
    return username
