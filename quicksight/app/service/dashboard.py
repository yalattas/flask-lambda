from model.dashboard import Dashboard

class DashboardService():
    def get(object):
        return Dashboard.get('a1455b57-b8ef-id-a45f-570f3297a265')
    def get_all(object):
        return Dashboard.fetch_all()