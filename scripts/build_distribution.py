#!/usr/bin/env python3
"""Build/check the self-contained draft; optionally create a prerelease ZIP.

Standard library only. Does not push, tag, or upload a release.
"""
import argparse
import hashlib
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MODULES = (
    "onboarding", "safety", "concerns", "products", "visuals", "storage",
    "reassessment", "continuity", "recovery",
)
STANDALONE = "SKINCARE_ASSISTANT_CHATGPT.md"
PACKAGE = "skincare-assistant-v2.8.1-draft9.zip"


def render():
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    skill = re.sub(r"\A---\n.*?\n---\n\n", "", skill, count=1, flags=re.S)
    parts = [skill.rstrip()]
    for name in MODULES:
        content = (ROOT / "references" / f"{name}.md").read_text(encoding="utf-8")
        parts.append(f'<a id="module-{name}"></a>\n\n{content.rstrip()}')
    result = "\n\n---\n\n".join(parts) + "\n"
    for name in MODULES:
        result = re.sub(rf"\((?:references/)?{name}\.md\)", f"(#module-{name})", result)
    return result


def checksum(data, name):
    return f"{hashlib.sha256(data).hexdigest()}  {name}\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if generated files are stale")
    parser.add_argument("--package", action="store_true", help="Write deterministic draft ZIP and hashes in dist/")
    args = parser.parse_args()
    data = render().encode("utf-8")
    outputs = {STANDALONE: data, "SHA256SUMS.txt": checksum(data, STANDALONE).encode()}
    for name, content in outputs.items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_bytes() != content:
                raise SystemExit(f"Stale output: {name}; run python3 scripts/build_distribution.py")
        else:
            path.write_bytes(content)
    if args.package:
        dist = ROOT / "dist"
        dist.mkdir(exist_ok=True)
        files = ["SKILL.md", STANDALONE, "README.md", "INSTALL.md", "RELEASE_NOTES.md", "LICENSE-NONCOMMERCIAL.txt", "SHA256SUMS.txt"]
        files += [f"references/{name}.md" for name in MODULES]
        with zipfile.ZipFile(dist / PACKAGE, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for name in sorted(files):
                info = zipfile.ZipInfo(name, date_time=(2026, 10, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                archive.writestr(info, (ROOT / name).read_bytes())
        (dist / STANDALONE).write_bytes(data)
        sums = checksum(data, STANDALONE) + checksum((dist / PACKAGE).read_bytes(), PACKAGE)
        (dist / "SHA256SUMS.txt").write_text(sums, encoding="utf-8")
        print(f"Built dist/{PACKAGE} (prerelease asset; not uploaded)")
    print("Distribution and checksum match canonical sources")


if __name__ == "__main__":
    main()
