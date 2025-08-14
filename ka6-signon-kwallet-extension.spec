#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.08.0
%define		kframever	6.13.0
%define		qtver		6.8
%define		kaname		signon-kwallet-extension
Summary:	signon-kwallet-extension
Name:		ka6-%{kaname}
Version:	25.08.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	96b23c3a93590f8cdb6665c5542f6723
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel
BuildRequires:	gettext-tools
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kwallet-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	signon-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
signon-kwallet-extension.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/signon/extensions/libkeyring-kwallet.so
