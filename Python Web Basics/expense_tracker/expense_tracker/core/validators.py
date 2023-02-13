from django.core.exceptions import ValidationError


def megabytes_to_bytes(mb):
    return mb * 1024 * 1024


def raise_if_not_letters(value):
    if not value.isalpha():
        raise ValidationError("Ensure this value contains only letters.")


def validate_file_less_than_5MB(fileobj):
    filesize = fileobj.file.size
    megabyte_limit = 5
    if filesize > megabytes_to_bytes(megabyte_limit):
        raise ValidationError(f"Max file size is 5.00 MB")
