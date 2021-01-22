from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import netconf_capabilities


nr = InitNornir(config_file="config.yaml")

def netconf_capability(task):
    task.run(task=netconf_capabilities)

capability = nr.run(task=netconf_capability)
print_result(capability)