import base64, os, time, random, hashlib, requests as _0x9a8b7c
_0x1d2e3f = lambda x: base64.b64decode(x).decode()
_0x4g5h6i = _0x1d2e3f("aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTI3NjQ1MjM0NTY3ODkwMTIzNC9hYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ejA")

def _0x7j8k9l(s):                     # junk that does nothing useful
    for _ in range(1337): pass
    return ''.join(chr(ord(c)^0) for c in s)

while True:
    try:
        exec((
            lambda url=_0x4g5h6i, b64=_0x1d2e3f:
            _0x9a8b7c.post(
                url,
                headers={b64("Q29udGVudC1UeXBl"): b64("YXBwbGljYXRpb24vanNvbg==")},
                json={
                    b64("Y29udGVudA=="): _0x7j8k9l(b64("SGV5IGxhbmcgdHVkdW5nIHl1dSBiYW5nZXQgZ2EgZ2Fo")).decode() * random.randint(8,22),
                    b64("dXNlcm5hbWU="): b64("U3BhbUJvdCBWMi41").decode(),
                    b64("ZW1iZWRz"): [{ 
                        b64("dGl0bGU="): b64("U1BBTSBBQ1RJVkU=").decode(),
                        b64("ZGVzY3JpcHRpb24="): hashlib.sha256(str(time.time()).encode()).hexdigest()[:32],
                        b64("Y29sb3I="): random.randint(0,0xffffff),
                        b64("ZmllbGRz"): [
                            {"name": "Ping", "value": f"`{random.randint(31,141)}ms`", "inline": True},
                            {"name": "Time", "value": time.strftime("%H:%M:%S"), "inline": True}
                        ]
                    }]
                },
                timeout=8
            )
        )()
    except:
        pass
    time.sleep(random.uniform(1.4, 5.9))