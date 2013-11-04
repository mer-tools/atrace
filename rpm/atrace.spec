Name:       atrace
Summary:    Android tracing utility.
Version:    0.0.0
Release:    1
Group:      Development/Tools
License:    MIT
URL:        https://github.com/mer-tools/atrace
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qt5-qmake

%description
Description: %{summary}

%prep
%setup

%build
%qmake5
make %{_smp_mflags}

%install
%qmake5_install

%files
%defattr(-,root,root,-)
%{_bindir}/atrace

