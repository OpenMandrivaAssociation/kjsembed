%define major 5
%define libname %mklibname KF5JSEmbed %{major}
%define devname %mklibname KF5JSEmbed -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kjsembed
Version: 5.104.0
Release: 2
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/portingAids/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 JavaScript Embedding library
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5JS)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5DocTools)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5UiTools)
BuildRequires: pkgconfig(Qt5Svg)
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
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}%{major} --all-name --with-man

%files -f %{name}%{major}.lang
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
