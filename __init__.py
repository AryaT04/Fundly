# __init__.py

from pages.dashboard import show_dashboard
from pages.transactions import show_transactions
from pages.insights import show_insights
from pages.security import show_security
from pages.quick_actions import quick_actions
# In data/__init__.py
def import_quick_actions():
    from pages.quick_actions import quick_actions
    return quick_actions
