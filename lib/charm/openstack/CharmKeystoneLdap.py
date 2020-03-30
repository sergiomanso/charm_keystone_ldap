import charms_openstack.charm as charm
import charmhelpers.core.hookenv as ch_hookenv  # noqa

charms_openstack.charm.use_defaults('charm.default-select-release')

class CharmKeystoneLDAP():

    name = 'keystone ldap configuration'
    version = 'v0.0.1'

    def config_ldap(self):
        """
        Define the destination LDAP server in the /etc/keystone/keystone.conf or
        /etc/keystone/domains/keystone.DOMAIN_NAME.conf :

        [ldap]
        url = ldap://localhost
        user = dc=Manager,dc=example,dc=org
        password = samplepassword
        suffix = dc=example,dc=org
        """

        return

"""
    # I think this can be implemented by using the apt layer or using inheritance
    # e.g. class CharmKeystoneLDAP(OpenStackCharm):    
    def install_dependencies(self):
        return
"""