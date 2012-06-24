Summary:	locks one or more virtual consoles
Summary(de):	sperrt eine oder mehrere virtuelle Konsolen
Summary(es):	Bloquea una o m�s consolas virtuales
Summary(fr):	verrouille une ou plusieurs consoles virtuelles
Summary(pl):	Umo�liwia zablokowanie dost�pu do terminala
Summary(pt_BR):	Trava uma ou mais consoles virtuais
Summary(ru):	��������� ���� ��� ������ �������� �� �������������������� �������
Summary(tr):	Sanal konsol kilitleme arac�
Summary(uk):	�������� ���� �� ¦���� �������� צ� ������æ��������� �������
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
das gesamte virtuelle Konsolensystem, wobei der Konsolenzugriff v�llig
deaktiviert wird. vlock gibt die Sperren frei, wenn entweder das
Pa�wort des Benutzers, der vlock gestartet hat, oder das Root- Pa�wort
eingegeben wird.

%description -l es
vlock igualmente cierra el terminal corriente (que puede ser cualquier
tipo de terminal, local o remoto), como cierra el sistema entero de
consola virtual, inhabilitando, por completo, todo el acceso a
consola. vlock se inhabilita cuando se teclea la contrase�a del
usuario que la haya iniciado o con la contrase�a del root.

%description -l fr
vlock verrouille soit le terminal courant (qui peut �tre de tout type,
local ou distant), soit le syst�me entier des consoles virtuelles,
d�sactivant ainsi tout acc�s aux consoles. vlock d�fait ces verrous
lorsque le mot de passe de l'utilisateur qui l'a lanc�, ou celui de
root, est entr�.

%description -l pl
Vlock blokuje bie��cy terminal lub ca�� konsol� systemu
uniemo�liwiaj�c dost�p do wszystkich wirtualnych terminali. Do
odblokowania potrzebne jest has�o u�ytkownika, kt�ry uruchomi� vlock,
albo administratora systemu (root-a).

%description -l pt_BR
O vlock igualmente tranca o terminal corrente (que pode ser qualquer
tipo de terminal, local ou remoto), ou tranca o sistema inteiro de
console virtual, desabilitando completamente todo o acesso ao console.
O vlock � desabilitado quando a senha do usu�rio que o iniciou ou a
senha do root � digitada.

%description -l ru
vlock ��������� ������� �������� (������� ����� ���� ������ ����, ���
���������, ��� � ���������) ��� ��� ������� ����������� ��������,
��������� �������� ����� ������� ����� ������ � �������. �������������
������������ ����� ����� ������ ������������, ������������ vlock, ���
������ root.

%description -l tr
vlock kullan�c�n�n kullanmakta oldu�u terminali kilitlemesini sa�lar.
Bu terminal yerel bir terminal ya da uzaktan eri�ilmi� bir terminal
olabilir. Di�er bir se�enek de b�t�n sanal konsol sistemini
kilitleyerek her t�rl� konsol eri�imini kapatmakt�r. Konsolun
kilidinin a��lmas� i�in ya kilitleyen kullan�c�n�n ya da root
kullan�c�s�n�n parolas�n�n girilmesi gerekir.

%description -l uk
vlock ����դ ��� �������� ���ͦ��� (�� ���� ���� ����-����� ����, ��
���������, ��� � צ��������) ��� ��� ������� צ��������� ��������,
���Φ��� �������� ����� ����� ����-���� ������ � �����̦.
������������� צ���������� ������ ����� ������ �����������, ��
�������� vlock, �� ������ root.

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
