
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

from pdf_with_js.printer import Printer


class PdfWithJS(BasePlugin):

    config_scheme = (
        ('enable', config_options.Type(bool, default=True)),
    )

    def __init__(self):

        self.printer = Printer()

        pass

    def on_config(self, config, **kwargs):
        self.enabled = self.config['enable']
        return config

    def on_nav(self, nav, config, files):
        return nav

    def on_post_page(self, output_content, page, config, **kwargs):
        if not self.enabled:
            return output_content

        page_paths = self.printer.add_page(page, config)
        output_content = self.printer.add_download_link(output_content, page_paths)

        return output_content

    def on_post_build(self, config):
        if not self.enabled:
            return

        self.printer.print_pages()
