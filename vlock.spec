#
# Conditional build:
%bcond_without	caca	# don't build libcaca-based screensaver module
#
Summary:	Locks one or more virtual consoles
Summary(de.UTF-8):	Sperrt eine oder mehrere virtuelle Konsolen
Summary(es.UTF-8):	Bloquea una o más consolas virtuales
Summary(fr.UTF-8):	Verrouille une ou plusieurs consoles virtuelles
Summary(pl.UTF-8):	Umożliwia zablokowanie dostępu do terminala
Summary(pt_BR.UTF-8):	Trava uma ou mais consoles virtuais
Summary(ru.UTF-8):	Закрывает одну или больше консолей от несанкционированного доступа
Summary(tr.UTF-8):	Sanal konsol kilitleme aracı
Summary(uk.UTF-8):	Закриває одну чи більше консолей від несанкціонованого доступу
Summary(zh_CN.UTF-8):	一个能够锁定一个或多个虚拟终端的程序
Name:		vlock
Version:	2.2.3
Release:	3
License:	GPL v2
Group:		Applications/Console
# dead URL, now sources are available at: https://github.com/WorMzy/vlock
Source0:	http://cthulhu.c3d2.de/~toidinamai/vlock/archive/%{name}-%{version}.tar.bz2
# Source0-md5:	2dd5677c97f2707db62532ae24f58433
Source1:	%{name}.pamd
Patch0:		%{name}-rootpw.patch
Patch1:		%{name}-linking.patch
Patch2:		%{name}-caca.patch
URL:		http://cthulhu.c3d2.de/~toidinamai/vlock/vlock.html
BuildRequires:	pam-devel >= 0.77.3
%if %{with caca}
BuildRequires:	libcaca-devel >= 0.99
BuildRequires:	ncurses-devel
%endif
Requires:	pam >= 0.77.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vlock either locks the current terminal (which may be any kind of
terminal, local or remote), or locks the entire virtual console
system, completely disabling all console access. vlock gives up these
locks when either the password of the user who started vlock or the
root password is typed. Note: root password can unlock session only if
vlock is setuid root (it isn't by default).

%description -l de.UTF-8
vlock sperrt entweder das aktuelle Terminal (lokal oder entfernt) oder
das gesamte virtuelle Konsolensystem, wobei der Konsolenzugriff völlig
deaktiviert wird. vlock gibt die Sperren frei, wenn entweder das
Paßwort des Benutzers, der vlock gestartet hat, oder das Root- Paßwort
eingegeben wird.

%description -l es.UTF-8
vlock igualmente cierra el terminal corriente (que puede ser cualquier
tipo de terminal, local o remoto), como cierra el sistema entero de
consola virtual, inhabilitando, por completo, todo el acceso a
consola. vlock se inhabilita cuando se teclea la contraseña del
usuario que la haya iniciado o con la contraseña del root.

%description -l fr.UTF-8
vlock verrouille soit le terminal courant (qui peut être de tout type,
local ou distant), soit le système entier des consoles virtuelles,
désactivant ainsi tout accès aux consoles. vlock défait ces verrous
lorsque le mot de passe de l'utilisateur qui l'a lancé, ou celui de
root, est entré.

%description -l pl.UTF-8
vlock blokuje bieżący terminal lub całą konsolę systemu
uniemożliwiając dostęp do wszystkich wirtualnych terminali. Do
odblokowania potrzebne jest hasło użytkownika, który uruchomił vlock,
albo administratora systemu (root-a). Uwaga: odblokować terminal
hasłem roota można tylko jeśli binarka vlock ma setuid root (domyślnie
nie ma).

%description -l pt_BR.UTF-8
O vlock igualmente tranca o terminal corrente (que pode ser qualquer
tipo de terminal, local ou remoto), ou tranca o sistema inteiro de
console virtual, desabilitando completamente todo o acesso ao console.
O vlock é desabilitado quando a senha do usuário que o iniciou ou a
senha do root é digitada.

%description -l ru.UTF-8
vlock блокирует текущий терминал (который может быть любого типа, как
локальный, так и удаленный) или всю систему виртуальных консолей,
полностью блокируя таким образом любой доступ с консоли. Разблокировка
производится путем ввода пароля пользователя, запустившего vlock, или
пароля root.

%description -l tr.UTF-8
vlock kullanıcının kullanmakta olduğu terminali kilitlemesini sağlar.
Bu terminal yerel bir terminal ya da uzaktan erişilmiş bir terminal
olabilir. Diğer bir seçenek de bütün sanal konsol sistemini
kilitleyerek her türlü konsol erişimini kapatmaktır. Konsolun
kilidinin açılması için ya kilitleyen kullanıcının ya da root
kullanıcısının parolasının girilmesi gerekir.

%description -l uk.UTF-8
vlock блокує або поточний термінал (що може бути будь-якого типу, як
локальний, так і віддалений) або всю систему віртуальних консолей,
повністю блокуючи таким чином будь-який доступ з консолі.
Розблокування відбувається шляхом вводу пароля користувача, що
запустив vlock, чи пароля root.

%package caca
Summary:	libcaca-based screensaver module for vlock
Summary(pl.UTF-8):	Moduł wygaszacza ekranu opartego na libcaca dla vlocka
Group:		Applications/Console
Requires:	%{name} = %{version}-%{release}

%description caca
libcaca-based screensaver module for vlock.

%description caca -l pl.UTF-8
Moduł wygaszacza ekranu opartego na libcaca dla vlocka.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# not autoconf-generated
./configure \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -W -pedantic -std=gnu99%{?with_caca: -I/usr/include/ncurses}" \
	LDFLAGS="%{rpmldflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--with-modules="all.so new.so nosysrq.so ttyblank.so vesablank.so%{?with_caca: caca.so}" \
	--with-scripts="alsa_mute.sh amarok.sh hibernate.sh mplayer.sh \
%ifarch %{ix86} %{x8664}
	thinkpad_light.sh \
%endif
%ifarch ppc
	powerbook_backlight.sh \
%endif
	"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/pam.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog PLUGINS README README.X11 SECURITY TODO
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/%{name}
%attr(755,root,root) %{_bindir}/vlock
# should have suid root for some functions (unlocking by root password, new or nosysrq modules)
# but should be limited to trusted users
%attr(755,root,root) %verify(not mode) %{_sbindir}/vlock-main
%dir %{_libdir}/vlock
%dir %{_libdir}/vlock/modules
%attr(755,root,root) %{_libdir}/vlock/modules/all.so
%attr(755,root,root) %{_libdir}/vlock/modules/new.so
%attr(755,root,root) %{_libdir}/vlock/modules/nosysrq.so
%attr(755,root,root) %{_libdir}/vlock/modules/ttyblank.so
%attr(755,root,root) %{_libdir}/vlock/modules/vesablank.so
%dir %{_libdir}/vlock/scripts
%attr(755,root,root) %{_libdir}/vlock/scripts/*
%{_mandir}/man1/vlock.1*
%{_mandir}/man5/vlock-plugins.5*
%{_mandir}/man8/vlock-main.8*

%if %{with caca}
%files caca
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vlock/modules/caca.so
%endif
