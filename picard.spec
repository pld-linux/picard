Summary:	Picard, the Next-Generation MusicBrainz Tagger
Summary(pl.UTF-8):	Picard - znaczniki MusicBrainz nowej generacji
Name:		picard
Version:	1.3.1
Release:	0.1
License:	GPL v2+
Group:		Applications
Source0:	ftp://ftp.musicbrainz.org/pub/musicbrainz/picard/%{name}-%{version}.tar.gz
# Source0-md5:	2c155a0c4a5589c18bac3016365d7fbd
Patch0:		%{name}-desktop.patch
URL:		http://musicbrainz.org/doc/PicardTagger
BuildRequires:	gettext-tools
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
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

find -type f | xargs sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g'

%build
%{__python} setup.py config
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%find_lang %{name}

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.txt NEWS.txt
%attr(755,root,root) %{_bindir}/%{name}
%{py_sitedir}/picard
%{py_sitedir}/%{name}-%{version}-py*.egg-info
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/picard.png
