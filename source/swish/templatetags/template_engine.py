from django import template
from pydoc import locate

register = template.Library()
'''

@register.simple_tag()
def has_position(position, request):

    elements = request.page.elements.all()  # .filter(board=request.board, position=position)

    if not len(elements) == 0:

        # detect elements types
        element_list = []

        for element in elements:

            if element.position == position:  # plugin - installed.
                return True
            else:
                pass
        return False
'''


# @register.simple_tag
@register.inclusion_tag('swish/render-element.html')
def element_position(position, request):

    try:
        pass
    except:
        return {"blank":True}

    elements = request.page.elements.all()  # .filter(board=request.board, position=position)

    if not len(elements) == 0:

        # detect elements types
        element_list = []

        for element in elements:

            if element.type == 'plugin':  # plugin - installed.

                try:
                    pass
                except:
                    pass

                load_element = locate(str(element.element_path) + '.load_element')
                load_element = load_element(request)

                element.data = load_element



        request = request
        return {"request": request, 'elements': elements}

