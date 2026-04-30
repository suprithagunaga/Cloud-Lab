from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()
compute = discovery.build('compute', 'v1', credentials=credentials)
project = 'your-project-id'
def create_vpc(network_name, auto_create_subnetworks=False):
    config = {
        'name': network_name,
        'autoCreateSubnetworks': auto_create_subnetworks
    }
    return compute.networks().insert(project=project,
body=config).execute()
def create_subnet(network_name, region, subnet_name, ip_range):
    config = {
        'name': subnet_name,
        'ipCidrRange': ip_range,
        'network':
f'projects/{project}/global/networks/{network_name}',
        'region': region
         }
    return compute.subnetworks().insert(project=project,
region=region, body=config).execute()
# Create dev-vpc and subnet
create_vpc('dev-vpc')
create_subnet('dev-vpc', 'us-central1', 'dev-subnet', '10.10.0.0/16')
# Create prod-vpc and subnet
create_vpc('prod-vpc')
create_subnet('prod-vpc', 'us-east1', 'prod-subnet', '10.20.0.0/16')
print("VPCs and Subnets created successfully.")
