import pytest
from kursy_walut import pobierz_cene_euro


def test_pobierz_cene_euro(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {
        'rates': [{'mid': 4.5}]
    }

    mocker.patch('requests.get', return_value=mock_response)

    cena = pobierz_cene_euro()
    assert cena == 4.5
