#!/usr/bin/env python3
"""Decode and write 8 inline QFT files from base64 content."""
import base64
import os
import re

MDX_DIR = "/home/user/Donkey/src/content/curriculum"

def get_stub_prefix(mdx_path):
    with open(mdx_path) as f:
        content = f.read()
    m = re.search(r'\{/\* Content from .+? \*/\}', content)
    if m:
        return content[:m.end()] + "\n\n"
    return content + "\n\n"

def write_content(name, b64_content):
    mdx_path = os.path.join(MDX_DIR, f"{name}.mdx")
    stub = get_stub_prefix(mdx_path)
    decoded = base64.b64decode(b64_content).decode("utf-8")
    with open(mdx_path, "w") as f:
        f.write(stub)
        f.write(decoded)
    print(f"Written: {name}.mdx ({len(decoded)} chars)")

FILES = {
    "qft_1_scalar_field_quantization": "IyBDYW5vbmljYWwgUXVhbnRpemF0aW9uIG9mIHRoZSBTY2FsYXIgRmllbGQKCipUaGUgY2xlYW5lc3QgZW50cnkgaW50byBxdWFudHVtIGZpZWxkIHRoZW9yeSDigJQgd2hlcmUgZmllbGRzIGJlY29tZSBvcGVyYXRvcnMgYW5kIHBhcnRpY2xlcyBlbWVyZ2UgYXMgdGhlaXIgZXhjaXRhdGlvbnMuKgoKVGhpcyBpcyB0aGUgZmlyc3Qgb2YgdGhlIFFGVCBkb2N1bWVudHMuIFRoZSBwcmVyZXF1aXNpdGUgaXMgZXZlcnl0aGluZyB3ZSd2ZSBidWlsdDogTGFncmFuZ2lhbiBtZWNoYW5pY3MsIHNwZWNpYWwgcmVsYXRpdml0eSBhbmQgdGVuc29ycywgY2xhc3NpY2FsIGZpZWxkIHRoZW9yeSAoZXNwZWNpYWxseSB0aGUgS2xlaW4tR29yZG9uIHRoZW9yeSksIHF1YW50dW0gbWVjaGFuaWNzLCBhbmQgYSBiaXQgb2Ygc3RhdGlzdGljYWwgbWVjaGFuaWNzLiBJZiB5b3UncmUgZmx1ZW50IHdpdGggdGhlIGhhcm1vbmljIG9zY2lsbGF0b3IgaW4gUU0gYW5kIGNhbiB3cml0ZSBkb3duIHRoZSBLbGVpbi1Hb3Jkb24gTGFncmFuZ2lhbiwgeW91J3JlIHJlYWR5Lg==",
    "qft_2_dirac_field_quantization": "IyBDYW5vbmljYWwgUXVhbnRpemF0aW9uIG9mIHRoZSBEaXJhYyBGaWVsZAoKKlFGVCBkb2N1bWVudCAyOiBmZXJtaW9ucywgYW50aXBhcnRpY2xlcywgYW5kIHRoZSBzcGluLXN0YXRpc3RpY3MgdGhlb3JlbSwgZmFsbGluZyBvdXQgb2YgdGhlIG1hdGhlbWF0aWNzLioKClRoZSBzY2FsYXIgZmllbGQgZG9jdW1lbnQgc2hvd2VkIGhvdyB0byBxdWFudGl6ZSBhIGJvc29uaWMgZmllbGQu",
}

# These will be replaced with the full base64 strings by a helper
for name, b64 in FILES.items():
    write_content(name, b64)

print("Done.")
