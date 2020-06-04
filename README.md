# MkDocs PDF with JS Plugin

A MkDocs plugin that exports your documentation as PDF with rendered JavaScript content. This is very useful if you want to have your mermaid diagrams in your pdf documents as well. A download link will be added to the top of your documentation.

## Requirements

For executing the JavaScript code ChromeDriver is used. So it is nesseccary to

- install Chrome or Chromium
- download ChromeDriver and
- add the ChromeDriver to your PATH

## Installation

Install the package with pip:

```bash
pip install mkdocs-pdf-with-js-plugin
```

Enable the plugin in your mkdocs.yml as folowing

```yml
plugins:
    - search
    - pdf-with-js
```

or with options

```yml
plugins:
    - search
    - pdf-with-js:
        enable: true
```

> **Note**: If you enable this plugin and you don't have plugins entry in your MkDocs config file yet, you will need to explicitly enable the search plugin. This plugin is enable by default when no plugins entry is set.

You can find further information about plugins in the [MkDocs documentation](http://www.mkdocs.org/user-guide/plugins/)

## Config

- `enable` - Enable or disable the PDF export. `default: true`

## Usage

While building `mkdocs build` or serving `mkdocs serve` the documentation the pdfs get generated. They are stored in `site_dir/pdfs`.
