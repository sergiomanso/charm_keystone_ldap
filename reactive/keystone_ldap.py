# Learning/testing phase
# Doesn't work yet lol
# based on:
#  https://github.com/openstack-charmers/cinder-storage-backend-template
#  https://jaas.ai/tutorials/tutorial-charm-development-part1#7-add-functionality-with-layers
#  https://charmsreactive.readthedocs.io/en/latest/
#  https://docs.openstack.org/charm-guide/latest/charm-anatomy.html


import charms_openstack.charm as charm
import charms.reactive as reactive

# This charm's library contains all of the handler code associated with
# this charm -- we will use the auto-discovery feature of charms.openstack
# to get the definitions for the charm.
import charms_openstack.bus as bus
bus.discover()

charm.use_defaults(
    'charm.installed',
    'update-status',
    'upgrade-charm',
    #'keystone-backend.connected', ##need to define this on metadata (why do I need this?)
    # I don't think I will need this because I'm not implementing an interface
)

@reactive.when('config.changed') #detects any change on config file
@reactive.when_not('keystone-ldap.installed') # not sure about this
def config():
    #this will get the instance of the charm that we are deploying
    with charm.provide_charm_instance() as keystone_charm:
        ##calls the method from the created charm
        keystone_charm.config_ldap()
        reactive.set_flag('config.finished')

# this will stay here just as an example
"""
@reactive.when_not('keystone-ldap.installed')
def install_keystone_ldap():

    #this will get the instance of the charm that we are deploying
    with charm.provide_charm_instance() as kcharm:
        # installs dependencies if they are defined
        charm.install_dependencies()

    # Do your setup here.
    #
    # If your charm has other dependencies before it can install,
    # add those as @when() clauses above., or as additional @when()
    # decorated handlers below
    #
    # See the following for information about reactive charms:
    #
    #  * https://jujucharms.com/docs/devel/developer-getting-started
    #  * https://github.com/juju-solutions/layer-basic#overview
    #
    set_flag('keystone-ldap.installed')

@reactive.when_not('keystone-ldap.installed')
def config():
        #this will get the instance of the charm that we are deploying
    with charm.provide_charm_instance() as kcharm:
        charm.install_dependencies() ##calls the install method from the OpenStack 

"""

@reactive.when_not('keystone-ldap.installed')
def config():
        #this will get the instance of the charm that we are deploying
    with charm.provide_charm_instance() as kcharm:
        charm.install_dependencies() ##calls the install method from the OpenStack 