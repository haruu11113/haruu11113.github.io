#!/usr/bin/env python3
"""Convert ResearchMap JSONL export to Hugo-compatible data/publications.json.

Usage:
    python scripts/rm2json.py <input.jsonl>

Output is written to data/publications.json.
If data/manual_publications.json exists, its entries are merged in.
"""

import json
import sys
from pathlib import Path


def get_text(obj, lang):
    if not obj or not isinstance(obj, dict):
        return ""
    return obj.get(lang) or ""


def format_names(names_list):
    if not names_list:
        return ""
    return ", ".join(n.get("name", "") for n in names_list if n.get("name"))


def extract_doi(merge):
    dois = (merge.get("identifiers") or {}).get("doi", [])
    if dois:
        return dois[0]
    return ""


def extract_url(merge):
    doi = extract_doi(merge)
    if doi:
        return f"https://doi.org/{doi}"
    for item in merge.get("see_also") or []:
        if item.get("label") == "url":
            u = item.get("@id", "")
            if u and u.startswith("http"):
                return u
    return ""


def year_of(date_str):
    s = str(date_str) if date_str else ""
    return s[:4] if len(s) >= 4 else s


def process_paper(merge):
    title = merge.get("paper_title") or {}
    authors = merge.get("authors") or {}
    pub_name = merge.get("publication_name") or {}
    publisher = merge.get("publisher") or {}

    start = str(merge.get("starting_page") or "")
    end = str(merge.get("ending_page") or "")
    pages = f"{start}-{end}" if start and end and start != end else start

    type_map = {
        "scientific_journal": "journal",
        "international_conference_proceedings": "conference",
        "in_book": "book",
    }
    paper_type = type_map.get(merge.get("published_paper_type") or "", "other")
    # Infer journal type from venue name when published_paper_type is not set
    if paper_type == "other":
        venue_check = (get_text(pub_name, "en") + get_text(pub_name, "ja")).lower()
        if "journal" in venue_check:
            paper_type = "journal"
    roles = merge.get("published_paper_owner_roles") or []

    date_str = str(merge.get("publication_date") or "")
    doi = extract_doi(merge)

    return {
        "title_en": get_text(title, "en"),
        "title_ja": get_text(title, "ja"),
        "authors_en": format_names((authors.get("en") or [])),
        "authors_ja": format_names((authors.get("ja") or [])),
        "year": year_of(date_str),
        "date": date_str,
        "venue_en": get_text(pub_name, "en") if isinstance(pub_name, dict) else str(pub_name),
        "venue_ja": get_text(pub_name, "ja") if isinstance(pub_name, dict) else "",
        "publisher_en": get_text(publisher, "en") if isinstance(publisher, dict) else str(publisher),
        "publisher_ja": get_text(publisher, "ja") if isinstance(publisher, dict) else "",
        "volume": str(merge.get("volume") or ""),
        "number": str(merge.get("number") or ""),
        "pages": pages,
        "doi": doi,
        "url": extract_url(merge),
        "is_reviewed": bool(merge.get("referee")),
        "paper_type": paper_type,
        "is_lead": "lead" in roles,
    }


def process_presentation(merge):
    title = merge.get("presentation_title") or {}
    presenters = merge.get("presenters") or {}
    event = merge.get("event") or {}
    date_str = str(merge.get("publication_date") or "")

    return {
        "title_en": get_text(title, "en"),
        "title_ja": get_text(title, "ja"),
        "presenters_en": format_names(presenters.get("en") or []),
        "presenters_ja": format_names(presenters.get("ja") or []),
        "year": year_of(date_str),
        "date": date_str,
        "event_en": get_text(event, "en") if isinstance(event, dict) else str(event),
        "event_ja": get_text(event, "ja") if isinstance(event, dict) else "",
        "is_international": bool(merge.get("is_international_presentation")),
    }


def process_misc(merge):
    title = merge.get("paper_title") or {}
    authors = merge.get("authors") or {}
    pub_name = merge.get("publication_name") or {}
    date_str = str(merge.get("publication_date") or "")

    return {
        "title_en": get_text(title, "en"),
        "title_ja": get_text(title, "ja"),
        "authors_en": format_names(authors.get("en") or []),
        "authors_ja": format_names(authors.get("ja") or []),
        "year": year_of(date_str),
        "date": date_str,
        "venue_en": get_text(pub_name, "en") if isinstance(pub_name, dict) else str(pub_name),
        "venue_ja": get_text(pub_name, "ja") if isinstance(pub_name, dict) else "",
        "volume": str(merge.get("volume") or ""),
        "number": str(merge.get("number") or ""),
        "doi": extract_doi(merge),
        "url": extract_url(merge),
        "is_reviewed": bool(merge.get("referee")),
    }


def sort_key(item):
    return (item.get("year") or "", item.get("date") or "")


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/rm2json.py <input.jsonl>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    repo_root = Path(__file__).parent.parent
    output_path = repo_root / "data" / "publications.json"
    manual_path = repo_root / "data" / "manual_publications.json"

    papers, presentations, misc = [], [], []

    with open(input_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            entry_type = record.get("insert", {}).get("type", "")
            merge = record.get("merge", {})
            if entry_type == "published_papers":
                papers.append(process_paper(merge))
            elif entry_type == "presentations":
                presentations.append(process_presentation(merge))
            elif entry_type == "misc":
                misc.append(process_misc(merge))

    # Merge manual additions
    if manual_path.exists():
        with open(manual_path, encoding="utf-8") as f:
            manual = json.load(f)
        papers.extend(manual.get("papers", []))
        presentations.extend(manual.get("presentations", []))
        misc.extend(manual.get("misc", []))

    papers.sort(key=sort_key, reverse=True)
    presentations.sort(key=sort_key, reverse=True)
    misc.sort(key=sort_key, reverse=True)

    result = {"papers": papers, "presentations": presentations, "misc": misc}
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Done: {len(papers)} papers, {len(presentations)} presentations, {len(misc)} misc")
    print(f"  → {output_path}")


if __name__ == "__main__":
    main()
