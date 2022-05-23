keys = []


def config(secret):
    keys.append(secret)
    return secret


def get_secret():
    return keys
