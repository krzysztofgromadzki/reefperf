from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from pprint import pprint

ComputeEngine = get_driver(Provider.GCE)
service_account_email = ''
pem_file = ''
project_id = ''
driver = ComputeEngine(service_account_email, pem_file, project=project_id)
# pprint(driver.list_images())
# pprint(driver.list_sizes())
node = driver.create_node("gce-instance", "f1-micro", "ubuntu-minimal-1804-bionic-v20180705", "europe-west4-a")
pprint(node)
# node.destroy()
