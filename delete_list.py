import click
import json
import requests
import sys

@click.command()
@click.option('--user', prompt='User', help='Target audience user.')
@click.option('--token', prompt='API Token', help='Target Audience API token.')
@click.option('--library_id', prompt='Library ID', help='User\'s Library ID.')
@click.option('--list_id', prompt='List ID to delete', help='ID of list to delete.')
def delete_list(user, token, library_id, list_id):
    """Script to delete a list from target audience. 
    
    All options are required, if you ommit them it will prompt
    you for the appropriate values.
    """

    url = 'https://survey.qualtrics.com/WRAPI/Contacts/api.php'
    api_params = {
            'Request': 'deleteList',
            'User': user, 
            'Token': token, 
            'Format': 'JSON',
            'Version': '2.3',
            'LibraryID': library_id,
            'ListID': list_id,
            }

    response = requests.get(url, api_params)
    print json.dumps(response.json(), indent=4)

if __name__ == '__main__':
    delete_list()
