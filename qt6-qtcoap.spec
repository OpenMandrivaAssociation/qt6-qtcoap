#define beta rc
#define snapshot 20200627
%define major 6

%define _qtdir %{_libdir}/qt%{major}

Name:		qt6-qtcoap
Version:	6.12.0
Release:	%{?beta:0.%{beta}.}%{?snapshot:0.%{snapshot}.}1
# Qt does not publish this module on download.qt.io. The tag archive
# unpacks as qtcoap-<version>.
Source0:	https://github.com/qt/qtcoap/archive/refs/tags/v%{version}%{?beta:-%{beta}}.tar.gz#/qtcoap-%{version}%{?beta:-%{beta}}.tar.gz
Group:		System/Libraries
Summary:	Qt %{major} CoAP module
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(Qt%{major}Core)
BuildRequires:	cmake(Qt%{major}CorePrivate)
BuildRequires:	cmake(Qt%{major}Network)
BuildRequires:	cmake(Qt%{major}NetworkPrivate)
BuildRequires:	cmake(Qt%{major}Gui)
BuildRequires:	cmake(Qt%{major}Widgets)
BuildRequires:	cmake(Qt%{major}Quick)
BuildRequires:	cmake(Qt%{major}Qml)
BuildRequires:	qt%{major}-cmake
License:	GPLv3
# The library is GPL-3.0-only. There is no LGPL edition, and the module
# sources do not carry the Qt GPL exception.

%description
Client library for the Constrained Application Protocol (RFC 7252).
The library is GPL-3.0-only (there is no LGPL edition).

%define extra_devel_files_Coap \
%{_qtdir}/sbom/*

%qt6libs Coap

%package examples
Summary:	Examples for the Qt %{major} CoAP module
Group:		Development/KDE and Qt

%description examples
Examples for the Qt %{major} CoAP module

%files examples
%{_qtdir}/examples/coap

%prep
%autosetup -p1 -n qtcoap-%{version}%{?beta:-%{beta}}
%cmake -G Ninja \
	-DQT_BUILD_TESTS:BOOL=OFF \
	-DCMAKE_INSTALL_PREFIX=%{_qtdir} \
	-DQT_BUILD_EXAMPLES:BOOL=ON \
	-DQT_WILL_INSTALL:BOOL=ON

%build
export LD_LIBRARY_PATH="$(pwd)/build/lib:${LD_LIBRARY_PATH}"
%ninja_build -C build

%install
%ninja_install -C build
%qt6_postinstall
