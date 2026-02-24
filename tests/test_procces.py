from src.process import add_one_to_number

def test_add_one_to_number():
    """Test to validate the add_one_to_number() function for value 4"""
    # Arrange
    input_number = 4
    #Act
    expected = 5
    # Assert
    assert expected == add_one_to_number(number=input_number)