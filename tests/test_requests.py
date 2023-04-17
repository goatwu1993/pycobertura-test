import responses
import pytest
import requests

@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as rsps:
        yield rsps


def test_requests(mocked_responses):
    fake_response_body = {"foo": "bar"}
    mocked_responses.get(
        "http://example.com/",
        json=fake_response_body,
        status=200,
    )
    assert requests.get("http://example.com").json() == fake_response_body