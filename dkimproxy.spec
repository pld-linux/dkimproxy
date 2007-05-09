# TODO
# - dkfilter user, initscript
%include	/usr/lib/rpm/macros.perl
Summary:	dkimproxy - an SMTP-proxy designed for Postfix
Name:		dkimproxy
Version:	0.15
Release:	0.1
License:	GPL v2
Group:		Daemons
Source0:	http://jason.long.name/dkimproxy/%{name}-%{version}.tar.gz
# Source0-md5:	41fa377a910f863d26681724f737fbaa
Patch0:		%{name}-perllib.patch
Patch1:		%{name}-am.patch
URL:		http://jason.long.name/dkimproxy/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-Error
BuildRequires:	perl-Mail-DKIM >= 0.20
BuildRequires:	perl-Net-Server >= 0.89
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _sysconfdir     /etc/%{name}

%description
DKIM Proxy is an SMTP-proxy that signs and/or verifies emails, using
the Mail::DKIM module. It is designed for Postfix. It comprises two
separate proxies, an "outbound" proxy for signing outgoing email, and
an "inbound" proxy for verifying signatures of incoming email. With
Postfix, the proxies can operate as either Before-Queue or After-Queue
content filters.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--libdir=%{perl_vendorlib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/ssl,/etc/rc.d/init.d,/etc/sysconfig}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS smtpprox.* TODO
%attr(755,root,root) %{_bindir}/dkim_responder.pl
%attr(755,root,root) %{_bindir}/dkimproxy.in
%attr(755,root,root) %{_bindir}/dkimproxy.out
%attr(755,root,root) %{_bindir}/dkimsign.pl
%attr(755,root,root) %{_bindir}/dkimverify.pl
%dir %{perl_vendorlib}/MSDW
%dir %{perl_vendorlib}/MSDW/SMTP
%{perl_vendorlib}/MSDW/SMTP/Client.pm
%{perl_vendorlib}/MSDW/SMTP/Server.pm
%{perl_vendorlib}/MySmtpProxyServer.pm
%{perl_vendorlib}/MySmtpServer.pm
