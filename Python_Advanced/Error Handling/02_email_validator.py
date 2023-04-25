class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def domain_is_invalid(domain, valid_domains):
    result = True
    for valid_domain in valid_domains:
        if domain.endswith(valid_domain):
            result = False
            break
    return result


valid_domains = ['.com', '.bg', '.org', '.net']
while True:
    email = input()
    if email == 'End':
        break

    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    username, domain_and_extension = email.split('@')

    if len(username) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    if domain_is_invalid(domain_and_extension, valid_domains):
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join(valid_domains)}')

    print('Email is valid')
