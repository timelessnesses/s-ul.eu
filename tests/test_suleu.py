import os

import pytest

import suleu


def test_main():
    a = suleu.Upload(os.getenv("TOKEN"))
    b = a.file_upload("tests/test.txt", raw=True)
    c = suleu.Delete(os.getenv("TOKEN"))
    d = c.delete(b["filename"], raw=True)
