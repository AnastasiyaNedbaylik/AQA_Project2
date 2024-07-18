import os
from array import array

from dotenv import load_dotenv
from utilities.settings import ProjectsPageData


load_dotenv()


class ApiData:
    API_BASE_URL = os.environ['API_BASE_URL']

    login_body = {
                'user[email]': os.environ["USER_VALID_EMAIL"],
                'user[password]': os.environ["USER_VALID_PASSWORD"]
            }

    create_project_required_data = {
                'name': f'API{ProjectsPageData.PROJECT_NAME}',
                'code': ProjectsPageData.SHORT_PROJECT_NAME,
                'color': '#70e6f9',
                'active': True,
                'kind': 'billable'
            }

    create_project_all_data = {
                "name": f'API{ProjectsPageData.PROJECT_NAME}',
                "code": ProjectsPageData.SHORT_PROJECT_NAME,
                "color": "#2642ab",
                'active': True,
                "kind": "billable",
                'icon_id': 1,
                'estimated': 80,
                'notes': 'test note',
                'client_id': 5563, # сделать создание клиента и возвращать  id
                'manager_id': 9526, # сделать получение id менеджера
                'status': 'Done',
                'business_unit': 'test'
            }

    expected_project_data = {
                "name": str,
                "code": str,
                'active': bool,
                "color": str,
                "kind": str,
                'icon_id': int,
                'estimated': int,
                'notes': str,
                'client_id': int,
                'start_date': str,
                'end_date': str,
                'manager_id': int,
                'status': str,
                'business_unit': str,
                'tasks': array[str],
                'custom_fields': str,
                'token': str
    }
