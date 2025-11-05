import pytest

from src import widget

from src import masks

@pytest.mark.parametrize('requisites, expected_mask', [('Maestro 1596  8378  6870 5199', 'Maestro 1596 83** **** 5199'),
                                                       ('  СчЁт   64686473678894779589', 'Счет **9589'),
                                                       ('_M_a_s_t_e_r_C_a_r_d_ 7158    3007 34 7 26 758', 'MasterCard 7158 30** **** 6758'),
                                                       ('сЧЁТ 353  830,334,744*478\955:60', 'Счет **5560'),
                                                       ('$Visa $Classic 6831+9824+7673+7658', 'Visa Classic 6831 98** **** 7658'),
                                                       ('Visa Platinum 8990 - 9221 - 1366 - 5229', 'Visa Platinum 8990 92** **** 5229'),
                                                       ('%V%isa     Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
                                                       ('СЧЕТ №7_36_5410&84301#35874305', 'Счет **4305'),
                                                       ('  %  #Some   #UNKNOWN   #Card???   № 1000#2000#3000#4000', 'Some UNKNOWN Card 1000 20** **** 4000')])
def test_mask_account_card(requisites, expected_mask):
    assert widget.mask_account_card(requisites) == expected_mask
