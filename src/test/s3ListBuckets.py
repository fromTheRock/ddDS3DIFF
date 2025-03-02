from S3Ops import S3Ops as s3

def main() -> None:
    """Main entry point of the script"""
    endpoint, region = s3.getConnectionData()
    client = s3.getS3Client(endpoint)
    response = s3.listBuckets(client, endpoint, region)
    #print(response)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print('S3 buckets listed successfully.')
        print(f'HTTP Status Code: {response["ResponseMetadata"]["HTTPStatusCode"]}')
        #print(f'Request ID: {response["ResponseMetadata"]["RequestId"]}')
        print(f'HTTP Headers: {response["ResponseMetadata"]["HTTPHeaders"]}')
        print(f'Retry Attempts: {response["ResponseMetadata"]["RetryAttempts"]}')
        print(f'Bucket Owner: {response["Owner"]["DisplayName"]}')
        print(f'Bucket Owner ID: {response["Owner"]["ID"]}')
        #print(f'Bucket Owner Type: {response["Owner"]["Type"]}')
        print(f'Bucket Owner Display Name: {response["Owner"]["DisplayName"]}')
    else:
        print(f'Error: {response["ResponseMetadata"]["HTTPStatusCode"]}')
        return
    
    print("Final Result:")
    print(f'Buckets: {response["Buckets"]}')

if __name__ == "__main__":
    main()
