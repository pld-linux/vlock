Summary:	locks one or more virtual consoles
Summary(de):	sperrt eine oder mehrere virtuelle Konsolen 
Summary(fr):	verrouille une ou plusieurs consoles virtuelles
Summary(pl):	Umo¿liwia zablokowanie dostêpu do terminala
Summary(tr):	Sanal konsol kilitleme aracý
Name:		vlock
Version:	1.3
Release:	8
License:	GPL
Group:		Applications/Console
Group(de):	Applikationen/Konsole
Group(pl):	Aplikacje/Konsola
Source0:	ftp://tsx-11.mit.edu:/pub/linux/sources/usr.bin/%{name}-%{version}.tar.gz
Source1:	%{name}.pamd
BuildRequires:	pam-devel >= 0.65
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vlock either locks the current terminal (which may be any kind of
terminal, local or remote), or locks the entire virtual console
system, completely disabling all console access. vlock gives up these
locks when either the password of the user who started vlock or the
root password is typed.

%description -l de
vlock sperrt entweder das aktuelle Terminal (lokal oder entfernt) oder
das gesamte virtuelle Konsolensystem, wobei der Konsolenzugriff völlig
deaktiviert wird. vlock gibt die Sperren frei, wenn entweder das
Paßwort des Benutzers, der vlock gestartet hat, oder das Root- Paßwort
eingegeben wird.

%description -l fr
vlock verrouille soit le terminal courant (qui peut être de tout type,
local ou distant), soit le système entier des consoles virtuelles,
désactivant ainsi tout accès aux consoles. vlock défait ces verrous
lorsque le mot de passe de l'utilisateur qui l'a lancé, ou celui de
root, est entré.

%description -l pl
Vlock blokuje bie¿±cy terminal lub ca³± konsolê systemu
uniemo¿liwiaj±c dostêp do wszystkich wirtualnych terminali. Do
odblokowania potrzebne jest has³o u¿ytkownika, który uruchomi³ vlock,
albo administratora systemu (root-a).

%description -l tr
vlock kullanýcýnýn kullanmakta olduðu terminali kilitlemesini saðlar.
Bu terminal yerel bir terminal ya da uzaktan eriþilmiþ bir terminal
olabilir. Diðer bir seçenek de bütün sanal konsol sistemini
kilitleyerek her türlü konsol eriþimini kapatmaktýr. Konsolun
kilidinin açýlmasý için ya kilitleyen kullanýcýnýn ya da root
kullanýcýsýnýn parolasýnýn girilmesi gerekir.

%prep
%setup -q

%build
%{__make} CFLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS} -DUSE_PAM"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,/etc/pam.d}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/%{name}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(644,root,root) %config %verify(not size mtime md5) /etc/pam.d/%{name}

%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
