{pkgs}: {
  deps = [
    pkgs.remote-exec
    pkgs.openssh
    pkgs.hdf5
    pkgs.glibcLocales
    pkgs.xsimd
    pkgs.libxcrypt
    pkgs.tk
    pkgs.tcl
    pkgs.qhull
    pkgs.pkg-config
    pkgs.gtk3
    pkgs.gobject-introspection
    pkgs.ghostscript
    pkgs.freetype
    pkgs.ffmpeg-full
    pkgs.cairo
  ];
}
