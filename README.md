OARepo
==============



Installation
--------------------

1. Create fcrepo.war with build in fedora_group_plugin and cesnet.fcrepo-http-api-with-states (this has to replace original fcrepo-http-api in fcrepo.war)

2. Modify `WEB-INF/classes/spring/auth-repo.xml`, and add/change the following:

        <bean name="djangoGroupPrincipalProvider" 
              class="cz.cesnet.fcrepo.auth.django.DjangoGroupPrincipalProvider"/>

        <util:set id="principalProviderSet">
          <ref bean="djangoGroupPrincipalProvider"/>
          <ref bean="delegatedPrincipalProvider"/>
        </util:set>

3. Modify `fcrepo/WEB-INF/classes/config/jdbc-postgresql` and add/change the following:

        "security" : {
           "anonymous" : {
               "roles" : ["readonly","readwrite","admin"],
               "useOnFailedLogin" : false
           },
           "providers" : [
               { "classname" : "org.fcrepo.auth.common.ServletContainerAuthenticationProvider" }
           ]
        },

4. Install oarepo and fedoralink and requirements into active virtualenv

    virtualenv should contain:
     *   Django 1.10
     *   pip
     *   fedoralink (`pip install -e /path/to/local/fedoralink/directory`)
     *   bleach
     *   django-bootstrap-pagination
     *   django-bootstrap3
     *   html5lib
     *   inflection
     *   isodate
     *   pyparsing
     *   python-dateutil
     *   rdflib
     *   requests
     *   setuptools
     *   six
     *   wheel

    Edit Settings.py in oarepo:

    		Set ALLOWED_HOSTS
        		DATABASES (postgresql)
    				Set FedoraAdmin username and password
        		STATIC_ROOT = '/apache/static'

5. Set fedoraAdmin user account in /etc/tomcat/tomcat-users.xml

6. Run `./manage.py migrate` (sets up Database)

7. Run `./manage.py collect_static` (copies static files - css, js into STATIC_ROOT directory)

8. Run from oarepo `python createTypes/createCollection.py`

9. Run from oarepo `./manage.py nastav_vyhledavaci_indexy` (creates indexes in Elasticsearch)

10. Run from oarepo `( cd createTypes; python nahraj_sablony.py )`

11. Create ACLs

12. Run from oarepo `./manage.py nastav_vyhledavaci_indexy` (creates indexes in Elasticsearch)

13. Create superuser in Django `./manage.py createsuperuser`

14. Create users and groups in Django.


