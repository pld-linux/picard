Summary:	Picard, the Next-Generation MusicBrainz Tagger
Summary(pl.UTF-8):	Picard - znaczniki MusicBrainz nowej generacji
Name:		picard
Version:	2.1.3
Release:	7
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.musicbrainz.org/pub/musicbrainz/picard/%{name}-%{version}.tar.gz
# Source0-md5:	272b5ce221594eb1271d48d1c997499a
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-PyQt5-no-egg.patch
URL:		https://picard.musicbrainz.org/
BuildRequires:	gettext-tools
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	python3-PyQt5-uic
BuildRequires:	python3-babel >= 2.6
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	python3-PyQt5 >= 5.7.1
Requires:	python3-libdiscid
Requires:	python3-modules >= 1:3.5
Requires:	python3-mutagen >= 1.37
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
%patch1 -p1

sed -i -e '1 s|/usr/bin/env python3|%{__python3}|g' \
	tagger.py scripts/picard.in

# unify
%{__mv} po/attributes/{pt_PT,pt}.po
# unsupported by glibc (as of 2.29)
%{__rm} po/sco.po

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%find_lang %{name}
%find_lang %{name}-countries -a %{name}.lang
%find_lang %{name}-attributes -a %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md AUTHORS.txt NEWS.txt
%attr(755,root,root) %{_bindir}/picard
%dir %{py3_sitedir}/%{name}
%{py3_sitedir}/%{name}/*.py
%{py3_sitedir}/%{name}/__pycache__
%{py3_sitedir}/%{name}/acoustid
%{py3_sitedir}/%{name}/browser
%{py3_sitedir}/%{name}/const
%{py3_sitedir}/%{name}/coverart
%{py3_sitedir}/%{name}/formats
%{py3_sitedir}/%{name}/plugins
%{py3_sitedir}/%{name}/ui
%dir %{py3_sitedir}/%{name}/util
%{py3_sitedir}/%{name}/util/*.py
%attr(755,root,root) %{py3_sitedir}/%{name}/util/_astrcmp.cpython-*.so
%{py3_sitedir}/%{name}/util/__pycache__
%{py3_sitedir}/%{name}/webservice
%{py3_sitedir}/%{name}-%{version}-py*.egg-info
%{_datadir}/metainfo/org.musicbrainz.Picard.appdata.xml
%{_desktopdir}/org.musicbrainz.Picard.desktop
%{_iconsdir}/hicolor/*x*/apps/org.musicbrainz.Picard.png
%{_iconsdir}/hicolor/scalable/apps/org.musicbrainz.Picard.svg
