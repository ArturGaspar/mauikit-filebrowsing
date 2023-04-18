%global qt5_min_version 5.15.0
%global kf5_min_version 5.70.0

Name:       opt-maui-mauikit-filebrowsing
Version:    2.2.1
Release:    1
Summary:    MauiKit FileBrowsing
License:    LGPL-2.1-or-later
URL:        https://mauikit.org/
Source:     mauikit-filebrowsing-%{version}.tar.xz
Requires:   opt-kf5-kconfig >= %{kf5_min_version}
Requires:   opt-kf5-kcoreaddons >= %{kf5_min_version}
Requires:   opt-kf5-ki18n >= %{kf5_min_version}
Requires:   opt-maui-mauikit
Requires:   opt-qt5-qtbase >= %{qt5_min_version}
Requires:   opt-qt5-qtdeclarative >= %{qt5_min_version}
BuildRequires:  cmake >= 3.16
BuildRequires:  opt-extra-cmake-modules >= %{kf5_min_version}
BuildRequires:  opt-kf5-kconfig-devel >= %{kf5_min_version}
BuildRequires:  opt-kf5-kcoreaddons-devel >= %{kf5_min_version}
BuildRequires:  opt-kf5-ki18n-devel >= %{kf5_min_version}
BuildRequires:  opt-kf5-rpm-macros
BuildRequires:  opt-maui-mauikit-devel
BuildRequires:  opt-qt5-qtbase-devel >= %{qt5_min_version}
BuildRequires:  opt-qt5-qtdeclarative-devel >= %{qt5_min_version}
%{?opt_kf5_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^libMauiKit.*$

%description
FileBrowsing is a MauiKit Framework to work with local and remote files.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}

mkdir -p build
pushd build

%_opt_cmake_kf5 .. \
    -DKDE_INSTALL_BINDIR:PATH=/usr/bin \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DQUICK_COMPILER=OFF \
    -DKIO_AVAILABLE=OFF
%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%files
%license LICENSES/*.txt
%{_opt_kf5_libdir}/libMauiKitFileBrowsing.so
# Sic. Fixed in next version.
%{_opt_kf5_libdir}/libMauiKitFileBrowsing.so.SOVERSION
%{_opt_kf5_qmldir}/org/mauikit/filebrowsing
%{_datadir}/locale/*/*/mauikitfilebrowsing.mo

%files devel
%{_opt_kf5_includedir}/MauiKit/FileBrowsing
%{_opt_kf5_libdir}/cmake/MauiKitFileBrowsing
