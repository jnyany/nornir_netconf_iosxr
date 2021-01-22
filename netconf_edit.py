from nornir import InitNornir
from nornir_scrapli.tasks import netconf_edit_config, netconf_commit
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file

nr = InitNornir(config_file="config.yaml")

def config_stuff(task):
    if_template = task.run(task=template_file, name="ifconfig", template="CC_LLF.j2",path="./templates")
    config_output = if_template.result
    task.run(task=netconf_edit_config, target="candidate", config=config_output)
    task.run(task=netconf_commit)

def delete_stuff(task):
    if_template = task.run(task=template_file, name="ifconfig", template="CC_LLF_Del.j2",path="./templates")
    config_output = if_template.result
    task.run(task=netconf_edit_config, target="candidate", config=config_output)
    task.run(task=netconf_commit)

# result = nr.run(task=config_stuff)
# print_result(result)

result = nr.run(task=delete_stuff)
print_result(result)