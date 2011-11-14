Name:           gnome-shell-extension-weather
Version:        0.0.0
Release:        0.3.14203f05git%{?dist}.R
Summary:        Weather forecast GNOME Shell Extension
Group:          User Interface/Desktops
License:        GPLv2+ 
URL:            https://github.com/simon04/gnome-shell-extension-weather

Source0:        %{name}-14203f055a84d08ac32.tar.bz2

# since we build from a git checkout
BuildRequires:  gnome-common
BuildRequires:  intltool

BuildRequires:  glib2-devel
Requires:       gnome-shell
BuildArch:      noarch


%description
Simple extension for displaying weather notifications in Gnome Shell


%prep
%setup -q -n %{name}-14203f055a84d08ac32


%build
# since we build from a git checkout
[ -x autogen.sh ] && NOCONFIGURE=1 ./autogen.sh

%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -dD $RPM_BUILD_ROOT%{_datadir}/applications
sed -i 's!weather-extension-configurator.py!weather-extension-configurator!g' weather-extension-configurator.desktop
install -m644 weather-extension-configurator.desktop $RPM_BUILD_ROOT%{_datadir}/applications

install -dD $RPM_BUILD_ROOT%{_bindir}
install -m755 weather-extension-configurator.py $RPM_BUILD_ROOT%{_bindir}/weather-extension-configurator

%find_lang gnome-shell-extension-weather

%posttrans
glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas &> /dev/null || :


%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files -f gnome-shell-extension-weather.lang
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/weather-extension-configurator
%{_datadir}/gnome-shell/extensions/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/*.desktop


%changelog
* Mon Nov 14 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.0.0-0.3.14203f05git.R
- new upstream release

* Mon Jun 27 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.0.0-0.2.d96e20869git.R
- new upstream release
- drop patches

* Fri Jun  3 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.0.0-0.1.9a2131396git
- initial build
- added Russian Translation
- Moscow is default city
