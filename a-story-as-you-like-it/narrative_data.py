import json
from dataclasses import dataclass
from typing import Optional


@dataclass
class StoryNode:
    id: int
    text: str
    forks: Optional[dict[int, str]]


def read_text_from_file(fn: str):
    texts = {}
    with open(fn, 'rt') as f:
        doc = json.load(f)
    for node in doc.get("texts", []):
        forks = {}
        forks_wrong_keys = node.get("forks", {})
        for k, v in forks_wrong_keys.items():
            if k:
                forks[int(k)] = v
            else:
                forks["END"] = v
    
        sn = StoryNode(node.get("id"),
                       node.get("text"),
                       forks)
        texts[sn.id] = sn

    return texts
