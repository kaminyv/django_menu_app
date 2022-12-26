"""
Tags for menu_app application.
"""
from collections import defaultdict
from django import template
from menu_app.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', name='draw_menu')
def show_menu(menu_filter=None):
    """
    Formation of menu items by menu name.
    """
    if not menu_filter:
        return {'menu': ''}

    query_items = MenuItem.objects.filter(menu__name=menu_filter).values()

    menu_map = defaultdict(list)

    for query_item in query_items:
        menu_map[query_item['parent_id']].append(query_item)

    def get_node_items(items_map, item_idx):
        level_items = items_map.get(item_idx, [])
        return [
            {
                "item": item,
                "items": get_node_items(items_map, item["id"])
            } for item in level_items
        ]

    return {'menu_tree': get_node_items(menu_map, None)}
