import json
import sys
import xml.etree.ElementTree as ET
from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests


class UnhandledException(Exception):
    pass


def rss_parser(xml: str, limit: Optional[int] = None, json_output: bool = False) -> List[str]:
    """
    Parses an RSS 2.0 XML document and formats it as either JSON or a human-readable string output.
    """
    try:
        root = ET.fromstring(xml)
    except ET.ParseError:
        raise UnhandledException("Invalid XML format")

    channel = root.find("channel")
    if channel is None:
        raise UnhandledException("Invalid RSS format: Missing <channel> element")

    # Extract required channel fields
    feed_data = {
        "title": channel.findtext("title", "Unknown"),
        "link": channel.findtext("link", "Unknown"),
        "lastBuildDate": channel.findtext("lastBuildDate", "Unknown"),
        "pubDate": channel.findtext("pubDate", "Unknown"),
        "language": channel.findtext("language", "Unknown"),
        "categories": [cat.text for cat in channel.findall("category") if cat.text],
        "managingEditor": channel.findtext("managingEditor", "Unknown"),
        "description": channel.findtext("description", "Unknown"),
        "items": []
    }

    # Remove fields that are set to "Unknown"
    for key in list(feed_data.keys()):
        if feed_data[key] == "Unknown" or not feed_data[key]:
            del feed_data[key]

    # Extract <item> elements
    items = []
    for item in channel.findall("item"):
        item_data = {
            "title": item.findtext("title", "No Title"),
            "author": item.findtext("author", "Unknown"),
            "pubDate": item.findtext("pubDate", "Unknown"),
            "link": item.findtext("link", "Unknown"),
            "categories": [cat.text for cat in item.findall("category") if cat.text],
            "description": item.findtext("description", "No Description")
        }
        items.append(item_data)

    if limit is not None:
        items = items[:limit]

    feed_data["items"] = items

    if json_output:
        return [json.dumps(feed_data, indent=2, ensure_ascii=False)]

    # Format text output
    output = [
        f"Feed: {feed_data['title']}",
        f"Link: {feed_data['link']}",
    ]

    if "lastBuildDate" in feed_data:
        output.append(f"Last Build Date: {feed_data['lastBuildDate']}")
    if "pubDate" in feed_data:
        output.append(f"Publish Date: {feed_data['pubDate']}")
    if "language" in feed_data:
        output.append(f"Language: {feed_data['language']}")
    if "managingEditor" in feed_data:
        output.append(f"Editor: {feed_data['managingEditor']}")
    if "description" in feed_data:
        output.append(f"Description: {feed_data['description']}\n")

    for item in items:
        output.append(f"Title: {item['title']}")
        output.append(f"Author: {item['author']}")
        output.append(f"Published: {item['pubDate']}")
        output.append(f"Link: {item['link']}")
        if item["categories"]:
            output.append(f"Categories: {', '.join(item['categories'])}")
        output.append("\n" + item["description"] + "\n")

    return output


def main(argv: Optional[Sequence] = None):
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader."
    )
    parser.add_argument("source", help="RSS URL", type=str)
    parser.add_argument("--json", help="Print result as JSON in stdout", action="store_true")
    parser.add_argument("--limit", help="Limit news topics if this parameter is provided", type=int)

    args = parser.parse_args(argv)

    try:
        response = requests.get(args.source)
        response.raise_for_status()
        xml = response.text

        output = rss_parser(xml, args.limit, args.json)
        print("\n".join(output))
    except requests.RequestException as e:
        raise UnhandledException(f"Network error: {e}")
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    try:
        main()
    except UnhandledException as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
