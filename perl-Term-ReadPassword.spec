%define upstream_name    Term-ReadPassword
%define upstream_version 0.11
Name:		perl-%{upstream_name}
Version:	0.11
Release:	4

Summary:	Asking the user for a password
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Term-ReadPassword
Source0:	https://cpan.metacpan.org/authors/id/P/PH/PHOENIX/Term-ReadPassword-0.11.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module lets you ask the user for a password in the traditional way,
from the keyboard, without echoing.

This is not intended for use over the web; user authentication over the web
is another matter entirely. Also, this module should generally be used in
conjunction with Perl's *crypt()* function, sold separately.

The *read_password* function prompts for input, reads a line of text from
the keyboard, then returns that line to the caller. The line of text
doesn't include the newline character, so there's no need to use *chomp*.

%prep
%setup -q -n Term-ReadPassword-0.11

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
#Commenting-out because it's interactive.
#make test || :

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


