from creational_patterns.prototype import RepairTemplateCache

def test_prototype_clone():
    cache = RepairTemplateCache()
    cache.load_defaults()

    original = cache.get("laptop_screen")
    cloned = cache.get("laptop_screen")

    assert original.summary() == cloned.summary()
    assert original is not cloned  # ensures it's a clone, not same object
