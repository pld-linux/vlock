Summary:     Locks one or more virtual consoles
Summary(de): Sperrt eine oder mehrere virtuelle Konsolen 
Summary(fr): Verrouille une ou plusieurs consoles virtuelles
Summary(pl): Umo�liwia zablokowanie dost�pu do terminala
Summary(tr): Sanal konsol kilitleme arac�
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
gesamte virtuelle Konsolensystem, wobei der Konsolenzugriff v�llig
deaktiviert wird. vlock gibt die Sperren frei, wenn entweder das Pa�wort des
Benutzers, der vlock gestartet hat, oder das Root- Pa�wort eingegeben wird.

%description -l fr
vlock verrouille soit le terminal courant (qui peut �tre de tout type, local
ou distant), soit le syst�me entier des consoles virtuelles, d�sactivant
ainsi tout acc�s aux consoles. vlock d�fait ces verrous lorsque le mot de
passe de l'utilisateur qui l'a lanc�, ou celui de root, est entr�.

%description -l pl
Vlock blokuje bie��cy terminal lub ca�� konsol� systemu uniemo�liwiaj�c
dost�p do wszystkich wirtualnych terminali. Do odblokowania potrzebne jest
has�o u�ytkownika, kt�ry uruchomi� vlock, albo administratora systemu
(root-a).

%description -l tr
vlock kullan�c�n�n kullanmakta oldu�u terminali kilitlemesini sa�lar. Bu
terminal yerel bir terminal ya da uzaktan eri�ilmi� bir terminal olabilir.
Di�er bir se�enek de b�t�n sanal konsol sistemini kilitleyerek her t�rl�
konsol eri�imini kapatmakt�r. Konsolun kilidinin a��lmas� i�in ya
kilitleyen kullan�c�n�n ya da root kullan�c�s�n�n parolas�n�n girilmesi
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
