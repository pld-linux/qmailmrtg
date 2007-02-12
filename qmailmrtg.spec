Summary:	qmailmrtg - qmail statistics as mrtg graphs
Summary(pl.UTF-8):   qmailmrts - statystyki qmaila w postaci wykresów mrtg
Name:		qmailmrtg
Version:	4.2
Release:	0.4
Epoch:		0
License:	GPL v2
Group:		Applications/Mail
Source0:	http://www.inter7.com/qmailmrtg7/%{name}7-%{version}.tar.gz
# Source0-md5:	b723ae00ecdffe87cf259e39a9fe6eb9
URL:		http://www.inter7.com/index.php?page=qmailmrtg7
# Doesn't require any of these directly:
#Requires:	daemontools
#Requires:	mrtg
#Requires:	qmail
#Requires:	ucspi-tcp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qmailmrtg7 uses qmail's excellent and extensive logging via multilog,
tcpserver and qmail-send. qmailmrtg7 takes the pop3, smtp and qmail
transaction logs and sends them to 9 different mrtg graphs, each graph
with 4 historical time series.

Features:
- very fast - typically processes in less than 2 seconds
- Intelligently uses the multilog file name time stamp to determine
  which logs to open and process.
- Single small C program with no external dependances and simple
  command line options. See the qmail.mrtg.cfg for working examples of
  the options.
- Works on any system that supports qmail

%description -l pl.UTF-8
qmailmrtg7 używa dobrego i rozszerzalnego systemu logowania poprzez
multilog, tcpserver i qmail-send. qmailmrtg7 pobiera logi transakcji
pop3, smtp i qmaila, a następnie rozsyła je na 9 różnych wykresów
mrtg, każdy z 4 okresami czasu.

Możliwości:
- bardzo szybki - zwykle przetwarza dane poniżej 2 sekund
- inteligentnie używa znaczników czasu pliku multilog w celu
  określenia, które logi otworzyć i przetworzyć
- jest to prosty, mały program w C bez zewnętrznych zależności i z
  prostymi opcjami linii poleceń; działające przykłady opcji można
  znaleźć w pliku qmail.mrtg.cfg
- działa na każdym systemie, na którym działa qmail

%prep
%setup -q -n %{name}7-%{version}

%build
# NOTE: This depends on how qmail is compiled. If you change these in qmail.spec
# You should update here too (just run 'make' as root to and copy qmailmrtg7.h contents).
cat <<EOF> qmailmrtg7.h
int BigTodo=0;
int ConfSplit=23;
EOF

%{__cc} %{rpmcflags} qmailmrtg7.c -o qmailmrtg7

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sbindir}
install qmailmrtg7 $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ INSTALL Info TODO
%doc index.html
%doc qmail.mrtg.cfg
%attr(755,root,root) %{_sbindir}/qmailmrtg7
