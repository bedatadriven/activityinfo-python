import requests
from activityinfo import auth


class Client:
    """Client to interact with the ActivityInfo API."""

    def __init__(self, token, base_url='https://www.activityinfo.org/'):
        """Initialize a Client object

        :param token: Your API token.
        :param base_url: The base URL of the ActivityInfo API. The client will append 'resources/' to this URL.
        """
        self.auth = auth.TokenAuth(token)
        self.path = base_url + 'resources/'

    def get(self, resource_path, query_params=None):
        """Send a GET request to the ActivityInfo API

        :param resource_path: The path of the resource. For example, 'databases'.
        :param query_params: Dictionary, list of tuples or bytes to send in the query string for the request.
        :return: JSON-encoded contents of the response.
        """
        r = requests.get(url=self.path + resource_path,
                         params=query_params,
                         auth=self.auth,
                         headers={'Accept': 'application/json'})
        r.raise_for_status()
        return r.json()

    # TODO: post().
