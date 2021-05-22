#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Type
Version  : 0.22
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/P/PM/PMISON/File-Type-0.22.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PM/PMISON/File-Type-0.22.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-type-perl/libfile-type-perl_0.22-3.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-Type-license = %{version}-%{release}
Requires: perl-File-Type-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
File::Type - determine file type using magic
INSTALLING
Install using the standard Module::Build method:

%package dev
Summary: dev components for the perl-File-Type package.
Group: Development
Provides: perl-File-Type-devel = %{version}-%{release}
Requires: perl-File-Type = %{version}-%{release}

%description dev
dev components for the perl-File-Type package.


%package license
Summary: license components for the perl-File-Type package.
Group: Default

%description license
license components for the perl-File-Type package.


%package perl
Summary: perl components for the perl-File-Type package.
Group: Default
Requires: perl-File-Type = %{version}-%{release}

%description perl
perl components for the perl-File-Type package.


%prep
%setup -q -n File-Type-0.22
cd %{_builddir}
tar xf %{_sourcedir}/libfile-type-perl_0.22-3.debian.tar.xz
cd %{_builddir}/File-Type-0.22
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/File-Type-0.22/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Type
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-File-Type/aaef585a6eb1da6fa99db135801024dc6fe42d4e
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Type.3
/usr/share/man/man3/File::Type::Builder.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Type/aaef585a6eb1da6fa99db135801024dc6fe42d4e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/File/Type.pm
/usr/lib/perl5/vendor_perl/5.34.0/File/Type/Builder.pm
