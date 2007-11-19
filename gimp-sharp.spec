%define name gimp-sharp
%define version 0.13
%define release %mkrel 2
%define gimpver 2.0
%define gimpapi 2.0
%define gimpmajor 0

Summary: Gimp# allows writing Gimp plugin with Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/gimp-sharp/%{name}-%{version}.tar.gz
Patch1: gimp-sharp-0.13-dllconfig.patch
License: GPL
Group: Graphics
Url: http://gimp-sharp.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgimp-devel >= %gimpver
BuildRequires: automake1.7
BuildRequires: gtk-sharp2
BuildRequires: mono-devel
#BuildRequires: ikvm
BuildRequires: ironpython
BuildRequires: libumfpack-devel blas-devel

%description
This are the C# bindings for GIMP 2.0 that allow the implementation of
plugins with mono.

%prep
%setup -q
%patch1 -p1 -b .dllconfig
aclocal-1.7
autoconf
automake-1.7

%build
%configure2_5x --with-unittest --with-ironpython
# --with-java 
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


