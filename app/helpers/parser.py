import re


def unique_error_msg_parser(msg):
    if "duplicate key error collection" in msg:
        extracted_fields = re.search('index: (.*) dup', msg).group(1)
        # replacing '_1_' with 'and' to form expression
        suffix = extracted_fields.replace('_1_', ' və ').replace('_1', '')

    else:
        suffix = "data"
    return f"Qeyd edilən xana(lar) üçün məlumat artıq mövuddur: ({suffix})"
