import pytest
from ..main import BMICalculator, BMIService

@pytest.fixture
def bmi_calculator():
    return BMICalculator()

@pytest.fixture
def bmi_service(bmi_calculator):
    return BMIService(bmi_calculator)

def test_calculate_bmi(bmi_calculator):
    # Test case for calculating BMI
    assert bmi_calculator.calculate_bmi(70, 1.75) == 22.86

def test_determine_weight_category(bmi_calculator):
    # Test cases for determining weight category
    assert bmi_calculator.determine_weight_category(17) == "Underweight"
    assert bmi_calculator.determine_weight_category(20) == "Normal weight"
    assert bmi_calculator.determine_weight_category(27) == "Overweight"
    assert bmi_calculator.determine_weight_category(32) == "Obese"

def test_calculate_bmi_and_category(bmi_service):
    # Test case for calculating BMI and weight category
    bmi, weight_category = bmi_service.calculate_bmi_and_category(70, 1.75)
    assert bmi == 22.86
    assert weight_category == "Normal weight"
