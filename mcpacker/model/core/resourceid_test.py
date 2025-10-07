from mcpacker.model.core.resourceid import ResourceId


# Tests ############################################################################################

def test_singlePart():
    assert str(ResourceId.parse("alpha")) == "minecraft:alpha"

def test_leadingSeparator():
    assert str(ResourceId.parse(":bravo")) == "minecraft:bravo"

def test_fullResource():
    assert str(ResourceId.parse("charlie:delta")) == "charlie:delta"

def test_fullTag():
    assert str(ResourceId.parse("#charlie:delta")) == "#charlie:delta"
