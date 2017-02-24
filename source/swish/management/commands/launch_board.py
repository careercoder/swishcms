from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils import translation
from board.models.board.main import Board
from board.models.profile.profile import BoardVendorProfile

from swish.models.swish.components import *
from swish.models.swish.menus import *

from django.contrib.auth.models import User

import sys
from pydoc import locate
print sys.argv
import uuid


class Command(BaseCommand):
    def handle(self, *args, **options):

        email = raw_input("Email: ")
        password = raw_input("Password: ")
        fname = raw_input("First name: ")
        lname = raw_input("Last name: ")

        print "--> Creating account."

        try:
            vendor_profile = BoardVendorProfile.objects.get(email=email)
        except BoardVendorProfile.DoesNotExist:

            # Create the User Auth Object
            user = User.objects.create_user(
                username='bv_' + str(uuid.uuid4())[-7:],
                password=password,
                email=email
            )
            user.save()

            vendor_profile = BoardVendorProfile()
            vendor_profile.user = user
            vendor_profile.first_name = fname
            vendor_profile.last_name = lname
            vendor_profile.email = email

            vendor_profile.save()

        print "--> Account Created."

        print "#"
        print "--> Basic Job Board Details "
        board_title = raw_input("Board name: ")
        board_domain = raw_input("Domain Only: ")
        board_alias = raw_input("Alias (for subdomain access): ")

        try:
            board = Board.objects.get(domain=board_domain)
            print "Board already exist."

        except Board.DoesNotExist:
            board = Board()
            board.user = vendor_profile.user
            board.title = board_title
            board.domain = board_domain
            board.alias = board_alias
            board.save()

            print "Board created."

        print "## <init page installations > ##"

        SWISH_APPS = settings.SWISH_APPS

        menutype = SwishMenuTypes()
        menutype.name = 'all'
        menutype.slug = 'all'
        menutype.board = board
        menutype.description = 'All available menu options installed.'
        menutype.save()
        h = False

        for component in SWISH_APPS:
            component_app_info_path = component + '.apps' + '.install'
            print "#< Loading App: " + component_app_info_path + ' >#'

            get_app = locate(component_app_info_path)

            if not get_app is None:
                app = get_app()

                for view in app['views']:
                    component = SwishComponent.objects.get(component=app['component'])
                    component_action = SwishComponentActions.objects.get(component=component, path=view['path'])

                    mitem = SwishMenu()
                    mitem.menutype = menutype
                    mitem.alias = view['default_alias']
                    mitem.board = board
                    mitem.note = view['description']
                    mitem.title = view['name']
                    mitem.component = component
                    mitem.action = component_action
                    mitem.save()

                    print str(component)
                    print view['path']


                if h is False:
                    mitem = SwishMenu()
                    mitem.menutype = menutype
                    mitem.alias = '/home/'
                    mitem.board = board
                    mitem.note = ''
                    mitem.title = 'Home Page'
                    mitem.component = component
                    mitem.action = component_action
                    mitem.save()
                    h = True
                    print "Home Page Created."


            # try:
            # get_component = locate(component_app_info_path)
            # get_component = get_component()



            try:
                pass
            except:
                get_component = None
                print str("Loading Component Failed")
                print str()
