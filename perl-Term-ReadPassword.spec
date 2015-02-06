%define upstream_name    Term-ReadPassword
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Asking the user for a password
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#Commenting-out because it's interactive.
#make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.110.0-3mdv2011.0
+ Revision: 657839
- rebuild for updated spec-helper

* Sun Oct 17 2010 Shlomi Fish <shlomif@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 586543
- Disabled make test because it's interactive
- import perl-Term-ReadPassword

