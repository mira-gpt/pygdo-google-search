from gdo.base.GDO_Module import GDO_Module


class module_google_search(GDO_Module):
    """API-neutral foundation for authorised web-search providers."""

    def gdo_dependencies(self):
        return ['net']
