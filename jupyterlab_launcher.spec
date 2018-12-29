#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyterlab_launcher
Version  : 0.13.1
Release  : 20
URL      : https://files.pythonhosted.org/packages/b0/30/96dd5c4caaacbc0c41754cb72547717ac8de67bb48a393b5d8b74080fbd9/jupyterlab_launcher-0.13.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b0/30/96dd5c4caaacbc0c41754cb72547717ac8de67bb48a393b5d8b74080fbd9/jupyterlab_launcher-0.13.1.tar.gz
Summary  : Jupyter Launcher
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jupyterlab_launcher-python3
Requires: jupyterlab_launcher-license
Requires: jupyterlab_launcher-python
Requires: jsonschema
Requires: notebook
Requires: requests
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
Requires: jupyterlab_launcher-python3

%description python
python components for the jupyterlab_launcher package.


%package python3
Summary: python3 components for the jupyterlab_launcher package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jupyterlab_launcher package.


%prep
%setup -q -n jupyterlab_launcher-0.13.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534617012
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/jupyterlab_launcher
cp LICENSE %{buildroot}/usr/share/doc/jupyterlab_launcher/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/jupyterlab_launcher/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
