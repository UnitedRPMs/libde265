%global commit0 fe395866e34f0740f1c7e9fb61e4ecfaa781ab6f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}


Name:           libde265
Version:        1.0.7
Release:        7%{?dist}
Summary:        Open h.265 video codec implementation
Group:		System Environment/Libraries
License:        LGPLv2 and GPLv2
URL:            https://github.com/strukturag/libde265
Source0:        https://github.com/strukturag/libde265/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  pkgconfig(sdl)
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libswscale)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)

%description
libde265 is an open source implementation of the h.265 video codec. It is
written from scratch and has a plain C API to enable a simple integration
into other software.

libde265 supports WPP and tile-based multithreading and includes SSE
optimizations. The decoder includes all features of the Main profile and
correctly decodes almost all conformance streams.

%package        devel
Summary:        Development files for libde265
Group:		System Environment/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The libde265 package contains libraries and header files for
developing applications that use libde265.

%package        tools
Summary:        Tools files for %{name}
Group:		System Environment/Libraries


%description    tools
The package contains the tools for libde265.

%prep
%autosetup -n %{name}-%{commit0} 

%build
./autogen.sh
%configure --enable-static=no --enable-shared
%make_build

%install
%make_install
find %{buildroot} -name '*.*a' -delete

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README.md
%{_libdir}/*.so.*

%files tools
%{_bindir}/*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libde265.pc

%changelog

* Thu Sep 24 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.0.7-7
- Updated to 1.0.7

* Thu Aug 27 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.0.6-7
- Updated to 1.0.6

* Fri Jan 17 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.0.5-7
- Updated to 1.0.5

* Fri Dec 20 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.0.4-7
- Updated to 1.0.4-7

* Tue Nov 27 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.0.3-3
- Migration to qt5

* Sat Nov 03 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.0.3-2
- Initial build

