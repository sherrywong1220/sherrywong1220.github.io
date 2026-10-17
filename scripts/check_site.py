#!/usr/bin/env python3
"""Check generated pages, local assets, and links, including project-site base paths."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.ids = set()
        self.canonical = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        for name in ("href", "src", "poster"):
            if attrs.get(name):
                self.links.append(attrs[name])
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")


def check(root, baseurl):
    errors = []
    pages = {p: Page(p.read_text()) for p in root.rglob("*.html")}
    home = pages.get(root / "index.html")
    assert home, "Homepage is missing"
    canonical = urlsplit(home.canonical or "/")
    prefix = (baseurl if baseurl is not None else canonical.path).rstrip("/")
    origin = f"{canonical.scheme}://{canonical.netloc}" if canonical.netloc else "http://local.test"
    for path in ("index.html", "research/index.html", "publications/index.html", "404.html"):
        if root / path not in pages:
            errors.append(f"Missing page: {path}")
    for path, page in pages.items():
        relative = path.relative_to(root).as_posix()
        page_url = origin + prefix + "/" + relative
        for link in page.links:
            if link == "#" or link.startswith(("mailto:", "tel:", "data:", "javascript:")):
                continue
            target = urlsplit(urljoin(page_url, link))
            if target.netloc != urlsplit(origin).netloc:
                continue
            target_path = unquote(target.path)
            if prefix and not (target_path == prefix or target_path.startswith(prefix + "/")):
                errors.append(f"{relative}: link escapes base path: {link}")
                continue
            target_path = target_path[len(prefix):].lstrip("/")
            dest = root / target_path
            if dest.is_dir():
                dest = dest / "index.html"
            if not dest.exists():
                errors.append(f"{relative}: missing local target {link}")
            elif target.fragment and dest in pages and unquote(target.fragment) not in pages[dest].ids:
                errors.append(f"{relative}: missing fragment {link}")
        text = path.read_text()
        for placeholder in ("You R. Name", "you@example.com", "Write your biography here", "Albert Einstein", "555 your office"):
            if placeholder in text:
                errors.append(f"{relative}: template placeholder {placeholder!r}")
    publications = (root / "publications/index.html").read_text()
    for key in ("yang2026ocean", "wang2026tierbpf", "lin2026hybridgen", "wang2026adaptive", "wang2025cmpi", "ma2025mlr", "wang2025characterization"):
        if f'id="{key}"' not in publications:
            errors.append(f"Missing publication: {key}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Verified {len(pages)} HTML pages, 7 publications, and all local links/assets (baseurl={prefix!r}).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--baseurl")
    args = parser.parse_args()
    check(args.directory, args.baseurl)
