#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-cloud-init
Version  : 21
Release  : 23
URL      : https://github.com/clearlinux/clr-cloud-init/releases/download/v21/clr-cloud-init-21.tar.xz
Source0  : https://github.com/clearlinux/clr-cloud-init/releases/download/v21/clr-cloud-init-21.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: clr-cloud-init-bin
Requires: clr-cloud-init-config
Requires: clr-cloud-init-doc
BuildRequires : e2fsprogs-bin
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libparted)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(yaml-0.1)
BuildRequires : systemd-dev

%description
A cloud-init for Clear Linux* Project for Intel Architecture
====
Contents:
1) Description of this project
2) Compiling, prerequisites
3) Bugs and feedback?

%package bin
Summary: bin components for the clr-cloud-init package.
Group: Binaries
Requires: clr-cloud-init-config

%description bin
bin components for the clr-cloud-init package.


%package config
Summary: config components for the clr-cloud-init package.
Group: Default

%description config
config components for the clr-cloud-init package.


%package doc
Summary: doc components for the clr-cloud-init package.
Group: Documentation

%description doc
doc components for the clr-cloud-init package.


%prep
%setup -q -n clr-cloud-init-21

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cloud-init

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/cloud-init-pre-network.service
/usr/lib/systemd/system/cloud-init.service
/usr/lib/systemd/system/multi-user.target.wants/cloud-init-pre-network.service
/usr/lib/systemd/system/multi-user.target.wants/cloud-init.service

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
