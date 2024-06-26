pkgname = "evince"
pkgver = "46.1"
pkgrel = 0
build_style = "meson"
# dvi needs kpathsea, which is in texlive
# does anyone actually need dvi?
configure_args = [
    "-Dintrospection=true",
    "-Dgtk_doc=false",
    "-Dnautilus=false",
    "-Dcomics=enabled",
    "-Dps=enabled",
    "-Ddvi=disabled",
]
hostmakedepends = [
    "adwaita-icon-theme",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "itstool",
    "meson",
    "perl-xml-parser",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "djvulibre-devel",
    "glib-devel",
    "gsettings-desktop-schemas-devel",
    "gspell-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "libarchive-devel",
    "libgxps-devel",
    "libhandy-devel",  # "nautilus-devel",
    "libpoppler-devel",
    "libsecret-devel",
    "libspectre-devel",
    "libtiff-devel",
]
pkgdesc = "GNOME document viewer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Evince"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "94bb525365b060a28c2f6017d22cbf2af5115507254aa42e9bfc000bbc18ab62"


@subpackage("evince-libs")
def _libs(self):
    return self.default_libs()


@subpackage("evince-devel")
def _devel(self):
    return self.default_devel()
