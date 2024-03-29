%define libname %mklibname fm-qt
%define devname %mklibname fm-qt -d

Name: libfm-qt
Version: 1.4.0
Release: 1
Source0: https://github.com/lxqt/libfm-qt/releases/download/%{version}/libfm-qt-%{version}.tar.xz
Summary: LXQt library for file management
URL: http://lxqt.github.io/
License: LGPL 2.1
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(libfm)
BuildRequires: pkgconfig(libfm-extra)
BuildRequires: pkgconfig(libmenu-cache)
BuildRequires: pkgconfig(libexif)
BuildRequires: qmake5
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Exif)
BuildRequires: cmake(lxqt)
BuildRequires: cmake(lxqt-build-tools)
BuildRequires: cmake(lxqt-menu-data)
Requires: lxqt-menu-data
Requires: %{libname} = %{EVRD}
Requires: %{name}-data = %{EVRD}

%description
LXQt library for file management.

%package -n %{libname}
Summary: LXQt library for file management
Group: System/Libraries
Obsoletes: %{_lib}fm-qt5_2 < %{EVRD}
Obsoletes: %{_lib}fm-qt3 < %{EVRD}
Obsoletes: %{mklibname fm-qt 9} < %{EVRD}
Obsoletes: %{mklibname fm-qt 10} < %{EVRD}
Requires: %{name}-data
%rename %{name}

%description -n %{libname}
LXQt library for file management.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Obsoletes: %{_lib}fm-qt5-devel < %{EVRD}
Requires: pkgconfig(libexif)
Requires: pkgconfig(libmenu-cache)

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package data
Summary: Data files needed for the LXQt file management library
Group: System/Libraries
BuildArch: noarch

%description data
Data files needed for the LXQt file management library

%prep
%autosetup -p1
%cmake_qt5 -DPULL_TRANSLATIONS=NO -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%files data
%{_datadir}/libfm-qt
%{_datadir}/mime/packages/libfm-qt-mimetypes.xml

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/fm-qt
