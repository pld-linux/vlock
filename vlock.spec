Summary:     Locks one or more virtual consoles
Summary(de): Sperrt eine oder mehrere virtuelle Konsolen 
Summary(fr): Verrouille une ou plusieurs consoles virtuelles
Summary(pl): Umo¿liwia zablokowanie dostêpu do terminala
Summary(tr): Sanal konsol kilitleme aracý
Name:        vlock
Version:     1.2
Release:     2
Copyright:   GPL
Group:       Utilities/Console
Source:      ftp://tsx-11.mit.edu:/pub/linux/sources/usr.bin/%{name}-%{version}.tar.gz
Patch:       vlock-glibc-2.1.patch  
Requires:    pam >= 0.64
Buildroot:   /tmp/%{name}-%{version}-root

%description
vlock either locks the current terminal (which may be any kind of terminal,
local or remote), or locks the entire virtual console system, completely
disabling all console access.  vlock gives up these locks when either the
password of the user who started vlock or the root password is typed.

%description -l de
vlock sperrt entweder das aktuelle Terminal (lokal oder entfernt) oder das
gesamte virtuelle Konsolensystem, wobei der Konsolenzugriff völlig
deaktiviert wird. vlock gibt die Sperren frei, wenn entweder das Paßwort des
Benutzers, der vlock gestartet hat, oder das Root- Paßwort eingegeben wird.

%description -l fr
vlock verrouille soit le terminal courant (qui peut être de tout type, local
ou distant), soit le système entier des consoles virtuelles, désactivant
ainsi tout accès aux consoles. vlock défait ces verrous lorsque le mot de
passe de l'utilisateur qui l'a lancé, ou celui de root, est entré.

%description -l pl
Vlock blokuje bie¿±cy terminal lub ca³± konsolê systemu uniemo¿liwiaj±c
dostêp do wszystkich wirtualnych terminali. Do odblokowania potrzebne jest
has³o u¿ytkownika, który uruchomi³ vlock, albo administratora systemu
(root-a).

%description -l tr
vlock kullanýcýnýn kullanmakta olduðu terminali kilitlemesini saðlar. Bu
terminal yerel bir terminal ya da uzaktan eriþilmiþ bir terminal olabilir.
Diðer bir seçenek de bütün sanal konsol sistemini kilitleyerek her türlü
konsol eriþimini kapatmaktýr. Konsolun kilidinin açýlmasý için ya
kilitleyen kullanýcýnýn ya da root kullanýcýsýnýn parolasýnýn girilmesi
gerekir.

%prep
%setup -q
%patch -p1

%build
OPTFLAGS="$RPM_OPT_FLAGS" make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/pam.d,usr/{bin,man/man1}}

install -s vlock $RPM_BUILD_ROOT/usr/bin
install vlock.1 $RPM_BUILD_ROOT/usr/man/man1
install vlock.pamd $RPM_BUILD_ROOT/etc/pam.d/vlock

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root)
%doc README
%attr(600, root, root) %config /etc/pam.d/vlock
%attr(755, root, root) /usr/bin/vlock
%attr(644, root,  man) /usr/man/man1/*

%changelog
* Fri Sep 18 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [1.2-2]
- added pl translation.

* Mon May 04 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Mar 12 1998 Michael K. Johnson <johnsonm@redhat.com>
- Does not create a DoS attack if pty is closed (not applicable
  to use on a VC)

* Fri Oct 10 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved to new pam conventions.
- Use pam according to spec, rather than abusing it as before.
- Updated to version 1.1.
- BuildRoot

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- moved from pam.conf to pam.d
