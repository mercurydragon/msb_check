import logging
from typing import Union

import requests
from django.conf import settings
from rest_framework.status import HTTP_200_OK


class MSBAPIHelper:
    url = settings.EXTERNAL_API_URL

    def is_msb(self, params: dict) -> Union[bool, None]:
        """
        Check with external API is a company with provided identifier (tin or prsn)
        is in the registry of small and medium companies.
        """
        params = self.prepare_params(params)
        response = requests.post(self.url, params=params)
        if response.status_code == HTTP_200_OK:
            result = response.json()
            if 'data' in result:
                # Company is small or medium if 'data' is not empty
                return bool(result['data'])

        logging.error(f'Unexpected API response:{response.text}')

    @staticmethod
    def prepare_params(params: dict) -> dict:
        """
        Check that only on identifier is provided  (tin or prsn)
        and create a dictionary of params according to external API requirements.
        """
        tin = params.get('tin')
        prsn = params.get('prsn')
        conditions = (tin is not None, prsn is not None)
        assert not all(conditions) and any(conditions)
        return {'query': tin or prsn}

