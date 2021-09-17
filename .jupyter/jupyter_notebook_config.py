# Configuration file for jupyter-notebook.

## Supply overrides for the tornado.web.Application that the Jupyter notebook
#  uses.
#  Default: {}
c.NotebookApp.tornado_settings = {"websocket_max_message_size": 500 * 1024 * 1024}