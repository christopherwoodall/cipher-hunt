#!/usr/bin/env python3
"""Create the christopherwoodall/cipher-hunt repo on GitHub.

Auth via the custom.github-locust connector (surrogate credential; raw
token never seen by this script). Idempotent: if the repo already exists,
reports its URL and exits 0.
"""
import json
import sys
import urllib.request
import urllib.error

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response

CRED = "custom.github-locust"
HOSTS = ["api.github.com"]
API = "https://api.github.com"


def api(method, path, payload=None):
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        API + path,
        data=data,
        method=method,
        headers={
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "User-Agent": "cipher-hunt-setup/1.0",
        },
    )
    add_surrogate_to_request(req, CRED, allowed_hosts=HOSTS)
    try:
        resp = urllib.request.urlopen(req)
        return resp.status, read_json_response(resp)
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", "replace")
        try:
            raw = json.loads(raw)
        except Exception:
            pass
        return e.code, raw


def main():
    status, existing = api("GET", "/repos/christopherwoodall/cipher-hunt")
    if status == 200:
        print(f"exists: {existing['full_name']} -> {existing['html_url']}")
        return 0
    status, result = api(
        "POST",
        "/user/repos",
        {
            "name": "cipher-hunt",
            "description": "Notes on unsolved ciphers — research companion",
            "private": False,
            "has_issues": True,
            "has_wiki": False,
        },
    )
    if status == 201:
        print(f"created: {result['full_name']} -> {result['html_url']}")
        return 0
    print(f"failed: {status} {result}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
