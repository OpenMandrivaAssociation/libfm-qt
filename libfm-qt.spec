%define major 3
%define libname %mklibname fm-qt %{major}
%define devname %mklibname fm-qt -d

Name: libfm-qt
Version: 0.11.0
Release: 1
Source0: https://downloads.lxqt.org/%{name}/%{version}/%{name}-%{version}.tar.xz
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
BuildRequires: pkgconfig(libmenu-cache)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5X11Extras)

%description
LXQt library for file management

%package -n %{libname}
Summary: LXQt library for file management
Group: System/Libraries
Requires: %{name} = %{EVRD}
Obsoletes: %{_lib}fm-qt5_2 < %{EVRD}

%description -n %{libname}
LXQt library for file management

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Obsoletes: %{_lib}fm-qt5-devel < %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_datadir}/%{name}

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/fm-qt
