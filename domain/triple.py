# from dataclasses import dataclass


# @dataclass
# class Triple:
#     subject: str
#     predicate: str
#     object: str

from dataclasses import dataclass


@dataclass
class Triple:

    subject: str
    subject_type: str

    predicate: str

    object: str
    object_type: str