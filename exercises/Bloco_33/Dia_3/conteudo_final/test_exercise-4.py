from exercise_4 import emails_to_validate


def test_emails_to_validate():
    validate_values_1 = ['Fulano@hotmail.com']
    expectate_result_1 = ['Fulano@hotmail.com']

    validate_values_2 = ['1Fulano@hotmail.com']
    expectate_result_2 = []

    validate_values_3 = ['Fulano@hotmail.com', '1Fulano@hotmail.com']
    expectate_result_3 = ['Fulano@hotmail.com']

    assert emails_to_validate(validate_values_1) == expectate_result_1
    assert emails_to_validate(validate_values_2) == expectate_result_2
    assert emails_to_validate(validate_values_3) == expectate_result_3
