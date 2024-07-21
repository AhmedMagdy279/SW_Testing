import time
import requests
import pytest
from UTILS.UTILS import *
from UTILS.payload import *


@pytest.fixture(scope="module")
def user_payload():
    # This fixture will provide the same user payload for all tests in the module
    return user_pay_load()


@pytest.mark.order(1)
def test_add_user_request_success(user_payload):
    # Positive test case
    # We aim to add a new user with the payload in payload.py file.
    # Expected: TC shall succeed by creating a new user.
    response_200 = {'code': 200, 'type': 'unknown', 'message': f'{user_payload["id"]}'}
    request_handler_and_verifier(request_type='POST', payload_data=user_payload, expected_response=response_200,
                                 expected_response_status_code=200)


@pytest.mark.order(2)
def test_get_user_request_success(user_payload):
    # Positive test case
    # We aim to get the user that was created in test(1).
    # Expected: TC shall succeed by getting the existing user.
    request_handler_and_verifier(request_type='GET', payload_data=user_payload, expected_response=None,
                                 expected_response_status_code=200)


@pytest.mark.order(3)
def test_edit_user_request_success(user_payload):
    # Positive test case
    # We aim to edit the user that was created in test(1).
    # Expected: TC shall succeed by editing the existing user.
    # creating new payload but with the old username and ID, but changing other data entries.
    new_payload = user_pay_load()
    new_payload["username"] = user_payload["username"]
    new_payload["id"] = user_payload["id"]
    response_200 = {'code': 200, 'type': 'unknown', 'message': f'{user_payload["id"]}'}

    request_handler_and_verifier(request_type='PUT', payload_data=new_payload, expected_response=response_200,
                                 expected_response_status_code=200)

    # using get request only to make sure that the data has been modified as the request doesn't return back response
    # body with the modified entry.
    request_handler_and_verifier(request_type='GET', payload_data=new_payload, expected_response=None,
                                 expected_response_status_code=200)


@pytest.mark.order(4)
def test_delete_user_request_success(user_payload):
    # Positive test case
    # We aim to delete the user that was created in test(1) and edited in test(3).
    # Expected: TC shall succeed by deleting the existing user.
    response_200 = {'code': 200, 'type': 'unknown', 'message': f'{user_payload["username"]}'}
    request_handler_and_verifier(request_type='DELETE', payload_data=user_payload, expected_response=response_200,
                                 expected_response_status_code=200)


@pytest.mark.order(5)
def test_get_nonexistent_user_request_failure(user_payload):
    # Negative test case
    # We aim to get the user we deleted in test(4).
    # Expected: TC shall fail as user is not existing anymore.
    response_404 = {'code': 1, 'type': 'error', 'message': 'User not found'}
    request_handler_and_verifier(request_type='GET', payload_data=user_payload, expected_response=response_404,
                                 expected_response_status_code=404)


@pytest.mark.order(6)
def test_delete_nonexistent_user_request_failure(user_payload):
    # Negative test case.
    # We aim to delete the user we deleted in test(4)
    # Expected: TC shall fail as user is not existing anymore.
    request_handler_and_verifier(request_type='DELETE', payload_data=user_payload, expected_response=None,
                                 expected_response_status_code=404)
