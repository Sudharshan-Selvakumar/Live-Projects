import pytest

class Test_Suite2:
    @pytest.mark.xfail
    def test_TC1(self, setup_normal, setup_class, setup_module):
        print("\nTC1")

    @pytest.mark.skip
    def test_TC2(self, setup_normal, setup_class, setup_module):
        print("\nTC2")
    @pytest.mark.parametrize("name, age, gender", [("sudha", "25", "male"), ("thara", "23", "female"), ("tulsi", "6", "dog")])
    @pytest.mark.sanity
    @pytest.mark.skipif(2>1, reason="apdithanda skip pannuven")
    def test_TC3(self, setup_normal, setup_class, setup_module, name, age, gender):
        print("\nTC3")
        print(f'{name} {age} {gender}')

    def pytest_configure(config):
        config.addinvalue_line("markers", "sanity:sanity test")