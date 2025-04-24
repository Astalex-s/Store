class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        contex = super(TitleMixin, self).get_context_data(**kwargs)
        contex['title'] = self.title
        return contex
