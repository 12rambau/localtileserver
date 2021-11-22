import scooby


class Report(scooby.Report):
    def __init__(self, additional=None, ncol=3, text_width=80, sort=False):
        """Initiate a scooby.Report instance."""

        # Mandatory packages.
        large_image_core = [
            "large_image",
            "large_image_source_gdal",
            "cachetools",
            "PIL",
            "psutil",
            "numpy",
            "palettable",
            "pyproj",
            "osgeo.gdal",
        ]
        core = [
            "tileserver",
            "flask",
            "flask_caching",
            "requests",
            "werkzeug",
            "scooby",
        ] + large_image_core

        # Optional packages.
        optional = ["ipyleaflet", "large_image_source_mapnik", "tifftools"]

        scooby.Report.__init__(
            self,
            additional=additional,
            core=core,
            optional=optional,
            ncol=ncol,
            text_width=text_width,
            sort=sort,
        )
