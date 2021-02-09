class NameTooShortError(Exception):
    def __init__(self):
        super().__init__('Name must be more than 4 characters')


class MustContainAtSymbolError(Exception):
    def __init__(self):
        super().__init__('Email must contain @')


class InvalidDomainError(Exception):
    def __init__(self):
        super().__init__('Domain must be one of the following: .com, .bg, .org, .net')


def validate_email(email):
    if '@' not in email:
        raise MustContainAtSymbolError
    name, domain = email.split('@')
    if len(name) < 4:
        raise NameTooShortError
    try:
        _, top_level_domain = domain.split('.')
        if top_level_domain not in ('com', 'bg', 'org', 'net'):
            raise InvalidDomainError
    except ValueError:
        raise InvalidDomainError
    return True


while True:
    command = input()
    if command == 'End':
        break
    if validate_email(command):
        print('Email valid')
