
# TODO:
#	- use system-wide lua

%define		snap	070804
Summary:	Blobby Volley 2 game
Summary(pl.UTF-8):	Gra Blobby Volley 2
Name:		blobby2
Version:	0.61
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	fffe00422e14879fe73db491ae782649
Patch0:		%{name}-gcc4.patch
URL:		http://blobby.redio.de/content/en/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	physfs-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blobby Volley 2 game.

%description -l pl.UTF-8
Gra Blobby Volley 2.

%prep
%setup -q -n %{name}-%{snap}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
sed -i -e "s:HAVE_LIBGL = @HAVE_LIBGL@:HAVE_LIBGL = 0:" src/Makefile.in
sed -i -e "s:-lSDL:-lSDL -lGL:" configure
%configure \
	%{?debug:--enable-debug}
%{__make} \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc AUTHORS ChangeLog NEWS README TODO doc/*.txt
%{_datadir}/blobby
