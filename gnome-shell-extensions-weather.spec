Name:           gnome-shell-extensions-weather
Version:        0.0.0
Release:        0.1.9a2131396git%{?dist}
Summary:        Weather forcast GNOME Shell Extension
Group:          User Interface/Desktops
License:        GPLv2+ 
URL:            https://github.com/ecyrbe/gnome-shell-extension-weather

Source0:        %{name}-9a2131396d0682f0fa54.tar.bz2
Patch0:		%{name}-9a2131396d0682f0fa54-ru.po.patch
Patch1:		%{name}-9a2131396d0682f0fa54-moscow-city.patch

# since we build from a git checkout
BuildRequires:  gnome-common
BuildRequires:  intltool

BuildRequires:  glib2-devel
Requires:       gnome-shell
BuildArch:      noarch


%description
Simple extension for displaying weather notifications in Gnome Shell


%prep
%setup -q -n %{name}-9a2131396d0682f0fa54
%patch0 -p1 -b .ru.po
%patch1 -p1 -b .moscow-city


%build
# since we build from a git checkout
[ -x autogen.sh ] && NOCONFIGURE=1 ./autogen.sh

%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang gnome-shell-extension-weather

%posttrans
glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas || :


%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files -f gnome-shell-extension-weather.lang
%defattr(-,root,root,-)
%doc README
%{_datadir}/gnome-shell/extensions/*
%{_datadir}/glib-2.0/schemas/*


%changelog
* Fri Jun  3 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.0.0-0.1.9a2131396git
- initial build
- added Russian Translation
- Moscow is default city
