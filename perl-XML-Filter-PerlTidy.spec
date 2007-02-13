#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Filter-PerlTidy
Summary:	XML::Filter::PerlTidy - SAX filter through Perl::Tidy
Summary(pl.UTF-8):	XML::Filter::PerlTidy - filtr SAX za pośrednictwem Perl::Tidy
Name:		perl-XML-Filter-PerlTidy
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9fc25034878e114a332fe2736d0e9513
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-Filter-BufferText
BuildRequires:	perl-XML-SAX
BuildRequires:	perl-XML-SAX-Writer
BuildRequires:	perltidy
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Filter::PerlTidy automatically calls XML::Filter::BufferText to
coalesce character data so that a complete element is fed to PerlTidy.

%description -l pl.UTF-8
XML::Filter::PerlTidy automatycznie wywołuje XML::Filter::BufferText
aby połączyć dane znakowe tak, aby dostarczyć kompletny element do
PerlTidy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/XML/*/*.pm
%{_mandir}/man3/*
