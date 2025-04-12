'''Contains the class with data needed to access the files
'''
import os

# DEFAULT VALUES

# endpoint to access my Buckets
#   s3 - for AWS S3 Buckets;
#   https://s3.cubbit.eu - for Cubbit S3 Archives
# It gives preference to the environment variable S3_ENDPOINT (if exists)
_ENDPOINT: str = "s3"

# Server Region
# It gives preference to the environment variable S3_REGION (if exists)
#   eu-west-1 - for Cubbit S3 Archives
_REGION: str = "eu-central-1"

class Config:
    '''Contains the class with data needed to access the files '''

    s3_endpoint: str = None
    s3_region: str = None

    def __init__(self):
        """
        Initialize the Config class.

        Args:
            endpoint_url (str, optional): The S3 endpoint URL. Defaults to None.
        """
        _end_pnt = os.environ.get("S3_ENDPOINT", None)
        _region = os.environ.get("S3_REGION", None)
        print(f'Environ Endpoint: {_end_pnt}; Region: {_region}')


        if _end_pnt is None:
            _end_pnt = _ENDPOINT
        if _region is None:
            _region = _REGION
        self.s3_endpoint = _end_pnt
        self.s3_region = _region
        print(f'Final Endpoint: {_end_pnt}; Region: {_region}')
