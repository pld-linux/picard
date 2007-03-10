Summary:	Picard, the Next-Generation MusicBrainz Tagger
Summary(pl.UTF-8):	Picard, znacznik MusicBrainz nowej generacji
Name:		picard
Version:	0.7.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://helixcommunity.org/frs/download.php/2252/%{name}-%{version}.tar.gz
# Source0-md5:	840d2202a792a36fc981fd691c8c49a5
Patch0:		%{name}-desktop.patch
URL:		http://musicbrainz.org/doc/PicardTagger
BuildRequires:	python-ctypes
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-musicbrainz2
Requires:	python-tunepimp
Requires:	python-wxPython
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The project code-named Picard is the next generation MusicBrainz
tagging application. This new tagging concept is Release oriented, as
opposed to track oriented like the ClassicTagger was. Picard is
written in Python, which is a cross-platform language - this allows
the same code to run both on Windows and on Linux. Before too long we
will add Mac OS X support as well.

%description -l pl.UTF-8
Projekt o nazwie Picard jest programem nowej generacji do generowania
znaczników MusicBranz. Picard jest napisany w Pythonie, który jest
językiem cross-platform - co pozwala uruchamiac ten sam kod na obu
systemach Windows oraz Linux. Niedługo dodamy wsparcie dla Mac OS X.

%prep
%setup -q
%patch0 -p0

%build
find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

python ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_pixmapsdir}
mv $RPM_BUILD_ROOT/%{_iconsdir}/* $RPM_BUILD_ROOT/%{_pixmapsdir}
%py_postclean
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{py_sitescriptdir}/picard
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*
