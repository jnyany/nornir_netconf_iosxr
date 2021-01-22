from nornir_scrapli.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result
from nornir import InitNornir
import xml.dom.minidom
from nornir_utils.plugins.tasks.files import write_file

nr = InitNornir(config_file="config.yaml")

filterstuff="""
  <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
    <interface-configuration>
      <interface-name>TenGigE0/0/0/29</interface-name>
    </interface-configuration>
  </interface-configurations>
  """

policymap="""
  <policy-manager xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-infra-policymgr-cfg">
    <policy-maps>
      <policy-map>
        <name>BW-1000Mbps-Class-Business2-TE_JBL</name>
      </policy-map>
    </policy-maps>
  </policy-manager>
  """

policymapegr="""
  <policy-manager xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-infra-policymgr-cfg">
    <policy-maps>
      <policy-map>
        <name>egr</name>
      </policy-map>
    </policy-maps>
  </policy-manager>
  """

classmap="""
  <policy-manager xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-infra-policymgr-cfg">
    <class-maps>
      <class-map>
        <name>Business2-PCP-4_JBL</name>
      </class-map>
    </class-maps>
  </policy-manager>
  """

l2vpnxc="""
  <l2vpn xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-l2vpn-cfg">
    <database>
      <xconnect-groups>
        <xconnect-group>
          <name>JBL5_JBL6_LE-123456</name>
        </xconnect-group>
      </xconnect-groups>
    </database>
  </l2vpn>
  """

evpnevi712="""
  <evpn xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-l2vpn-cfg">
    <evpn-tables>
      <evpn-instances>
        <evpn-instance>
          <vpn-id>2600</vpn-id>
        </evpn-instance>
      </evpn-instances>
    </evpn-tables>
  </evpn>
  """

evpnevi663="""
  <evpn xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-l2vpn-cfg">
    <evpn-tables>
      <evpnevis>
        <evpnevi>
          <eviid>2600</eviid>
        </evpnevi>
      </evpnevis>
    </evpn-tables>
  </evpn>
  """

ethernetcfm="""
  <ethernet-features xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-l2-eth-infra-cfg">
    <cfm xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ethernet-cfm-cfg">
      <domains>
        <domain>
          <services>
            <service>
              <service>JBL5_JBL6_LE-654321</service>
            </service >
          </services>
        </domain>
      </domains>
    </cfm>
  </ethernet-features>
  """

def get_yang(task):
    task.run(task=netconf_get_config, source= "running", filter_type="subtree", filters=ethernetcfm)
    # task.run(task=netconf_get_config, source= "running")

result = nr.run(task=get_yang)
print_result(result)
