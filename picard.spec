Summary:	Picard, the Next-Generation MusicBrainz Tagger
Summary(pl.UTF-8):	Picard - znaczniki MusicBrainz nowej generacji
Name:		picard
Version:	2.8.5
Release:	2
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://ftp.musicbrainz.org/pub/musicbrainz/picard/%{name}-%{version}.tar.gz
# Source0-md5:	7bea5a3963d27ed4d069ab7dd3ac3485
Patch0:		%{name}-desktop.patch
URL:		https://picard.musicbrainz.org/
BuildRequires:	gettext-tools
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	python3-PyQt5-uic
BuildRequires:	python3-babel >= 2.9.1
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-setuptools
# PyInstaller >= 4.10?
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	python3-libdiscid
Requires:	python3-modules >= 1:3.6
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

%{__sed} -i -e '1 s|/usr/bin/env python3|%{__python3}|g' \
	tagger.py.in scripts/picard.in

# unify
%{__mv} po/attributes/{pt_PT,pt}.po
# unsupported by glibc (as of 2.29)
%{__rm} po/sco.po

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{es_419,ms_MY,zh-Hans,zh}

%find_lang %{name} --all-name

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
%doc AUTHORS.txt NEWS.md README.md
%attr(755,root,root) %{_bindir}/picard
%dir %{py3_sitedir}/%{name}
%{py3_sitedir}/%{name}/*.py
%{py3_sitedir}/%{name}/__pycache__
%{py3_sitedir}/%{name}/acoustid
%{py3_sitedir}/%{name}/browser
%{py3_sitedir}/%{name}/const
%{py3_sitedir}/%{name}/coverart
%{py3_sitedir}/%{name}/disc
%{py3_sitedir}/%{name}/formats
%{py3_sitedir}/%{name}/plugins
%{py3_sitedir}/%{name}/script
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
