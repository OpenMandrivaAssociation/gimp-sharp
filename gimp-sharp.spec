%define name gimp-sharp
%define version 0.15
%define release %mkrel 1
%define gimpver 2.0
%define gimpapi 2.0
%define gimpmajor 0

Summary: Gimp# allows writing Gimp plugin with Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/gimp-sharp/%{name}-%{version}.tar.gz
Patch: gimp-sharp-0.13-paths.patch
Patch1: gimp-sharp-0.14-dllconfig.patch
License: GPL
Group: Graphics
Url: http://gimp-sharp.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgimp-devel >= %gimpver
BuildRequires: automake1.7
BuildRequires: gtk-sharp2
BuildRequires: mono-devel
BuildRequires: mono-basic
BuildRequires: boo
BuildRequires: ikvm > 0.36.0.5
BuildRequires: ironpython
BuildRequires: umfpack-devel blas-devel

%description
This are the C# bindings for GIMP 2.0 that allow the implementation of
plugins with mono.

%prep
%setup -q
%patch -p1 -b .paths
%patch1 -p1 -b .dllconfig
perl -pi -e "s!LIBDIR!%_libdir!" plug-ins/PythonSample/PythonSample

%build
%configure2_5x --with-unittest --with-vb --with-boo --with-java
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


