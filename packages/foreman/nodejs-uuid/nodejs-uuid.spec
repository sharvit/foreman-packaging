%global npm_name uuid

Name: nodejs-uuid
Version: 3.3.2
Release: 1%{?dist}
Summary: RFC4122 (v1, v4, and v5) UUIDs
License: MIT
Group: Development/Libraries
URL: https://github.com/kelektiv/node-uuid#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr bin %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr v1.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr v3.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr v4.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr v5.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/uuid
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/uuid %{buildroot}%{_bindir}/uuid

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/uuid
%license LICENSE.md
%doc AUTHORS
%doc CHANGELOG.md
%doc README.md
%doc README_js.md

%changelog
* Thu Jan 17 2019 Avi Sharvit <asharvit@redhat.com> 3.3.2-1
- Update to 3.3.2

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 3.2.1-1
- Update to 3.2.1

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.1.0-1
- Bump nodejs-uuid to 3.1.0 (ewoud@kohlvanwijngaarden.nl)

* Mon May 08 2017 Dominic Cleal <dominic@cleal.org> 3.0.1-1
- new package built with tito

