import base64, time, random, hashlib, requests as _0x1337

_0xb64 = lambda x: base64.b64decode(x).decode('utf-8')
_0xurl = _0xb64("aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTI3NjQ1MjM0NTY3ODkwMTIzNC9hYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ejA=")

def _0xdeadbeef(s):
    for _ in range(9999):           # junk loop
        pass
    return ''.join(chr(ord(c) ^ 0) for c in s)

while 1:
    try:
        (_0x1337.post)(
            _0xurl,
            headers={_0xb64("Q29udGVudC1UeXBl"): _0xb64("YXBwbGljYXRpb24vanNvbg==")},
            json={
                _0xb64("Y29udGVudA=="): _0xdeadbeef(_0xb64("SGV5IGxhbmcgdHVkdW5nIHl1dSBiYW5nZXQgZ2EgZ2Fo")) * random.randint(9, 25),
                _0xb64("dXNlcm5hbWU="): _0xb64("U3BhbUJvdCBWMw=="),
                _0xb64("ZW1iZWRz"): [{
                    _0xb64("dGl0bGU="): _0xb64("U1BBTSBPTkxJTkU="),
                    _0xb64("ZGVzY3JpcHRpb24="): hashlib.md5(str(time.time()).encode()).hexdigest(),
                    _0xb64("Y29sb3I="): random.randint(0, 16777215),
                    _0xb64("ZmllbGRz"): [
                        {"name": "Latency", "value": f"`{random.randint(27, 157)}ms`", "inline": True},
                        {"name": "Uptime",   "value": time.strftime("%H:%M:%S"), "inline": True},
                        {"name": "Status",   "value": "Spamming...", "inline": False}
                    ],
                    _0xb64("Zm9vdGVy"): {_0xb64("dGV4dA=="): "Made with chaos"}
                }]
            },
            timeout=10
        )
    except:
        pass
    time.sleep(random.uniform(1.2, 5.8))