Summary:	Picard, the Next-Generation MusicBrainz Tagger
Summary(pl.UTF-8):	Picard - znaczniki MusicBrainz nowej generacji
Name:		picard
Version:	1.3.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.musicbrainz.org/pub/musicbrainz/picard/%{name}-%{version}.tar.gz
# Source0-md5:	0df8899ba834b2c9ac59165122256257
Patch0:		%{name}-desktop.patch
URL:		http://musicbrainz.org/doc/PicardTagger
BuildRequires:	gettext-tools
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	python-PyQt4
Requires:	python-musicbrainz2
Requires:	python-mutagen
Requires:	python-tunepimp
Requires:	python-wxPython
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
językiem cross-platform - co pozwala uruchamiać ten sam kod zarówno
pod Windows jak i Linuksem. Niedługo zostanie dodana obsługa Mac OS X.

%prep
%setup -q -n %{name}-release-%{version}
%patch0 -p1

find -type f | xargs sed -i -e '1 s|#!.*python|#!%{__python}|g'

%{__rm} po/sco.po

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%py_install
%py_postclean

# install plugins
cp -a contrib/plugins/* $RPM_BUILD_ROOT%{py_sitedir}/%{name}/plugins

%find_lang %{name}
%find_lang %{name}-countries -a %{name}.lang
%find_lang %{name}-attributes -a %{name}.lang

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md AUTHORS.txt NEWS.txt
%attr(755,root,root) %{_bindir}/%{name}
%dir %{py_sitedir}/%{name}
%{py_sitedir}/%{name}/*.py*
%{py_sitedir}/%{name}/browser
%{py_sitedir}/%{name}/const
%{py_sitedir}/%{name}/coverart
%{py_sitedir}/%{name}/formats
%{py_sitedir}/%{name}/plugins
%{py_sitedir}/%{name}/ui
%dir %{py_sitedir}/%{name}/util
%{py_sitedir}/%{name}/util/*.py*
%{py_sitedir}/%{name}/util/devutil
%attr(755,root,root) %{py_sitedir}/%{name}/util/astrcmp.so
%{py_sitedir}/%{name}-%{version}-py*.egg-info
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/picard.png
