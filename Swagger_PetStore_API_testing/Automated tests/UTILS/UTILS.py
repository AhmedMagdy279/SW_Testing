import requests

Base_URL = 'https://petstore.swagger.io/v2'
endpoint = '/user'


def request_handler_and_verifier(request_type='GET', payload_data=None, expected_response=None,
                                 expected_response_status_code=None):
    response = None
    try:
        if request_type == 'POST':
            response = requests.post(f"{Base_URL}{endpoint}", json=payload_data)
        elif request_type == 'GET':
            response = requests.get(f"{Base_URL}{endpoint}/{payload_data['username']}")
        elif request_type == 'PUT':
            response = requests.put(f"{Base_URL}{endpoint}/{payload_data['username']}", json=payload_data)
        elif request_type == 'DELETE':
            response = requests.delete(f"{Base_URL}{endpoint}/{payload_data['username']}")
        else:
            print(
                "Suppported End Point Request Types are POST, GET, PUT, DELETE. Raise Future Request for additional "
                "types...")
    except Exception as err:
        assert False, f"{request_type} request is failing due exception with message : {err}"

    try:
        print(response.json())
        print(expected_response)
        print(response.status_code)
    except Exception as err:
        print(f"{request_type} request is not printing due to {err}")

    if expected_response_status_code is None:
        assert response.status_code == 200
    else:
        assert response.status_code == expected_response_status_code

    if request_type == 'GET' and response.status_code == 200:
        assert response.json() == payload_data
    elif expected_response is not None:
        assert response.json() == expected_response
    else:
        pass
