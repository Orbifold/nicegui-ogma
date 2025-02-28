from typing import Callable, Optional

from nicegui.element import Element


class GraphViz(Element, component='graphviz.vue'):

    def __init__(self, title: str, *, on_change: Optional[Callable] = None) -> None:
        super().__init__()
        
        self.on('change', on_change)
 