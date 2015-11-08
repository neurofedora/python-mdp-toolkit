%global modname mdp-toolkit
%global commit 9ce79a81161781478785ffd71f8c33cc1f897b74
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global srcname MDP

Name:           python-%{modname}
Version:        3.3
Release:        1%{?dist}
Summary:        data processing framework
License:        BSD
URL:            http://mdp-toolkit.sourceforge.net/
Source0:	https://github.com/%{modname}/%{modname}/archive/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  numpy
%description -n python2-%{modname}

Python 2 version.


%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
%description -n python3-%{modname}

Python 3 version.


%prep
%autosetup -n %{modname}-%{srcname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install


%files -n python2-%{modname}
%doc README
%license COPYRIGHT
%{python2_sitelib}/%{srcname}*
%{python2_sitelib}/bimdp/*
%{python2_sitelib}/mdp/*

%files -n python3-%{modname}
%doc README
%license COPYRIGHT
%{python3_sitelib}/%{srcname}*
%{python3_sitelib}/bimdp/*
%{python3_sitelib}/mdp/*

%changelog
* Sat Nov  7 2015 Adrian Alves <alvesadrian@fedoraporject.org> - 3.3-1
- Initial build
