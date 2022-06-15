from service.dashboard import DashboardService

class DashboardController():
    def get_dashboard(object):
        return DashboardService.get(object)
    def get_dashboards(object):
        return DashboardService.get_all(object)