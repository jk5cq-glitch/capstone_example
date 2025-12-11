import sys
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, sub, mult, div, squ, root, sin, cos, root, log, perc

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(6, 9) == 15 

def test_add3():
    assert add(5, 6) != 10

def test_sub():
    assert sub(5,4) == 1

def test_sub2():
    assert sub(10,5) == 5

def test_mult1():
    assert mult(6, 3) == 18

def test_mult2():
    assert mult(5, 4) == 20

def test_div1():
    assert div(10, 5) == 2

def test_div2():
    assert div(50, 10) == 5

def test_squ1():
    assert squ(4) == 16

def test_squ2():
    assert squ(6) != 35

def test_sin():
    assert sin(0) == 0

def test_cos1():
    assert cos(math.pi) == -1

def test_root1():
    assert root(16) == 4

def test_root2():
    assert root(36) == 6

def test_root3():
    assert root(-16) == 'Invalid number'

def test_perc1():
    assert perc(3, 4) == 75

def test_perc2():
    assert perc(-3, 4) != 75

def test_perc3():
    assert perc(5, 0) == 'Invalid'

def test_log1():
    assert log(math.e) == 1

def test_log2():
    assert log(math.e) != -1