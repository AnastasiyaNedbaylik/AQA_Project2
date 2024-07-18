import json

import requests

from logic.api_client.data.body_data import ApiData as AD
from utilities.api_functions.get_token import Token


class Projects:
    """ API library for website https://web.teambooktest.com """

    def __init__(self):
        self.token = Token().get_token()
        self.base_url = AD.API_BASE_URL

    def create_project(self) -> json:
        """Positive: Create a new project with required data"""
        try:
            params = {'token': self.token}
            data = AD.create_project_required_data
            res = requests.post(self.base_url + 'projects', data=data, params=params)
            status = res.status_code
            project_id = res.json().get('id')
            project_data = res.json()
            code = res.json().get('code')
            # color = not res.json().get('color')
            assert isinstance(project_data, dict), 'The data obtained does not correspond to the expected structure'
            assert all(key in project_data for key in AD.expected_project_data)
            return status, project_id
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while processing this request: {e}")

    def create_project_all_data(self) -> json:
        """Positive: Create a new project with all data"""
        try:
            params = {'token': self.token}
            data = AD.create_project_all_data
            res = requests.post(self.base_url + 'projects', data=data, params=params)
            status = res.status_code
            project_id = res.json().get('id')
            name = res.json().get('name')
            assert name == data['name']
            return status, project_id
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while processing this request: {e}")

    def get_project_by_id(self, project_id) -> json:
        """Positive: Get a project by id """
        try:
            params = {'token': self.token,
                      'project_ids[]': project_id
                      }
            res = requests.get(self.base_url + 'projects/in_range', params=params)
            status = res.status_code
            project_name = res.json()[0]['name']
            client_id = res.json()[0]['client_id']
            manager_id = res.json()[0]['manager_id']
            project_status = res.json()[0]['status']
            return status, project_name, client_id, manager_id, project_status
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while processing this request: {e}")


    def deactivate_project(self, project_id) -> json:
        """Positive: Deactivate a project"""
        try:
            params = {'token': self.token,
                      'project_ids[]': project_id
                      }
            res = requests.patch(self.base_url + 'projects/deactivate', params=params)
            status = res.status_code
            return status
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while processing this request: {e}")

    def activate_project(self, project_id) -> json:
        """Positive: Activate a project """
        try:
            params = {
                'token': self.token,
                'project_ids[]': project_id
            }
            res = requests.patch(self.base_url + 'projects/activate', params=params)
            status = res.status_code
            return status
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while processing this request: {e}")

    def delete_project(self, project_id) -> json:
        """Positive: Delete a project """
        try:
            params = {
                'token': self.token,
                'project_ids[]': project_id
            }
            res = requests.patch(self.base_url + 'projects/delete', params=params)
            status = res.status_code
            assert status == 200
            return status
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while processing this request: {e}")

    def get_all_managers(self):
        """Positive: Get all managers """
        try:
            res = requests.get(self.base_url + 'users' + '?token=' + self.token)
            # res.raise_for_status()
            status = res.status_code
            managers = res.json()
            # for i in managers:
            #     managers = i.get('id')
            #     return managers
            # managers = text.get('id')
            return status, managers
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while processing this request: {e}")


Projects().create_project()
# Projects().get_managers()
# Projects().deactivate_project()
# Projects().activate_project()
# Projects().delete_project()
# Projects().get_all_managers()
