#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from base64 import b64encode, b64decode
from hashlib import sha256
from hmac import HMAC


def sastoken(sign_key, key):
    signature = b64encode(
        HMAC(b64decode(key), sign_key.encode("utf-8"), sha256).digest())
    return signature


class FilterModule():
    @staticmethod
    def filters():
        return {
            "sastoken": sastoken,
        }


class TestFiltersFunctions(unittest.TestCase):
    def test_sastoken(self):
        self.assertEqual(
            sastoken(
                '1585061666',
                "8Js3Ow87vJ6p7Xi1/NEgLU+H4juNk1eqmEQHVhlMg1Y="  #pragma: allowlist secret
            ),
            b'eiYjcy1Xvj/ecEOClmkp0bMAhGFzQcjhnsuTUpBZoJM='  #pragma: allowlist secret
        )
        self.assertEqual(
            sastoken(
                "Hello",
                "8Js3Ow87vJ6p7Xi1/NEgLU+H4juNk1eqmEQHVhlMg1Y="  #pragma: allowlist secret
            ),
            b'QmeSkGao5fY06NZGby7SmwvgxahU9oKql8PAofixpVg='  #pragma: allowlist secret
        )

    @staticmethod
    def test_pytest():
        assert sastoken(
            '1585061666',
            "8Js3Ow87vJ6p7Xi1/NEgLU+H4juNk1eqmEQHVhlMg1Y="  #pragma: allowlist secret
        ) == b'eiYjcy1Xvj/ecEOClmkp0bMAhGFzQcjhnsuTUpBZoJM='  #pragma: allowlist secret


if __name__ == '__main__':
    unittest.main()
