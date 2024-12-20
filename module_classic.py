from gdo.base.GDO_Module import GDO_Module


class module_classic(GDO_Module):

    async def gdo_load_scripts(self, page):
        self.add_css('css/pygdo_classic.css')
        self.add_css('css/pygdo_sidebar.css')
        self.add_js('css/pygdo_classic.js')
