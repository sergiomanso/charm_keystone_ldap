import os
import charms_openstack.charm as ldap_charm
import charmhelpers.core.hookenv as ch_hookenv  # noqa
#https://github.com/juju-solutions/charms.templating.jinja2
from charms.templating.jinja2 import render

#https://charm-helpers.readthedocs.io/en/latest/examples/config.html
hooks = ch_hookenv.Hooks()

ldap_charm.use_defaults('charm.default-select-release')

LDAP_CONFIG_FILE_DIR = "/etc/keystone/domains/"
LDAP_CONFIG_FILE = LDAP_CONFIG_FILE_DIR + "keystone.{}.conf"
TEMPLATE = "keystone_ldap.j2"

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
        config = hookenv.config()

        if not os.path.exists(LDAP_CONFIG_FILE_DIR):
            try:
                os.mkdir(LDAP_CONFIG_FILE_DIR)
            except:
                print("Could not create domain folder")

        target = os.path.join(LDAP_CONFIG_FILE_DIR, 
                                LDAP_CONFIG_FILE.format(config['ldap-domain'])
        # dont need the absolute path, lib searches for templates folder
        #templates_dir = os.path.join(hookenv.charm_dir(), 'templates')
        try:
            render(
                TEMPLATE,
                target
                {
                    'url' : config['ldap-url'],
                    'user' : config['ldap-user'],
                    'password' : config['ldap-password'],
                    'suffix' : config['ldap-suffix'],
                })
        except:
            print("Could not render template")

        return

"""
    # I think this can be implemented by using the apt layer or using inheritance
    # e.g. class CharmKeystoneLDAP(OpenStackCharm):    
    def install_dependencies(self):
        return
"""