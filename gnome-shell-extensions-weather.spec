Name:           gnome-shell-extensions-weather
Version:        0.0.0
Release:        0.2.d96e20869git%{?dist}.R
Summary:        Weather forcast GNOME Shell Extension
Group:          User Interface/Desktops
License:        GPLv2+ 
URL:            https://github.com/ecyrbe/gnome-shell-extension-weather

Source0:        %{name}-d96e2086948a7737929e.tar.bz2

# since we build from a git checkout
BuildRequires:  gnome-common
BuildRequires:  intltool

BuildRequires:  glib2-devel
Requires:       gnome-shell
BuildArch:      noarch


%description
Simple extension for displaying weather notifications in Gnome Shell


%prep
%setup -q -n %{name}-d96e2086948a7737929e


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
%doc README.md
%{_datadir}/gnome-shell/extensions/*
%{_datadir}/glib-2.0/schemas/*


%changelog
* Mon Jun 27 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.0.0-0.2.d96e20869git.R
- new upstream release
- drop patches

* Fri Jun  3 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.0.0-0.1.9a2131396git
- initial build
- added Russian Translation
- Moscow is default city
