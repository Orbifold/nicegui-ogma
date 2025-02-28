from nicegui import ui, app
from graphviz import GraphViz

app.add_static_files('/public', 'public')
ui.add_head_html('''<script  src="/public/ogma/ogma.js"></script>''', shared=True)
with ui.row(align_items='center'):
    on_off = GraphViz('State', on_change=lambda e: ui.notify(f'The value changed to {e.args}.'))


ui.run(uvicorn_reload_includes='*.py,*.js,*.vue')  