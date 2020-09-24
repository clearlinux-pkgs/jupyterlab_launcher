#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyterlab_launcher
Version  : 0.13.1
Release  : 28
URL      : https://files.pythonhosted.org/packages/b0/30/96dd5c4caaacbc0c41754cb72547717ac8de67bb48a393b5d8b74080fbd9/jupyterlab_launcher-0.13.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b0/30/96dd5c4caaacbc0c41754cb72547717ac8de67bb48a393b5d8b74080fbd9/jupyterlab_launcher-0.13.1.tar.gz
Summary  : Jupyter Launcher
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jupyterlab_launcher-license = %{version}-%{release}
Requires: jupyterlab_launcher-python = %{version}-%{release}
Requires: jupyterlab_launcher-python3 = %{version}-%{release}
Requires: jsonschema
Requires: notebook
BuildRequires : buildreq-distutils3
BuildRequires : jsonschema
BuildRequires : notebook

%description
This package is used to launch an application built using JupyterLab

%package license
Summary: license components for the jupyterlab_launcher package.
Group: Default

%description license
license components for the jupyterlab_launcher package.


%package python
Summary: python components for the jupyterlab_launcher package.
Group: Default
Requires: jupyterlab_launcher-python3 = %{version}-%{release}

%description python
python components for the jupyterlab_launcher package.


%package python3
Summary: python3 components for the jupyterlab_launcher package.
Group: Default
Requires: python3-core
Provides: pypi(jupyterlab_launcher)
Requires: pypi(jsonschema)
Requires: pypi(notebook)

%description python3
python3 components for the jupyterlab_launcher package.


%prep
%setup -q -n jupyterlab_launcher-0.13.1
cd %{_builddir}/jupyterlab_launcher-0.13.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583536715
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyterlab_launcher
cp %{_builddir}/jupyterlab_launcher-0.13.1/LICENSE %{buildroot}/usr/share/package-licenses/jupyterlab_launcher/8cd4cef90d28bff5235d6343a8158b70a0668dc4
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jupyterlab_launcher/8cd4cef90d28bff5235d6343a8158b70a0668dc4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
