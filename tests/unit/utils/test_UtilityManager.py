def test_set_seed(test_utility_manager) -> None:
    test_utility_manager.set_seed(42)


def test_root_path(test_utility_manager) -> None:
    print(test_utility_manager.root_path)


def test_config_path(test_utility_manager) -> None:
    print(test_utility_manager.config_path)
