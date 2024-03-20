import re
from pathlib import Path
import shutil
from typing import List

def replace_keywords(directory: Path, pattern: str, replacement: str, without_suffix: List[str] = ['.md', '.rst']):
    for path in Path(directory).rglob('*'):
        if any(p.name == '.git' for p in path.parents):
            continue
        if path.absolute() == Path(__file__).absolute():
            continue
        if path.is_dir():
            continue
        if without_suffix and path.suffix in without_suffix:
            continue
        try:
            content = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        content_new = re.sub(pattern, replacement, content, flags=re.MULTILINE)
        if content != content_new:
            path.write_text(content_new)

if __name__ == '__main__':
    replace_keywords(Path.cwd(), 'rdkit', 'rdkix')
    replace_keywords(Path.cwd(), 'RDKit', 'RDKix')
    replace_keywords(Path.cwd(), 'Rdkit', 'Rdkix')
    replace_keywords(Path.cwd(), 'RDKIT', 'RDKIX')
    replace_keywords(Path.cwd(), 'RDkit', 'RDkix')
    replace_keywords(Path.cwd(), 'rdkix.org', 'rdkit.org')
    replace_keywords(Path.cwd(), 'github.com/rdkix/rdkix', 'github.com/rdkit/rdkit')
    replace_keywords(Path.cwd(), 'github.com/rdkix', 'github.com/rdkit')
