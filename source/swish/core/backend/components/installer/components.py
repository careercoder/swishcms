from django.conf import  settings

from pydoc import locate

from swish.models.swish.components import SwishComponent, SwishComponentActions
from swish.models.swish.permissions import *


class SwishInstaller:


    def get_components(self):


        components = getattr(settings, "SWISH_APPS", [])

        for component in components:


            component_app_info_path = component + '.apps' + '.install'
            print "#< Loading ># " + component_app_info_path

            try:
                get_component = locate(component_app_info_path)
                get_component = get_component()
                
            except:
                get_component = None
                print str("Loading Component Failed: " + component_app_info_path)
                print str()

            if not get_component == None:

                # return get_component['component']

                try:
                    component_check = SwishComponent.objects.get(component=str(get_component['component']))
                    print "--> Component Already Installed"
                    print ""
                    for view in get_component['views']:

                        try:
                            component_action = SwishComponentActions.objects.get(name=view['name'], component=component_check)
                            print "--> " + str(component_action.name) + ' ' + str("already installed.")
                            print "--> " + "checking views and action version."
                            print "--> " + "view version is up-to-date."
                            print ""
                        except SwishComponentActions.DoesNotExist:

                            print "Installing view:  " + str(view['name'])

                            o_view = SwishComponentActions()
                            o_view.component = component_check
                            o_view.name = view['name']
                            o_view.path = view['path']
                            o_view.alias = view['default_alias']
                            o_view.description = view['description']
                            o_view.save()

                            print str(view['name'] + " installed successfully.")
                            print str(".......................................")

                        #except:
                         #   print "An error occured while processing the installation."




                except SwishComponent.DoesNotExist:

                    print "--> Installing Component"

                    o_component = SwishComponent()
                    o_component.name = get_component['name']
                    o_component.component = get_component['component']
                    o_component.alias = get_component['alias']
                    o_component.version = get_component['version']
                    o_component.path = get_component['path']
                    o_component.save()

                    print "... Component Installation Complete."
                    print "# Action View Installation"
                    print "# Installing Component Actions/Views"

                    for view in get_component['views']:

                        print "... Installing view:  " + str(view['name'])
                        '''
                                    {
                                        "name": "Recent Postings",
                                        "default_alias": "/jobs/recent/",
                                        "path": ".views.recent.view",
                                        "description": "View Recent Postings",
                                    },
                        '''
                        o_view = SwishComponentActions()
                        o_view.component = o_component
                        o_view.name = view['name']
                        o_view.path = view['path']
                        o_view.alias = view['default_alias']
                        o_view.description = view['description']
                        o_view.save()

                        print str("..." + view['name'] + " installed successfully.")
                        print str(".......................................")





               # except:
               #     print "Failed to load."

            try:
                pass
            except:
                print False

        return str("Component Installation Complete.")

