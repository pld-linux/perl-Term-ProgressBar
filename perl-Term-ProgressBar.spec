#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Term
%define pnam	ProgressBar
Summary:	Term::ProgressBar - Perl extension to display a progress bar
Summary(pl):	Term::ProgressBar - rozszerzenie Perla do wy¶wietlania paska postêpu
Name:		perl-Term-ProgressBar
Version:	2.05
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ffbc791ad39273ad00e0662efee804fc
BuildRequires:	perl-Class-MethodMaker >= 1.02
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A progress bar for things that take a while. It looks like
 50% [=====     ]
and is as long as the terminal. Linear estimation of the time left for
the process to run is available.

%description -l pl
Pasek postêpu dla rzeczy trwaj±cych nieco czasu. Wygl±da tak:
 50% [=====     ]
i jest takiej szeroko¶ci jak terminal. Dostêpna jest liniowa estymacja
czasu potrzebnego na wykonanie procesu.

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
%doc BUGS Changes README
%{perl_vendorlib}/Term/ProgressBar.pm
%{_mandir}/man3/*
