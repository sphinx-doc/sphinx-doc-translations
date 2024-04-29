#!/usr/bin/env python3
"""
Convert a lowercased IETF language tag (ll-cc) to Gettext's ISO 639 (ll_CC),
and print the result.

This script will return the same input value if the language tag doesn't have
the country part (ll) or it is already a Gettext's ISO 639 (ll_CC).

Exit with error in case the input is not a valid language tag
(i.e. not ll-cc or ll_CC)
"""

import argparse
import re
import sys

IETF_LANG_TAG_PATTERN = r"^[a-z]{2}-[a-z]{2}$"
A_LANG_TAG_PATTERN = r"^[a-z]{2}(-[a-z]{2}|_[A-Z]{2})?$"


def is_valid_language_tag(input_str: str, pattern: str) -> bool:
    """Check if the input string matches the language tag pattern."""
    return bool(re.match(pattern, input_str))


def convert_to_iso639_gettext(input_str: str) -> str:
    """Convert a ll-cc to ll_CC language code."""
    first_part, _, last_part = input_str.partition("-")
    return f"{first_part}_{last_part.upper()}"


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("language")
    arg = parser.parse_args()

    if not is_valid_language_tag(arg.language, A_LANG_TAG_PATTERN):
        sys.exit(
            f"Error: Expected a language code like pt_BR or pt-br. "
            f"Invalid language code given: {arg.language}"
        )

    output_language = (
        convert_to_iso639_gettext(arg.language)
        if is_valid_language_tag(arg.language, IETF_LANG_TAG_PATTERN)
        else arg.language
    )
    print(output_language)


if __name__ == "__main__":
    main()
