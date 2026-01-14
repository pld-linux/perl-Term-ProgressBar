#
# Conditional build:
%bcond_with	tests	# do perform "make test"
			# it needs imported gpg key or network connection, do disabled

%define		pdir	Term
%define		pnam	ProgressBar
Summary:	Term::ProgressBar - Perl extension to display a progress bar
Summary(pl.UTF-8):	Term::ProgressBar - rozszerzenie Perla do wyświetlania paska postępu
Name:		perl-Term-ProgressBar
Version:	2.10
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e8c6a2c779440698f7fbd2b024fae0ac
URL:		http://search.cpan.org/dist/Term-ProgressBar/
BuildRequires:	perl-Class-MethodMaker >= 1.02
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A progress bar for things that take a while. It looks like
 50% [=====	]
and is as long as the terminal. Linear estimation of the time left for
the process to run is available.

%description -l pl.UTF-8
Pasek postępu dla rzeczy trwających nieco czasu. Wygląda tak:
 50% [=====	]
i jest takiej szerokości jak terminal. Dostępna jest liniowa estymacja
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
