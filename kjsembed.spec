%define major 5
%define libname %mklibname KF5JSEmbed %{major}
%define devname %mklibname KF5JSEmbed -d
%define debug_package %{nil}

Name: kjsembed
Version: 4.99.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/portingAids/%{version}/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 JavaScript Embedding library
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: qmake5
BuildRequires: cmake
BuildRequires: extra-cmake-modules5
BuildRequires: cmake(KF5JS)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5DocTools)
BuildRequires: pkgconfig(Qt5Core)
Requires: %{libname} = %{EVRD}

%description
The KDE Frameworks 5 JavaScript Embedding library.

%package -n %{libname}
Summary: The KDE Frameworks 5 JavaScript Embedding library
Group: System/Libraries

%description -n %{libname}
The KDE Frameworks 5 JavaScript Embedding library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: %{name} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%apply_patches
%cmake

%build
%make -C build

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5

%files
%{_bindir}/*
%{_mandir}/man1/kjscmd5.1*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*
