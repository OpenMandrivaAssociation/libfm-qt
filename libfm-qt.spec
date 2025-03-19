%define libname %mklibname fm-qt
%define devname %mklibname fm-qt -d

Name: libfm-qt
Version: 2.1.0
Release: 2
Source0: https://github.com/lxqt/libfm-qt/releases/download/%{version}/libfm-qt-%{version}.tar.xz
Summary: LXQt library for file management
URL: https://lxqt.github.io/
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
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Exif)
BuildRequires: cmake(lxqt)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: cmake(lxqt-menu-data) >= 2.0.0
Requires: lxqt-menu-data
Requires: %{libname} = %{EVRD}
Requires: %{name}-data = %{EVRD}

%description
LXQt library for file management.

%package -n %{libname}
Summary: LXQt library for file management
Group: System/Libraries
Requires: %{name}-data
%rename %{name}

%description -n %{libname}
LXQt library for file management.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
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
%cmake -DPULL_TRANSLATIONS=NO -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%files data
%{_datadir}/libfm-qt6
%{_datadir}/mime/packages/libfm-qt6-mimetypes.xml

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/fm-qt6
