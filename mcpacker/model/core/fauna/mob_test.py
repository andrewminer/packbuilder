from mcpacker.model.core.fauna.mob import Mob
from pytest import fixture

import mcpacker.model.core.fauna.active as AC


# Fixtures #########################################################################################

@fixture(name="squid")
def createSquid():
    yield Mob("minecraft:squid", AC.ANY)

@fixture(name="cow")
def createCow():
    yield Mob("minecraft:cow", AC.DIURNAL)

@fixture(name="mobMap")
def createMobMap(cow, squid):
    yield {
        cow: "beef",
        squid: "calamari"
    }


# Tests ############################################################################################

def test_eq(squid):
    assert squid == Mob("minecraft:squid")
    assert squid != Mob("animalsplus:squid")

def test_hash(cow, squid, mobMap):
    assert mobMap[cow] == "beef"
    assert mobMap[squid] == "calamari"

def test_str(squid):
    assert str(squid) == "minecraft:squid"

def test_repr(cow):
    assert repr(cow) == "Mob<minecraft:cow>{active:[Active<day>{start:0, end:12000}]}"
