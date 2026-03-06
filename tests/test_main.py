import pytest
from requests.models import Response

from src.main import get_data


TEST_URL = "www.fake-url.com"


def create_mock_response() -> Response:
    response = Response()
    response.status_code = 200
    response._content = b'[{"title": "Mock Product"}, {"title": "Another Product"}]'
    return response


def test_get_data_returns_first_product_title(mocker):
    mock_requests = mocker.patch("src.main.requests")
    mock_requests.get.return_value = create_mock_response()

    expected = "Mock Product"
    actual = get_data(TEST_URL)

    assert actual == expected


def test_get_data_raises_when_request_fails(mocker):
    mock_requests = mocker.patch("src.main.requests")
    mock_requests.get.side_effect = Exception("request failed")

    with pytest.raises(Exception, match="request failed"):
        get_data(TEST_URL)
