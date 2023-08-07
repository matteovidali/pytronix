from pytronix.scopes import LoggedVXI11
from pathlib import Path
import os

def test_logged_vxi_dfault() -> None:
    instr = LoggedVXI11("123.123.123.123")
    assert(type(instr) == LoggedVXI11)

def test_make_init() -> None:
    instr = LoggedVXI11("123.123.123.123")
    instr.make_init()
    assert(Path("./123.123.123.123_init.txt").exists())
    os.remove("./123.123.123.123_init.txt")    
