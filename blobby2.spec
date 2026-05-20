Summary:	Blobby Volley 2 game
Summary(pl.UTF-8):	Gra Blobby Volley 2
Name:		blobby2
Version:	1.1.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	https://github.com/danielknobe/blobbyvolley2/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2c95af30dc3a40d2505b6367299849e7
URL:		https://blobbyvolley.de/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL2-devel
BuildRequires:	boost-devel
BuildRequires:	cmake >= 3.7
BuildRequires:	physfs-devel
BuildRequires:	rpmbuild(macros) >= 1.605
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blobby Volley 2 game.

%description -l pl.UTF-8
Gra Blobby Volley 2.

%package server
Summary:	Blobby Volley 2 dedicated server
Summary(pl.UTF-8):	Dedykowany serwer gry Blobby Volley 2
Group:		Applications/Games

%description server
Dedicated server for Blobby Volley 2.

%description server -l pl.UTF-8
Dedykowany serwer gry Blobby Volley 2.

%prep
%setup -q -n blobbyvolley2-%{version}

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -C build \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md doc/*.txt
%attr(755,root,root) %{_bindir}/blobby
%{_datadir}/blobby
%{_desktopdir}/blobby.desktop
%{_iconsdir}/hicolor/128x128/apps/blobby.png
%{_datadir}/metainfo/blobby.appdata.xml

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/blobby-server
