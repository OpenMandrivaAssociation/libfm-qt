%define major 6
%define libname %mklibname fm-qt %{major}
%define devname %mklibname fm-qt -d

Name: libfm-qt
Version: 0.14.0
Release: 1
Source0: https://downloads.lxqt.org/downloads/%{name}/%{version}/%{name}-%{version}.tar.xz
Patch0: libfm-qt-0.14.0-fix-pkgconfig.patch
Summary: LXQt library for file management
URL: http://lxqt.org/
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
Requires: %{libname} = %{EVRD}
Requires: %{name}-data = %{EVRD}

%description
LXQt library for file management.

%package -n %{libname}
Summary: LXQt library for file management
Group: System/Libraries
Obsoletes: %{_lib}fm-qt5_2 < %{EVRD}
Obsoletes: %{_lib}fm-qt3 < %{EVRD}
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
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/fm-qt
