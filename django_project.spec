%if 0%{?rhel} > 7 || 0%{?fedora}
%global use_python3 1
%global use_python2 0
%global ourpythonbin %{__python3}
%global our_sitelib %{python3_sitelib}
%else
%global use_python3 0
%global use_python2 1
%if 0%{?__python2:1}
%global ourpythonbin %{__python2}
%global our_sitelib %{python2_sitelib}
%else
%global ourpythonbin %{__python}
%global our_sitelib %{our_sitelib}
%endif
%endif
%{!?our_sitelib: %define our_sitelib %(%{ourpythonbin} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: django_chart
Version: 0.0.3
Release: 1%{?dist}
Summary: A tool for managing rpm based git projects

License: GPLv2
URL: https://github.com/catafest/django_chart
Source0: https://github.com/catafest/django_chart/archive/django_chart-%{version}-1.tar.gz

BuildArch: noarch
%if %{use_python3}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: python3-setuptools
Requires: python3-bugzilla
Requires: python3-blessings
Requires: rpm-python3
%else
BuildRequires: python2-devel
BuildRequires: python-setuptools
Requires: python-setuptools
Requires: python-bugzilla
Requires: python-blessings
Requires: rpm-python
%endif
BuildRequires: asciidoc
BuildRequires: docbook-style-xsl
BuildRequires: libxslt
BuildRequires: rpmdevtools
BuildRequires: rpm-build
BuildRequires: tar
BuildRequires: which

%if 0%{?fedora}
# todo: add %%check to spec file in accordance with
# https://fedoraproject.org/wiki/QA/Testing_in_check
BuildRequires: git
BuildRequires: python-bugzilla
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-bugzilla
BuildRequires: rpm-python3
%endif

Requires: rpm-build
Requires: rpmlint
Requires: fedpkg
Requires: fedora-packager
Requires: rpmdevtools
# Cheetah used not to exist for Python 3, but it's what Mead uses.  We
# install it and call via the command line instead of importing the
# previously potentially incompatible code, as we have not yet got
# around to changing this
Requires: /usr/bin/cheetah

%description
django_chart is a project for managing chart with django 
git.

%prep
# the weird directory name is because github makes the directory name
# '(projectname)-(tag)', and the tags for django_chart have 'django_chart' in them and
# '-1' on the end...
%setup -q -n django_chart-django_chart-%{version}-1
sed -i 1"s|#!.*|#!%{ourpythonbin}|" bin/django_chart

%build
%{ourpythonbin} setup.py build
# convert manages
a2x -d manpage -f manpage django_chartrc.5.asciidoc
a2x -d manpage -f manpage django_chart.8.asciidoc
a2x -d manpage -f manpage django_chart.props.5.asciidoc
a2x -d manpage -f manpage releasers.conf.5.asciidoc

%install
rm -rf $RPM_BUILD_ROOT
%{ourpythonbin} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{our_sitelib}/*egg-info/requires.txt
# manpages
%{__mkdir_p} %{buildroot}%{_mandir}/man5
%{__mkdir_p} %{buildroot}%{_mandir}/man8
cp -a django_chartrc.5 django_chart.props.5 releasers.conf.5 %{buildroot}/%{_mandir}/man5/
cp -a django_chart.8 %{buildroot}/%{_mandir}/man8/
# bash completion facilities
install -Dp -m 0644 share/django_chart_completion.sh %{buildroot}%{_datadir}/bash-completion/completions/django_chart


%files
%doc AUTHORS COPYING
%doc doc/*
%doc %{_mandir}/man5/django_chartrc.5*
%doc %{_mandir}/man5/django_chart.props.5*
%doc %{_mandir}/man5/releasers.conf.5*
%doc %{_mandir}/man8/django_chart.8*
%{_bindir}/django_chart
%{_bindir}/generate-patches.pl
%{_datadir}/bash-completion/completions/django_chart
%dir %{our_sitelib}/django_chart
%{our_sitelib}/django_chart/*
%{our_sitelib}/django_chart-*.egg-info


%changelog
* Fri Dec 20 2019 catafest <catalinfest@gmail.com> 0.0.3-1
- new package built with tito

* Fri Dec 20 2019 catafest <catalinfest@gmail.com> 0.0.2-1
- new package built with tito

* Fri Dec 20 2019 Catalin George Festila <catafest@yahoo.com> 0.6.12-1
