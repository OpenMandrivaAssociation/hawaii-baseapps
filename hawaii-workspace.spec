Summary:	Base applications for the Hawaii desktop
Name:		hawaii-workspace
Version:	0.5.0
Release:	1
Group:		Graphical desktop/Other
License:	BSD and LGPLv2+ and GPLv3+
URL:		http://www.hawaiios.org
Source0:	https://github.com/hawaii-desktop/hawaii-workspace/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(libsystemd-daemon)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(PolkitQt5-1)
BuildRequires:	cmake(GreenIsland)

%track
prog %{name} = {
    url = https://github.com/hawaii-desktop/hawaii-workspace/releases/download/v%{version}/
    regex = "v(__VER__)\.tar\.xz"
    version = %{version}
}

%description
Base applications for the Hawaii desktop environment.

%prep
%setup -q

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%{_sysconfdir}/xdg/autostart/*.desktop
%{_bindir}/hawaii-*
%{_datadir}/applications/*.desktop
