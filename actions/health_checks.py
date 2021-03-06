from lib import action


class ConsulHealthChecksAction(action.ConsulBaseAction):
    def run(self,
            service,
            index=None,
            wait=None,
            dc=None,
            near=None,
            token=None):

        return (True, self.consul.health.checks(
            service,
            index=index,
            wait=wait,
            dc=dc,
            near=near,
            token=token))
