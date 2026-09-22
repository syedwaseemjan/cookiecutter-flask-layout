"""Services. Add one module per area.

Web views and API modules call services. A service uses models and ``db.session``.
It does not import Flask request, response, or template helpers. Models do not
import Flask.
"""
