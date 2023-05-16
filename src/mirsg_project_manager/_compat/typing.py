"""
Copyright (c) 2023 Haroon Raza Chughtai. All rights reserved.

mirsg_project_manager: Notebooks and tools to help with managing MIRSG projects
"""


from __future__ import annotations

import sys

if sys.version_info < (3, 8):
    from typing_extensions import Literal, Protocol, runtime_checkable
else:
    from typing import Literal, Protocol, runtime_checkable

__all__ = ["Protocol", "runtime_checkable", "Literal"]


def __dir__() -> list[str]:
    return __all__
