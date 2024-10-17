%define name gimp-sharp
%define version 0.17
%define release %mkrel 4
%define gimpver 2.0
%define gimpapi 2.0
%define gimpmajor 0

Summary: Gimp# allows writing Gimp plugin with Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/gimp-sharp/%{name}-%{version}.tar.gz
Patch0: gimp-sharp-0.13-paths.patch
Patch1: gimp-sharp-0.15-dllconfig.patch
Patch2: gimp-sharp-0.16-plugindir.patch
Patch3: gimp-sharp-0.16-ikvmstubpath.patch
License: LGPLv2+
Group: Graphics
Url: https://gimp-sharp.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgimp-devel >= %gimpver
BuildRequires: automake
BuildRequires: gtk-sharp2
BuildRequires: mono-devel >= 2.8
BuildRequires: ikvm > 0.36.0.5
BuildRequires: ironpython
#BuildRequires: nemerle
BuildRequires: umfpack-devel blas-devel

%description
This are the C# bindings for GIMP 2.0 that allow the implementation of
plugins with mono.

%prep
%setup -q
%autopatch -p1

perl -pi -e "s!LIBDIR!%_libdir!" plug-ins/PythonSample/PythonSample
autoreconf -fi

%build
export CPPFLAGS=-I%_includedir/suitesparse
%configure2_5x --with-java --with-ironpython
#--with-nemerle --with-unittest
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_libdir/gimp/%gimpapi/plug-ins/ %buildroot%_datadir/locale/{it,ru}/LC_MESSAGES/
%makeinstall_std GIMPLOCALE=%buildroot%_datadir/locale
install -m 644 plug-ins/Colorize/Colorize.exe.config %buildroot%_libdir/gimp/%gimpapi/plug-ins/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS NEWS TODO README
%lang(it) %_datadir/locale/it/LC_MESSAGES/*.mo
%lang(ru) %_datadir/locale/ru/LC_MESSAGES/*.mo
%{_libdir}/gimp/%gimpapi/plug-ins/*
