
import re

def redact_free_text(free_text: str) -> str:
    """
    :param: free_text The free text to remove sensitive data from
    :returns: The redacted free text
    """
    # TODO: Implement this! Feel free to change the function parameters if you need to
    # Regular expressions for detecting and redacting sensitive information
    name_pattern = re.compile(r'\b([A-Z][a-z]+)\b')
    phone_number_pattern = re.compile(r'\b(?:\(\d{3}\)|\d{3})(?:[ -]?\d{3}[ -]?\d{4})\b')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    national_id_pattern = re.compile(r'\b(?:\d{3}[ -]?\d{2}[ -]?\d{4})\b')

    # Redact sensitive information in the free text
    redacted_text = free_text
    redacted_text = name_pattern.sub('[REDACTED NAME]', redacted_text)
    redacted_text = phone_number_pattern.sub('[REDACTED PHONE NUMBER]', redacted_text)
    redacted_text = email_pattern.sub('[REDACTED EMAIL]', redacted_text)
    redacted_text = national_id_pattern.sub('[REDACTED NATIONAL ID]', redacted_text)

    return redacted_text
    #raise NotImplementedError()
