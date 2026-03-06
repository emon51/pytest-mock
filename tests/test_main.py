# import pytest
# from requests.models import Response
# from src.main import get_data

# TEST_URL = "www.fake-url.com"

# def create_mock_response() -> Response:
#     response = Response()
#     response.status_code = 200
#     response._content = b'[{"title": "Mock Product"}, {"title": "Another Product"}]'
#     return response


# def test_get_data_returns_first_product_title(mocker):
#     mock_requests = mocker.patch("src.main.requests")
#     mock_requests.get.return_value = create_mock_response()

#     expected = "Mock Product"
#     actual = get_data(TEST_URL)

#     assert actual == expected


# def test_get_data_raises_when_request_fails(mocker):
#     mock_requests = mocker.patch("src.main.requests")
#     mock_requests.get.side_effect = Exception("request failed")

#     with pytest.raises(Exception, match="request failed"):
#         get_data(TEST_URL)

#=================================================================================================================#
# import pytest
# from src.main import get_data


# TEST_URL = "https://www.fake-url.com"

# def test_get_data_returns_first_product_title(mocker):
#     # Mock requests.get
#     mock_get = mocker.patch("src.main.requests.get")
#     # Define fake JSON response
#     mock_get.return_value.json.return_value = [
#         {"title": "Mock Product"},
#         {"title": "Another Product"},
#     ]
#     result = get_data(TEST_URL)
#     assert result == "Mock Product"

# def test_get_data_raises_when_request_fails(mocker):
#     mock_get = mocker.patch("src.main.requests.get")
#     mock_get.side_effect = Exception("request failed")

#     with pytest.raises(Exception, match="request failed"):
#         get_data(TEST_URL)
#=================================================================================================================#

import pytest
from src.main import get_data


TEST_URL = "https://fake-url.com"


def test_get_data_returns_first_product_title(mocker):
    # Create fake response object
    mock_response = mocker.Mock()

    # Define what response.json() should return
    mock_response.json.return_value = [
        {"title": "Mock Product"},
        {"title": "Another Product"}
    ]

    # Replace requests.get with our mock
    # Because of this line (mocker.patch...): Replace requests.get inside src.main with a fake function.
    # That's why instead of calling the real API (requests.get(url)) it will now return: mock_response
    mocker.patch("src.main.requests.get", return_value=mock_response)
    result = get_data(TEST_URL)

    assert result == "Mock Product"


def test_get_data_raises_when_request_fails(mocker):
    mocker.patch("src.main.requests.get", side_effect=Exception("request failed"))

    with pytest.raises(Exception, match="request failed"):
        get_data(TEST_URL)