#!/usr/bin/env python3
"""
Convert a READTHEDOCS_LANGUAGE (ll-cc) to Sphinx-compatible format (ll_CC),
and print the result.

This script reads Read the Docs's READTHEDOCS_LANGUAGE environment variable,
and convert ll-cc into ll_CC.

The output is the same as input if the input language has only language
without country part ('ll') or is already Gettext's ISO 639 (ll_CC).

Exit with error in case READTHEDOCS_LANGUAGE is not set or th input is not
one of the valid language formats (ll, ll-cc or ll_CC)
"""

import os
import re
import sys

IETF_LANG_TAG_PATTERN = r"^[a-z]{2}-[a-z]{2}$"
A_LANG_TAG_PATTERN = r"^[a-z]{2}(-[a-z]{2}|_[A-Z]{2})?$"


def match_language_tag(input_str: str, pattern: str) -> bool:
    """Match the *input_str* string with the language tag *pattern*."""
    return bool(re.match(pattern, input_str))


def convert_to_iso639_gettext(input_str: str) -> str:
    """Convert *input_str* from ll-cc to ll_CC language format."""
    first_part, _, last_part = input_str.partition("-")
    return f"{first_part}_{last_part.upper()}"


def main():
    rtd_language = os.getenv("READTHEDOCS_LANGUAGE")
    if not rtd_language:
        sys.exit(
            "Error: READTHEDOCS_LANGUAGE not set, "
            + "is this being run in readthedocs build env?"
        )

    if not match_language_tag(rtd_language, A_LANG_TAG_PATTERN):
        sys.exit(
            "Error: Expected a language code like pt, pt_BR or pt-br. "
            f"Invalid language code given: {rtd_language}"
        )

    output_language = (
        convert_to_iso639_gettext(rtd_language)
        if match_language_tag(rtd_language, IETF_LANG_TAG_PATTERN)
        else rtd_language
    )
    print(output_language)


if __name__ == "__main__":
    main()
