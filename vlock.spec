Summary:	locks one or more virtual consoles
Summary(de):	sperrt eine oder mehrere virtuelle Konsolen
Summary(es):	Bloquea una o mАs consolas virtuales
Summary(fr):	verrouille une ou plusieurs consoles virtuelles
Summary(pl):	Umo©liwia zablokowanie dostЙpu do terminala
Summary(pt_BR):	Trava uma ou mais consoles virtuais
Summary(ru):	Закрывает одну или больше консолей от несанкционированного доступа
Summary(tr):	Sanal konsol kilitleme aracЩ
Summary(uk):	Закрива╓ одну чи б╕льше консолей в╕д несанкц╕онованого доступу
Name:		vlock
Version:	1.3
Release:	10
License:	GPL
Group:		Applications/Console
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
das gesamte virtuelle Konsolensystem, wobei der Konsolenzugriff vЖllig
deaktiviert wird. vlock gibt die Sperren frei, wenn entweder das
Paъwort des Benutzers, der vlock gestartet hat, oder das Root- Paъwort
eingegeben wird.

%description -l es
vlock igualmente cierra el terminal corriente (que puede ser cualquier
tipo de terminal, local o remoto), como cierra el sistema entero de
consola virtual, inhabilitando, por completo, todo el acceso a
consola. vlock se inhabilita cuando se teclea la contraseЯa del
usuario que la haya iniciado o con la contraseЯa del root.

%description -l fr
vlock verrouille soit le terminal courant (qui peut Йtre de tout type,
local ou distant), soit le systХme entier des consoles virtuelles,
dИsactivant ainsi tout accХs aux consoles. vlock dИfait ces verrous
lorsque le mot de passe de l'utilisateur qui l'a lancИ, ou celui de
root, est entrИ.

%description -l pl
Vlock blokuje bie©╠cy terminal lub caЁ╠ konsolЙ systemu
uniemo©liwiaj╠c dostЙp do wszystkich wirtualnych terminali. Do
odblokowania potrzebne jest hasЁo u©ytkownika, ktСry uruchomiЁ vlock,
albo administratora systemu (root-a).

%description -l pt_BR
O vlock igualmente tranca o terminal corrente (que pode ser qualquer
tipo de terminal, local ou remoto), ou tranca o sistema inteiro de
console virtual, desabilitando completamente todo o acesso ao console.
O vlock И desabilitado quando a senha do usuАrio que o iniciou ou a
senha do root И digitada.

%description -l ru
vlock блокирует текущий терминал (который может быть любого типа, как
локальный, так и удаленный) или всю систему виртуальных консолей,
полностью блокируя таким образом любой доступ с консоли. Разблокировка
производится путем ввода пароля пользователя, запустившего vlock, или
пароля root.

%description -l tr
vlock kullanЩcЩnЩn kullanmakta olduПu terminali kilitlemesini saПlar.
Bu terminal yerel bir terminal ya da uzaktan eriЧilmiЧ bir terminal
olabilir. DiПer bir seГenek de bЭtЭn sanal konsol sistemini
kilitleyerek her tЭrlЭ konsol eriЧimini kapatmaktЩr. Konsolun
kilidinin aГЩlmasЩ iГin ya kilitleyen kullanЩcЩnЩn ya da root
kullanЩcЩsЩnЩn parolasЩnЩn girilmesi gerekir.

%description -l uk
vlock блоку╓ або поточний терм╕нал (що може бути будь-якого типу, як
локальний, так ╕ в╕ддалений) або всю систему в╕ртуальних консолей,
повн╕стю блокуючи таким чином будь-який доступ з консол╕.
Розблокування в╕дбува╓ться шляхом вводу пароля користувача, що
запустив vlock, чи пароля root.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags} -DUSE_PAM"

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
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/%{name}

%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
