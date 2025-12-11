import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, sub, mult, div, squ, root, sin, cos, root, 

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(6, 9) == 15 

def test_add3():
    assert add(5, 6) != 10

